"""Trích cấu trúc Drizzle pgTable / pgEnum từ lib/db/src/schema/*.ts."""
from __future__ import annotations

import re
from dataclasses import dataclass, field


PG_ENUM_RE = re.compile(
    r"export const (\w+)\s*=\s*pgEnum\(\s*[\"']([^\"']+)[\"']\s*,\s*(\[[^\]]+\])\s*\)",
    re.MULTILINE,
)
PG_TABLE_RE = re.compile(
    r"export const (\w+)\s*=\s*pgTable\(\s*[\"']([^\"']+)[\"']\s*,\s*\{",
    re.MULTILINE,
)
INDEX_RE = re.compile(
    r"(?:uniqueIndex|index)\(\s*[\"']([^\"']+)[\"']\s*\)\.on\(([^)]+)\)",
)
UNIQUE_ON_RE = re.compile(r"unique\(\)\.on\(([^)]+)\)")
TYPE_EXPORT_RE = re.compile(r"^export type (\w+)\s*=", re.MULTILINE)
INSERT_SCHEMA_RE = re.compile(r"^export const (insert\w+Schema)\s*=", re.MULTILINE)
# Chỉ comment ngay trước export (không nuốt JSDoc cột bên trong pgTable).
TABLE_COMMENT_RE = re.compile(
    r"(/\*\*(?:[^*]|\*(?!/))*\*/)\s*\nexport const (\w+)\s*=\s*pgTable\s*\(",
)


@dataclass
class ColumnDef:
    prop: str
    sql_name: str
    type_label: str
    constraints: str
    fk_table: str
    note: str


@dataclass
class TableDef:
    var_name: str
    pg_name: str
    table_comment: str
    columns: list[ColumnDef] = field(default_factory=list)
    indexes: list[tuple[str, str, bool]] = field(default_factory=list)  # name, on, unique


@dataclass
class SchemaFile:
    stem: str
    enums: list[tuple[str, str, str]]  # ts_name, pg_name, values_literal
    tables: list[TableDef]
    type_exports: list[str]
    insert_schemas: list[str]


def _brace_block(text: str, open_pos: int) -> tuple[str, int]:
    """Return content inside `{` at open_pos (exclusive) and index after closing `}`."""
    if open_pos >= len(text) or text[open_pos] != "{":
        return "", open_pos
    depth = 0
    i = open_pos
    while i < len(text):
        c = text[i]
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return text[open_pos + 1 : i], i + 1
        i += 1
    return text[open_pos + 1 :], len(text)


def _clean_comment(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith("/**"):
        raw = raw[3:]
    if raw.endswith("*/"):
        raw = raw[:-2]
    lines = []
    for ln in raw.splitlines():
        ln = ln.strip()
        if ln.startswith("*"):
            ln = ln[1:].strip()
        if ln:
            lines.append(ln)
    return " ".join(lines).strip()


COL_PROP_RE = re.compile(
    r"^(\s+)(\w+):\s*(serial|integer|text|timestamp|jsonb|numeric|boolean|uuid|bigint|smallint|\w+Enum|\w+Table|\w+)\(",
)


def _column_indent(body: str) -> str:
    indents: list[int] = []
    for line in body.split("\n"):
        m = COL_PROP_RE.match(line)
        if m:
            indents.append(len(m.group(1)))
    if not indents:
        return "  "
    width = min(indents)
    return " " * width


def _split_table_columns(body: str) -> list[tuple[str, str, str]]:
    """(prop, column_chunk, leading_comment)."""
    lines = body.split("\n")
    col_prefix = _column_indent(body)
    col_start = re.compile(rf"^{re.escape(col_prefix)}(\w+):\s*(.*)")
    out: list[tuple[str, str, str]] = []
    i = 0
    pending = ""
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if stripped.startswith("/**"):
            buf = [line]
            if "*/" in line:
                i += 1
            else:
                i += 1
                while i < len(lines):
                    buf.append(lines[i])
                    if "*/" in lines[i]:
                        i += 1
                        break
                    i += 1
            pending = _clean_comment("\n".join(buf))
            continue
        if stripped.startswith("//"):
            pending = stripped.lstrip("/").strip()
            i += 1
            continue
        m = col_start.match(line)
        if m:
            prop = m.group(1)
            chunk_lines = [m.group(2)]
            i += 1
            while i < len(lines):
                nl = lines[i]
                if col_start.match(nl):
                    break
                chunk_lines.append(nl)
                i += 1
            out.append((prop, "\n".join(chunk_lines), pending))
            pending = ""
            continue
        i += 1
    return out


def _parse_column(
    prop: str,
    chunk: str,
    note: str,
    enum_pg: dict[str, str],
    var_to_pg: dict[str, str],
) -> ColumnDef:
    sql_m = re.search(r'\w+\(\s*["\']([^"\']+)["\']', chunk)
    sql_name = sql_m.group(1) if sql_m else "?"
    head_m = re.match(r"(\w+)", chunk.strip())
    head = head_m.group(1) if head_m else "?"
    type_label = head
    if head in enum_pg:
        type_label = f"enum `{enum_pg[head]}`"
    num_m = re.search(r"numeric\([^)]+\)", chunk)
    if num_m:
        type_label = num_m.group(0)
    ts_m = re.search(r"timestamp\([^)]+\)", chunk)
    if ts_m and "timestamp" in type_label:
        type_label = ts_m.group(0)
    if "jsonb" in chunk.split("(")[0] or chunk.strip().startswith("jsonb"):
        type_label = "jsonb"
    flat = chunk.replace("\n", " ")
    flags: list[str] = []
    if ".primaryKey()" in flat:
        flags.append("**PK**")
    if ".notNull()" in flat:
        flags.append("NOT NULL")
    if ".defaultNow()" in flat:
        flags.append("default `now()`")
    else:
        def_m = re.search(r'\.default\(\s*["\']?([^"\')\s]+)["\']?\s*\)', flat)
        if def_m:
            flags.append(f"default `{def_m.group(1)}`")
    if ".$type" in flat:
        flags.append("JSON typed")
    fk_table = ""
    ref_m = re.search(r"\.references\(\(\)\s*=>\s*(\w+)\.", flat)
    if ref_m:
        fk_table = var_to_pg.get(ref_m.group(1), ref_m.group(1))
    return ColumnDef(
        prop=prop,
        sql_name=sql_name,
        type_label=type_label,
        constraints=", ".join(flags) if flags else "—",
        fk_table=fk_table,
        note=note,
    )


def parse_enums(text: str) -> dict[str, str]:
    """TS enum const name -> Postgres enum name."""
    out: dict[str, str] = {}
    for m in PG_ENUM_RE.finditer(text):
        out[m.group(1)] = m.group(2)
    return out


def index_var_to_prop(on_expr: str) -> str:
    parts = re.findall(r"t\.(\w+)", on_expr)
    return ", ".join(f"`{p}`" for p in parts) if parts else on_expr.strip()


def parse_schema_file(stem: str, text: str, var_to_pg: dict[str, str]) -> SchemaFile:
    enum_pg = parse_enums(text)
    enums_list: list[tuple[str, str, str]] = []
    for m in PG_ENUM_RE.finditer(text):
        enums_list.append((m.group(1), m.group(2), m.group(3).strip()))

    table_comments: dict[str, str] = {}
    for m in TABLE_COMMENT_RE.finditer(text):
        table_comments[m.group(2)] = _clean_comment(m.group(1))

    tables: list[TableDef] = []
    for m in PG_TABLE_RE.finditer(text):
        var_name = m.group(1)
        pg_name = m.group(2)
        body, after_body = _brace_block(text, m.end() - 1)
        td = TableDef(
            var_name=var_name,
            pg_name=pg_name,
            table_comment=table_comments.get(var_name, ""),
        )
        for prop, chunk, note in _split_table_columns(body):
            td.columns.append(
                _parse_column(prop, chunk, note, enum_pg, var_to_pg)
            )
        tail = text[after_body : after_body + 800]
        for im in INDEX_RE.finditer(tail):
            unique = "uniqueIndex" in text[max(0, im.start() - 20) : im.start() + 5]
            td.indexes.append((im.group(1), index_var_to_prop(im.group(2)), unique))
        for um in UNIQUE_ON_RE.finditer(tail):
            td.indexes.append(
                ("(unique)", index_var_to_prop(um.group(1)), True)
            )
        tables.append(td)

    type_exports = TYPE_EXPORT_RE.findall(text)
    insert_schemas = INSERT_SCHEMA_RE.findall(text)
    return SchemaFile(
        stem=stem,
        enums=enums_list,
        tables=tables,
        type_exports=type_exports,
        insert_schemas=insert_schemas,
    )


def build_var_to_pg_map(schema_dir_files: dict[str, str]) -> dict[str, str]:
    var_to_pg: dict[str, str] = {}
    for text in schema_dir_files.values():
        for m in PG_TABLE_RE.finditer(text):
            var_to_pg[m.group(1)] = m.group(2)
    return var_to_pg


def schema_summary(sf: SchemaFile) -> str:
    n_tables = len(sf.tables)
    n_cols = sum(len(t.columns) for t in sf.tables)
    n_idx = sum(len(t.indexes) for t in sf.tables)
    parts = [f"{n_tables} bảng", f"{n_cols} cột"]
    if sf.enums:
        parts.append(f"{len(sf.enums)} enum")
    if n_idx:
        parts.append(f"{n_idx} index")
    tbl_names = ", ".join(f"`{t.pg_name}`" for t in sf.tables[:3])
    if n_tables > 3:
        tbl_names += f" (+{n_tables - 3})"
    return f"Drizzle `{sf.stem}.ts` — {', '.join(parts)} ({tbl_names})."


def render_schema_markdown(sf: SchemaFile, *, ref_db_href: str) -> str:
    lines: list[str] = []
    if sf.enums:
        lines.extend(["## Enum Postgres", ""])
        for ts_name, pg_name, values in sf.enums:
            lines.append(f"### `{pg_name}` (`{ts_name}`)")
            lines.append("")
            lines.append(f"- Giá trị: `{values}`")
            lines.append("")

    for td in sf.tables:
        lines.append(f"## Bảng `{td.pg_name}`")
        lines.append("")
        if td.table_comment:
            lines.append(f"*{td.table_comment}*")
            lines.append("")
        lines.append(f"- **Biến Drizzle:** `{td.var_name}`")
        lines.append("")
        lines.append(
            "| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |"
        )
        lines.append(
            "|---------|---------------|------|-----------|-----------|---------|"
        )
        for col in td.columns:
            note = col.note.replace("|", "\\|")[:120]
            if len(col.note) > 120:
                note += "…"
            fk = f"`{col.fk_table}`" if col.fk_table else "—"
            lines.append(
                f"| `{col.sql_name}` | `{col.prop}` | {col.type_label} | "
                f"{col.constraints} | {fk} | {note or '—'} |"
            )
        lines.append("")
        if td.indexes:
            lines.append("**Index:**")
            lines.append("")
            for iname, on_cols, unique in td.indexes:
                kind = "UNIQUE " if unique else ""
                lines.append(f"- {kind}`{iname}` on {on_cols}")
            lines.append("")

    if sf.insert_schemas or sf.type_exports:
        lines.append("## Kiểu & Zod (insert)")
        lines.append("")
        if sf.insert_schemas:
            for s in sf.insert_schemas:
                lines.append(f"- `{s}` — `createInsertSchema` (xem file TS)")
        if sf.type_exports:
            for t in sf.type_exports:
                lines.append(f"- `export type {t}`")
        lines.append("")

    lines.append(f"Tổng quan ER / naming: [{ref_db_href}]({ref_db_href}).")
    lines.append("")
    return "\n".join(lines)
