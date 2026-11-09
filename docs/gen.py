#!/usr/bin/env python3
"""Build VietPOS-Map: long TOC + detailed per-topic files from Shop codebase."""
from __future__ import annotations

import base64
import json
import re
import shutil
from pathlib import Path

from api_extract import build_endpoint_detail_auto, iter_route_handlers, load_zod_schemas
from page_extract import extract_page_ui, is_shell_page, render_page_ui_markdown
from schema_extract import (
    build_var_to_pg_map,
    parse_schema_file,
    render_schema_markdown,
    schema_summary,
)

from doc_paths import (
    README,
    ban_do_path,
    MAP_PORTAL_INDEX,
    portal_doc_href,
    portal_index_href,
    chi_muc_path,
    chuyen_de_path,
    co_so_du_lieu_path,
    he_thong_path,
    huong_dan_doc_path,
    legacy_desc_key,
    map_index_path,
    module_api_path,
    nghiep_vu_path,
    PAGE_SLUG,
    rewrite_legacy_links,
    resolve_doc_link,
    tham_chieu_path,
    thu_vien_path,
    trang_path,
    md_href,
    md_relpath,
    camel_to_kebab,
)

ROOT = Path(__file__).resolve().parent
SHOP = ROOT.parent.parent / "Shop-Manager-System-Offline"

# Chạy sync trong <head> trước doc.css / portal.css (tránh :root kẹt tối)
THEME_HEAD_INLINE = """<script>
(function(){var k="vietpos-map-theme",MD={dark:"https://cdn.jsdelivr.net/npm/github-markdown-css@5.6.1/github-markdown-dark.min.css",light:"https://cdn.jsdelivr.net/npm/github-markdown-css@5.6.1/github-markdown-light.min.css"},t=localStorage.getItem(k);
if(t!=="light"&&t!=="dark")t=matchMedia("(prefers-color-scheme: light)").matches?"light":"dark";
var r=document.documentElement;r.setAttribute("data-theme",t);r.style.colorScheme=t;r.classList.remove("theme-light","theme-dark");r.classList.add("theme-"+t);
if(document.querySelector('meta[name="vietpos-doc"]')){var l=document.createElement("link");l.id="md-theme-css";l.rel="stylesheet";l.href=MD[t];document.head.appendChild(l);}})();
</script>"""
ROUTES_DIR = SHOP / "artifacts/api-server/src/routes"
PAGES_DIR = SHOP / "artifacts/pos-app/src/pages"
SCHEMA_DIR = SHOP / "lib/db/src/schema"
LIB_ROOT = SHOP / "artifacts/api-server/src/lib"
APP_TSX = SHOP / "artifacts/pos-app/src/App.tsx"
APP_LAYOUT = SHOP / "artifacts/pos-app/src/components/layout/app-layout.tsx"
COMPONENTS_DIR = SHOP / "artifacts/pos-app/src/components"

# Route → file nghiệp vụ (gợi ý đọc thêm)
ROUTE_NGHIEP_VU: dict[str, str] = {
    "/login": nghiep_vu_path("01-dang-nhap-va-shop-context"),
    "/dashboard": nghiep_vu_path("01-dang-nhap-va-shop-context"),
    "/pos": nghiep_vu_path("02-pos-ban-hang"),
    "/orders": nghiep_vu_path("02-pos-ban-hang"),
    "/products": nghiep_vu_path("03-san-pham-va-ton"),
    "/inventory": nghiep_vu_path("03-san-pham-va-ton"),
    "/stock-requests": nghiep_vu_path("04-phieu-nhap-xuat-chuyen-kho"),
    "/purchase-orders": nghiep_vu_path("04-phieu-nhap-xuat-chuyen-kho"),
    "/vat-invoices": nghiep_vu_path("05-hoa-don-vat-xuat"),
    "/vat-inbound": nghiep_vu_path("06-hoa-don-dau-vao-tong-quan"),
    "/access-block": nghiep_vu_path("10-truy-cap-an-ninh"),
}

_MENU_BY_HREF: dict[str, dict[str, str]] | None = None

ROUTE_RE = re.compile(
    r'router\.(get|post|patch|put|delete)\(\s*["\']([^"\']+)["\']',
    re.IGNORECASE,
)
ROUTE_BLOCK_RE = re.compile(
    r'router\.(get|post|patch|put|delete)\(\s*["\']([^"\']+)["\'](.*?)async\s*\(',
    re.DOTALL | re.IGNORECASE,
)
PG_TABLE_RE = re.compile(r'pgTable\(\s*["\']([^"\']+)["\']')
COL_RE = re.compile(r'^\s*(\w+):\s*\w+\(["\']([^"\']+)["\']', re.MULTILINE)
FK_RE = re.compile(r'\.references\(\(\)\s*=>\s*(\w+)', re.MULTILINE)

# schema TS stem → route file (khi không trùng camelToKebab)
SCHEMA_ROUTE_ALIAS: dict[str, str] = {
    "stockTransfers": "chain",
    "warehouses": "chain",
    "shopVariantStock": "inventory",
    "inventoryMovements": "inventory",
    "vatInboundInvoices": "vat-inbound",
    "vatInboundAuditLogs": "vat-inbound",
    "orgGdtTaxSessions": "org-gdt-portal",
    "orderAuditLogs": "order-audit-reports",
    "productAuditLogs": "product-audit-reports",
    "posCartAuditLogs": "pos-cart-audit",
    "purchaseOrders": "purchase-orders",
    "shopApiKeys": "shop-api-keys",
    "salesStaff": "sales-staff",
    "shiftSessions": "shift-sessions",
    "productCategories": "product-categories",
    "userNotifications": "notifications",
    "customerFeedback": "feedback",
    "agentChat": "agent",
    "shopDailyVisitorCounts": "walk-in-customers",
    "orderPreprintReservations": "orders",
    "orderSyncKeys": "sync",
    "allowedDevices": "access-observations",
    "blockedDevices": "blocked-devices",
    "blockedIps": "blocked-ips",
    "deviceLoginEvents": "access-observations",
}

SCHEMA_DOMAINS: list[tuple[str, str, list[str]]] = [
    (
        "Tài khoản, shop & tổ chức",
        "users, shops, organizations, nhân viên bán, reset PIN.",
        [
            "users",
            "shops",
            "organizations",
            "salesStaff",
            "pinResetRequests",
        ],
    ),
    (
        "An ninh truy cập",
        "Chặn IP/thiết bị, allowlist, sự kiện đăng nhập.",
        [
            "blockedIps",
            "blockedDevices",
            "allowedDevices",
            "deviceLoginEvents",
        ],
    ),
    (
        "POS & đơn hàng",
        "Đơn, dòng đơn, ca, in trước, đồng bộ offline, audit POS.",
        [
            "orders",
            "orderItems",
            "shiftSessions",
            "orderPreprintReservations",
            "orderSyncKeys",
            "orderAuditLogs",
            "posCartAuditLogs",
            "reprintLogs",
            "paymentChangeLogs",
            "invoiceChangeLogs",
        ],
    ),
    (
        "Sản phẩm & tồn",
        "SP, biến thể, danh mục, tồn shop, biến động, NCC.",
        [
            "products",
            "productVariants",
            "productCategories",
            "inventory",
            "inventoryMovements",
            "shopVariantStock",
            "suppliers",
            "productAuditLogs",
        ],
    ),
    (
        "Kho, phiếu & đặt hàng",
        "Kho vật lý, phiếu nhập/xuất, chuyển kho, PO.",
        [
            "warehouses",
            "stockRequests",
            "stockTransfers",
            "purchaseOrders",
        ],
    ),
    (
        "Hóa đơn đầu vào & CQT",
        "HĐ mua vào, audit, phiên GDT.",
        [
            "vatInboundInvoices",
            "vatInboundAuditLogs",
            "orgGdtTaxSessions",
        ],
    ),
    (
        "Thông báo, widget & nhật ký hệ thống",
        "API key, khách qua cửa, feedback, AI chat, event log.",
        [
            "shopApiKeys",
            "shopDailyVisitorCounts",
            "customerFeedback",
            "agentChat",
            "platformNotificationSettings",
            "userNotifications",
            "changeLog",
            "systemEventLogs",
            "shopOperationalEvents",
        ],
    ),
]

SCHEMA_STEM_REL: dict[str, str] = {}

EXPORT_RE = re.compile(
    r"^export (?:async )?function (\w+)|^export const (\w+)\s*=",
    re.MULTILINE,
)

# Ghi chú chi tiết HĐ đầu vào (bổ sung bảng endpoint)
VAT_INBOUND_ENDPOINT_NOTES: dict[str, str] = {
    "GET /vat-inbound": "Danh sách HĐ mua vào của **hub shop**; không trả `pdfBase64` (chỉ cờ `hasPdf`); tự relink PO nếu thiếu; join trạng thái PO.",
    "GET /vat-inbound/marked-mst-archive": "Đọc chuỗi MST lọc từ `organizations.vat_inbound_auto_archive_tax_codes`.",
    "PATCH /vat-inbound/marked-mst-archive": "Lưu MST lọc (admin/manager); normalize input; **backfill** archive HĐ trùng MST ngay sau lưu.",
    "POST /vat-inbound/backfill-marked-mst-archive": "Chạy lại backfill archive theo MST (ops / sau migration).",
    "POST /vat-inbound/gdt/captcha": "Lấy captcha CQT cho org `gdt_direct` — trả session tạm captcha store.",
    "POST /vat-inbound/gdt/reconnect": "Đăng nhập lại CQT sau captcha; lưu session org GDT.",
    "POST /vat-inbound/sync-tax": "Kéo HĐ từ CQT/Viettel theo `from`/`to`; map XML → DB; auto archive MST; có thể split khoảng dài.",
    "GET /vat-inbound/:id/pdf": "Tải PDF base64 đã lưu hoặc fetch Viettel nếu thiếu.",
    "GET /vat-inbound/:id": "Chi tiết một HĐ (metadata + stock lines, không full PDF trong list).",
    "POST /vat-inbound": "Upsert HĐ (import PDF/Excel từ client); parse fields; sync archive MST on write.",
    "POST /vat-inbound/:id/verify-viettel": "Xác thực HĐ với Viettel SInvoice; cập nhật trạng thái verify.",
    "POST /vat-inbound/:id/stock-receipt": "Ghép dòng HĐ ↔ SP; tạo/cập nhật `stockLines`; có thể tạo SP/NCC/PO inline.",
    "GET /vat-inbound/:id/purchase-order": "Lấy PO gắn HĐ (nếu có).",
    "POST /vat-inbound/:id/receive-stock": "Nhập kho theo dòng đã ghép; cập nhật tồn + giá vốn BQ; đổi `stockStatus`.",
    "POST /vat-inbound/:id/restore-line": "Khôi phục dòng đã loại trừ khỏi ghép hàng.",
    "POST /vat-inbound/:id/dismiss-excluded-lines": "Bỏ qua dòng không nhập (phí, dịch vụ…) — ghi audit.",
    "POST /vat-inbound/:id/undo-dismiss-excluded-lines": "Hoàn tác bỏ qua dòng (nếu policy cho phép).",
    "POST /vat-inbound/:id/request-undo-dismiss-excluded": "NV gửi yêu cầu hoàn tác bỏ qua dòng.",
    "POST /vat-inbound/:id/approve-undo-dismiss-excluded": "Quản lý duyệt hoàn tác bỏ qua dòng.",
    "POST /vat-inbound/:id/reject-undo-dismiss-excluded": "Từ chối yêu cầu hoàn tác bỏ qua dòng.",
    "POST /vat-inbound/:id/close-short": "Chốt nhập **thiếu** — đóng phiếu với trạng thái `closed_short`.",
    "POST /vat-inbound/:id/request-rollback": "Yêu cầu hoàn tác nhập kho (rollback inventory).",
    "POST /vat-inbound/:id/approve-rollback": "Duyệt rollback — trừ lại tồn đã nhập.",
    "POST /vat-inbound/:id/reject-rollback": "Từ chối yêu cầu rollback.",
    "GET /vat-inbound/:id/audit-logs": "Nhật ký thao tác trên HĐ (`vat_inbound_audit_logs`).",
    "POST /vat-inbound/:id/archive": "Lưu trữ thủ công (`archivedAt`).",
    "POST /vat-inbound/:id/unarchive": "Bỏ lưu trữ.",
    "DELETE /vat-inbound/:id": "Xóa HĐ (policy + trạng thái kho); thường admin.",
}

# Mô tả một dòng cho mục lục (he-thong / nghiep-vu)
HE_THONG_DESC: dict[str, str] = {
    "00-huong-dan-doc-tai-lieu.md": "Cách đọc VietPOS-Map: ba tầng tài liệu, lộ trình theo việc cần làm, tránh lạc trong ~250 file.",
    "ban-do-kien-truc.md": "Bản đồ hình (ASCII): kiến trúc VietPOS + cách đi trong tài liệu Map — xem được mọi trình đọc markdown.",
    "he-thong/01-kien-truc-runtime.md": "Sơ đồ runtime: client React → Express API → PostgreSQL; tùy chọn cloud-sync Railway.",
    "he-thong/02-workspace-luu-niem.md": "Các repo trong LuuNiem (Shop, Widget, Map, ESP32, HDSD) và vai trò từng thư mục.",
    "he-thong/03-monorepo-packages.md": "Cấu trúc pnpm workspace: artifacts, lib, scripts trong Shop-Manager.",
    "he-thong/04-docker-va-cloud-sync.md": "Docker Compose local, biến CLOUD_DATABASE_URL, worker cloud-sync và Trợ lý AI.",
}

NGHIEP_VU_DESC: dict[str, str] = {
    "nghiep-vu/01-dang-nhap-va-shop-context.md": "Đăng nhập, JWT gắn shop/role, hub shop và ngữ cảnh vận hành API.",
    "nghiep-vu/02-pos-ban-hang.md": "Luồng POS: ca làm việc, giỏ hàng, thanh toán, in bill, hủy đơn và audit.",
    "nghiep-vu/03-san-pham-va-ton.md": "Quản lý sản phẩm, import Excel, tồn shop và điều chỉnh inventory.",
    "nghiep-vu/04-phieu-nhap-xuat-chuyen-kho.md": "Phiếu stock-request, chuyển kho chuỗi, PO và liên kết nhập hàng.",
    "nghiep-vu/05-hoa-don-vat-xuat.md": "Hóa đơn VAT bán ra qua Viettel SInvoice và cấu hình org.",
    "nghiep-vu/06-hoa-don-dau-vao-tong-quan.md": "Vòng đời HĐ mua vào: import, ghép SP, nhập kho, trạng thái stockStatus.",
    "nghiep-vu/07-hd-dau-vao-mst-loc.md": "MST lọc tự archive HĐ; tab Khác / Lưu trữ / Đang dùng; modal trên trang HĐ đầu vào.",
    "nghiep-vu/08-hd-dau-vao-cqt-sync.md": "Kéo HĐ từ CQT (GDT direct): captcha, sync-tax, map XML vào DB.",
    "nghiep-vu/09-chuoi-va-da-chi-nhanh.md": "Organization, nhiều shop, kho trung tâm, dashboard chuỗi và heartbeat.",
    "nghiep-vu/10-truy-cap-an-ninh.md": "Chặn IP/thiết bị, quan sát truy cập và RBAC liên quan.",
    "nghiep-vu/11-offline-va-sync-client.md": "IndexedDB local-db, checkout offline, pull/push sync với server.",
    "nghiep-vu/12-widget-va-dem-khach.md": "App widget Android, ESP32 visitor-counts và shop API keys.",
}

DOC_DESCRIPTIONS: dict[str, str] = {}

MIRROR_FROM_SHOP = [
    "docs/architecture.md",
    "docs/api-routes.md",
    "docs/database.md",
    "docs/rbac.md",
    "docs/business-flows.md",
    "docs/offline-first.md",
    "docs/offline-first-audit.md",
    "docs/offline-first-roadmap.md",
    "docs/docker-may-chu.md",
    "docs/running-local.md",
    "docs/code-tour/api-server.md",
    "docs/code-tour/pos-app.md",
    "docs/code-tour/db.md",
    "docs/code-annotations.md",
    "docs/public-access.md",
]

# Vietnamese intros per API module (expanded manually)
API_MODULE_INTRO: dict[str, str] = {
    "vat-inbound": """
Module **lớn nhất** về HĐ mua vào VAT: import PDF/Excel, kéo **CQT/Viettel**, ghép SP, nhập kho,
lưu trữ, MST lọc (tab Khác), audit, hoàn tác nhập kho / bỏ ghép dòng.

**Lib quan trọng:** `lib/vat-inbound-tax-sync.ts`, `lib/gdt-portal/*`, `lib/vat-inbound-auto-archive-mst.ts`,
`lib/viettel-sinvoice/*`, `lib/inbound-stock-receive.ts`.

**Giao diện:** `pages/vat-inbound.tsx`, `lib/vat-inbound-api.ts`, IndexedDB `@workspace/local-db`.

**Quyền:** hub shop + `requireVatInboundAccess` (admin, manager, accountant, warehouse_keeper tại CN chính).
""",
    "orders": """
Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (`shift-sessions`), audit cart.

**Giao diện:** `pages/pos.tsx`, `pages/orders.tsx`, `lib/offline/checkout.ts` (offline).
""",
    "chain": """
Tổ chức, shop, kho, điều chuyển (`transfers`). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).

**Giao diện:** `pages/chain.tsx`, `chain-dashboard.tsx`.
""",
    "stock-requests": """
Phiếu yêu cầu nhập/xuất nội bộ: tạo → duyệt → hoàn tất → cập nhật tồn.

**Giao diện:** `pages/stock-requests.tsx`.
""",
    "products": """
Quản lý sản phẩm (thêm/sửa/xóa), import Excel, biến thể, ẩn/hiện SP, giá/giá vốn theo role.

**Giao diện:** `pages/products.tsx`.
""",
    "agent": """
Trợ lý AI: chat, thông tin hệ thống (DB, đồng bộ cloud, shop online), cấp quyền `agent_assistant_enabled`.

**Giao diện:** `pages/agent-assistant.tsx`, `agent-chat-audit.tsx`.
""",
    "widget": """
API phục vụ app Android widget: thống kê quầy (JWT / shop context).

**Repo:** `VietPOS-Widget/`.
""",
    "shop-api-keys": """
API key cho widget / thiết bị (ESP32 visitor-counts).

**Giao diện:** `pages/chain-api-keys.tsx` (nếu có).
""",
    "org-gdt-portal": """
Session CQT trực tiếp (captcha, connect) — dùng chung org với HĐ đầu vào.
""",
    "sync": """
API đồng bộ client (kéo/đẩy) cho IndexedDB offline.
""",
    "blocked-ips": """
Danh sách IP bị chặn toàn cục trên **mọi** request `/api/*`.

- **Quyền:** `requireAuth` + role **`super_admin`** (403 nếu không đủ).
- Sau POST/DELETE: gọi `refreshIpDenylistFromDb()` — cache in-memory middleware cập nhật ngay.
- GET trả thêm `envDenylistEnabled` (biến `IP_DENYLIST` / `BLOCKED_IPS`) và `describeSeenClientIp(req)`.

**Middleware:** `ipDenylistMiddleware()` mount trên `/api` trong `app.ts` (trước router).

**Lib:** `lib/ip-denylist.ts`. **UI:** tab **Chặn IP** trong `access-block.tsx` → `IpBanSection`.
""",
    "blocked-devices": """
Danh sách **Device ID** (header client) bị chặn mọi `/api/*`.

- **Quyền:** `super_admin` (giống blocked-ips).
- Device ID lấy từ client (`x-device-id` / cookie — xem `device-denylist.ts`).

**Middleware:** `deviceDenylistMiddleware()` trên `/api`.

**UI:** tab **Chặn thiết bị** → `DeviceBanSection` trong `access-block.tsx`.
""",
    "access-observations": """
Tổng hợp **cặp (deviceId, IP)** đã gọi API — lưu **in-memory** (TTL giờ, xem `accessObservationTtlHours`).

- Dùng tab **Tổng quan** trên `/access-block`: bảng hit count, chặn nhanh IP hoặc thiết bị từ một dòng.
- Ghi nhận qua `accessObservationMiddleware()` trên mọi `/api` (không chặn, chỉ quan sát).

**Lib:** `lib/api-access-observations.ts`. **UI:** `AccessOverviewSection`.
""",
}

# Một dòng tiếng Việt cho module API chưa có intro dài
API_MODULE_SHORT_VI: dict[str, str] = {
    "access-observations": "Quan sát cặp thiết bị + IP gọi API (RAM, TTL).",
    "agent": "Trợ lý AI: chat và công cụ đọc dữ liệu kinh doanh.",
    "auth": "Đăng nhập, JWT, PIN, phiên người dùng.",
    "blocked-devices": "Quản lý danh sách thiết bị bị chặn mọi `/api`.",
    "blocked-ips": "Quản lý IP bị chặn mọi `/api`.",
    "chain": "Tổ chức, shop, kho, điều chuyển hàng.",
    "dashboard": "Số liệu tổng quan: doanh thu, đơn, tồn thấp.",
    "feedback": "Phản hồi khách và form công khai.",
    "health": "Kiểm tra service còn sống (`healthz`).",
    "inventory": "Tồn kho cấp shop (số lượng POS).",
    "media": "Upload và quản lý file media.",
    "notification-settings": "Cấu hình thông báo platform/org.",
    "notifications": "Thông báo in-app cho user.",
    "order-audit-reports": "Báo cáo audit đơn hàng.",
    "orders": "Đơn POS: tạo, hủy, duyệt, in lại.",
    "org-gdt-portal": "Phiên đăng nhập CQT (captcha).",
    "org-viettel-settings": "Cấu hình Viettel SInvoice theo org.",
    "pos-cart-audit": "Audit thao tác giỏ hàng POS.",
    "product-audit-reports": "Báo cáo thay đổi sản phẩm.",
    "product-categories": "Danh mục sản phẩm.",
    "products": "Sản phẩm: thêm/sửa/xóa, import Excel, biến thể.",
    "public-vat-invoice": "API/form HĐ VAT công khai.",
    "purchase-order-audit-reports": "Báo cáo audit phiếu mua.",
    "purchase-orders": "Phiếu đặt mua (PO).",
    "reports": "Báo cáo nhân viên, in lại bill.",
    "sales-staff": "Nhân viên bán hàng gắn quầy.",
    "shift-sessions": "Ca làm việc mở/đóng.",
    "shop-api-keys": "API key shop (widget, ESP32).",
    "shops": "Danh sách shop user được truy cập.",
    "staff": "Quản lý tài khoản nhân viên (admin).",
    "statistics": "Thống kê bán theo sản phẩm.",
    "stock-request-audit-reports": "Báo cáo audit phiếu nhập/xuất.",
    "stock-requests": "Phiếu yêu cầu nhập/xuất nội bộ.",
    "suppliers": "Nhà cung cấp.",
    "sync": "Đồng bộ offline IndexedDB ↔ server.",
    "system-events": "Sự kiện / lỗi hệ thống.",
    "vat-inbound": "Hóa đơn mua vào VAT (lớn nhất).",
    "walk-in-customers": "Khách vãng lai (walk-in).",
    "widget": "API cho app widget Android.",
}

# Spec đầy đủ module an ninh (summary = 1 dòng bảng; detail = markdown dưới mục endpoint)
ACCESS_ENDPOINT_SPEC: dict[str, dict[str, str]] = {
    "GET /blocked-ips": {
        "summary": "Liệt kê IP bị chặn; kèm IP client đang xem và cờ denylist từ env.",
        "detail": """
**URL:** `GET /api/blocked-ips`

**Quyền:** Cookie/JWT qua `requireAuth` → trong handler bắt buộc `req.auth.role === "super_admin"`.

| HTTP | Khi nào | Body lỗi (JSON) |
|------|---------|-----------------|
| **403** | Không phải super_admin | `{ "error": "Chỉ quản trị hệ thống được quản lý IP bị chặn" }` |
| **500** | Lỗi DB / chưa có bảng | `{ "error": "Không tải được danh sách IP. Cập nhật cơ sở dữ liệu (pnpm --filter @workspace/db push) rồi thử lại." }` |

**Response 200:**

| Trường | Kiểu | Ý nghĩa |
|--------|------|---------|
| `items[]` | array | Mỗi phần tử: `id`, `ip`, `note`, `createdAt` (ISO), `createdByLabel` (tên hoặc email người tạo) |
| `envDenylistEnabled` | boolean | `true` nếu có `IP_DENYLIST` hoặc `BLOCKED_IPS` trong env (chặn thêm ngoài DB) |
| `seenClientIp` | string | IP đã dùng để đối chiếu denylist (proxy-aware) |
| `socketIp` | string | IP socket trực tiếp |
| `trustProxy` | boolean | Express trust proxy |
| `xForwardedFor` | string \\| null | Header X-Forwarded-For nếu có |

**Side effect:** không đổi DB (chỉ đọc). Sau POST/DELETE module khác gọi `refreshIpDenylistFromDb()`.
""",
    },
    "POST /blocked-ips": {
        "summary": "Thêm một IP vào `blocked_ips`; refresh cache denylist.",
        "detail": """
**URL:** `POST /api/blocked-ips`

**Quyền:** `requireAuth` + **super_admin** (403 giống GET).

**Request body** (`application/json`):

| Trường | Bắt buộc | Mô tả |
|--------|----------|--------|
| `ip` | có | Chuỗi IPv4/IPv6; server `normalizeClientIp` + `isValidBlockedIp` |
| `note` | không | Ghi chú, tối đa 500 ký tự |

**Response 201:** `{ id, ip, note, createdAt, createdByLabel: null }`

| HTTP | Khi nào | `error` |
|------|---------|---------|
| **400** | Thiếu/sai `ip` | `"Cần địa chỉ IP"` hoặc `"Địa chỉ IP không hợp lệ"` |
| **409** | Trùng IP (unique) | `"IP này đã có trong danh sách chặn"` |
| **500** | Lỗi insert | `"Không thêm được IP vào danh sách chặn"` |

**Side effect:** insert `blocked_ips`; gọi `refreshIpDenylistFromDb()` — middleware chặn IP ngay trên mọi `/api/*`.
""",
    },
    "DELETE /blocked-ips/:id": {
        "summary": "Xóa một dòng `blocked_ips` theo id; refresh cache.",
        "detail": """
**URL:** `DELETE /api/blocked-ips/:id`

**Quyền:** `requireAuth` + **super_admin**.

**Path:** `id` — số nguyên dương (PK bảng `blocked_ips`).

| HTTP | Khi nào | Body |
|------|---------|------|
| **400** | `id` không hợp lệ | `{ "error": "ID không hợp lệ" }` |
| **404** | Không có dòng | `{ "error": "Không tìm thấy IP trong danh sách" }` |
| **200** | OK | `{ "ok": true }` |
| **500** | Lỗi xóa | `{ "error": "Không xóa được IP khỏi danh sách" }` |

**Side effect:** `refreshIpDenylistFromDb()`.
""",
    },
    "GET /blocked-devices": {
        "summary": "Liệt kê thiết bị bị chặn + Device ID request hiện tại.",
        "detail": """
**URL:** `GET /api/blocked-devices`

**Quyền:** `requireAuth` + **super_admin** (403: `"Chỉ quản trị hệ thống được quản lý thiết bị bị chặn"`).

**Response 200:**

| Trường | Ý nghĩa |
|--------|---------|
| `items[]` | `id`, `deviceId`, `deviceName` (từ `allowed_devices` nếu có), `note`, `createdAt`, `createdByLabel` |
| `thisDeviceId` | Device ID client gửi lên request (header/cookie — xem `device-denylist.ts`) |

**500:** `{ "error": "Không tải được danh sách. Chạy pnpm --filter @workspace/db run apply:blocked-devices rồi thử lại." }`
""",
    },
    "POST /blocked-devices": {
        "summary": "Thêm Device ID vào denylist; refresh cache.",
        "detail": """
**URL:** `POST /api/blocked-devices`

**Quyền:** super_admin.

**Body JSON:**

| Trường | Bắt buộc | Mô tả |
|--------|----------|--------|
| `deviceId` hoặc `device_id` | có | Chuỗi 8–128 ký tự sau `normalizeDeviceId` |
| `note` | không | ≤ 500 ký tự |

**201:** `{ id, deviceId, deviceName, note, createdAt, createdByLabel: null }`

| HTTP | `error` |
|------|---------|
| **400** | `"Cần Device ID"` / `"Device ID không hợp lệ (8–128 ký tự)"` |
| **409** | `"Thiết bị này đã có trong danh sách chặn"` |
| **500** | `"Không thêm được thiết bị vào danh sách chặn"` |

**Side effect:** `refreshDeviceDenylistFromDb()`.
""",
    },
    "DELETE /blocked-devices/:id": {
        "summary": "Bỏ chặn thiết bị theo id bảng `blocked_devices`.",
        "detail": """
**URL:** `DELETE /api/blocked-devices/:id`

**Quyền:** super_admin. Path `id` — integer > 0.

| HTTP | Body |
|------|------|
| **400** | `{ "error": "ID không hợp lệ" }` |
| **404** | `{ "error": "Không tìm thấy thiết bị trong danh sách" }` |
| **200** | `{ "ok": true }` |
| **500** | `{ "error": "Không xóa được thiết bị khỏi danh sách" }` |

**Side effect:** `refreshDeviceDenylistFromDb()`.
""",
    },
    "GET /access-observations": {
        "summary": "Bảng quan sát cặp deviceId+IP (RAM, TTL ~48h).",
        "detail": """
**URL:** `GET /api/access-observations`

**Quyền:** super_admin (403: `"Chỉ quản trị hệ thống được xem tổng quan truy cập"`).

**Query:**

| Param | Mặc định | Mô tả |
|-------|----------|--------|
| `limit` | `200` | Số dòng trả về (parse number; NaN → 200) |

**Response 200:**

| Trường | Ý nghĩa |
|--------|---------|
| `items[]` | Mỗi dòng: `deviceId`, `ip`, `hitCount`, `todayHitCount`, `firstSeen`, `lastSeen` (ISO), `deviceName` |
| `today` | `{ calendarDay, totalHits, uniqueDevices, uniqueIps, activePairs }` — theo lịch VN |
| `ttlHours` | TTL store (lib: 48h) |
| `storage` | Luôn `"memory"` — **mất khi restart API** |

**Ghi nhận dữ liệu:** middleware `accessObservationMiddleware` trên mọi `/api` (không chặn).

**500:** `{ "error": "Không tải được tổng quan truy cập" }`
""",
    },
}


def access_endpoint_key(method: str, path: str) -> str:
    return f"{method} {path}"


def endpoint_summary(module_key: str, method: str, path: str, middleware: list[str]) -> str:
    key = access_endpoint_key(method, path)
    if key in ACCESS_ENDPOINT_SPEC:
        base = ACCESS_ENDPOINT_SPEC[key]["summary"]
        mw = ", ".join(middleware) if middleware else "requireAuth"
        return f"{base} Route: `{mw}` + **super_admin** trong handler."
    if module_key == "vat-inbound" and key in VAT_INBOUND_ENDPOINT_NOTES:
        note = VAT_INBOUND_ENDPOINT_NOTES[key]
        if middleware:
            note += f" Lớp kiểm tra: `{', '.join(middleware)}`."
        return note
    api = path if path.startswith("/") else f"/{path}"
    mw = ", ".join(middleware) if middleware else "requireAuth (mặc định — xem file)"
    return f"Đường dẫn đầy đủ `/api{api}`. Lớp kiểm tra: `{mw}`."


def endpoint_detail_body(method: str, path: str) -> str:
    key = access_endpoint_key(method, path)
    spec = ACCESS_ENDPOINT_SPEC.get(key)
    return spec.get("detail", "").strip() if spec else ""

PAGE_DOCS: dict[str, str] = {
    "pos.tsx": """
**Đường dẫn:** `/pos`

Màn hình bán hàng chính: tìm SP, giỏ hàng, thanh toán, yêu cầu HĐ VAT, mở/đóng ca.
Offline: ghi Dexie qua `checkoutOffline()`; sync sau khi có mạng.

**File lớn** — tìm theo: cart state, barcode, payment method, print bill, de nghị hủy đơn.
**Quyền:** `userCanUsePos`, NV bán hàng / thu ngân.
""",
    "vat-inbound.tsx": """
**Đường dẫn:** `/vat-inbound`

## Cấu trúc UI

- **Tab Hoá đơn:** lọc archive (Tất cả / Đang dùng / Lưu trữ / **Khác**), lọc trạng thái ghép hàng, lọc ngày.
- **Tab Danh sách phiếu:** HĐ đã ghép — chờ nhập kho, thiếu, đã nhận, đề nghị hoàn tác, ghép thiếu dòng.
- **Toolbar:** MST lọc (modal), Mẫu Excel, Nhập Excel, Nhập PDF.
- **Khối Lấy từ cơ quan thuế:** chọn from/to, POST sync-tax; toast archive MST.

## State & logic quan trọng

- `PageTab`: `invoices` | `receipts`.
- `InvoiceArchiveFilter`: `active` | `archived` | `other` | `all` — HĐ trùng MST lọc vào **Khác**.
- IndexedDB `allRows` merge server qua `mergeServerInvoices`, `listVatInboundInvoices`.
- Parse PDF local: `parseVatInboundPdfBytes`, revision `VAT_INBOUND_PARSE_REVISION`.
- Ghép hàng: `openStockReceipt`, `createVatInboundStockReceipt`, PO inline trên HĐ.
- Dialog chi tiết HĐ: dòng VAT, ghép SP, nhật ký audit, PDF preview.

## API client (`lib/vat-inbound-api.ts`)

- `syncVatInboundFromTax`, `saveVatInboundMarkedMstArchive`, `getVatInboundMarkedMstArchive`
- `createVatInboundStockReceipt`, `receiveVatInboundStock`, `archiveVatInboundInvoice`
- Upsert/list: `listVatInboundFromApi`, `upsertVatInboundToApi`

## Quyền

- `canAccess`: hub + role accountant/manager/admin/warehouse_keeper (xem file đầu component).
- `canEditMarkedMst`: admin/manager — MST lọc modal.
""",
    "stock-requests.tsx": """
**Đường dẫn:** `/stock-requests`

Phiếu nhập/xuất: trạng thái chờ duyệt, vận chuyển, nhận hàng, huỷ.
""",
    "chain.tsx": """
**Đường dẫn:** `/chain`

Sửa tổ chức: thông tin, shop, Viettel inbound/outbound, CQT, Trợ lý AI, URL feedback công khai.
""",
    "products.tsx": """
**Đường dẫn:** `/products`

Danh mục SP: grid/table, import Excel, variant, giá, ảnh.
""",
    "inventory.tsx": """
**Đường dẫn:** `/inventory`

Tồn kho shop: số lượng, tạo phiếu nhập từ SP sắp hết (thủ kho).
""",
    "vat-invoices.tsx": """
**Đường dẫn:** `/vat-invoices`

HĐ VAT **xuất** (Viettel SInvoice): phát hành, tra cứu, điều chỉnh theo tích hợp Viettel.
""",
    "agent-assistant.tsx": """
**Đường dẫn:** `/agent-assistant`

Trợ lý AI + panel hệ thống (DB, cloud sync URL, shops online). Chat khi đã cấu hình LLM org.
""",
    "dashboard.tsx": """
**Đường dẫn:** `/dashboard`

Tổng quan doanh thu, đơn, tồn thấp — theo quyền và scope shop.
""",
    "login.tsx": """
**Đường dẫn:** `/login`

Email/password, PIN máy, tài khoản đã lưu trên thiết bị. JWT → `pos_token`.
""",
    "my-permissions.tsx": """
**Đường dẫn:** `/my-permissions`

Giải thích quyền role hiện tại (đối chiếu menu thực tế).
""",
    "access-block.tsx": """
**Đường dẫn:** `/access-block` (query `?tab=overview|ip|device`)

## Vai trò

Trang **quản trị hệ thống** gom ba màn con thành một: quan sát truy cập bất thường, quản lý denylist IP, denylist thiết bị.
Mọi denylist áp dụng **trước** handler API — client bị chặn nhận 403 trên `/api/*`.

## Quyền

| Điều kiện | Hành vi |
|-----------|---------|
| `user.role === "super_admin"` | Hiển thị đủ 3 tab |
| Role khác | `<Redirect to="/dashboard" />` ngay khi mount |

Menu sidebar: mục **Chặn truy cập** (`app-layout.tsx`, icon `Ban`) — `show: isSuperAdmin`.

## Cấu trúc UI

1. **Header:** tiêu đề + mô tả ngắn (mọi request `/api` bị từ chối nếu nằm trong denylist).
2. **Tabs (3 cột):**
   - **Tổng quan** → `<AccessOverviewSection />` — bảng quan sát, chặn nhanh.
   - **Chặn IP** → `<IpBanSection />` — CRUD `blocked_ips`.
   - **Chặn thiết bị** → `<DeviceBanSection />` — CRUD `blocked_devices`.

Tab mặc định: `initialTabFromSearch()` đọc `?tab=` (`ip` | `device` | mặc định `overview`).

## Route legacy (App.tsx)

| URL cũ | Chuyển tới |
|--------|------------|
| `/ip-ban` | `/access-block?tab=ip` |
| `/device-ban` | `/access-block?tab=device` |
| `/access-block/overview` | `/access-block?tab=overview` |

File `ip-ban.tsx` / `device-ban.tsx` vẫn tồn tại như **section export** (không còn route riêng).

## Luồng nghiệp vụ (tóm tắt)

```
Request /api/*
  → accessObservationMiddleware (ghi hit device+IP, RAM)
  → ipDenylistMiddleware (403 nếu IP trong DB/env)
  → deviceDenylistMiddleware (403 nếu device id trong DB)
  → router handlers
```

Super admin mở **Tổng quan** → thấy IP/device lạ → bấm **Chặn** → POST blocked-* → middleware refresh cache.

## API (spec đầy đủ trong Map)

Mỗi module có bảng endpoint + **body/response/mã lỗi** từng route:

- `module-api/chan-ip-api/README.md` — blocked-ips
- `module-api/chan-thiet-bi-api/README.md` — blocked-devices
- `module-api/quan-sat-truy-cap/README.md` — access-observations

## Đọc tiếp

- Nghiệp vu: `nghiep-vu/10-truy-cap-an-ninh/README.md`
- Lib: `thu-vien/ip-denylist/README.md`, `thu-vien/device-denylist/README.md`, `thu-vien/api-access-observations/README.md`
- Schema: `co-so-du-lieu/ip-bi-chan/README.md`, `co-so-du-lieu/thiet-bi-bi-chan/README.md`
""",
    "access-overview-section.tsx": """
**Không có route riêng** — embed trong tab **Tổng quan** của `/access-block`.

## API

- `GET /api/access-observations?limit=200` — React Query key `["access-observations"]`.
- Chặn nhanh: `POST /api/blocked-ips` hoặc `POST /api/blocked-devices` (note tự động ghi nguồn quan sát).

## UI chính

- Thẻ thống kê **hôm nay:** tổng hit, số device, số IP, số cặp active.
- Bảng: device (tên nếu có trong `allowed_devices`), IP, hit tổng / hit hôm nay, first/last seen.
- Nút **Làm mới**, **Chặn IP**, **Chặn thiết bị** trên từng dòng (confirm dialog).
- Trạng thái đã chặn: nút disabled + icon check.

## Ghi chú kỹ thuật

- Dữ liệu quan sát **không** lưu Postgres — mất khi restart API (TTL vài giờ).
- `deviceName` join từ `lookupDeviceNamesByDeviceIds`.
""",
    "ip-ban.tsx": """
**Export:** `IpBanSection` (dùng trong `access-block.tsx`, tab **Chặn IP**).

## API (React Query `["blocked-ips"]`)

| Thao tác | HTTP |
|----------|------|
| Tải danh sách | `GET /api/blocked-ips` |
| Thêm | `POST /api/blocked-ips` body `{ ip, note? }` |
| Bỏ chặn | `DELETE /api/blocked-ips/:id` |

Response GET gồm `items[]`, `envDenylistEnabled` (denylist từ biến môi trường).

## UI

- Form: IP + ghi chú (optional) → **Thêm IP**.
- Bảng: IP, ghi chú, người tạo, thời gian; **Bỏ chặn** (AlertDialog).
- Card cảnh báo nếu `envDenylistEnabled` (IP chặn thêm từ env, không chỉ DB).
""",
    "orders.tsx": """
**Đường dẫn:** `/orders`

Trang **vỏ mỏng** (~20 dòng): toàn bộ UI/logic nằm trong **`OrdersPanel`** (`components/OrdersPanel.tsx`, prop `variant="page"`).

## Redirect query (useEffect)

| Query | Hành vi |
|-------|---------|
| `invoiceStatus` hoặc `vat=1` | Chuyển sang `/vat-invoices` (giữ `shopId` nếu có) |

Dùng cho link cũ / badge menu trỏ nhầm sang orders thay vì HĐ VAT.

## Nghiệp vụ (trong OrdersPanel)

- Danh sách đơn theo shop; lọc trạng thái, tìm kiếm.
- Hủy đơn / duyệt hủy (role admin); in lại bill → `reprint_logs`.
- API chủ yếu module **`orders`** — xem `api-modules/orders.md`.

**Mirror:** `nghiep-vu/02-pos-ban-hang.md`.
""",
    "device-ban.tsx": """
**Export:** `DeviceBanSection` (tab **Chặn thiết bị** trên `/access-block`).

## API (React Query `["blocked-devices"]`)

| Thao tác | HTTP |
|----------|------|
| Tải danh sách | `GET /api/blocked-devices` |
| Thêm | `POST /api/blocked-devices` body `{ deviceId, note? }` |
| Bỏ chặn | `DELETE /api/blocked-devices/:id` |

## UI

- Form nhập **Device ID** (client gửi qua header — xem `lib/device/device-id.ts`).
- Bảng tương tự IP ban; có thể hiển thị device id hiện tại của trình duyệt để tham chiếu.
""",
}

# Mô tả một dòng cho mục lục (frontend-pages)
PAGE_ONE_LINE: dict[str, str] = {
    "access-block.tsx": "Chặn IP/thiết bị và tab tổng quan truy cập bất thường.",
    "access-overview-section.tsx": "Section embed tổng quan access trong trang chặn truy cập.",
    "agent-assistant.tsx": "Trợ lý AI chat + panel trạng thái hệ thống (DB, cloud sync, shop online).",
    "agent-chat-audit.tsx": "Xem lịch sử hội thoại Trợ lý AI đã lưu.",
    "camera-settings.tsx": "Cấu hình camera (desktop) phục vụ POS/media.",
    "chain-api-keys.tsx": "Tạo API key shop cho widget và thiết bị ESP32.",
    "chain-dashboard.tsx": "Dashboard tổng hợp chuỗi cửa hàng theo quyền.",
    "chain.tsx": "Sửa tổ chức: shop, Viettel, CQT, Trợ lý AI, URL feedback.",
    "customer-feedback.tsx": "Quản lý phản hồi khách đã gửi từ form công khai.",
    "dashboard.tsx": "Tổng quan doanh thu, đơn, tồn thấp theo shop.",
    "device-ban.tsx": "Redirect legacy → access-block tab thiết bị.",
    "feedback-form.tsx": "Form công khai `/feedback` cho khách gửi ý kiến.",
    "inventory.tsx": "Tồn kho shop, điều chỉnh số lượng, cảnh báo sắp hết.",
    "ip-ban.tsx": "Redirect legacy → access-block tab IP.",
    "keyboard-shortcuts.tsx": "Bảng phím tắt POS/desktop.",
    "lan-devices.tsx": "Thiết bị LAN peer (in, widget nội bộ).",
    "login.tsx": "Đăng nhập email/PIN, lưu phiên thiết bị.",
    "media.tsx": "Thư viện media/upload ảnh sản phẩm.",
    "my-permissions.tsx": "Giải thích quyền role và menu hiện tại.",
    "not-found.tsx": "Trang 404 SPA.",
    "notification-settings.tsx": "Cấu hình thông báo platform/org.",
    "orders.tsx": "Danh sách đơn, hủy/duyệt hủy, in lại.",
    "page-status.tsx": "Trạng thái triển khai từng trang (dev/ops).",
    "pos.tsx": "Màn bán hàng: giỏ, thanh toán, in bill, checkout offline.",
    "products.tsx": "Danh mục sản phẩm, variant, import Excel, giá.",
    "purchase-orders.tsx": "Phiếu đặt mua (PO) và trạng thái nhận hàng.",
    "reports.tsx": "Báo cáo nhân viên, in lại bill, doanh số.",
    "sales-staff.tsx": "Nhân viên bán hàng (sales staff) gắn POS.",
    "staff.tsx": "Quản lý tài khoản nhân viên (admin).",
    "statistics.tsx": "Thống kê bán theo sản phẩm/kỳ.",
    "stock-requests.tsx": "Phiếu yêu cầu nhập/xuất nội bộ giữa shop.",
    "suppliers.tsx": "Danh mục nhà cung cấp.",
    "system-reports.tsx": "Báo cáo hệ thống, sự kiện, lỗi.",
    "vat-inbound.tsx": "HĐ đầu vào VAT: import, kéo CQT, MST lọc, ghép SP, nhập kho.",
    "vat-invoice-public.tsx": "Form công khai tra cứu/xem HĐ VAT `/vat-invoice`.",
    "vat-invoices.tsx": "Phát hành và quản lý HĐ VAT bán ra (Viettel).",
}

NGHIEP_VU_FILES: dict[str, str] = {
    "nghiep-vu/01-dang-nhap-va-shop-context.md": """
# Đăng nhập và ngữ cảnh shop

- User đăng nhập email/mật khẩu (`POST /api/auth/login`).
- JWT gắn **shop_id**, **role**, **organization_id** (nếu có).
- Hầu hết API dùng `requireOperationalContext` — mọi thao tác gắn shop đang chọn.
- **Hub shop** (chi nhánh chính): HĐ đầu vào, một số cấu hình chuỗi.
- Offline: không login user mới; checkout vẫn ghi local nếu đã có session.

**Code:** `middlewares/auth.ts`, `pages/login.tsx`, `lib/session-cache.ts`.
""",
    "nghiep-vu/02-pos-ban-hang.md": """
# POS — bán hàng

1. Mở ca (`shift-sessions`) nếu policy bật.
2. Thêm SP vào giỏ — trừ tồn khi **complete** order (server) hoặc ghi offline.
3. Chọn PT thanh toán; optional yêu cầu xuất HĐ (buyer fields trên order).
4. In bill / reprint → `reprint_logs`, báo cáo audit.

**Hủy đơn:** NV gửi yêu cầu + note; admin duyệt → hoàn tồn.

**Tables:** `orders`, `order_items`, `inventory`, `reprint_logs`, `pos_cart_audit_logs`.

**Mirror:** `reference/business-flows.md` § POS.
""",
    "nghiep-vu/03-san-pham-va-ton.md": """
# Sản phẩm và tồn kho

- SP scoped **shop_id**; internal_code, vat_name, giá, giá vốn, VAT rate.
- Import Excel: trùng mã nội bộ → **cộng tồn**; có thể kích hoạt lại SP discontinued.
- Tồn shop: bảng `inventory` (`warehouse_id` NULL cho POS).
- Điều chỉnh tồn: PATCH inventory; warehouse riêng cho chuỗi/kho tổng.

**API:** `products.ts`, `inventory.ts`. **UI:** `products.tsx`, `inventory.tsx`.
""",
    "nghiep-vu/04-phieu-nhap-xuat-chuyen-kho.md": """
# Phiếu nhập/xuất và chuyển kho

**Stock requests:** CN con xin hàng từ hub — duyệt tại hub; vận chuyển trừ tồn nguồn; nhận cộng đích.

**Transfers (chain):** draft → approve → ship → receive; `inventory_movements` audit.

**Purchase orders:** liên kết HĐ đầu vào khi ghép hàng (không bắt buộc PO riêng cho mọi flow).

**API:** `stock-requests.ts`, `purchase-orders.ts`, `chain.ts` (transfers).
""",
    "nghiep-vu/05-hoa-don-vat-xuat.md": """
# Hóa đơn VAT xuất (bán ra)

Tích hợp **Viettel SInvoice** (cấu hình org). Phát hành từ POS khi khách yêu cầu HĐ.

**UI:** `vat-invoices.tsx`. **API:** routes Viettel org settings, public form `/vat-invoice`.

Cấu hình tại **Chuỗi → Sửa tổ chức** (tab HĐ VAT / Viettel).
""",
    "nghiep-vu/06-hoa-don-dau-vao-tong-quan.md": """
# Hóa đơn đầu vào — tổng quan

## Nguồn dữ liệu

| Kênh | UI / API | Ghi chú |
|------|----------|---------|
| PDF | Nhập PDF → parse local → upsert server | Revision parse `VAT_INBOUND_PARSE_REVISION` |
| Excel | Mẫu + import | `vat-inbound-excel-import.ts` |
| CQT | Lấy hóa đơn → `POST /vat-inbound/sync-tax` | GDT direct / Viettel tùy org |
| Viettel | Verify từng HĐ | `verify-viettel` endpoint |

## Vòng đời (happy path)

1. HĐ vào DB `vat_inbound_invoices` (shop hub).
2. Nếu MST trùng **MST lọc** → `archivedAt`, tab **Khác** (xem mục 07).
3. Kế toán mở HĐ → ghép từng dòng SP (`stock-receipt`) — tạo/cập nhật `stockLines`, có thể tạo SP/NCC.
4. **Nhập kho** (`receive-stock`) — cộng tồn, giá vốn BQ.
5. Trạng thái: `mapped` → `partial`/`received` hoặc `closed_short`.

## Trạng thái `stockStatus`

- `mapped`: đã ghép, chưa nhập kho
- `partial`: nhập một phần
- `received`: đủ
- `closed_short`: chốt thiếu
- `rollback_requested`: chờ duyệt hoàn tác nhập kho

## Offline / IndexedDB

- Máy client giữ bản copy + PDF bytes; sync khi online.
- `listPendingVatInboundInvoices` push lên server.

## Đọc tiếp

- API đầy đủ: `api-modules/vat-inbound.md`
- UI: `frontend-pages/vat-inbound.md`
- DB: `schema/vatInboundInvoices.md`
""",
    "nghiep-vu/07-hd-dau-vao-mst-loc.md": """
# HĐ đầu vào — MST lọc (tab Khác)

## Mục đích

Tự động **lưu trữ** hóa đơn mua vào có MST người bán/người mua nằm trong danh sách loại trừ
(công ty nội bộ, đối tác không cần nhập kho, v.v.) để kế toán không thấy ở tab **Đang dùng**.

## Cấu hình

| Lớp | Chi tiết |
|-----|----------|
| DB | `organizations.vat_inbound_auto_archive_tax_codes` — chuỗi text, nhiều MST (xuống dòng hoặc phân tách) |
| API GET | `/api/vat-inbound/marked-mst-archive` |
| API PATCH | `/api/vat-inbound/marked-mst-archive` body `{ codes }` (string hoặc null) |
| Quyền sửa | Admin / manager (`canEditVatInboundMarkedMst`) |

**Không** cấu hình trong Chuỗi → Sửa tổ chức (đã chuyển về trang HĐ đầu vào).

## Hành vi UI

- Tab **Khác:** HĐ đã `archivedAt` **và** MST khớp danh sách lọc.
- Tab **Lưu trữ:** archived nhưng **không** khớp MST lọc (lưu trữ thủ công / lý do khác).
- Tab **Đang dùng:** chưa archive, không thuộc Khác.
- Nút **MST lọc** trên toolbar (trước Mẫu Excel): modal textarea → **Lưu** → PATCH + backfill.

## Backfill

- Khi PATCH danh sách: `backfillVatInboundArchiveByMarkedMst(orgId)`.
- Khi insert/update HĐ / sau sync thuế: helper `syncVatInboundTaxArchivesForInvoice` (xem lib auto-archive).

## Code map

- `lib/vat-inbound-auto-archive-mst.ts` — normalize MST, so khớp
- `lib/vat-inbound-marked-mst-backfill.ts` — quét HĐ org
- `routes/vat-inbound.ts` — endpoint marked-mst-archive
- `pages/vat-inbound.tsx` — modal, tab lọc `other`
""",
    "nghiep-vu/08-hd-dau-vao-cqt-sync.md": """
# HĐ đầu vào — kéo CQT

- Org `vat_inbound_provider = gdt_direct` → captcha + login CQT (`/vat-inbound/gdt/*`).
- `POST /vat-inbound/sync-tax` body `{ from, to }` — tối đa 3 tháng/lần, split dài.
- Map row GDT → insert/update DB; VAT rate label 0.08 → 8%; auto archive MST.

**Lib:** `gdt-portal/`, `vat-inbound-tax-sync.ts`, `map-inbound.ts`.
""",
    "nghiep-vu/09-chuoi-va-da-chi-nhanh.md": """
# Chuỗi và đa chi nhánh

- **Organization** → nhiều **shops**; warehouse central / transit / shop backroom.
- Dashboard chuỗi: aggregate theo scope quyền (`chain-dashboard.tsx`).
- Heartbeat shop: `last_seen_at` — Trợ lý AI báo offline/clock drift.

**API:** `chain.ts`, `dashboard.ts`, `statistics.ts`.
""",
    "nghiep-vu/10-truy-cap-an-ninh.md": """
# Truy cập và an ninh

## Mục đích

Bảo vệ API khỏi client lạ (IP / thiết bị) và cho **super admin** quan sát ai đang gọi `/api` trước khi quyết định chặn.

## Lớp bảo vệ (thứ tự trong `app.ts`)

| Lớp | File lib | Hành vi |
|-----|----------|---------|
| Quan sát | `api-access-observations.ts` | Ghi cặp deviceId+IP, đếm hit; **không** chặn |
| Chặn IP | `ip-denylist.ts` | 403 nếu IP trong DB hoặc env `IP_DENYLIST` / `BLOCKED_IPS` |
| Chặn thiết bị | `device-denylist.ts` | 403 nếu `deviceId` header trong `blocked_devices` |

Cache denylist refresh định kỳ + ngay sau POST/DELETE từ UI admin.

## UI quản trị

**Đường dẫn:** `/access-block` — menu **Chặn truy cập** (chỉ `super_admin`).

| Tab | Component | Chức năng |
|-----|-----------|-----------|
| Tổng quan | `AccessOverviewSection` | Bảng quan sát RAM, chặn nhanh |
| Chặn IP | `IpBanSection` | CRUD bảng `blocked_ips` |
| Chặn thiết bị | `DeviceBanSection` | CRUD bảng `blocked_devices` |

URL cũ `/ip-ban`, `/device-ban` redirect sang `?tab=`.

## API modules

- `GET/POST/DELETE /api/blocked-ips` — `routes/blocked-ips.ts`
- `GET/POST/DELETE /api/blocked-devices` — `routes/blocked-devices.ts`
- `GET /api/access-observations` — `routes/access-observations.ts`

Tất cả yêu cầu JWT + **`super_admin`**.

## Database

- `blocked_ips` — cột `ip`, `note`, `created_by` → users
- `blocked_devices` — `device_id`, `note`, `created_by`
- Quan sát: **không** có bảng Postgres (in-memory TTL)

## RBAC liên quan khác

- Menu POS / quyền shop: `lib/session-permissions.ts`, `reference/rbac.md`
- **Device login events** / **allowed devices**: schema riêng — đăng nhập thiết bị tin cậy, khác denylist

## Frontend docs

- `frontend-pages/access-block.md`
- `frontend-pages/access-overview-section.md`
- `frontend-pages/ip-ban.md`, `device-ban.md`

**Mirror:** `reference/rbac.md`, `reference/public-access.md`.
""",
    "nghiep-vu/11-offline-va-sync-client.md": """
# Offline và sync client

- IndexedDB (`local-db`): orders pending, vat inbound local copy, outbox.
- `lib/sync`: pull/push theo endpoint `sync.ts`.
- POS checkout **không** chờ sync worker — ghi local trước.

**Mirror:** `reference/offline-first.md`, `offline-first-audit.md`.
""",
    "nghiep-vu/12-widget-va-dem-khach.md": """
# Widget Android và đếm khách

- Widget: JWT, WorkManager — repo **VietPOS-Widget**.
- ESP32: POST visitor-counts + API key — repo **ESP32-DemKhach**.
- Schema: `shop_daily_visitor_counts`, `shop_api_keys`.

**API:** `widget.ts`, `shop-api-keys.ts`.
""",
}

HE_THONG_FILES: dict[str, str] = {
    "he-thong/01-kien-truc-runtime.md": """
# Kiến trúc runtime

Trình duyệt hoặc app desktop (Tauri) chạy **pos-app** (React). Mọi thao tác nghiệp vụ gọi **api-server** (Express) qua prefix `/api`, server đọc/ghi **PostgreSQL** qua Drizzle (`@workspace/db`).

```
Trình duyệt / Tauri
  → pos-app (React, Vite)
  → /api/* → api-server (Express 5)
  → @workspace/db (Drizzle) → PostgreSQL 16
  → (tùy chọn) cloud-sync → Postgres trên Railway
```

- **Production:** web build tĩnh phục vụ nginx; API chạy `dist/index.mjs`.
- **Xác thực:** JWT trên hầu hết route; một số route công khai (form HĐ, feedback) dùng cookie/session riêng.

**Đọc tiếp:** [02-workspace](02-workspace-luu-niem.md) · Tham chiếu gốc: `reference/architecture.md`
""",
    "he-thong/02-workspace-luu-niem.md": """
# Workspace LuuNiem

| Thư mục | Vai trò |
|---------|---------|
| Shop-Manager-System-Offline | Mã nguồn phát triển chính |
| HDSD-VietPOS | Hướng dẫn sử dụng HTML (Vercel) |
| VietPOS-Widget | Ứng dụng widget Android |
| VietPOS-Map | Bản đồ tài liệu (repo này) |
| ESP32-DemKhach | Firmware đếm khách |

**Đọc tiếp:** [03-monorepo-packages](03-monorepo-packages.md) · [Hướng dẫn đọc Map](../00-huong-dan-doc-tai-lieu.md)
""",
    "he-thong/03-monorepo-packages.md": """
# Gói trong monorepo Shop

Monorepo **pnpm** — một repo chứa API, giao diện, thư viện dùng chung.

| Nhóm | Thành phần |
|------|------------|
| **artifacts** | `api-server`, `pos-app`, `pos-desktop`, `mockup-sandbox` |
| **lib** | `db`, `local-db`, `sync`, `api-zod`, `api-spec`, `api-client-react` |
| **scripts** | seed DB, helper Docker |

Khai báo workspace: `Shop-Manager-System-Offline/pnpm-workspace.yaml`.

**Đọc tiếp:** [04-docker-va-cloud-sync](04-docker-va-cloud-sync.md) · Tour code: `reference/api-server.md`, `reference/pos-app.md`
""",
    "he-thong/04-docker-va-cloud-sync.md": """
# Docker và đồng bộ cloud

Compose local thường gồm: Postgres (cổng **5434**), init schema, **api** (**3002**), **web** (**8080**), service **cloud-sync**.

- Worker **cloud-sync** chạy `scripts/cloud-sync.sh`, khóa `_sync_lock`, cần `CLOUD_DATABASE_URL` trỏ Postgres cloud (Railway).
- Trạng thái «đã cấu hình cloud» trên POS/Trợ lý AI đọc biến môi trường trên container **api** (không chỉ cloud-sync).

**Đọc tiếp:** `reference/docker-may-chu.md`, `reference/running-local.md` · Nghiệp vụ offline: [nghiep-vu/11](../nghiep-vu/11-offline-va-sync-client.md)
""",
}

# Hub chủ đề — điểm vào theo việc cần làm (tránh lạc trong ~250 file)
TOPIC_HUBS: list[dict[str, object]] = [
    {
        "file": "00-kien-truc-he-thong.md",
        "title": "Kiến trúc hệ thống",
        "desc": "Sơ đồ tổng thể: pos-app, api-server, Postgres, offline, cloud-sync — đọc đầu tiên.",
        "intro": """
Hệ thống VietPOS gồm **giao diện web** (pos-app), **API** (api-server) và **PostgreSQL**.
Máy quầy có thể ghi **offline** (IndexedDB) rồi đồng bộ; tùy chọn **cloud-sync** lên Postgres cloud.

```mermaid
flowchart TB
  subgraph may["Máy người dùng"]
    UI[pos-app React]
    IDB[(IndexedDB offline)]
  end
  UI --> IDB
  UI -->|"/api"| API[api-server Express]
  API --> PG[(PostgreSQL)]
  IDB -. pull/push .-> API
  API -. cloud-sync .-> CLOUD[(Postgres cloud)]
  WIDGET[Widget Android / ESP32] -->|API key| API

  click UI "../../trang/ban-hang-pos/README.md" "Màn POS"
  click API "../../he-thong/01-kien-truc-runtime/README.md" "Runtime API"
  click IDB "../offline-dong-bo/README.md" "Offline & đồng bộ"
  click PG "../../chi-muc/co-so-du-lieu/README.md" "Schema Postgres"
  click CLOUD "../../he-thong/04-docker-va-cloud-sync/README.md" "Docker & cloud-sync"
  click WIDGET "../tro-ly-widget/README.md" "Widget & đếm khách"
```

**Sơ đồ HTML (bấm ô):** [index.html](../../index.html)

| Thành phần | Vai trò |
|------------|---------|
| **pos-app** | Màn hình POS, kho, HĐ VAT, cấu hình chuỗi |
| **api-server** | Xử lý nghiệp vụ, quyền JWT, gọi Viettel/CQT |
| **@workspace/db** | Schema Drizzle → Postgres |
| **local-db / sync** | Đơn & HĐ chờ đẩy khi mất mạng |
| **cloud-sync** | Mirror DB lên Railway (ops) |

**Bản đồ hình (ASCII, luôn hiển thị):** [ban-do-kien-truc.md](../ban-do-kien-truc.md)

**Chi tiết từng phần:** [he-thong/01](../he-thong/01-kien-truc-runtime.md) · [02 workspace](../he-thong/02-workspace-luu-niem.md) · [03 monorepo](../he-thong/03-monorepo-packages.md) · [04 Docker](../he-thong/04-docker-va-cloud-sync.md)
""",
        "nghiep_vu": [],
        "ui": [],
        "api": [],
        "schema": [],
        "lib_prefixes": [],
    },
    {
        "file": "dang-nhap-va-phien.md",
        "title": "Đăng nhập và phiên làm việc",
        "desc": "JWT, shop đang chọn, hub shop, quyền menu.",
        "intro": "Mọi API gần như đều gắn **shop_id** và **role** sau khi đăng nhập.",
        "nghiep_vu": ["nghiep-vu/01-dang-nhap-va-shop-context.md"],
        "ui": ["frontend-pages/login.md", "frontend-pages/my-permissions.md"],
        "api": ["api-modules/auth.md", "api-modules/shops.md"],
        "schema": ["schema/users.md", "schema/shops.md"],
        "lib_prefixes": ["session-cookie", "user-pin", "pin-"],
    },
    {
        "file": "pos-va-don-hang.md",
        "title": "POS và đơn hàng",
        "desc": "Quầy bán, giỏ hàng, thanh toán, ca làm việc, hủy đơn.",
        "intro": "Luồng doanh thu chính — từ màn POS đến bảng `orders`.",
        "nghiep_vu": ["nghiep-vu/02-pos-ban-hang.md"],
        "ui": ["frontend-pages/pos.md", "frontend-pages/orders.md"],
        "api": ["api-modules/orders.md", "api-modules/shift-sessions.md", "api-modules/pos-cart-audit.md"],
        "schema": ["schema/orders.md", "schema/orderItems.md", "schema/shiftSessions.md"],
        "lib_prefixes": ["order-", "shift-sessions", "payment-"],
    },
    {
        "file": "san-pham-va-kho.md",
        "title": "Sản phẩm và tồn kho",
        "desc": "Danh mục SP, tồn shop, phiếu nhập/xuất, PO.",
        "intro": "Dữ liệu master + tồn trước khi bán hoặc nhập HĐ.",
        "nghiep_vu": ["nghiep-vu/03-san-pham-va-ton.md", "nghiep-vu/04-phieu-nhap-xuat-chuyen-kho.md"],
        "ui": [
            "frontend-pages/products.md",
            "frontend-pages/inventory.md",
            "frontend-pages/stock-requests.md",
            "frontend-pages/purchase-orders.md",
            "frontend-pages/suppliers.md",
        ],
        "api": [
            "api-modules/products.md",
            "api-modules/inventory.md",
            "api-modules/stock-requests.md",
            "api-modules/purchase-orders.md",
            "api-modules/suppliers.md",
        ],
        "schema": ["schema/products.md", "schema/inventory.md", "schema/stockRequests.md"],
        "lib_prefixes": ["product-", "inventory", "weighted-average"],
    },
    {
        "file": "hoa-don-dau-vao.md",
        "title": "Hóa đơn đầu vào (VAT mua vào)",
        "desc": "Import PDF/Excel, kéo CQT, MST lọc, ghép hàng, nhập kho.",
        "intro": "Chủ đề phức tạp nhất — đọc **06 → 07 → 08** trước khi mở file API/UI.",
        "nghiep_vu": [
            "nghiep-vu/06-hoa-don-dau-vao-tong-quan.md",
            "nghiep-vu/07-hd-dau-vao-mst-loc.md",
            "nghiep-vu/08-hd-dau-vao-cqt-sync.md",
        ],
        "ui": ["frontend-pages/vat-inbound.md"],
        "api": ["api-modules/vat-inbound.md", "api-modules/org-gdt-portal.md"],
        "schema": ["schema/vatInboundInvoices.md", "schema/vatInboundAuditLogs.md", "schema/orgGdtTaxSessions.md"],
        "lib_prefixes": ["vat-inbound", "gdt-portal", "inbound-stock", "viettel-sinvoice/search-inbound"],
    },
    {
        "file": "hoa-don-ban-ra.md",
        "title": "Hóa đơn bán ra (Viettel)",
        "desc": "Phát hành HĐ VAT từ POS, tra cứu, form công khai.",
        "intro": "Tích hợp Viettel SInvoice — cấu hình tại Chuỗi → Sửa tổ chức.",
        "nghiep_vu": ["nghiep-vu/05-hoa-don-vat-xuat.md"],
        "ui": ["frontend-pages/vat-invoices.md", "frontend-pages/vat-invoice-public.md"],
        "api": ["api-modules/org-viettel-settings.md", "api-modules/public-vat-invoice.md"],
        "schema": ["schema/organizations.md"],
        "lib_prefixes": ["viettel-sinvoice", "vat-invoice", "org-viettel"],
    },
    {
        "file": "chuoi-cua-hang.md",
        "title": "Chuỗi và nhiều cửa hàng",
        "desc": "Tổ chức, shop, kho, điều chuyển, dashboard chuỗi.",
        "intro": "Một **organization** nhiều **shop**; hub shop cho HĐ đầu vào.",
        "nghiep_vu": ["nghiep-vu/09-chuoi-va-da-chi-nhanh.md"],
        "ui": ["frontend-pages/chain.md", "frontend-pages/chain-dashboard.md", "frontend-pages/chain-api-keys.md"],
        "api": ["api-modules/chain.md", "api-modules/dashboard.md", "api-modules/shop-api-keys.md"],
        "schema": ["schema/organizations.md", "schema/warehouses.md", "schema/stockTransfers.md"],
        "lib_prefixes": ["chain-shop", "shop-presence", "dashboard-"],
    },
    {
        "file": "an-ninh-truy-cap.md",
        "title": "An ninh và chặn truy cập",
        "desc": "Chặn IP/thiết bị, quan sát truy cập, super_admin.",
        "intro": "Denylist chạy **trước** router API — 403 ngay nếu bị chặn.",
        "nghiep_vu": ["nghiep-vu/10-truy-cap-an-ninh.md"],
        "ui": ["frontend-pages/access-block.md"],
        "api": [
            "api-modules/blocked-ips.md",
            "api-modules/blocked-devices.md",
            "api-modules/access-observations.md",
        ],
        "schema": ["schema/blockedIps.md", "schema/blockedDevices.md"],
        "lib_prefixes": ["ip-denylist", "device-denylist", "api-access-observations"],
    },
    {
        "file": "offline-dong-bo.md",
        "title": "Offline và đồng bộ",
        "desc": "IndexedDB, checkout offline, API sync.",
        "intro": "POS ghi local trước; worker đẩy khi có mạng.",
        "nghiep_vu": ["nghiep-vu/11-offline-va-sync-client.md"],
        "ui": ["frontend-pages/pos.md"],
        "api": ["api-modules/sync.md", "api-modules/orders.md"],
        "schema": ["schema/orderSyncKeys.md"],
        "lib_prefixes": [],
    },
    {
        "file": "tro-ly-widget.md",
        "title": "Trợ lý AI, widget, đếm khách",
        "desc": "Agent chat, widget Android, ESP32 visitor-counts.",
        "intro": "Tích hợp ngoài quầy — API key shop.",
        "nghiep_vu": ["nghiep-vu/12-widget-va-dem-khach.md"],
        "ui": ["frontend-pages/agent-assistant.md", "frontend-pages/agent-chat-audit.md"],
        "api": ["api-modules/agent.md", "api-modules/widget.md", "api-modules/shop-api-keys.md"],
        "schema": ["schema/shopApiKeys.md", "schema/shopDailyVisitorCounts.md", "schema/agentChat.md"],
        "lib_prefixes": ["agent/", "widget-home"],
    },
]


def lib_topic_for_path(rel_posix: str) -> tuple[str, str]:
    r = rel_posix.replace("\\", "/").lower()
    if r.startswith("gdt-portal") or "vat-inbound" in r or "inbound-stock" in r:
        return chuyen_de_path("hoa-don-dau-vao"), "Hóa đơn đầu vào"
    if "viettel" in r or "vat-invoice" in r:
        return chuyen_de_path("hoa-don-ban-ra"), "Hóa đơn bán ra"
    if r.startswith("agent/") or r.startswith("agent-"):
        return chuyen_de_path("tro-ly-widget"), "Trợ lý AI"
    if "ip-denylist" in r or "device-denylist" in r or "access-observation" in r:
        return chuyen_de_path("an-ninh-truy-cap"), "An ninh"
    if "order" in r or "shift-session" in r or "payment" in r:
        return chuyen_de_path("pos-va-don-hang"), "POS & đơn hàng"
    if "product" in r or "inventory" in r or "weighted-average" in r:
        return chuyen_de_path("san-pham-va-kho"), "Sản phẩm & kho"
    if "chain" in r or "dashboard" in r or "shop-presence" in r:
        return chuyen_de_path("chuoi-cua-hang"), "Chuỗi cửa hàng"
    if "session" in r or "pin" in r or "user-" in r:
        return chuyen_de_path("dang-nhap-va-phien"), "Đăng nhập & phiên"
    return chuyen_de_path("kien-truc-he-thong"), "Kiến trúc / dùng chung"


def lib_files_matching_prefixes(all_lib: list[str], prefixes: list[str]) -> list[str]:
    if not prefixes:
        return []
    out: list[str] = []
    for p in sorted(all_lib):
        base = p.replace("thu-vien/", "")
        if any(base.startswith(pr) or pr in base for pr in prefixes):
            out.append(p)
    return out[:25]


def write_chuyen_de_hubs(all_paths: list[str]) -> list[str]:
    lib_paths = [p for p in all_paths if p.startswith("thu-vien/")]
    paths: list[str] = []
    for hub in TOPIC_HUBS:
        fname = str(hub["file"])
        rel = chuyen_de_path(fname)
        title = str(hub["title"])
        desc = str(hub["desc"])
        register_desc(rel, desc)
        lines = [
            f"# {title}",
            "",
            f"**Mô tả:** {desc}",
            "",
            f"**Về trang chủ Map:** [{README}]({md_href(rel, map_index_path())}) · "
            f"[Hướng dẫn đọc]({md_href(rel, huong_dan_doc_path())})",
            "",
            rewrite_legacy_links(str(hub.get("intro", "")).strip()),
            "",
        ]
        for section, key in [
            ("## 1. Luồng nghiệp vụ (đọc trước)", "nghiep_vu"),
            ("## 2. Màn hình (giao diện)", "ui"),
            ("## 3. Module API", "api"),
            ("## 4. Bảng dữ liệu (schema)", "schema"),
        ]:
            items = hub.get(key) or []
            if not items:
                continue
            lines.append(section)
            lines.append("")
            for item in items:
                target = resolve_doc_link(str(item))
                label = Path(target).parent.name
                d = DOC_DESCRIPTIONS.get(target, "")
                lines.append(
                    f"- [{label}]({md_href(rel, target)})"
                    + (f" — {one_line(d, 100)}" if d else "")
                )
            lines.append("")
        prefixes = hub.get("lib_prefixes") or []
        lib_hits = lib_files_matching_prefixes(lib_paths, list(prefixes))
        if lib_hits:
            lines.append("## 5. Thư viện backend (một số file quan trọng)")
            lines.append("")
            idx = chi_muc_path("thu-vien-backend")
            lines.append(f"Tra cứu đủ: [{README}]({md_href(rel, idx)})")
            lines.append("")
            for item in lib_hits:
                label = Path(item).parent.name
                d = DOC_DESCRIPTIONS.get(item, "")
                lines.append(
                    f"- [{label}]({md_href(rel, item)})"
                    + (f" — {one_line(d, 90)}" if d else "")
                )
            lines.append("")
        lines.append("---")
        lines.append("")
        lines.append("*Sinh tự động — `python3 docs/gen.py`*")
        out = ROOT / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text("\n".join(lines) + "\n", encoding="utf-8")
        paths.append(rel)
    return paths


def write_chi_muc(all_paths: list[str], flat_endpoints: list[tuple[str, str, str, str]]) -> list[str]:
    out: list[str] = []

    def write_one(slug: str, title: str, desc: str, body_lines: list[str]) -> None:
        rel = chi_muc_path(slug)
        register_desc(rel, desc)
        hdr = [
            f"# {title}",
            "",
            f"**Mô tả:** {desc}",
            "",
            f"← [Bản đồ chính]({md_href(rel, map_index_path())}) · "
            f"[Hướng dẫn đọc]({md_href(rel, huong_dan_doc_path())})",
            "",
            "---",
            "",
        ]
        p = ROOT / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("\n".join(hdr + body_lines) + "\n", encoding="utf-8")
        out.append(rel)

    api_items = sorted(p for p in all_paths if p.startswith("module-api/"))
    chi_api = chi_muc_path("danh-sach-api")
    body = []
    for i, item in enumerate(api_items, 1):
        d = one_line(DOC_DESCRIPTIONS.get(item, ""), 130)
        label = Path(item).parent.name
        body.append(f"{i}. [{label}]({md_href(chi_api, item)}) — {d}")
    write_one(
        "danh-sach-api",
        "Chỉ mục module API",
        f"Danh sách {len(api_items)} module routes — dùng khi đã biết cần sửa API nào.",
        body,
    )

    ui_items = sorted(p for p in all_paths if p.startswith("trang/"))
    chi_ui = chi_muc_path("danh-sach-trang")
    body = []
    for i, item in enumerate(ui_items, 1):
        d = one_line(DOC_DESCRIPTIONS.get(item, ""), 130)
        label = Path(item).parent.name
        body.append(f"{i}. [{label}]({md_href(chi_ui, item)}) — {d}")
    write_one(
        "danh-sach-trang",
        "Chỉ mục trang giao diện",
        f"Danh sách {len(ui_items)} trang React — dùng sau khi đọc hub chủ đề.",
        body,
    )

    schema_items = sorted(p for p in all_paths if p.startswith("co-so-du-lieu/"))
    chi_schema = chi_muc_path("co-so-du-lieu")
    body = [
        "Postgres + **Drizzle ORM** (`lib/db/src/schema`). Mỗi file TS có thể khai báo "
        "nhiều bảng; trang con có **bảng cột đầy đủ** (kiểu, PK/FK, index, enum, ghi chú JSDoc).",
        "",
        f"Tài liệu ER tổng thể (tiếng Anh, Shop gốc): "
        f"[co-so-du-lieu-goc]({md_href(chi_schema, tham_chieu_path('database.md'))}).",
        "",
    ]
    listed: set[str] = set()
    for title, blurb, stems in SCHEMA_DOMAINS:
        body.append(f"### {title}")
        body.append("")
        body.append(blurb)
        body.append("")
        for stem in stems:
            item = SCHEMA_STEM_REL.get(stem)
            if not item:
                continue
            listed.add(item)
            d = one_line(DOC_DESCRIPTIONS.get(item, ""), 110)
            label = Path(item).parent.name
            body.append(f"- [{label}]({md_href(chi_schema, item)}) — {d}")
        body.append("")
    rest = [p for p in schema_items if p not in listed]
    if rest:
        body.append("### Khác")
        body.append("")
        for item in rest:
            d = one_line(DOC_DESCRIPTIONS.get(item, ""), 110)
            label = Path(item).parent.name
            body.append(f"- [{label}]({md_href(chi_schema, item)}) — {d}")
        body.append("")
    write_one(
        "co-so-du-lieu",
        "Chỉ mục cơ sở dữ liệu (Drizzle)",
        f"{len(schema_items)} file schema — bảng cột, quan hệ FK, index; nhóm theo nghiệp vụ.",
        body,
    )

    lib_items = sorted(p for p in all_paths if p.startswith("thu-vien/"))
    by_folder: dict[str, list[str]] = {}
    for item in lib_items:
        parts = Path(item).parts
        folder = parts[1] if len(parts) > 2 else "(gốc lib)"
        by_folder.setdefault(folder, []).append(item)
    chi_lib = chi_muc_path("thu-vien-backend")
    body = []
    for folder in sorted(by_folder.keys()):
        body.append(f"### `{folder}/`")
        body.append("")
        for item in by_folder[folder]:
            d = one_line(DOC_DESCRIPTIONS.get(item, ""), 100)
            label = Path(item).parent.name
            body.append(f"- [{label}]({md_href(chi_lib, item)}) — {d}")
        body.append("")
    write_one(
        "thu-vien-backend",
        "Chỉ mục thư viện backend",
        f"Danh sách {len(lib_items)} file lib — nhóm theo thư mục, không đọc tuần tự hết.",
        body,
    )

    chi_ep = chi_muc_path("endpoint-http")
    body = []
    for i, (mod, method, api_path, doc_path) in enumerate(
        sorted(flat_endpoints, key=lambda x: (x[2], x[1])), start=1
    ):
        blurb = one_line(endpoint_index_blurb(mod, method, api_path), 100)
        body.append(
            f"{i}. `{method}` `/api{api_path}` — {blurb} → "
            f"[`{mod}`]({md_href(chi_ep, doc_path)})"
        )
    write_one(
        "endpoint-http",
        "Chỉ mục endpoint HTTP",
        f"Danh sách {len(flat_endpoints)} endpoint — tra cứu nhanh URL API.",
        body,
    )
    return out


def clean_generated() -> None:
    for p in list(ROOT.iterdir()):
        if p.name in ("gen.py", "doc_paths.py", "api_extract.py"):
            continue
        if p.is_dir():
            shutil.rmtree(p)
        elif p.suffix == ".md":
            p.unlink()


def mirror_shop() -> list[str]:
    paths: list[str] = []
    for rel in MIRROR_FROM_SHOP:
        src = SHOP / rel
        if not src.is_file():
            continue
        fname = Path(rel).name
        rel_doc = tham_chieu_path(fname)
        dst = ROOT / rel_doc
        dst.parent.mkdir(parents=True, exist_ok=True)
        body = src.read_text(encoding="utf-8")
        hdr = f"<!-- Mirror: Shop-Manager-System-Offline/{rel} -->\n\n"
        title_m = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
        title = title_m.group(1).strip() if title_m else Path(rel).stem
        register_desc(
            rel_doc,
            f"Tài liệu tham chiếu gốc Shop `{rel}` — {one_line(title, 120)} (nội dung dưới thường tiếng Anh).",
        )
        mo_ta = (
            f"**Mô tả:** {DOC_DESCRIPTIONS[rel_doc]}\n\n"
            "> **Ghi chú:** Phần dưới giữ nguyên tiếng Anh từ repo Shop (tham chiếu kỹ thuật). "
            "Luồng tiếng Việt ưu tiên đọc `nghiep-vu/` và `he-thong/`.\n\n"
        )
        if body.lstrip().startswith("#"):
            first_nl = body.find("\n")
            if first_nl != -1:
                body = body[: first_nl + 1] + "\n" + mo_ta + body[first_nl + 1 :].lstrip()
            else:
                body = body + "\n\n" + mo_ta
        else:
            body = mo_ta + body
        dst.write_text(hdr + body, encoding="utf-8")
        paths.append(rel_doc)
    return paths


def extract_routes(text: str) -> list[tuple[str, str]]:
    return [(m.upper(), p) for m, p in ROUTE_RE.findall(text)]


def one_line(text: str, max_len: int = 200) -> str:
    s = re.sub(r"\s+", " ", text.strip())
    s = re.sub(r"\*\*|__|`", "", s)
    if len(s) > max_len:
        return s[: max_len - 1].rstrip() + "…"
    return s


def register_desc(rel: str, desc: str) -> str:
    d = one_line(desc)
    DOC_DESCRIPTIONS[rel] = d
    return d


def summary_from_markdown_body(body: str) -> str:
    m = re.search(r"## Mục đích\s*\n+\s*(.+?)(?:\n\n|\n##|\Z)", body, re.DOTALL)
    if m:
        return one_line(m.group(1))
    for ln in body.splitlines():
        t = ln.strip()
        if not t or t.startswith("#") or t.startswith("|") or t.startswith("```"):
            continue
        if t.startswith("- "):
            return one_line(t[2:])
        if not t.startswith("-") and not t.startswith("*"):
            return one_line(t)
    return ""


def prepend_mo_ta_block(lines: list[str], desc: str) -> list[str]:
    """Chèn **Mô tả:** ngay sau dòng tiêu đề # đầu tiên."""
    out: list[str] = []
    inserted = False
    for i, ln in enumerate(lines):
        out.append(ln)
        if not inserted and ln.startswith("# "):
            out.append("")
            out.append(f"**Mô tả:** {desc}")
            inserted = True
    return out


def endpoint_index_blurb(mod: str, method: str, api_path: str) -> str:
    p = api_path if api_path.startswith("/") else f"/{api_path}"
    key = f"{method} {p}"
    if key in ACCESS_ENDPOINT_SPEC:
        return one_line(ACCESS_ENDPOINT_SPEC[key]["summary"], 140)
    if mod == "vat-inbound" and key in VAT_INBOUND_ENDPOINT_NOTES:
        return one_line(VAT_INBOUND_ENDPOINT_NOTES[key], 140)
    intro = API_MODULE_INTRO.get(mod, "")
    if intro:
        return one_line(intro, 100)
    return f"HTTP `{method}` trong module `{mod}`."


def api_module_intro_text(key: str) -> str:
    if key in API_MODULE_INTRO:
        return API_MODULE_INTRO[key]
    return API_MODULE_SHORT_VI.get(key, f"Module HTTP `/api/...` cho nhóm **{key}**.")


def write_huong_dan_doc() -> str:
    rel = huong_dan_doc_path()
    body = f"""
# Hướng dẫn đọc VietPOS-Map

**Mô tả:** Ba bước đọc Map — không cần lướt ~250 file trên một trang.

---

## Cách đọc (3 bước)

| Bước | Làm gì | Mở thư mục |
|------|--------|------------|
| **1** | Xem **sơ đồ bấm được** + kiến trúc | [index.html]({portal_index_href(rel)}) (gốc repo) · [{README}]({md_href(rel, ban_do_path())}) (ASCII/Mermaid) · [kien-truc-he-thong]({md_href(rel, chuyen_de_path("kien-truc-he-thong"))}) |
| **2** | Chọn **một chủ đề** gần việc bạn làm | [Danh sách chủ đề]({md_href(rel, map_index_path())}#chủ-đề-chuyen-de) |
| **3** | Sửa code → tra **chỉ mục kỹ thuật** | [chi-muc/danh-sach-api]({md_href(rel, chi_muc_path("danh-sach-api"))}) và các chỉ mục cùng cấp |

**Không nên:** mở `thu-vien/` và đọc lần lượt mọi README — mỗi hub chủ đề chỉ liệt kê lib **liên quan**.

---

## Trong mỗi hub chủ đề (`chuyen-de/…/README.md`)

Thứ tự gợi ý:

1. **Luồng nghiệp vụ** (`nghiep-vu/…`) — *tại sao / quy trình*
2. **Màn hình** (`trang/…`) — *người dùng thao tác ở đâu*
3. **Module API** (`module-api/…`) — *endpoint nào*
4. **Schema** (`co-so-du-lieu/…`) — *bảng Postgres*
5. **Thư viện** (`thu-vien/…`) — *logic phức tạp* (subset)

---

## Tài liệu gốc tiếng Anh

`tham-chieu/…/README.md` = bản sao doc Shop. Dùng khi cần RBAC, database tổng thể, Docker — xem mục tham chiếu trên [bản đồ chính]({md_href(rel, map_index_path())}).

---

## Tạo lại Map

```bash
python3 docs/gen.py
```

→ [Bản đồ chính]({md_href(rel, map_index_path())})
"""
    register_desc(rel, HE_THONG_DESC[legacy_desc_key(rel)])
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(body.strip() + "\n", encoding="utf-8")
    return rel


def _html_href(from_html: str, to_doc: str) -> str:
    return md_relpath(from_html, to_doc).replace("\\", "/")


def mermaid_hub_map(from_doc: str) -> str:
    """Mermaid 10 hub — node click mở README hub (Cursor / GitHub preview)."""
    lines = [
        "```mermaid",
        "flowchart TB",
        "  HOME[Trang chủ Map]",
    ]
    for i, hub in enumerate(TOPIC_HUBS):
        nid = f"H{i}"
        title = str(hub["title"]).replace('"', "'")
        lines.append(f"  HOME --> {nid}[\"{title}\"]")
    home_href = _html_href(from_doc, map_index_path())
    lines.append(f'  click HOME "{home_href}" "Mục lục"')
    for i, hub in enumerate(TOPIC_HUBS):
        nid = f"H{i}"
        href = _html_href(from_doc, chuyen_de_path(str(hub["file"])))
        title = str(hub["title"]).replace('"', "'")
        lines.append(f'  click {nid} "{href}" "{title}"')
    lines.append("```")
    return "\n".join(lines)


HUB_PORTAL_META: dict[str, dict[str, str]] = {
    "00-kien-truc-he-thong.md": {"icon": "◈", "tone": "#818cf8", "group": "Nền tảng"},
    "dang-nhap-va-phien.md": {"icon": "⦿", "tone": "#38bdf8", "group": "Nền tảng"},
    "an-ninh-truy-cap.md": {"icon": "⛨", "tone": "#f87171", "group": "Nền tảng"},
    "offline-dong-bo.md": {"icon": "⇄", "tone": "#a78bfa", "group": "Nền tảng"},
    "pos-va-don-hang.md": {"icon": "₿", "tone": "#34d399", "group": "Bán hàng"},
    "san-pham-va-kho.md": {"icon": "▤", "tone": "#2dd4bf", "group": "Kho & hàng"},
    "chuoi-cua-hang.md": {"icon": "⛓", "tone": "#fbbf24", "group": "Chuỗi"},
    "hoa-don-dau-vao.md": {"icon": "↓", "tone": "#fb923c", "group": "Thuế VAT"},
    "hoa-don-ban-ra.md": {"icon": "↑", "tone": "#f472b6", "group": "Thuế VAT"},
    "tro-ly-widget.md": {"icon": "◇", "tone": "#94a3b8", "group": "Thiết bị & AI"},
}


def _esc_html(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def _portal_svg_runtime() -> str:
    h = portal_doc_href
    u_pos = h(trang_path("pos"))
    u_off = h(chuyen_de_path("offline-dong-bo"))
    u_api = h(he_thong_path("01-kien-truc-runtime"))
    u_pg = h(chi_muc_path("co-so-du-lieu"))
    u_cloud = h(he_thong_path("04-docker-va-cloud-sync"))
    u_wid = h(chuyen_de_path("tro-ly-widget"))

    def box(
        x: int, y: int, w: int, ht: int, title: str, sub: str, href: str, tone: str
    ) -> str:
        t = _esc_html(title)
        s = _esc_html(sub)
        hr = _esc_html(href)
        return f"""
  <a class="map-node" href="{hr}">
    <rect x="{x}" y="{y}" width="{w}" height="{ht}" rx="10" class="svg-node svg-node-{tone}" stroke="var(--svg-stroke)" stroke-width="1.2"/>
    <text x="{x + w/2}" y="{y + 22}" text-anchor="middle" class="svg-t" font-weight="600">{t}</text>
    <text x="{x + w/2}" y="{y + 40}" text-anchor="middle" class="svg-s">{s}</text>
  </a>"""

    return f"""<svg class="arch-map" viewBox="0 0 900 300" role="img" aria-label="Bản đồ runtime VietPOS">
  <defs>
    <marker id="arr" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" class="svg-arrow"/>
    </marker>
  </defs>
  <rect x="8" y="8" width="884" height="284" rx="14" class="svg-canvas" stroke-width="1"/>
  <text x="24" y="32" class="svg-h">Bản đồ hệ thống (bấm từng khối → tài liệu)</text>
  <rect x="24" y="48" width="200" height="200" rx="12" class="svg-zone" stroke-dasharray="4 3" stroke-width="1"/>
  <text x="124" y="68" text-anchor="middle" class="svg-s" font-weight="600">Máy quầy / admin</text>
{box(40, 82, 168, 52, "pos-app", "React · Tauri · PWA", u_pos, "blue")}
{box(40, 144, 168, 52, "IndexedDB", "Đơn & HĐ chờ sync", u_off, "indigo")}
  <line x1="208" y1="108" x2="268" y2="108" class="svg-line" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="238" y="98" text-anchor="middle" class="svg-s">HTTPS /api</text>
  <line x1="172" y1="170" x2="248" y2="140" class="svg-line" stroke-width="1.2" stroke-dasharray="5 4" marker-end="url(#arr)"/>
  <text x="195" y="162" class="svg-s">pull / push</text>
{box(268, 86, 176, 64, "api-server", "Express · JWT · nghiệp vụ", u_api, "green")}
  <line x1="444" y1="118" x2="504" y2="118" class="svg-line" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="474" y="108" text-anchor="middle" class="svg-s">Drizzle</text>
{box(504, 86, 160, 64, "PostgreSQL", "DB tại shop", u_pg, "amber")}
  <line x1="376" y1="150" x2="376" y2="200" class="svg-line" stroke-width="1.2" marker-end="url(#arr)"/>
  <line x1="376" y1="200" x2="568" y2="200" class="svg-line" stroke-width="1.2"/>
  <line x1="568" y1="200" x2="568" y2="168" class="svg-line" stroke-width="1.2" marker-end="url(#arr)"/>
  <text x="470" y="192" text-anchor="middle" class="svg-s">cloud-sync (tùy chọn)</text>
{box(648, 86, 148, 64, "Postgres cloud", "Railway · ops", u_cloud, "purple")}
{box(268, 200, 176, 52, "Widget / ESP32", "API key · đếm khách", u_wid, "slate")}
  <line x1="356" y1="200" x2="356" y2="150" class="svg-line" stroke-width="1.2" marker-end="url(#arr)"/>
</svg>"""


def _portal_svg_doc_flow() -> str:
    steps = [
        ("index.html", "Cửa vào", "#"),
        (portal_doc_href(chuyen_de_path("pos-va-don-hang")), "① Hub chủ đề", "Chọn việc cần làm"),
        (portal_doc_href(nghiep_vu_path("02-pos-ban-hang")), "② Nghiệp vụ", "Luồng / quy trình"),
        (portal_doc_href(trang_path("pos")), "③ Màn hình", "UI người dùng"),
        (portal_doc_href(module_api_path("orders")), "④ Module API", "HTTP /api"),
        (portal_doc_href(co_so_du_lieu_path("orders")), "⑤ Schema", "Bảng Postgres"),
    ]
    chunks: list[str] = []
    x = 20
    for i, (href, title, sub) in enumerate(steps):
        if i > 0:
            chunks.append(
                f'<line x1="{x - 18}" y1="52" x2="{x}" y2="52" class="svg-line" stroke-width="1.2" marker-end="url(#arr2)"/>'
            )
        hr = _esc_html(href)
        t = _esc_html(title)
        s = _esc_html(sub)
        active = ' class="flow-step active"' if i == 0 else ' class="flow-step"'
        chunks.append(
            f"""  <a{active} href="{hr}">
    <rect x="{x}" y="24" width="128" height="56" rx="8" class="svg-node svg-node-slate" stroke="var(--svg-stroke)" stroke-width="1.2"/>
    <text x="{x + 64}" y="46" text-anchor="middle" class="svg-t">{t}</text>
    <text x="{x + 64}" y="64" text-anchor="middle" class="svg-s">{s}</text>
  </a>"""
        )
        x += 146
    inner = "\n".join(chunks)
    return f"""<svg class="flow-map" viewBox="0 0 920 100" role="img" aria-label="Cách đọc tài liệu Map">
  <defs>
    <marker id="arr2" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" class="svg-arrow"/>
    </marker>
  </defs>
  <text x="20" y="16" class="svg-h">Lộ trình đọc (ví dụ nhánh POS)</text>
{inner}
</svg>"""


def _portal_svg_inbound() -> str:
    u = portal_doc_href(chuyen_de_path("hoa-don-dau-vao"))
    hr = _esc_html(u)
    return f"""<svg class="flow-map" viewBox="0 0 880 88" role="img" aria-label="Luồng hóa đơn đầu vào">
  <defs>
    <marker id="arr3" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" class="svg-arrow"/>
    </marker>
  </defs>
  <text x="20" y="18" class="svg-h">Luồng HĐ đầu vào (tóm tắt)</text>
  <a class="map-node" href="{hr}"><rect x="20" y="30" width="120" height="44" rx="8" class="svg-node svg-node-orange" stroke="var(--svg-stroke)" stroke-width="1.2"/><text x="80" y="56" text-anchor="middle" class="svg-t">PDF / CQT</text></a>
  <line x1="140" y1="52" x2="168" y2="52" class="svg-line" stroke-width="1.2" marker-end="url(#arr3)"/>
  <a class="map-node" href="{hr}"><rect x="168" y="30" width="150" height="44" rx="8" class="svg-node svg-node-stone" stroke="var(--svg-stroke)" stroke-width="1.2"/><text x="243" y="56" text-anchor="middle" class="svg-t">vat_inbound DB</text></a>
  <line x1="318" y1="52" x2="346" y2="52" class="svg-line" stroke-width="1.2" marker-end="url(#arr3)"/>
  <a class="map-node" href="{hr}"><rect x="346" y="30" width="130" height="44" rx="8" class="svg-node svg-node-slate" stroke="var(--svg-stroke)" stroke-width="1.2"/><text x="411" y="56" text-anchor="middle" class="svg-t">Ghép SP</text></a>
  <line x1="476" y1="52" x2="504" y2="52" class="svg-line" stroke-width="1.2" marker-end="url(#arr3)"/>
  <a class="map-node" href="{hr}"><rect x="504" y="30" width="130" height="44" rx="8" class="svg-node svg-node-green" stroke="var(--svg-active-stroke)" stroke-width="1.2"/><text x="569" y="56" text-anchor="middle" class="svg-t">Nhập kho</text></a>
  <line x1="634" y1="52" x2="662" y2="52" class="svg-line" stroke-width="1.2" marker-end="url(#arr3)"/>
  <a class="map-node" href="{hr}"><rect x="662" y="30" width="110" height="44" rx="8" class="svg-node svg-node-teal" stroke="var(--svg-active-stroke)" stroke-width="1.2"/><text x="717" y="56" text-anchor="middle" class="svg-t">Tồn + giá vốn</text></a>
</svg>"""


def write_map_portal_index_html(
    *,
    endpoint_count: int,
    page_count: int,
    api_count: int,
    schema_count: int,
) -> str:
    hub_cards: list[str] = []
    for hub in TOPIC_HUBS:
        fkey = str(hub["file"])
        meta = HUB_PORTAL_META.get(
            fkey, {"icon": "•", "tone": "#64748b", "group": "Chủ đề"}
        )
        href = portal_doc_href(chuyen_de_path(fkey))
        title = _esc_html(str(hub["title"]))
        desc = _esc_html(str(hub["desc"]))
        tone = meta["tone"]
        icon = _esc_html(meta["icon"])
        group = _esc_html(meta["group"])
        hub_cards.append(
            f"""      <a class="hub-card" href="{href}" style="--tone:{tone}">
        <span class="hub-icon" aria-hidden="true">{icon}</span>
        <span class="hub-group">{group}</span>
        <strong>{title}</strong>
        <p>{desc}</p>
      </a>"""
        )

    chi_muc = [
        ("danh-sach-api", "39 module", "Module API"),
        ("danh-sach-trang", "Màn hình", "Danh sách trang UI"),
        ("co-so-du-lieu", "Schema", "Bảng Postgres"),
        ("thu-vien-backend", "Lib", "Thư viện backend"),
        ("endpoint-http", "URL", "Endpoint HTTP"),
    ]
    chi_links = "\n".join(
        f'        <a class="chip" href="{portal_doc_href(chi_muc_path(name))}">'
        f"<span>{_esc_html(tag)}</span>{_esc_html(label)}</a>"
        for name, tag, label in chi_muc
    )

    nav = [
        ("Mục lục Markdown", map_index_path()),
        ("Hướng dẫn 3 bước", huong_dan_doc_path()),
        ("Bản đồ ASCII", ban_do_path()),
        ("Workspace", he_thong_path("02-workspace-luu-niem")),
    ]
    nav_links = "".join(
        f'<a class="nav-pill" href="{portal_doc_href(target)}">{_esc_html(label)}</a>'
        for label, target in nav
    )

    svg_runtime = _portal_svg_runtime()
    svg_flow = _portal_svg_doc_flow()
    svg_inbound = _portal_svg_inbound()

    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>VietPOS-Map — Bản đồ tài liệu</title>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🗺</text></svg>" />
  {THEME_HEAD_INLINE}
  <link rel="stylesheet" href="/assets/portal.css" />
  <style>* {{ box-sizing: border-box; }}</style>
</head>
<body class="portal-page">
  <div class="wrap">
    <header class="hero">
      <h1>VietPOS-Map</h1>
      <p class="lead">Bản đồ tài liệu tiếng Việt — bấm trên sơ đồ hoặc thẻ hub để mở đúng README (nghiệp vụ → màn hình → API → DB).</p>
      <div class="stats">
        <div class="stat"><b>{len(TOPIC_HUBS)}</b> hub chủ đề</div>
        <div class="stat"><b>{page_count}</b> trang UI</div>
        <div class="stat"><b>{api_count}</b> module API</div>
        <div class="stat"><b>{endpoint_count}</b> endpoint</div>
        <div class="stat"><b>{schema_count}</b> schema</div>
      </div>
      <nav class="nav-pills" aria-label="Liên kết nhanh">{nav_links}</nav>
    </header>

    <section>
      <h2>Bản đồ runtime</h2>
      <p class="hint">Luồng chạy thật của VietPOS — mỗi khối mở tài liệu liên quan.</p>
      <div class="map-frame">{svg_runtime}</div>
    </section>

    <section>
      <h2>Cách đọc Map</h2>
      <p class="hint">Đi từ cửa vào → hub → nghiệp vụ → UI → API → schema (ví dụ nhánh POS).</p>
      <div class="map-frame">{svg_flow}</div>
    </section>

    <section>
      <h2>Luồng HĐ đầu vào</h2>
      <p class="hint">Tóm tắt một trong các luồng phức tạp nhất — bấm để vào hub HĐ mua vào.</p>
      <div class="map-frame">{svg_inbound}</div>
    </section>

    <section>
      <h2>10 hub chủ đề</h2>
      <p class="hint">Chọn đúng việc anh đang làm — mỗi hub gom link đầy đủ theo tầng.</p>
      <div class="hub-grid">
{chr(10).join(hub_cards)}
      </div>
    </section>

    <section>
      <h2>Tra cứu kỹ thuật</h2>
      <p class="hint">Danh sách dài — dùng khi sửa code hoặc cần URL / file cụ thể.</p>
      <div class="chip-row">
{chi_links}
      </div>
    </section>

    <footer class="foot">
      Sinh tự động bởi <code>python3 docs/gen.py</code> · Nguồn code: Shop-Manager-System-Offline
    </footer>
  </div>
  <script src="/assets/theme.js"></script>
  <script src="/assets/portal-init.js"></script>
</body>
</html>
"""
    repo_root = ROOT.parent
    out = repo_root / MAP_PORTAL_INDEX
    out.write_text(html, encoding="utf-8")
    legacy = ROOT / "ban-do-kien-truc" / "so-do-tuong-tac.html"
    if legacy.is_file():
        legacy.unlink()
    return MAP_PORTAL_INDEX


def _md_page_title(md: str) -> str:
    m = re.search(r"^#\s+(.+)$", md, re.MULTILINE)
    return m.group(1).strip() if m else "VietPOS-Map"


def _view_path_from_rel(rel: str) -> str:
    if rel == README:
        return "/docs"
    if rel.endswith(f"/{README}"):
        base = rel[: -len(f"/{README}")]
        return f"/docs/{base}" if base else "/docs"
    return f"/docs/{rel}"


def _nav_item_title(rel: str) -> str:
    if rel == README:
        return "Trang chủ Map"
    folder = Path(rel).parent.name
    if folder in PAGE_SLUG.values():
        return folder.replace("-", " ").title()
    return folder.replace("-", " ")


def write_site_nav_json(all_paths: list[str]) -> None:
    hubs = [
        {"title": str(h["title"]), "href": _view_path_from_rel(chuyen_de_path(str(h["file"])))}
        for h in TOPIC_HUBS
    ]
    quick = [
        ("API (chi-muc)", _view_path_from_rel(chi_muc_path("danh-sach-api"))),
        ("Màn hình", _view_path_from_rel(chi_muc_path("danh-sach-trang"))),
        ("Schema", _view_path_from_rel(chi_muc_path("co-so-du-lieu"))),
        ("Endpoint HTTP", _view_path_from_rel(chi_muc_path("endpoint-http"))),
        ("Bản đồ hình", _view_path_from_rel(ban_do_path())),
    ]
    groups: dict[str, list[dict[str, str]]] = {}
    skip_roots = {"chuyen-de"}
    for rel in sorted(all_paths):
        if rel != README and not rel.endswith(f"/{README}"):
            continue
        if rel == README:
            continue
        parts = rel.split("/")
        if len(parts) < 2:
            continue
        sec = parts[0]
        if sec in skip_roots:
            continue
        groups.setdefault(sec, []).append(
            {"title": _nav_item_title(rel), "href": _view_path_from_rel(rel)},
        )
    payload = {
        "hubs": hubs,
        "quick": [{"title": t, "href": h} for t, h in quick],
        "groups": groups,
    }
    out = ROOT.parent / "assets" / "site-nav.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_md_index_pages(all_paths: list[str]) -> int:
    """Mỗi README.md → index.html cùng thư mục (Vercel đọc giống GitHub README)."""
    repo_root = ROOT.parent
    assets_src = repo_root / "assets" / "reader.js"
    if not assets_src.is_file():
        raise SystemExit("Missing assets/reader.js")
    count = 0
    shell = """<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title} — VietPOS-Map</title>
  <meta name="vietpos-doc" content="1" />
  {theme_head_inline}
  <link rel="stylesheet" href="/assets/doc.css" />
</head>
<body data-md-path="{md_web_path}">
  <div id="sidebar-backdrop" class="doc-sidebar-backdrop" aria-hidden="true"></div>
  <div class="doc-layout">
    <nav id="doc-sidebar" class="doc-sidebar" aria-label="Cây tài liệu"></nav>
    <div class="doc-main">
      <header class="doc-topbar">
        <button type="button" class="sidebar-toggle" id="sidebar-toggle" aria-label="Mở cây tài liệu">☰</button>
        <a href="/index.html">Bản đồ</a>
        <a href="/docs">Mục lục</a>
        <span class="doc-topbar-spacer"></span>
        <button type="button" class="theme-toggle" id="theme-toggle" aria-label="Đổi sáng tối">☀ Sáng</button>
      </header>
      <nav id="doc-breadcrumb" class="doc-breadcrumb" aria-label="Breadcrumb"></nav>
      <div class="doc-body-row">
        <main class="doc-wrap">
          <article id="content" class="markdown-body"></article>
        </main>
        <aside id="doc-toc" class="doc-toc" aria-label="Mục lục trang"></aside>
      </div>
    </div>
  </div>
  <script id="md-b64" type="application/octet-stream">{b64}</script>
  <script src="https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.min.js"></script>
  <script src="/assets/theme.js"></script>
  <script src="/assets/reader.js"></script>
</body>
</html>
"""
    for rel in all_paths:
        if rel != README and not rel.endswith(f"/{README}"):
            continue
        md_path = ROOT / rel
        if not md_path.is_file():
            continue
        md_text = md_path.read_text(encoding="utf-8")
        b64 = base64.standard_b64encode(md_text.encode("utf-8")).decode("ascii")
        title = _esc_html(_md_page_title(md_text))
        if rel == README:
            md_web_path = "/docs/README.md"
        else:
            md_web_path = "/docs/" + rel
        html = shell.format(
            title=title,
            md_web_path=_esc_html(md_web_path),
            b64=b64,
            theme_head_inline=THEME_HEAD_INLINE,
        )
        (md_path.parent / "index.html").write_text(html, encoding="utf-8")
        count += 1
    return count


def write_doc_assets() -> None:
    """doc.css + reader.js giữ tay trong repo; gen chỉ đảm bảo thư mục assets/."""
    (ROOT.parent / "assets").mkdir(parents=True, exist_ok=True)


def write_ban_do_hinh() -> str:
    rel = ban_do_path()
    register_desc(rel, HE_THONG_DESC[legacy_desc_key(rel)])
    hub_table = "\n".join(
        f"| [{hub['title']}]({md_href(rel, chuyen_de_path(str(hub['file'])))}) | {hub['desc']} |"
        for hub in TOPIC_HUBS
    )
    so_do_html_href = portal_index_href(rel)
    hub_mermaid = mermaid_hub_map(rel)
    mermaid_placeholder = "___VIETPOS_MAP_MERMAID_HUB___"
    body = f"""
# Bản đồ kiến trúc (hình)

**Mô tả:** Sơ đồ **vẽ bằng ký tự** — hiển thị trực tiếp trong Cursor/GitHub, không cần plugin Mermaid.

← [Trang chủ Map](00-muc-luc-va-kien-truc.md) · [Hướng dẫn đọc](00-huong-dan-doc-tai-lieu.md)

---

## 0. Sơ đồ bấm được (khuyên dùng)

1. **[Mở index.html — sơ đồ bấm được]({so_do_html_href})** (gốc repo VietPOS-Map; 10 hub + runtime + chỉ mục).
2. **Mermaid hub** (preview Markdown — bấm nút trên sơ đồ nếu viewer hỗ trợ `click`):

{mermaid_placeholder}

| Hub | Mô tả ngắn |
|-----|------------|
{hub_table}

---

## 1. Hệ thống VietPOS (runtime)

```
┌─────────────────────────────────────────────────────────────────┐
│                     MÁY NGƯỜI DÙNG                            │
│  ┌──────────────┐      ┌──────────────────┐                     │
│  │ Trình duyệt  │      │ IndexedDB        │                     │
│  │ hoặc Tauri   │─────▶│ (offline: đơn,   │                     │
│  │              │      │  HĐ chờ sync)    │                     │
│  └──────┬───────┘      └────────▲─────────┘                     │
│         │                       │ pull / push                   │
│         │  HTTPS  /api/*        │                               │
│         ▼                       │                               │
└─────────┼───────────────────────┼───────────────────────────────┘
          │                       │
          ▼                       │
┌─────────────────────────────────┴───────────────────────────────┐
│                      api-server (Express)                        │
│   JWT · quyền shop · Viettel/CQT · nghiệp vụ POS/kho/HĐ VAT      │
└─────────┬───────────────────────────────┬───────────────────────┘
          │ Drizzle                         │ cloud-sync (tùy chọn)
          ▼                                 ▼
┌──────────────────┐              ┌──────────────────┐
│ PostgreSQL       │              │ Postgres cloud   │
│ (máy chủ shop)   │─────────────▶│ (Railway, ops)   │
└──────────────────┘   mirror     └──────────────────┘

     Widget Android / ESP32 ──API key──▶ visitor-counts, widget/home
```

| Thành phần | Ghi chú |
|------------|---------|
| **pos-app** | React — POS, kho, HĐ, cấu hình chuỗi |
| **api-server** | Một cửa `/api` cho mọi nghiệp vụ |
| **local-db + sync** | Quầy vẫn bán khi mất mạng |
| **cloud-sync** | Sao chép DB lên cloud (không thay thế DB local) |

*Phiên bản Mermaid (nếu IDE hỗ trợ):* [chuyen-de/00-kien-truc-he-thong.md](chuyen-de/00-kien-truc-he-thong.md)

---

## 2. Bản đồ tài liệu VietPOS-Map (cách đi)

```
                    ┌─────────────────────────────┐
                    │  ban-do-kien-truc.md (đây)  │
                    │  sơ đồ hình + hướng dẫn     │
                    └──────────────┬──────────────┘
                                   │
         ┌─────────────────────────┼─────────────────────────┐
         ▼                         ▼                         ▼
┌─────────────────┐    ┌──────────────────────┐    ┌─────────────────┐
│ 00-huong-dan    │    │ 00-muc-luc (trang    │    │ chuyen-de/      │
│ (3 bước đọc)    │    │ chủ Map)             │    │ 10 hub chủ đề   │
└────────┬────────┘    └──────────┬───────────┘    └────────┬────────┘
         │                        │                         │
         │            chọn 1 chủ đề (POS, HĐ đầu vào…)     │
         │                        └────────────┬────────────┘
         │                                     ▼
         │              ┌──────────────────────────────────────────┐
         │              │  Trên mỗi hub, đọc theo thứ tự:           │
         │              │  ① nghiep-vu/  →  ② frontend-pages/      │
         │              │  →  ③ api-modules/  →  ④ schema/        │
         │              │  →  ⑤ lib-modules/ (một phần)             │
         │              └────────────────────┬─────────────────────┘
         │                                   │
         │         cần tra hết URL / file    ▼
         │              ┌──────────────────────────────────────────┐
         └─────────────▶│  chi-muc/  (danh sách dài, tách riêng)   │
                        │  · api-modules · trang-giao-dien          │
                        │  · thu-vien-backend · schema · endpoint   │
                        └──────────────────────────────────────────┘

   reference/  = doc gốc Shop (tiếng Anh) — RBAC, database, Docker
```

---

## 3. Hub chủ đề (chọn một nhánh)

```
                    [00-muc-luc / chuyen-de]
                              │
    ┌────────────┬────────────┼────────────┬────────────┐
    ▼            ▼            ▼            ▼            ▼
 Đăng nhập     POS &       Sản phẩm    HĐ đầu vào   HĐ bán ra
 & phiên       đơn hàng    & kho       (VAT mua)    (Viettel)
    │            │            │            │            │
    └────────────┴────────────┴────────────┴────────────┘
                              │
         Chuỗi shop · An ninh · Offline · Trợ lý/widget
```

Danh sách link đầy đủ (bấm được): mục **[0. Sơ đồ bấm được](#0-sơ-đồ-bấm-được-khuyên-dùng)** phía trên · [Trang chủ Map](00-muc-luc-va-kien-truc.md)

---

## 4. Luồng dữ liệu HĐ đầu vào (tóm tắt)

```
 PDF / Excel / CQT sync
         │
         ▼
  vat_inbound_invoices (Postgres)
         │
         ├── MST lọc? ──▶ archived → tab "Khác"
         │
         ▼
  Ghép dòng SP (stock-receipt) → nhập kho (receive-stock) → tồn + giá vốn
```

Chi tiết: [hoa-don-dau-vao](../chuyen-de/hoa-don-dau-vao/README.md)
"""
    text = rewrite_legacy_links(body.strip()) + "\n"
    text = text.replace(mermaid_placeholder, hub_mermaid)
    text = text.replace(
        "← [Trang chủ Map](00-muc-luc-va-kien-truc.md) · [Hướng dẫn đọc](00-huong-dan-doc-tai-lieu.md)",
        f"← [Trang chủ Map]({md_href(rel, map_index_path())}) · "
        f"[Hướng dẫn đọc]({md_href(rel, huong_dan_doc_path())})",
    )
    p = ROOT / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    return rel


def menu_by_href() -> dict[str, dict[str, str]]:
    global _MENU_BY_HREF
    if _MENU_BY_HREF is not None:
        return _MENU_BY_HREF
    out: dict[str, dict[str, str]] = {}
    if APP_LAYOUT.is_file():
        layout = APP_LAYOUT.read_text(encoding="utf-8", errors="replace")
        for block in re.finditer(r"\{[^{}]*href:\s*\"([^\"]+)\"[^{}]*\}", layout):
            chunk = block.group(0)
            href = block.group(1)
            label_m = re.search(r'label:\s*"([^"]+)"', chunk)
            show_m = re.search(r"show:\s*([^,}\n]+)", chunk)
            out[href] = {
                "label": label_m.group(1) if label_m else "",
                "show": show_m.group(1).strip() if show_m else "",
            }
    _MENU_BY_HREF = out
    return out


def api_paths_in_source(text: str) -> list[str]:
    hits = set(re.findall(r'["\'](/api/[^"\']+)["\']', text))
    hits.update(re.findall(r"[`](/api/[^`]+)[`]", text))
    return sorted(hits)


def embedded_shop_components(text: str) -> list[tuple[str, Path]]:
    """Import từ @/components/... → đường dẫn file thực."""
    found: list[tuple[str, Path]] = []
    for mod in re.findall(r'from ["\']@/components/([^"\']+)["\']', text):
        base = COMPONENTS_DIR / mod
        candidates = [base.with_suffix(".tsx"), base / "index.tsx"]
        for p in candidates:
            if p.is_file():
                found.append((mod, p))
                break
    return found


def embedded_page_sections(text: str) -> list[tuple[str, Path]]:
    """Section/page con import từ @/pages/... (vd. access-block → ip-ban)."""
    found: list[tuple[str, Path]] = []
    for mod in re.findall(r'from ["\']@/pages/([^"\']+)["\']', text):
        p = PAGES_DIR / f"{mod}.tsx"
        if p.is_file():
            found.append((f"pages/{mod}", p))
    return found


def page_embedded_modules(text: str) -> list[tuple[str, Path]]:
    seen: set[Path] = set()
    out: list[tuple[str, Path]] = []
    for mod, p in embedded_shop_components(text) + embedded_page_sections(text):
        if p in seen:
            continue
        seen.add(p)
        out.append((mod, p))
    return out


def collect_page_api_hits(page_file: Path, text: str, depth: int = 0) -> tuple[list[str], list[tuple[str, Path]]]:
    """API trong page + 1 lớp component @/components (shell pages)."""
    hits = set(api_paths_in_source(text))
    embedded = page_embedded_modules(text)
    if depth < 1 and len(hits) < 3 and embedded:
        for _mod, path in embedded:
            child = path.read_text(encoding="utf-8", errors="replace")
            hits.update(api_paths_in_source(child))
    return sorted(hits), embedded


def ui_scan_components(
    text: str, embedded: list[tuple[str, Path]]
) -> list[tuple[str, Path]]:
    """Component/section con cần quét nhãn UI."""
    if is_shell_page(text):
        return embedded
    picked = [
        (mod, p)
        for mod, p in embedded
        if re.search(r"(Section|Panel|BanSection)$", mod.split("/")[-1])
        or mod.startswith("pages/")
    ]
    return picked


def build_page_ui_markdown(
    name: str, text: str, embedded: list[tuple[str, Path]]
) -> str:
    page_ui = extract_page_ui(text)
    child_blocks: list[tuple[str, object]] = []
    for mod, path in ui_scan_components(text, embedded):
        child_text = path.read_text(encoding="utf-8", errors="replace")
        child_blocks.append((mod, extract_page_ui(child_text)))
    return render_page_ui_markdown(name, page_ui, child_blocks)


def default_page_doc(
    name: str,
    route: str,
    one_line: str,
    api_hits: list[str],
    embedded: list[tuple[str, Path]],
    from_doc: str = "",
) -> str:
    slug = name.replace(".tsx", "")
    menu = menu_by_href().get(route, {})
    lines = [
        f"**Đường dẫn:** `{route}`",
        "",
        one_line or f"Màn hình **{slug}** trong POS hoặc admin.",
        "",
    ]
    if menu.get("label"):
        lines.extend(
            [
                "## Menu sidebar",
                "",
                f"- **Nhãn:** {menu['label']}",
                f"- **Điều kiện hiện menu (`show`):** `{menu.get('show', '—')}`",
                "",
            ]
        )
    nv = ROUTE_NGHIEP_VU.get(route)
    if nv:
        lines.extend(["## Nghiệp vụ (doc)", "", f"- `{nv}`", ""])
    if embedded:
        lines.append("## Component con (logic UI chính)")
        lines.append("")
        for mod, path in embedded:
            rel = path.relative_to(SHOP)
            lines.append(f"- `@/components/{mod}` → `{rel}`")
        lines.append("")
    lines.extend(
        [
            "## Cách đọc code",
            "",
            "- API: tìm `useQuery`, `useMutation`, `apiFetch`, hoặc mục **Chuỗi `/api/...`** bên dưới.",
            "- Quyền: `lib/session-permissions.ts`, biểu thức trong `app-layout.tsx` và file page.",
            "- Offline: các trang POS có thể gọi Dexie qua `@/lib/offline/...`.",
            "",
        ]
    )
    modules = sorted(
        {
            h.split("/")[2]
            for h in api_hits
            if h.startswith("/api/") and len(h.split("/")) > 2
        }
    )
    if modules:
        lines.append("## Module API liên quan (trong Map)")
        lines.append("")
        for m in modules:
            target = module_api_path(m)
            href = md_href(from_doc, target) if from_doc else target
            lines.append(f"- [`{m}`]({href}) — nhóm `/api/{m}`")
        lines.append("")
    return "\n".join(lines)


def append_page_analysis(lines: list[str], name: str, text: str) -> None:
    """Bổ sung mục phân tích tự động từ source TSX."""
    sub_exports = re.findall(r"export function (\w+)", text)
    if sub_exports:
        lines.append("## Component con export trong file")
        lines.append("")
        for e in sub_exports:
            lines.append(f"- `{e}`")
        lines.append("")

    if re.search(r"super_admin", text):
        lines.append("## Quyền (phát hiện trong source)")
        lines.append("")
        lines.append("- Có kiểm tra role **`super_admin`** (hoặc redirect dashboard).")
        lines.append("")

    qkeys = re.findall(r"const QUERY_KEY = (\[[^\]]+\])", text)
    if qkeys:
        lines.append("## React Query keys")
        lines.append("")
        for qk in qkeys:
            lines.append(f"- `{qk}`")
        lines.append("")

    tab_vals = sorted(set(re.findall(r'<TabsTrigger[^>]*value="(\w+)"', text)))
    if tab_vals:
        lines.append("## Tab UI (`TabsTrigger` value)")
        lines.append("")
        for t in tab_vals:
            lines.append(f"- `{t}`")
        lines.append("")

    if "?tab=" in text or "initialTabFromSearch" in text:
        lines.append("## Query string URL")
        lines.append("")
        lines.append("- Tab qua `?tab=` — xem `initialTabFromSearch` trong file.")
        lines.append("")
    elif "URLSearchParams" in text:
        params = sorted(set(re.findall(r'params\.get\(["\'](\w+)["\']', text)))
        if params:
            lines.append("## Query string URL (đọc trong code)")
            lines.append("")
            for p in params:
                lines.append(f"- `{p}`")
            lines.append("")

    redirects = sorted(set(re.findall(r'<Redirect to="([^"]+)"', text)))
    if redirects:
        lines.append("## Redirect trong component")
        lines.append("")
        for r in redirects:
            lines.append(f"- → `{r}`")
        lines.append("")

    fetch_fns = re.findall(r"async function (\w+)\([^)]*\)[^{]*\{[^}]*fetch\(\s*['\"](/api/[^'\"]+)", text)
    if fetch_fns:
        lines.append("## Hàm fetch API (trích)")
        lines.append("")
        seen: set[str] = set()
        for fn, path in fetch_fns:
            key = f"{fn} → {path}"
            if key in seen:
                continue
            seen.add(key)
            lines.append(f"- `{fn}` → `{path}`")
        lines.append("")

    jsx_comps = sorted(
        set(re.findall(r"<([A-Z][A-Za-z0-9]+)", text))
        - {"Redirect", "Route", "Fragment", "Suspense", "AppLayout"}
    )
    if jsx_comps:
        lines.append("## JSX component dùng trong file (PascalCase)")
        lines.append("")
        for c in jsx_comps[:25]:
            lines.append(f"- `<{c} />`")
        if len(jsx_comps) > 25:
            lines.append(f"- … {len(jsx_comps) - 25} component khác")
        lines.append("")

    dialog_titles = re.findall(r"<(?:AlertDialogTitle|DialogTitle)[^>]*>([^<]+)</", text)
    if dialog_titles:
        lines.append("## Dialog / modal (tiêu đề)")
        lines.append("")
        for t in sorted(set(dialog_titles)):
            lines.append(f"- {t.strip()}")
        lines.append("")


def parse_page_routes() -> dict[str, str]:
    if not APP_TSX.is_file():
        return {}
    text = APP_TSX.read_text(encoding="utf-8")
    comp_to_file = {
        m.group(1): f"{m.group(2)}.tsx"
        for m in re.finditer(r'import\s+(\w+)\s+from\s+"@/pages/([\w-]+)"', text)
    }
    path_by_comp: dict[str, str] = {}
    for m in re.finditer(
        r'<Route path="([^"]+)"\s+component=\{(\w+)\}',
        text,
    ):
        path_by_comp[m.group(2)] = m.group(1)
    for m in re.finditer(
        r'<Route path="([^"]+)">\s*<AppLayout>\s*<(\w+)\s*/>\s*</AppLayout>',
        text,
    ):
        path_by_comp[m.group(2)] = m.group(1)
    return {
        fname: path_by_comp[comp]
        for comp, fname in comp_to_file.items()
        if comp in path_by_comp
    }


def middleware_from_block(block: str) -> list[str]:
    return sorted(set(re.findall(r"(require\w+)", block)))


def endpoint_anchor(method: str, path: str) -> str:
    raw = f"{method.lower()}-{path.strip('/')}".replace("/", "-")
    return re.sub(r"[^a-zA-Z0-9_-]", "-", raw).strip("-")


def endpoint_note(module_key: str, method: str, path: str, middleware: list[str]) -> str:
    return endpoint_summary(module_key, method, path, middleware)


def write_api_modules() -> tuple[list[str], list[tuple[str, str, str, str]]]:
    paths: list[str] = []
    flat_endpoints: list[tuple[str, str, str, str]] = []
    zod_schemas = load_zod_schemas(SHOP)
    for f in sorted(ROUTES_DIR.glob("*.ts")):
        if f.name == "index.ts":
            continue
        key = f.stem
        text = f.read_text(encoding="utf-8", errors="replace")
        blocks = [
            (m.group(1).upper(), m.group(2), m.group(3))
            for m in ROUTE_BLOCK_RE.finditer(text)
        ]
        routes = extract_routes(text)
        handlers_by_route = {
            (meth, pth): chunk for meth, pth, chunk in iter_route_handlers(text)
        }
        rel_shop = f"artifacts/api-server/src/routes/{f.name}"
        intro = api_module_intro_text(key)
        rel = module_api_path(key)
        desc = register_desc(
            rel,
            f"Module API `{key}.ts` — {len(routes)} endpoint. {one_line(intro, 120)}",
        )
        lines = [
            f"# Module API: `{key}`",
            "",
            f"**Mô tả:** {desc}",
            "",
            f"**Mã nguồn Shop:** `{rel_shop}`",
            "",
            intro.strip(),
            "",
            f"**Số endpoint:** {len(routes)}",
            "",
            "**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), "
            "bảng lỗi `error`, và response (Zod hoặc trường `res.json`).",
            "",
            "## Bảng endpoint (tóm tắt)",
            "",
            "| Method | Path | Mô tả ngắn |",
            "|--------|------|------------|",
        ]
        block_map = {(m, p): mid for m, p, mid in blocks}
        for method, path in routes:
            api_path = path if path.startswith("/") else f"/{path}"
            mid = block_map.get((method, path), "")
            mw = middleware_from_block(mid)
            note = endpoint_note(key, method, path, mw)
            short = note.split(".")[0][:120] + ("…" if len(note) > 120 else "")
            lines.append(f"| {method} | `{api_path}` | {short} |")
            flat_endpoints.append((key, method, api_path, rel))
        lines.extend(
            [
                "",
                "## Chi tiết từng endpoint",
                "",
            ]
        )
        for method, path, mid in blocks:
            api_path = path if path.startswith("/") else f"/{path}"
            chunk = handlers_by_route.get((method, path), "")
            mw = middleware_from_block(mid or chunk[:600])
            anchor = endpoint_anchor(method, path)
            note = endpoint_note(key, method, path, mw)
            lines.append(f"### `{method} {api_path}` {{#{anchor}}}")
            lines.append("")
            lines.append(note)
            lines.append("")
            detail = endpoint_detail_body(method, path)
            if not detail:
                detail = build_endpoint_detail_auto(
                    method, path, chunk, mw, zod_schemas
                )
            if detail:
                lines.append(detail)
                lines.append("")
            elif mw:
                lines.append(f"- **Lớp kiểm tra (middleware):** {', '.join(f'`{x}`' for x in mw)}")
                lines.append("")
        lines.extend(
            [
                "## Ghi chú đọc mã",
                "",
                f"- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./{f.name}`.",
                "- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).",
                f"- Quyền role: `{tham_chieu_path('rbac.md')}` (tiếng Anh gốc) + các `require*` trong từng endpoint.",
                "",
                f"**Đọc tiếp:** [Hướng dẫn Map]({md_href(rel, huong_dan_doc_path())}) · "
                f"[Mục lục]({md_href(rel, map_index_path())})",
                "",
            ]
        )
        if key == "vat-inbound":
            lines.extend(
                [
                    "## Luồng nghiệp vụ liên quan",
                    "",
                    f"- `{nghiep_vu_path('06-hoa-don-dau-vao-tong-quan')}`",
                    f"- `{nghiep_vu_path('07-hd-dau-vao-mst-loc')}`",
                    f"- `{nghiep_vu_path('08-hd-dau-vao-cqt-sync')}`",
                    f"- UI: `{trang_path('vat-inbound')}`",
                    f"- Lib: `{thu_vien_path('vat-inbound-tax-sync')}`, `{thu_vien_path('gdt-portal')}`…",
                    "",
                ]
            )
        if key in ("blocked-ips", "blocked-devices", "access-observations"):
            lines.extend(
                [
                    "## Luồng nghiệp vụ liên quan",
                    "",
                    f"- `{nghiep_vu_path('10-truy-cap-an-ninh')}`",
                    f"- UI: `{trang_path('access-block')}`",
                    f"- Middleware: `{thu_vien_path('ip-denylist')}`, `{thu_vien_path('device-denylist')}`, "
                    f"`{thu_vien_path('api-access-observations')}`",
                    "",
                ]
            )
        out = ROOT / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text("\n".join(lines), encoding="utf-8")
        paths.append(rel)
    return paths, flat_endpoints


def write_pages() -> list[str]:
    paths: list[str] = []
    page_routes = parse_page_routes()
    for f in sorted(PAGES_DIR.glob("*.tsx")):
        name = f.name
        text = f.read_text(encoding="utf-8", errors="replace")
        line_count = text.count("\n") + 1
        route = page_routes.get(name, "*(public hoặc redirect — xem App.tsx)*")
        one = PAGE_ONE_LINE.get(name, "")
        api_hits, embedded = collect_page_api_hits(f, text)
        rel = trang_path(name.replace(".tsx", ""))
        doc = rewrite_legacy_links(
            PAGE_DOCS.get(
                name,
                default_page_doc(name, route, one, api_hits, embedded, rel),
            )
        )
        lib_api = sorted(set(re.findall(r"from ['\"]@/lib/([\w/-]+)['\"]", text)))[:20]
        perm_hits = sorted(set(re.findall(r"(userCan\w+|canAccess\w+|require\w+)", text)))[:15]
        comp_match = re.search(r"export default function (\w+)", text)
        comp_name = comp_match.group(1) if comp_match else "*(default export)*"
        imports = [ln.strip() for ln in text.splitlines()[:55] if ln.strip().startswith("import ")]
        desc = register_desc(
            rel,
            f"{one} (URL `{route}`, `{comp_name}`, ~{line_count} dòng)."
            if one
            else f"Trang React `{route}` — `{comp_name}`, ~{line_count} dòng.",
        )
        ui_md = build_page_ui_markdown(name, text, embedded)
        lines = [
            f"# Trang giao diện: `{name}`",
            "",
            f"**Mô tả:** {desc}",
            "",
            f"**Mã nguồn Shop:** `artifacts/pos-app/src/pages/{name}`",
            "",
            f"**Đường dẫn URL:** `{route}`",
            f"**Tên component React:** `{comp_name}`",
            f"**Quy mô:** ~{line_count} dòng.",
            "",
        ]
        if ui_md:
            lines.append(ui_md)
        lines.extend(
            [
                doc.strip(),
                "",
                f"**Đọc tiếp:** [Hướng dẫn đọc Map]({md_href(rel, huong_dan_doc_path())})",
                "",
            ]
        )
        append_page_analysis(lines, name, text)
        if perm_hits:
            lines.append("## Biểu thức quyền / guard trong file")
            lines.append("")
            for p in perm_hits:
                lines.append(f"- `{p}`")
            lines.append("")
        lines.append("## Import chính (đầu file)")
        lines.append("")
        for imp in imports[:18]:
            lines.append(f"- `{imp}`")
        if len(imports) > 18:
            lines.append(f"- … {len(imports) - 18} import khác")
        lines.append("")
        if lib_api:
            lines.append("## Module `@/lib/...` được import")
            lines.append("")
            for h in lib_api:
                lines.append(f"- `@/lib/{h}`")
            lines.append("")
        if embedded and name not in PAGE_DOCS:
            lines.append("## Component `@/components/...` (đã quét API lớp 1)")
            lines.append("")
            for mod, path in embedded:
                rel_c = path.relative_to(SHOP)
                lines.append(f"- `{mod}` → `{rel_c}`")
            lines.append("")
        if api_hits:
            lines.append(
                f"## Chuỗi `/api/...` (page + component con, {len(api_hits)} mục)"
            )
            lines.append("")
            for h in api_hits:
                mod = h.split("/")[2] if h.startswith("/api/") and len(h.split("/")) > 2 else ""
                api_doc = module_api_path(mod)
                if mod and (ROOT / api_doc).is_file():
                    lines.append(f"- `{h}` → [`{mod}`]({md_href(rel, api_doc)})")
                else:
                    lines.append(f"- `{h}`")
            lines.append("")
        nv = ROUTE_NGHIEP_VU.get(route)
        if nv:
            lines.extend(
                [
                    "## Luồng nghiệp vụ (doc)",
                    "",
                    f"- [{Path(nv).parent.name}]({md_href(rel, nv)})",
                    "",
                ]
            )
        lines.extend(
            [
                "## Liên kết mã",
                "",
                "- Khai báo URL: `artifacts/pos-app/src/App.tsx`",
                "- Menu/layout: `components/layout/app-layout.tsx`",
                "- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`",
                "",
            ]
        )
        out = ROOT / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text("\n".join(lines), encoding="utf-8")
        paths.append(rel)
    return paths


def route_stem_for_schema(schema_stem: str) -> str | None:
    if schema_stem in SCHEMA_ROUTE_ALIAS:
        alias = SCHEMA_ROUTE_ALIAS[schema_stem]
        if (ROUTES_DIR / f"{alias}.ts").is_file():
            return alias
    kebab = camel_to_kebab(schema_stem)
    if (ROUTES_DIR / f"{kebab}.ts").is_file():
        return kebab
    if (ROUTES_DIR / f"{schema_stem}.ts").is_file():
        return schema_stem
    return None


def schema_related_links(rel: str, schema_stem: str) -> list[str]:
    lines: list[str] = []
    route = route_stem_for_schema(schema_stem)
    if route:
        api_rel = module_api_path(route)
        lines.append(
            f"- **HTTP API:** [{Path(api_rel).parent.name}]({md_href(rel, api_rel)}) "
            f"(`routes/{route}.ts`)"
        )
    page_key = schema_stem
    if page_key not in PAGE_SLUG:
        page_key = camel_to_kebab(schema_stem)
    page_candidates = [schema_stem, camel_to_kebab(schema_stem)]
    for pc in page_candidates:
        if pc in PAGE_SLUG and (PAGES_DIR / f"{pc}.tsx").is_file():
            pg = trang_path(pc)
            lines.append(
                f"- **Giao diện:** [{Path(pg).parent.name}]({md_href(rel, pg)})"
            )
            break
    return lines


def write_schemas() -> list[str]:
    paths: list[str] = []
    SCHEMA_STEM_REL.clear()
    files = sorted(p for p in SCHEMA_DIR.glob("*.ts") if p.name != "index.ts")
    texts = {f.stem: f.read_text(encoding="utf-8", errors="replace") for f in files}
    var_to_pg = build_var_to_pg_map(texts)

    for f in files:
        text = texts[f.stem]
        sf = parse_schema_file(f.stem, text, var_to_pg)
        if not sf.tables and not sf.enums:
            continue
        rel = co_so_du_lieu_path(f.stem)
        SCHEMA_STEM_REL[f.stem] = rel
        desc = register_desc(rel, schema_summary(sf))
        ref_href = md_href(rel, tham_chieu_path("database.md"))
        lines = [
            f"# Schema: `{f.stem}`",
            "",
            f"**Mô tả:** {desc}",
            "",
            f"**Mã nguồn Shop:** `lib/db/src/schema/{f.name}`",
            "",
            "## Cách đọc trang này",
            "",
            "Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại "
            "(cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê "
            "riêng khi có trong file.",
            "",
        ]
        related = schema_related_links(rel, f.stem)
        if related:
            lines.extend(["## Liên kết nhanh", ""] + related + [""])
        lines.append(render_schema_markdown(sf, ref_db_href=ref_href))
        out = ROOT / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text("\n".join(lines), encoding="utf-8")
        paths.append(rel)
    return paths


def write_lib_modules() -> list[str]:
    paths: list[str] = []
    if not LIB_ROOT.is_dir():
        return paths
    for f in sorted(LIB_ROOT.rglob("*.ts")):
        rel_from_lib = f.relative_to(LIB_ROOT)
        rel = thu_vien_path(rel_from_lib.with_suffix("").as_posix())
        text = f.read_text(encoding="utf-8", errors="replace")
        line_count = text.count("\n") + 1
        exports = [a or b for a, b in EXPORT_RE.findall(text)]
        imports_db = [ln.strip() for ln in text.splitlines() if "@workspace/db" in ln][:8]
        rel_shop = f"artifacts/api-server/src/lib/{rel_from_lib.as_posix()}"
        ex_preview = ", ".join(exports[:5]) if exports else "(không export tên rõ)"
        if exports and len(exports) > 5:
            ex_preview += ", …"
        hub, topic = lib_topic_for_path(rel_from_lib.as_posix())
        desc = register_desc(
            rel,
            f"[{topic}] `{rel_from_lib.as_posix()}` — {ex_preview}.",
        )
        lines = [
            f"# Thư viện: `{rel_from_lib.as_posix()}`",
            "",
            f"**Mô tả:** {desc}",
            "",
            f"**Chủ đề:** [{topic}]({md_href(rel, hub)})",
            "",
            f"**Mã nguồn Shop:** `{rel_shop}` · **Quy mô:** ~{line_count} dòng",
            "",
            "File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. "
            "Thuật toán đầy đủ nằm trong mã TypeScript gốc.",
            "",
        ]
        if exports:
            lines.append(f"## Hàm/hằng export ({len(exports)})")
            lines.append("")
            for ex in exports[:40]:
                lines.append(f"- `{ex}`")
            if len(exports) > 40:
                lines.append(f"- … {len(exports) - 40} export khác")
            lines.append("")
        if imports_db:
            lines.append("## Import cơ sở dữ liệu")
            lines.append("")
            for imp in imports_db:
                lines.append(f"- `{imp}`")
            lines.append("")
        if line_count <= 80:
            preview = "\n".join(text.splitlines()[: min(line_count, 45)])
            lines.extend(
                [
                    "## Trích mã (tham khảo)",
                    "",
                    "```typescript",
                    preview,
                    "```",
                    "",
                ]
            )
        lines.extend(
            [
                f"← [Chỉ mục lib]({md_href(rel, chi_muc_path('thu-vien-backend'))}) · "
                f"[Hub {topic}]({md_href(rel, hub)})",
                "",
            ]
        )
        out_path = ROOT / rel
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text("\n".join(lines), encoding="utf-8")
        paths.append(rel)
    return paths


def write_dict_files(mapping: dict[str, str]) -> list[str]:
    paths: list[str] = []
    for rel, body in mapping.items():
        rel_out = resolve_doc_link(rel)
        b = rewrite_legacy_links(body.strip())
        leg = legacy_desc_key(rel_out)
        desc = (
            HE_THONG_DESC.get(leg)
            or HE_THONG_DESC.get(rel)
            or NGHIEP_VU_DESC.get(leg)
            or NGHIEP_VU_DESC.get(rel)
            or summary_from_markdown_body(b)
            or Path(rel_out).parent.name.replace("-", " ")
        )
        register_desc(rel_out, desc)
        p = ROOT / rel_out
        p.parent.mkdir(parents=True, exist_ok=True)
        if b.startswith("#"):
            lines = prepend_mo_ta_block(b.splitlines(), DOC_DESCRIPTIONS[rel_out])
            p.write_text("\n".join(lines) + "\n", encoding="utf-8")
        else:
            title = Path(rel_out).parent.name.replace("-", " ").title()
            lines = [
                f"# {title}",
                "",
                f"**Mô tả:** {DOC_DESCRIPTIONS[rel_out]}",
                "",
                b,
            ]
            p.write_text("\n".join(lines) + "\n", encoding="utf-8")
        paths.append(rel_out)
    return paths


def write_index(
    all_paths: list[str],
    flat_endpoints: list[tuple[str, str, str, str]],
) -> None:
    nghiep = sorted(p for p in all_paths if p.startswith("nghiep-vu/"))
    he_thong = sorted(p for p in all_paths if p.startswith("he-thong/"))
    ref_files = sorted(p for p in all_paths if p.startswith("tham-chieu/"))

    lines = [
        "# VietPOS-Map — Bản đồ tài liệu",
        "",
        "**Mô tả:** Trang chủ Map — mỗi chủ đề nằm trong **một thư mục**, file **`README.md`**.",
        "",
        f"**Cửa vào (index.html):** [{portal_index_href(map_index_path())}]({portal_index_href(map_index_path())})",
        f"**Bản đồ hình (ASCII + Mermaid):** [{README}]({ban_do_path()})",
        "",
        f"1. [Hướng dẫn đọc (3 bước)]({huong_dan_doc_path()})",
        f"2. [Kiến trúc — Mermaid]({chuyen_de_path('kien-truc-he-thong')})",
        "",
        "**Tạo lại:** `python3 docs/gen.py`",
        "",
        "---",
        "",
        "## Chủ đề (chuyen-de)",
        "",
        "Mỗi thư mục gom link **nghiệp vụ → màn hình → API → schema → lib** theo một việc.",
        "",
    ]
    for hub in TOPIC_HUBS:
        rel = chuyen_de_path(str(hub["file"]))
        lines.append(f"- [{hub['title']}]({rel}) — {hub['desc']}")
    lines.extend(["", "---", "", "## Mười hai chương nghiệp vụ", ""])
    for i, item in enumerate(nghiep, 1):
        d = one_line(DOC_DESCRIPTIONS.get(item, ""), 120)
        label = Path(item).parent.name
        lines.append(f"{i}. [{label}]({item}) — {d}")
    lines.extend(
        [
            "",
            "---",
            "",
            "## Hệ thống (chi tiết kỹ thuật)",
            "",
        ]
    )
    for item in he_thong:
        d = one_line(DOC_DESCRIPTIONS.get(item, ""), 120)
        label = Path(item).parent.name
        lines.append(f"- [{label}]({item}) — {d}")
    lines.extend(
        [
            "",
            "---",
            "",
            "## Tra cứu kỹ thuật (chi-muc)",
            "",
            "Dùng **sau** hub chủ đề — danh sách dài, không đọc từ đầu đến cuối.",
            "",
            "| Chỉ mục | Nội dung |",
            "|---------|----------|",
            f"| [danh-sach-api]({chi_muc_path('danh-sach-api')}) | {sum(1 for p in all_paths if p.startswith('module-api/'))} module API |",
            f"| [danh-sach-trang]({chi_muc_path('danh-sach-trang')}) | {sum(1 for p in all_paths if p.startswith('trang/'))} trang UI |",
            f"| [thu-vien-backend]({chi_muc_path('thu-vien-backend')}) | {sum(1 for p in all_paths if p.startswith('thu-vien/'))} file lib |",
            f"| [co-so-du-lieu]({chi_muc_path('co-so-du-lieu')}) | {sum(1 for p in all_paths if p.startswith('co-so-du-lieu/'))} schema |",
            f"| [endpoint-http]({chi_muc_path('endpoint-http')}) | {len(flat_endpoints)} endpoint HTTP |",
            "",
            "---",
            "",
            "## Tài liệu tham chiếu gốc Shop (tiếng Anh)",
            "",
        ]
    )
    for rel in ref_files:
        label = Path(rel).parent.name
        d = one_line(DOC_DESCRIPTIONS.get(rel, ""), 100)
        lines.append(f"- [{label}]({rel}) — {d}")
    lines.extend(
        [
            "",
            "---",
            "",
            "## Thống kê",
            "",
            f"- Hub chủ đề: {len(TOPIC_HUBS)}",
            f"- README sinh tự động: ~{len(all_paths)}",
            f"- Endpoint HTTP: {len(flat_endpoints)}",
            "",
        ]
    )
    rel_index = map_index_path()
    register_desc(
        rel_index,
        "Trang chủ Map — hub chủ đề, 12 chương nghiệp vụ, link chỉ mục kỹ thuật.",
    )
    (ROOT / rel_index).write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    if not SHOP.is_dir():
        raise SystemExit(f"Missing Shop: {SHOP}")
    DOC_DESCRIPTIONS.clear()
    clean_generated()
    all_paths: list[str] = []
    all_paths.extend(mirror_shop())
    all_paths.append(write_huong_dan_doc())
    all_paths.append(write_ban_do_hinh())
    all_paths.extend(write_dict_files(HE_THONG_FILES))
    all_paths.extend(write_dict_files(NGHIEP_VU_FILES))
    api_paths, flat_endpoints = write_api_modules()
    all_paths.extend(api_paths)
    all_paths.extend(write_lib_modules())
    all_paths.extend(write_pages())
    all_paths.extend(write_schemas())
    all_paths.extend(write_chuyen_de_hubs(all_paths))
    chi_muc = write_chi_muc(all_paths, flat_endpoints)
    all_paths.extend(chi_muc)
    write_index(all_paths, flat_endpoints)
    paths_for_html = [*all_paths, map_index_path()]
    write_map_portal_index_html(
        endpoint_count=len(flat_endpoints),
        page_count=sum(1 for p in all_paths if p.startswith("trang/")),
        api_count=sum(1 for p in all_paths if p.startswith("module-api/")),
        schema_count=sum(1 for p in all_paths if p.startswith("co-so-du-lieu/")),
    )
    write_doc_assets()
    write_site_nav_json(all_paths)
    html_pages = write_md_index_pages(paths_for_html)
    print(
        f"HTML doc pages: {html_pages}; ",
        end="",
    )
    print(
        f"Built {len(all_paths)} topic files + index; "
        f"endpoints: {len(flat_endpoints)}; "
        f"tham-chieu: {sum(1 for _ in (ROOT / 'tham-chieu').rglob('README.md')) if (ROOT / 'tham-chieu').is_dir() else 0}"
    )


if __name__ == "__main__":
    main()
