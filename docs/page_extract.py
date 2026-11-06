"""Trích nhãn hiển thị & thao tác từ page TSX (+ component con khi trang vỏ mỏng)."""
from __future__ import annotations

import re
from dataclasses import dataclass, field


def _clean_label(s: str) -> str | None:
    s = re.sub(r"\s+", " ", s.strip())
    if not s or len(s) < 2 or len(s) > 120:
        return None
    if s.startswith("{") or "${" in s or "`" in s:
        return None
    if re.fullmatch(r"[\W\d_]+", s):
        return None
    return s


def _inner_text_no_jsx(inner: str) -> str | None:
    t = re.sub(r"<[^>]+>", " ", inner)
    t = re.sub(r"\{[^}]*\}", " ", t)
    return _clean_label(t)


@dataclass
class PageUIExtract:
    titles: list[str] = field(default_factory=list)
    cards: list[str] = field(default_factory=list)
    table_columns: list[str] = field(default_factory=list)
    tabs: list[str] = field(default_factory=list)
    filters: list[str] = field(default_factory=list)
    headings: list[str] = field(default_factory=list)
    actions: list[str] = field(default_factory=list)
    dialogs: list[str] = field(default_factory=list)


def _dedupe(items: list[str], limit: int = 45) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for x in items:
        key = x.casefold()
        if key in seen:
            continue
        seen.add(key)
        out.append(x)
        if len(out) >= limit:
            break
    return out


def extract_page_ui(text: str) -> PageUIExtract:
    ui = PageUIExtract()

    for m in re.finditer(r"<h1[^>]*>([\s\S]*?)</h1>", text):
        if t := _inner_text_no_jsx(m.group(1)):
            ui.headings.append(t)
    for m in re.finditer(r"<h2[^>]*>([\s\S]*?)</h2>", text):
        if t := _inner_text_no_jsx(m.group(1)):
            ui.headings.append(t)

    for m in re.finditer(r"<CardTitle[^>]*>([^<]+)</CardTitle>", text):
        if t := _clean_label(m.group(1)):
            ui.cards.append(t)

    for m in re.finditer(r"<TableHead(?:[^>]*)>([^<]+)</TableHead>", text):
        if t := _clean_label(m.group(1)):
            ui.table_columns.append(t)

    for m in re.finditer(
        r'<TabsTrigger[^>]*value="[^"]*"[^>]*>([\s\S]*?)</TabsTrigger>', text
    ):
        if t := _inner_text_no_jsx(m.group(1)):
            ui.tabs.append(t)

    for m in re.finditer(r'<Label[^>]*(?:htmlFor=[^>]*)?>([^<]+)</Label>', text):
        if t := _clean_label(m.group(1)):
            ui.filters.append(t)

    for m in re.finditer(r'placeholder=["\']([^"\']+)["\']', text):
        if t := _clean_label(m.group(1)):
            ui.filters.append(f"Ô nhập: {t}")

    for m in re.finditer(r'label:\s*["\']([^"\']+)["\']', text):
        if t := _clean_label(m.group(1)):
            ui.filters.append(t)

    for m in re.finditer(
        r'(?:DialogTitle|AlertDialogTitle)[^>]*>([^<]+)</(?:DialogTitle|AlertDialogTitle)>',
        text,
    ):
        if t := _clean_label(m.group(1)):
            ui.dialogs.append(t)

    for m in re.finditer(r"<Button[^>]*>([\s\S]*?)</Button>", text):
        if t := _inner_text_no_jsx(m.group(1)):
            ui.actions.append(t)

    for tag in ("DropdownMenuItem", "AlertDialogAction", "AlertDialogCancel"):
        for m in re.finditer(rf"<{tag}[^>]*>([\s\S]*?)</{tag}>", text):
            if t := _inner_text_no_jsx(m.group(1)):
                ui.actions.append(t)

    for m in re.finditer(r'title=["\']([^"\']{4,80})["\']', text):
        t = _clean_label(m.group(1))
        if t and any(ord(c) > 127 for c in t):
            ui.titles.append(t)

    for m in re.finditer(r'aria-label=["\']([^"\']+)["\']', text):
        if t := _clean_label(m.group(1)):
            ui.actions.append(t)

    ui.headings = _dedupe(ui.headings, 15)
    ui.cards = _dedupe(ui.cards, 35)
    ui.table_columns = _dedupe(ui.table_columns, 40)
    ui.tabs = _dedupe(ui.tabs, 20)
    ui.filters = _dedupe(ui.filters, 25)
    ui.dialogs = _dedupe(ui.dialogs, 20)
    ui.actions = _dedupe(ui.actions, 40)
    ui.titles = _dedupe(ui.titles, 15)
    return ui


def merge_ui(parts: list[PageUIExtract]) -> PageUIExtract:
    out = PageUIExtract()
    for key in PageUIExtract.__dataclass_fields__:
        vals: list[str] = []
        for p in parts:
            vals.extend(getattr(p, key))
        setattr(out, key, _dedupe(vals, 50))
    return out


def is_shell_page(text: str) -> bool:
    lines = text.count("\n") + 1
    jsx_tags = len(re.findall(r"<[A-Z][A-Za-z0-9]*", text))
    return lines < 85 or jsx_tags < 10


def render_page_ui_markdown(
    page_name: str,
    page_ui: PageUIExtract,
    child_blocks: list[tuple[str, PageUIExtract]],
) -> str:
    has_main = any(
        getattr(page_ui, k)
        for k in ("headings", "cards", "table_columns", "tabs", "filters", "actions", "dialogs")
    )
    has_child = any(
        any(getattr(c, k) for k in PageUIExtract.__dataclass_fields__ if k != "titles")
        for _, c in child_blocks
    )
    if not has_main and not has_child:
        return ""

    lines: list[str] = [
        "## Thông tin hiển thị",
        "",
        "Nội dung người dùng **nhìn thấy** trên màn hình (trích nhãn từ TSX; số liệu động từ API).",
        "",
    ]

    def block_display(label: str, ui: PageUIExtract) -> None:
        sub: list[str] = []
        if ui.headings:
            sub.append("**Tiêu đề trang:** " + ", ".join(f"“{x}”" for x in ui.headings))
        if ui.cards:
            sub.append("**Thẻ / chỉ số (CardTitle):**")
            sub.extend(f"- {x}" for x in ui.cards)
        if ui.table_columns:
            sub.append("**Cột bảng:**")
            sub.extend(f"- {x}" for x in ui.table_columns)
        if ui.tabs:
            sub.append("**Tab / khu vực:**")
            sub.extend(f"- {x}" for x in ui.tabs)
        if ui.filters:
            sub.append("**Nhãn lọc / preset / placeholder:**")
            sub.extend(f"- {x}" for x in ui.filters)
        if ui.titles:
            sub.append("**Tooltip / mô tả ngắn (title=):**")
            sub.extend(f"- {x}" for x in ui.titles[:12])
        if not sub:
            return
        lines.append(f"### {label}")
        lines.append("")
        lines.extend(sub)
        lines.append("")

    if has_main:
        block_display(f"`{page_name}`", page_ui)
    for mod, cui in child_blocks:
        if not any(getattr(cui, k) for k in PageUIExtract.__dataclass_fields__):
            continue
        prefix = "@/pages/" if mod.startswith("pages/") else "@/components/"
        block_display(f"`{prefix}{mod.removeprefix('pages/')}`", cui)

    lines.extend(
        [
            "## Thao tác người dùng",
            "",
            "Hành động chính (nút, menu, mục dialog) — không liệt kê mọi nút icon-only.",
            "",
        ]
    )

    def block_actions(label: str, ui: PageUIExtract) -> None:
        if not ui.actions and not ui.dialogs:
            return
        lines.append(f"### {label}")
        lines.append("")
        if ui.actions:
            lines.append("**Thao tác:**")
            lines.extend(f"- {x}" for x in ui.actions)
            lines.append("")
        if ui.dialogs:
            lines.append("**Hộp thoại (tiêu đề):**")
            lines.extend(f"- {x}" for x in ui.dialogs)
            lines.append("")

    if page_ui.actions or page_ui.dialogs:
        block_actions(f"`{page_name}`", page_ui)
    for mod, cui in child_blocks:
        if not (cui.actions or cui.dialogs):
            continue
        prefix = "@/pages/" if mod.startswith("pages/") else "@/components/"
        block_actions(f"`{prefix}{mod.removeprefix('pages/')}`", cui)

    return "\n".join(lines).rstrip() + "\n"
