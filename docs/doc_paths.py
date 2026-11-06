"""Quy ước thư mục + README.md — tên thư mục ưu tiên tiếng Việt."""
from __future__ import annotations

import os
import re
from pathlib import Path

README = "README.md"


def _readme(*parts: str) -> str:
    return "/".join([*parts, README])


def camel_to_kebab(name: str) -> str:
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", name)
    return s.lower()


# slug thư mục — tách riêng trang / API / schema (tránh ghi đè cùng tên file)
PAGE_SLUG: dict[str, str] = {
    "access-block": "chan-truy-cap",
    "access-overview-section": "tong-quan-truy-cap",
    "agent-assistant": "tro-ly-ai",
    "agent-chat-audit": "kiem-audit-tro-ly",
    "camera-settings": "cau-hinh-camera",
    "chain": "chuoi-cua-hang",
    "chain-api-keys": "khoa-api-chuoi",
    "chain-dashboard": "bang-dieu-khiem-chuoi",
    "customer-feedback": "phan-hoi-khach",
    "dashboard": "bang-dieu-khiem",
    "device-ban": "chan-thiet-bi",
    "feedback-form": "form-phan-hoi",
    "inventory": "ton-kho",
    "ip-ban": "chan-ip",
    "keyboard-shortcuts": "phim-tat",
    "lan-devices": "thiet-bi-mang-lan",
    "login": "dang-nhap",
    "media": "quan-ly-media",
    "my-permissions": "quyen-cua-toi",
    "not-found": "khong-tim-thay",
    "notification-settings": "cau-hinh-thong-bao",
    "orders": "don-hang",
    "page-status": "trang-thai-trien-khai",
    "pos": "ban-hang-pos",
    "products": "san-pham",
    "purchase-orders": "dat-hang",
    "reports": "bao-cao",
    "sales-staff": "nhan-vien-ban-hang",
    "staff": "nhan-vien",
    "statistics": "thong-ke",
    "stock-requests": "phieu-nhap-xuat",
    "suppliers": "nha-cung-cap",
    "system-reports": "bao-cao-he-thong",
    "vat-inbound": "hoa-don-dau-vao",
    "vat-invoice-public": "tra-cuu-hoa-don-cong-khai",
    "vat-invoices": "hoa-don-xuat-vat",
}

API_SLUG: dict[str, str] = {
    "access-observations": "quan-sat-truy-cap",
    "blocked-devices": "chan-thiet-bi-api",
    "blocked-ips": "chan-ip-api",
    "auth": "xac-thuc",
    "agent": "tro-ly-ai-api",
    "chain": "chuoi-api",
    "dashboard": "bang-dieu-khiem-api",
    "feedback": "phan-hoi-api",
    "health": "kiem-tra-suc-khoe",
    "media": "media-api",
    "notifications": "thong-bao",
    "notification-settings": "cau-hinh-thong-bao-api",
    "order-audit-reports": "bao-cao-audit-don",
    "org-gdt-portal": "cong-cqt",
    "org-viettel-settings": "cau-hinh-viettel",
    "pos-cart-audit": "audit-gio-hang-pos",
    "product-audit-reports": "bao-cao-audit-san-pham",
    "product-categories": "danh-muc-san-pham",
    "public-vat-invoice": "hoa-don-vat-cong-khai",
    "purchase-order-audit-reports": "bao-cao-audit-dat-hang",
    "reports": "bao-cao-api",
    "sales-staff": "nhan-vien-ban-api",
    "shift-sessions": "ca-lam-viec",
    "shop-api-keys": "khoa-api-cua-hang",
    "shops": "cua-hang",
    "statistics": "thong-ke-api",
    "stock-request-audit-reports": "bao-cao-audit-phieu-kho",
    "sync": "dong-bo-du-lieu",
    "system-events": "su-kien-he-thong",
    "walk-in-customers": "khach-vang-lai",
    "widget": "widget-quay",
    "products": "san-pham-api",
    "inventory": "ton-kho-api",
    "orders": "don-hang-api",
    "suppliers": "nha-cung-cap-api",
}

SCHEMA_SLUG: dict[str, str] = {
    "agentChat": "tro-ly-ai-chat",
    "allowedDevices": "thiet-bi-duoc-phep",
    "blockedDevices": "thiet-bi-bi-chan",
    "blockedIps": "ip-bi-chan",
    "changeLog": "nhat-ky-thay-doi",
    "customerFeedback": "phan-hoi-khach-hang",
    "deviceLoginEvents": "su-kien-dang-nhap-thiet-bi",
    "inventory": "ton-kho-db",
    "inventoryMovements": "bien-dong-ton",
    "invoiceChangeLogs": "nhat-ky-hoa-don",
    "orderAuditLogs": "audit-don-hang",
    "orderItems": "chi-tiet-don-hang",
    "orderPreprintReservations": "giu-so-in-truoc",
    "orders": "don-hang-db",
    "orderSyncKeys": "khoa-dong-bo-don",
    "orgGdtTaxSessions": "phien-thue-cqt",
    "organizations": "to-chuc",
    "paymentChangeLogs": "nhat-ky-thanh-toan",
    "pinResetRequests": "yeu-cau-reset-pin",
    "platformNotificationSettings": "cau-hinh-thong-bao-nen-tang",
    "posCartAuditLogs": "audit-gio-pos",
    "productAuditLogs": "audit-san-pham",
    "productCategories": "danh-muc-san-pham-db",
    "products": "san-pham-db",
    "productVariants": "bien-the-san-pham",
    "purchaseOrders": "phieu-dat-hang",
    "reprintLogs": "nhat-ky-in-lai",
    "salesStaff": "nhan-vien-ban-db",
    "shiftSessions": "ca-lam-viec-db",
    "shopApiKeys": "khoa-api-shop",
    "shopDailyVisitorCounts": "dem-khach-theo-ngay",
    "shopOperationalEvents": "su-kien-van-hanh-shop",
    "shops": "cua-hang-db",
    "shopVariantStock": "ton-bien-the-shop",
    "stockRequests": "phieu-yeu-cau-kho",
    "stockTransfers": "chuyen-kho",
    "suppliers": "nha-cung-cap-db",
    "systemEventLogs": "nhat-ky-su-kien",
    "userNotifications": "thong-bao-nguoi-dung",
    "users": "nguoi-dung",
    "vatInboundAuditLogs": "audit-hoa-don-dau-vao",
    "vatInboundInvoices": "hoa-don-dau-vao-db",
    "warehouses": "kho-hang",
}

LIB_DIR_SLUG: dict[str, str] = {
    "gdt-portal": "cong-cqt",
    "viettel-sinvoice": "hoa-don-viettel",
    "agent": "tro-ly-ai-lib",
}

# Tài liệu tham chiếu Shop (mirror) — thư mục tiếng Việt
THAM_CHIEU_SLUG: dict[str, str] = {
    "architecture.md": "kien-truc",
    "api-routes.md": "danh-sach-api-goc",
    "database.md": "co-so-du-lieu-goc",
    "rbac.md": "phan-quyen-rbac",
    "business-flows.md": "luong-nghiep-vu-goc",
    "offline-first.md": "offline-first",
    "offline-first-audit.md": "audit-offline",
    "offline-first-roadmap.md": "lo-trinh-offline",
    "docker-may-chu.md": "docker-may-chu",
    "running-local.md": "chay-local",
    "api-server.md": "code-tour-api",
    "pos-app.md": "code-tour-pos",
    "db.md": "code-tour-db",
    "code-annotations.md": "chu-thich-ma",
    "public-access.md": "truy-cap-cong-khai",
}


def page_folder(stem: str) -> str:
    return PAGE_SLUG.get(stem, stem)


def api_folder(stem: str) -> str:
    return API_SLUG.get(stem, PAGE_SLUG.get(stem, stem))


def schema_folder(stem: str) -> str:
    if stem in SCHEMA_SLUG:
        return SCHEMA_SLUG[stem]
    return camel_to_kebab(stem) if re.search(r"[A-Z]", stem) else stem


def lib_segment(stem: str) -> str:
    return LIB_DIR_SLUG.get(stem, stem)


def trang_path(page_stem: str) -> str:
    return _readme("trang", page_folder(page_stem))


def module_api_path(api_stem: str) -> str:
    return _readme("module-api", api_folder(api_stem))


def co_so_du_lieu_path(schema_stem: str) -> str:
    return _readme("co-so-du-lieu", schema_folder(schema_stem))


def thu_vien_path(rel_posix: str) -> str:
    """rel_posix: path dưới lib/ không có .ts, vd. vat-inbound-tax-sync hoặc gdt-portal/captcha-store."""
    rel_posix = rel_posix.replace("\\", "/").strip("/")
    parts = rel_posix.split("/")
    mapped = [lib_segment(p) for p in parts]
    return _readme("thu-vien", *mapped)


def nghiep_vu_path(chapter_stem: str) -> str:
    return _readme("nghiep-vu", chapter_stem)


def he_thong_path(stem: str) -> str:
    return _readme("he-thong", stem)


def chuyen_de_path(hub_stem: str) -> str:
    hub_stem = hub_stem.replace(".md", "")
    if hub_stem.startswith("00-"):
        hub_stem = hub_stem[3:]
    return _readme("chuyen-de", hub_stem)


def chi_muc_path(name: str) -> str:
    name = name.replace(".md", "")
    return _readme("chi-muc", name)


def tham_chieu_path(shop_filename: str) -> str:
    slug = THAM_CHIEU_SLUG.get(shop_filename, Path(shop_filename).stem)
    return _readme("tham-chieu", slug)


def huong_dan_doc_path() -> str:
    return _readme("huong-dan-doc")


def ban_do_path() -> str:
    return _readme("ban-do-kien-truc")


def map_index_path() -> str:
    return README


def md_relpath(from_doc: str, to_doc: str) -> str:
    """Đường dẫn markdown tương đối từ file `from_doc` tới `to_doc` (đều relative docs ROOT)."""
    from_doc = from_doc.replace("\\", "/")
    to_doc = to_doc.replace("\\", "/")
    from_dir = os.path.dirname(from_doc) or "."
    rel = os.path.relpath(to_doc, from_dir)
    return rel.replace("\\", "/")


def md_href(from_doc: str, to_doc: str) -> str:
    """
    Link markdown tới **thư mục** doc (README nằm trong thư mục đó).
    Trang chủ `docs/README.md` giữ tên file; mọi doc con dùng href kết thúc `/`.
    """
    to_doc = to_doc.replace("\\", "/")
    rel = md_relpath(from_doc, to_doc)
    if to_doc == README or "/" not in to_doc:
        return rel
    if rel.endswith(f"/{README}"):
        return rel[: -len(README)]
    return rel


def resolve_doc_link(legacy: str) -> str:
    """Đổi đường dẫn doc cũ (*.md phẳng) sang thư mục/README.md."""
    legacy = legacy.strip().replace("\\", "/")
    if legacy.endswith(f"/{README}") or legacy == README:
        return legacy
    if legacy == "00-muc-luc-va-kien-truc.md":
        return map_index_path()
    if legacy == "00-huong-dan-doc-tai-lieu.md":
        return huong_dan_doc_path()
    if legacy == "ban-do-kien-truc.md":
        return ban_do_path()

    m = re.fullmatch(r"frontend-pages/([\w-]+)\.md", legacy)
    if m:
        return trang_path(m.group(1))
    m = re.fullmatch(r"api-modules/([\w-]+)\.md", legacy)
    if m:
        return module_api_path(m.group(1))
    m = re.fullmatch(r"schema/([\w-]+)\.md", legacy)
    if m:
        return co_so_du_lieu_path(m.group(1))
    m = re.fullmatch(r"lib-modules/(.+)\.md", legacy)
    if m:
        return thu_vien_path(m.group(1))
    m = re.fullmatch(r"nghiep-vu/([\w-]+)\.md", legacy)
    if m:
        return nghiep_vu_path(m.group(1))
    m = re.fullmatch(r"he-thong/([\w-]+)\.md", legacy)
    if m:
        return he_thong_path(m.group(1))
    m = re.fullmatch(r"chuyen-de/([\w-]+)\.md", legacy)
    if m:
        return chuyen_de_path(m.group(1))
    m = re.fullmatch(r"chi-muc/([\w-]+)\.md", legacy)
    if m:
        return chi_muc_path(m.group(1))
    m = re.fullmatch(r"reference/([\w-]+)\.md", legacy)
    if m:
        return tham_chieu_path(m.group(1))
    return legacy


def rewrite_legacy_links(text: str) -> str:
    """Thay link/backtick path doc cũ trong nội dung markdown."""

    def sub_pat(pattern: str, repl_fn) -> None:
        nonlocal text
        text = re.sub(pattern, lambda m: repl_fn(m), text)

    patterns = [
        (r"frontend-pages/([\w-]+)\.md", lambda m: trang_path(m.group(1))),
        (r"api-modules/([\w-]+)\.md", lambda m: module_api_path(m.group(1))),
        (r"schema/([\w-]+)\.md", lambda m: co_so_du_lieu_path(m.group(1))),
        (r"lib-modules/([\w/-]+)\.md", lambda m: thu_vien_path(m.group(1))),
        (r"nghiep-vu/([\w-]+)\.md", lambda m: nghiep_vu_path(m.group(1))),
        (r"he-thong/([\w-]+)\.md", lambda m: he_thong_path(m.group(1))),
        (r"chuyen-de/00-kien-truc-he-thong\.md", lambda _m: chuyen_de_path("00-kien-truc-he-thong")),
        (r"chuyen-de/([\w-]+)\.md", lambda m: chuyen_de_path(m.group(1))),
        (r"chi-muc/([\w-]+)\.md", lambda m: chi_muc_path(m.group(1))),
        (r"reference/([\w-]+)\.md", lambda m: tham_chieu_path(m.group(1))),
        (r"00-muc-luc-va-kien-truc\.md", lambda _m: map_index_path()),
        (r"00-huong-dan-doc-tai-lieu\.md", lambda _m: huong_dan_doc_path()),
        (r"ban-do-kien-truc\.md", lambda _m: ban_do_path()),
    ]
    for pat, fn in patterns:
        text = re.sub(pat, lambda m, f=fn: f(m), text)
    return text


def doc_prefix(kind: str) -> str:
    return {
        "api": "module-api/",
        "page": "trang/",
        "schema": "co-so-du-lieu/",
        "lib": "thu-vien/",
        "nghiep": "nghiep-vu/",
        "he": "he-thong/",
    }.get(kind, "")


def legacy_desc_key(rel_readme: str) -> str:
    """Map README path → key cũ trong NGHIEP_VU_DESC / HE_THONG_DESC."""
    rel_readme = rel_readme.replace("\\", "/")
    if rel_readme == huong_dan_doc_path():
        return "00-huong-dan-doc-tai-lieu.md"
    if rel_readme == ban_do_path():
        return "ban-do-kien-truc.md"
    if rel_readme.startswith("nghiep-vu/") and rel_readme.endswith(f"/{README}"):
        stem = rel_readme.split("/")[-2]
        return f"nghiep-vu/{stem}.md"
    if rel_readme.startswith("he-thong/") and rel_readme.endswith(f"/{README}"):
        stem = rel_readme.split("/")[-2]
        return f"he-thong/{stem}.md"
    return rel_readme
