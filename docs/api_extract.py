"""Trích body / response / lỗi từ routes TS + schema Zod (OpenAPI orval)."""
from __future__ import annotations

import re
from typing import Iterator

ZOD_OBJECT_RE = re.compile(
    r"export const (\w+) = zod\.object\(\{([\s\S]*?)\n\}\)",
    re.MULTILINE,
)
ZOD_FIELD_RE = re.compile(
    r"^\s{2}(\w+):\s*zod\.(\w+(?:\([^)]*\))?)",
    re.MULTILINE,
)
ZOD_OPTIONAL_RE = re.compile(r"\.optional\(\)")

ROUTER_START_RE = re.compile(
    r'router\.(get|post|patch|put|delete)\(\s*["\']([^"\']+)["\']',
    re.IGNORECASE,
)


def iter_route_handlers(route_text: str) -> Iterator[tuple[str, str, str]]:
    """Yield (METHOD, path, handler_chunk) for each router.METHOD("path"...)."""
    matches = list(ROUTER_START_RE.finditer(route_text))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(route_text)
        chunk = route_text[m.start() : end]
        yield m.group(1).upper(), m.group(2), chunk


def parse_zod_schemas(api_ts: str) -> dict[str, list[tuple[str, str, bool]]]:
    """schema name -> [(field, zod_type, optional), ...]"""
    out: dict[str, list[tuple[str, str, bool]]] = {}
    for m in ZOD_OBJECT_RE.finditer(api_ts):
        name = m.group(1)
        body = m.group(2)
        fields: list[tuple[str, str, bool]] = []
        for fm in ZOD_FIELD_RE.finditer(body):
            field = fm.group(1)
            rest = body[fm.start() : fm.start() + 200]
            optional = bool(ZOD_OPTIONAL_RE.search(rest.split("\n")[0]))
            fields.append((field, fm.group(2), optional))
        if fields:
            out[name] = fields
    return out


def _schema_table(name: str, schemas: dict[str, list[tuple[str, str, bool]]]) -> str:
    fields = schemas.get(name)
    if not fields:
        return f"*(schema `{name}` — xem `lib/api-zod/src/generated/api.ts`)*"
    lines = ["| Trường | Kiểu (Zod) | Bắt buộc |", "|--------|------------|----------|"]
    for field, zt, opt in fields[:40]:
        req = "không" if opt else "**có**"
        lines.append(f"| `{field}` | `{zt}` | {req} |")
    if len(fields) > 40:
        lines.append(f"| … | | (+{len(fields) - 40} trường) |")
    return "\n".join(lines)


def _errors_table(chunk: str) -> list[str]:
    rows: list[str] = []
    seen: set[tuple[str, str]] = set()
    for m in re.finditer(
        r'res\.status\((\d+)\)\.json\(\s*\{[^}]*error:\s*"([^"]+)"',
        chunk,
    ):
        key = (m.group(1), m.group(2))
        if key in seen:
            continue
        seen.add(key)
        rows.append(f"| **{m.group(1)}** | `{m.group(2)}` |")
    return rows


def _infer_success_status(chunk: str) -> str:
    if re.search(r"res\.status\(201\)", chunk):
        return "201"
    if re.search(r"res\.status\(204\)", chunk):
        return "204"
    return "200"


def _json_top_level_keys(chunk: str) -> list[str]:
    keys: set[str] = set()
    for block in re.findall(r"res\.(?:status\(\d+\)\.)?json\(\s*\{([^;]{0,1200})", chunk, re.DOTALL):
        for k in re.findall(r"(\w+)\s*:", block):
            if k not in ("error", "catch", "if", "return"):
                keys.add(k)
    return sorted(keys)[:25]


def build_endpoint_detail_auto(
    method: str,
    path: str,
    handler_chunk: str,
    route_middleware: list[str],
    zod_schemas: dict[str, list[tuple[str, str, bool]]],
) -> str:
    if not handler_chunk.strip():
        return ""

    api_path = path if path.startswith("/") else f"/{path}"
    lines = [f"**URL:** `{method} /api{api_path}`", ""]

    mw = ", ".join(f"`{x}`" for x in route_middleware) if route_middleware else "`requireAuth` (hoặc public — xem route)"
    lines.append(f"**Lớp route:** {mw}")

    if "super_admin" in handler_chunk or "requireSuperAdmin" in handler_chunk:
        lines.append("- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).")
    lines.append("")

    # Zod body / response
    body_schemas = sorted(
        set(re.findall(r"(\w+Body)\.(?:parse|safeParse)", handler_chunk))
        | set(re.findall(r"(\w+Body)\.parse\(", handler_chunk))
    )
    resp_schemas = sorted(
        set(re.findall(r"(\w+Response)\.(?:parse|safeParse)", handler_chunk))
        | set(re.findall(r"(\w+Response)\.parse\(", handler_chunk))
    )
    if not resp_schemas:
        resp_schemas = sorted(set(re.findall(r"(\w+Response)\s*=", handler_chunk)))

    body_fields = sorted(
        set(re.findall(r"req\.body\??\.(\w+)", handler_chunk))
        | set(re.findall(r"req\.body\?\.(\w+)\s*\?\?", handler_chunk))
    )
    query_fields = sorted(set(re.findall(r"req\.query\.(\w+)", handler_chunk)))
    param_fields = sorted(set(re.findall(r"req\.params\.(\w+)", handler_chunk)))

    if body_schemas:
        for bs in body_schemas[:3]:
            lines.append(f"**Request body** — schema `{bs}` (`@workspace/api-zod`):")
            lines.append("")
            lines.append(_schema_table(bs, zod_schemas))
            lines.append("")
    elif body_fields:
        lines.append("**Request body** (`application/json`, trích từ code):")
        lines.append("")
        lines.append("| Trường | Ghi chú |")
        lines.append("|--------|---------|")
        for f in body_fields:
            lines.append(f"| `{f}` | xem handler |")
        lines.append("")

    if query_fields:
        lines.append("**Query:** " + ", ".join(f"`{q}`" for q in query_fields))
        lines.append("")
    if param_fields:
        lines.append("**Path params:** " + ", ".join(f"`{p}`" for p in param_fields))
        lines.append("")

    err_rows = _errors_table(handler_chunk)
    if err_rows:
        lines.append("**Lỗi JSON** (`error` string):")
        lines.append("")
        lines.append("| HTTP | Message |")
        lines.append("|------|---------|")
        lines.extend(err_rows)
        lines.append("")

    success = _infer_success_status(handler_chunk)
    if resp_schemas:
        for rs in resp_schemas[:2]:
            lines.append(f"**Response {success}** — schema `{rs}`:")
            lines.append("")
            lines.append(_schema_table(rs, zod_schemas))
            lines.append("")
    else:
        keys = _json_top_level_keys(handler_chunk)
        if keys:
            lines.append(f"**Response {success}** — trường top-level (trích `res.json`):")
            lines.append("")
            lines.append(", ".join(f"`{k}`" for k in keys))
            lines.append("")

    if not body_schemas and not body_fields and not err_rows and not keys and not resp_schemas:
        lines.append("*Handler không trích được contract tự động — mở file route TypeScript.*")
        lines.append("")

    return "\n".join(lines).strip()


def load_zod_schemas(shop_root) -> dict[str, list[tuple[str, str, bool]]]:
    p = shop_root / "lib/api-zod/src/generated/api.ts"
    if not p.is_file():
        return {}
    return parse_zod_schemas(p.read_text(encoding="utf-8", errors="replace"))
