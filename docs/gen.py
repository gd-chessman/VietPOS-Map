#!/usr/bin/env python3
"""Build VietPOS-Map: long TOC + detailed per-topic files from Shop codebase."""
from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SHOP = ROOT.parent.parent / "Shop-Manager-System-Offline"
ROUTES_DIR = SHOP / "artifacts/api-server/src/routes"
PAGES_DIR = SHOP / "artifacts/pos-app/src/pages"
SCHEMA_DIR = SHOP / "lib/db/src/schema"
LIB_ROOT = SHOP / "artifacts/api-server/src/lib"
APP_TSX = SHOP / "artifacts/pos-app/src/App.tsx"
APP_LAYOUT = SHOP / "artifacts/pos-app/src/components/layout/app-layout.tsx"
COMPONENTS_DIR = SHOP / "artifacts/pos-app/src/components"

# Route → file nghiệp vụ (gợi ý đọc thêm)
ROUTE_NGHIEP_VU: dict[str, str] = {
    "/login": "nghiep-vu/01-dang-nhap-va-shop-context.md",
    "/dashboard": "nghiep-vu/01-dang-nhap-va-shop-context.md",
    "/pos": "nghiep-vu/02-pos-ban-hang.md",
    "/orders": "nghiep-vu/02-pos-ban-hang.md",
    "/products": "nghiep-vu/03-san-pham-va-ton.md",
    "/inventory": "nghiep-vu/03-san-pham-va-ton.md",
    "/stock-requests": "nghiep-vu/04-phieu-nhap-xuat-chuyen-kho.md",
    "/purchase-orders": "nghiep-vu/04-phieu-nhap-xuat-chuyen-kho.md",
    "/vat-invoices": "nghiep-vu/05-hoa-don-vat-xuat.md",
    "/vat-inbound": "nghiep-vu/06-hoa-don-dau-vao-tong-quan.md",
    "/access-block": "nghiep-vu/10-truy-cap-an-ninh.md",
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
    "he-thong/01-kien-truc-runtime.md": "Sơ đồ runtime: client React → Express API → PostgreSQL; tùy chọn cloud-sync Railway.",
    "he-thong/02-workspace-luu-niem.md": "Các repo trong LuuNiem (Shop, Deploy, Widget, Map, ESP32) và vai trò từng thư mục.",
    "he-thong/03-monorepo-packages.md": "Cấu trúc pnpm workspace: artifacts, lib, scripts trong Shop-Manager.",
    "he-thong/04-docker-va-cloud-sync.md": "Docker Compose local, biến CLOUD_DATABASE_URL, worker cloud-sync và Trợ lý AI.",
}

NGHIEP_VU_DESC: dict[str, str] = {
    "nghiep-vu/01-dang-nhap-va-shop-context.md": "Đăng nhập, JWT gắn shop/role, hub shop và ngữ cảnh vận hành API.",
    "nghiep-vu/02-pos-ban-hang.md": "Luồng POS: ca làm việc, giỏ hàng, thanh toán, in bill, hủy đơn và audit.",
    "nghiep-vu/03-san-pham-va-ton.md": "CRUD sản phẩm, import Excel, tồn shop và điều chỉnh inventory.",
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

**Frontend:** `pages/vat-inbound.tsx`, `lib/vat-inbound-api.ts`, IndexedDB `@workspace/local-db`.

**Quyền:** hub shop + `requireVatInboundAccess` (admin, manager, accountant, warehouse_keeper tại CN chính).
""",
    "orders": """
Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (`shift-sessions`), audit cart.

**Frontend:** `pages/pos.tsx`, `pages/orders.tsx`, `lib/offline/checkout.ts` (offline).
""",
    "chain": """
Tổ chức, shop, kho, điều chuyển (`transfers`). Cấu hình org (Viettel, CQT, feedback URL, agent LLM).

**Frontend:** `pages/chain.tsx`, `chain-dashboard.tsx`.
""",
    "stock-requests": """
Phiếu yêu cầu nhập/xuất nội bộ: tạo → duyệt → hoàn tất → cập nhật tồn.

**Frontend:** `pages/stock-requests.tsx`.
""",
    "products": """
CRUD sản phẩm, import Excel, variant, ẩn/hiện SP, giá/giá vốn theo role.

**Frontend:** `pages/products.tsx`.
""",
    "agent": """
Trợ lý AI: chat, system info (DB, cloud sync, shops online), cấp quyền `agent_assistant_enabled`.

**Frontend:** `pages/agent-assistant.tsx`, `agent-chat-audit.tsx`.
""",
    "widget": """
API phục vụ app Android widget: thống kê quầy (JWT / shop context).

**Repo:** `VietPOS-Widget/`.
""",
    "shop-api-keys": """
API key cho widget / thiết bị (ESP32 visitor-counts).

**Frontend:** `pages/chain-api-keys.tsx` (nếu có).
""",
    "org-gdt-portal": """
Session CQT trực tiếp (captcha, connect) — dùng chung org với HĐ đầu vào.
""",
    "sync": """
Endpoint đồng bộ client (pull/push) cho offline IndexedDB.
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

ACCESS_ENDPOINT_NOTES: dict[str, str] = {
    "GET /blocked-ips": "Liệt kê `blocked_ips` + nhãn người tạo; kèm cờ env denylist và IP client hiện tại.",
    "POST /blocked-ips": "Thêm IP (normalize IPv4/IPv6); body `{ ip, note? }`; refresh denylist cache.",
    "DELETE /blocked-ips/:id": "Xóa một dòng; refresh denylist cache.",
    "GET /blocked-devices": "Liệt kê thiết bị bị chặn (tương tự IP).",
    "POST /blocked-devices": "Thêm device id; validate qua `isValidBlockedDeviceId`.",
    "DELETE /blocked-devices/:id": "Bỏ chặn thiết bị.",
    "GET /access-observations": "Query `?limit=` (mặc định 200); trả `items`, thống kê `today`, `ttlHours`, `storage: memory`.",
}

PAGE_DOCS: dict[str, str] = {
    "pos.tsx": """
**Route:** `/pos`

Màn hình bán hàng chính: tìm SP, giỏ hàng, thanh toán, yêu cầu HĐ VAT, mở/đóng ca.
Offline: ghi Dexie qua `checkoutOffline()`; sync sau khi có mạng.

**File lớn** — tìm theo: cart state, barcode, payment method, print bill, de nghị hủy đơn.
**Quyền:** `userCanUsePos`, NV bán hàng / thu ngân.
""",
    "vat-inbound.tsx": """
**Route:** `/vat-inbound`

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
**Route:** `/stock-requests`

Phiếu nhập/xuất: trạng thái chờ duyệt, vận chuyển, nhận hàng, huỷ.
""",
    "chain.tsx": """
**Route:** `/chain`

Sửa tổ chức: thông tin, shop, Viettel inbound/outbound, CQT, Trợ lý AI, URL feedback công khai.
""",
    "products.tsx": """
**Route:** `/products`

Danh mục SP: grid/table, import Excel, variant, giá, ảnh.
""",
    "inventory.tsx": """
**Route:** `/inventory`

Tồn kho shop: số lượng, tạo phiếu nhập từ SP sắp hết (thủ kho).
""",
    "vat-invoices.tsx": """
**Route:** `/vat-invoices`

HĐ VAT **xuất** (Viettel SInvoice): phát hành, tra cứu, điều chỉnh theo tích hợp Viettel.
""",
    "agent-assistant.tsx": """
**Route:** `/agent-assistant`

Trợ lý AI + panel hệ thống (DB, cloud sync URL, shops online). Chat khi đã cấu hình LLM org.
""",
    "dashboard.tsx": """
**Route:** `/dashboard`

Tổng quan doanh thu, đơn, tồn thấp — theo quyền và scope shop.
""",
    "login.tsx": """
**Route:** `/login`

Email/password, PIN máy, tài khoản đã lưu trên thiết bị. JWT → `pos_token`.
""",
    "my-permissions.tsx": """
**Route:** `/my-permissions`

Giải thích quyền role hiện tại (đối chiếu menu thực tế).
""",
    "access-block.tsx": """
**Route:** `/access-block` (query `?tab=overview|ip|device`)

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

## Đọc tiếp

- Nghiệp vụ: `nghiep-vu/10-truy-cap-an-ninh.md`
- API: `api-modules/blocked-ips.md`, `blocked-devices.md`, `access-observations.md`
- Lib: `lib-modules/ip-denylist.md`, `device-denylist.md`, `api-access-observations.md`
- Schema: `schema/blockedIps.md`, `schema/blockedDevices.md`
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
**Route:** `/orders`

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

**Tool dev:** `gdt-cqt-tester/` (ngoài monorepo).
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

**Route:** `/access-block` — menu **Chặn truy cập** (chỉ `super_admin`).

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

```
Client (Browser / Tauri)
  → pos-app (React, Vite)
  → /api/* → api-server (Express 5)
  → @workspace/db (Drizzle) → PostgreSQL 16
  → (optional) cloud-sync → Railway Postgres
```

**Build prod:** web static trong container nginx; API node dist/index.mjs.

**Auth:** JWT middleware; cookie/session tùy endpoint public.

Xem thêm: `reference/architecture.md`.
""",
    "he-thong/02-workspace-luu-niem.md": """
# Workspace LuuNiem

| Thư mục | Vai trò |
|---------|---------|
| Shop-Manager-System-Offline | Source phát triển |
| Deploy-VietPOS | Mirror deploy (`sync.sh`) |
| HDSD-VietPOS | Hướng dẫn HTML Vercel |
| VietPOS-Widget | Android |
| VietPOS-Map | Tài liệu bản đồ (repo này) |
| ESP32-DemKhach | Firmware đếm khách |
| gdt-cqt-tester | Test CQT |

**sync.sh:** nhánh QuyLV → Deploy; working tree sạch.
""",
    "he-thong/03-monorepo-packages.md": """
# Monorepo packages

**artifacts:** api-server, pos-app, pos-desktop, mockup-sandbox.

**lib:** db, local-db, sync, api-zod, api-spec, api-client-react.

**scripts:** seed, docker helpers.

File: `Shop-Manager-System-Offline/pnpm-workspace.yaml`.
""",
    "he-thong/04-docker-va-cloud-sync.md": """
# Docker và cloud sync

Compose: postgres (5434), init, api (3002), web (8080), cloud-sync.

**cloud-sync:** `scripts/cloud-sync.sh`, khóa `_sync_lock`, CLOUD_DATABASE_URL public Railway.

POS hiển thị trạng thái: Trợ lý AI ← env trên container **api**.

Mirror: `reference/docker-may-chu.md`, `reference/running-local.md`.
""",
}


def clean_generated() -> None:
    for p in list(ROOT.iterdir()):
        if p.name in ("gen.py", "reference"):
            continue
        if p.is_dir():
            shutil.rmtree(p)
        elif p.suffix == ".md":
            p.unlink()


def mirror_shop() -> None:
    REF = ROOT / "reference"
    REF.mkdir(parents=True, exist_ok=True)
    for rel in MIRROR_FROM_SHOP:
        src = SHOP / rel
        if not src.is_file():
            continue
        dst = REF / Path(rel).name
        body = src.read_text(encoding="utf-8")
        hdr = f"<!-- Mirror: Shop-Manager-System-Offline/{rel} -->\n\n"
        rel_doc = f"reference/{Path(rel).name}"
        title_m = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
        title = title_m.group(1).strip() if title_m else Path(rel).stem
        register_desc(
            rel_doc,
            f"Bản mirror doc Shop `{rel}` — {one_line(title, 120)}.",
        )
        mo_ta = f"**Mô tả:** {DOC_DESCRIPTIONS[rel_doc]}\n\n"
        if body.lstrip().startswith("#"):
            first_nl = body.find("\n")
            if first_nl != -1:
                body = body[: first_nl + 1] + "\n" + mo_ta + body[first_nl + 1 :].lstrip()
            else:
                body = body + "\n\n" + mo_ta
        else:
            body = mo_ta + body
        dst.write_text(hdr + body, encoding="utf-8")


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
    if mod == "vat-inbound" and key in VAT_INBOUND_ENDPOINT_NOTES:
        return one_line(VAT_INBOUND_ENDPOINT_NOTES[key], 140)
    intro = API_MODULE_INTRO.get(mod, "")
    if intro:
        return one_line(intro, 100)
    return f"REST `{method}` trên module `{mod}`."


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


def collect_page_api_hits(page_file: Path, text: str, depth: int = 0) -> tuple[list[str], list[tuple[str, Path]]]:
    """API trong page + 1 lớp component @/components (shell pages)."""
    hits = set(api_paths_in_source(text))
    embedded = embedded_shop_components(text)
    if depth < 1 and len(hits) < 3 and embedded:
        for _mod, path in embedded:
            child = path.read_text(encoding="utf-8", errors="replace")
            hits.update(api_paths_in_source(child))
    return sorted(hits), embedded


def default_page_doc(
    name: str,
    route: str,
    one_line: str,
    api_hits: list[str],
    embedded: list[tuple[str, Path]],
) -> str:
    slug = name.replace(".tsx", "")
    menu = menu_by_href().get(route, {})
    lines = [
        f"**Route:** `{route}`",
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
        lines.append("## API modules (map sang docs)")
        lines.append("")
        for m in modules:
            lines.append(f"- [`api-modules/{m}.md`](../api-modules/{m}.md) — prefix `/api/{m}`")
        lines.append("")
    return "\n".join(lines)


def append_page_analysis(lines: list[str], name: str, text: str) -> None:
    """Bổ sung mục phân tích tự động từ source TSX."""
    sub_exports = re.findall(r"export function (\w+)", text)
    if sub_exports:
        lines.append("## Section / component export trong file")
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
    key = f"{method} {path}"
    if module_key == "vat-inbound" and key in VAT_INBOUND_ENDPOINT_NOTES:
        note = VAT_INBOUND_ENDPOINT_NOTES[key]
        if middleware:
            note += f" Middleware: `{', '.join(middleware)}`."
        return note
    if key in ACCESS_ENDPOINT_NOTES:
        note = ACCESS_ENDPOINT_NOTES[key]
        if middleware:
            note += f" Middleware: `{', '.join(middleware)}`."
        return note
    api = path if path.startswith("/") else f"/{path}"
    mw = ", ".join(middleware) if middleware else "requireAuth (mặc định — kiểm tra file)"
    return f"`/api{api}`. Middleware: `{mw}`."


def write_api_modules() -> tuple[list[str], list[tuple[str, str, str, str]]]:
    out_dir = ROOT / "api-modules"
    out_dir.mkdir(parents=True, exist_ok=True)
    paths: list[str] = []
    flat_endpoints: list[tuple[str, str, str, str]] = []
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
        rel_shop = f"artifacts/api-server/src/routes/{f.name}"
        intro = API_MODULE_INTRO.get(key, f"REST handlers cho domain **{key}**.")
        rel = f"api-modules/{key}.md"
        desc = register_desc(
            rel,
            f"File routes `{key}.ts` — {len(routes)} endpoint HTTP cho `/api/...`. {one_line(intro, 120)}",
        )
        lines = [
            f"# API module: `{key}`",
            "",
            f"**Mô tả:** {desc}",
            "",
            f"**Source Shop:** `{rel_shop}`",
            "",
            intro.strip(),
            "",
            f"**Số endpoint trong file:** {len(routes)}",
            "",
            "## Danh sách endpoint (tóm tắt)",
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
            flat_endpoints.append((key, method, api_path, f"api-modules/{key}.md"))
        lines.extend(
            [
                "",
                "## Chi tiết từng endpoint",
                "",
            ]
        )
        for method, path, mid in blocks:
            api_path = path if path.startswith("/") else f"/{path}"
            mw = middleware_from_block(mid)
            anchor = endpoint_anchor(method, path)
            note = endpoint_note(key, method, path, mw)
            lines.append(f"### `{method} {api_path}` {{#{anchor}}}")
            lines.append("")
            lines.append(note)
            lines.append("")
            if mw:
                lines.append(f"- **Middleware:** {', '.join(f'`{x}`' for x in mw)}")
                lines.append("")
        lines.extend(
            [
                "## Ghi chú đọc code",
                "",
                f"- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./{f.name}`.",
                "- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).",
                "- Quyền role: xem `reference/rbac.md` và middleware trong từng block.",
                "",
            ]
        )
        if key == "vat-inbound":
            lines.extend(
                [
                    "## Luồng nghiệp vụ liên quan",
                    "",
                    "- `nghiep-vu/06-hoa-don-dau-vao-tong-quan.md`",
                    "- `nghiep-vu/07-hd-dau-vao-mst-loc.md`",
                    "- `nghiep-vu/08-hd-dau-vao-cqt-sync.md`",
                    "- UI: `frontend-pages/vat-inbound.md`",
                    "- Lib: `lib-modules/vat-inbound-tax-sync.md`, `lib-modules/gdt-portal/`…",
                    "",
                ]
            )
        if key in ("blocked-ips", "blocked-devices", "access-observations"):
            lines.extend(
                [
                    "## Luồng nghiệp vụ liên quan",
                    "",
                    "- `nghiep-vu/10-truy-cap-an-ninh.md`",
                    "- UI: `frontend-pages/access-block.md`",
                    "- Middleware: `lib-modules/ip-denylist.md`, `lib-modules/device-denylist.md`, "
                    "`lib-modules/api-access-observations.md`",
                    "",
                ]
            )
        (ROOT / rel).write_text("\n".join(lines), encoding="utf-8")
        paths.append(rel)
    return paths, flat_endpoints


def write_pages() -> list[str]:
    out_dir = ROOT / "frontend-pages"
    out_dir.mkdir(parents=True, exist_ok=True)
    paths: list[str] = []
    page_routes = parse_page_routes()
    for f in sorted(PAGES_DIR.glob("*.tsx")):
        name = f.name
        text = f.read_text(encoding="utf-8", errors="replace")
        line_count = text.count("\n") + 1
        route = page_routes.get(name, "*(public hoặc redirect — xem App.tsx)*")
        one = PAGE_ONE_LINE.get(name, "")
        api_hits, embedded = collect_page_api_hits(f, text)
        doc = PAGE_DOCS.get(
            name,
            default_page_doc(name, route, one, api_hits, embedded),
        )
        lib_api = sorted(set(re.findall(r"from ['\"]@/lib/([\w/-]+)['\"]", text)))[:20]
        perm_hits = sorted(set(re.findall(r"(userCan\w+|canAccess\w+|require\w+)", text)))[:15]
        comp_match = re.search(r"export default function (\w+)", text)
        comp_name = comp_match.group(1) if comp_match else "*(default export)*"
        imports = [ln.strip() for ln in text.splitlines()[:55] if ln.strip().startswith("import ")]
        rel = f"frontend-pages/{name.replace('.tsx', '')}.md"
        desc = register_desc(
            rel,
            f"{one} (URL `{route}`, `{comp_name}`, ~{line_count} dòng)."
            if one
            else f"Trang React `{route}` — `{comp_name}`, ~{line_count} dòng.",
        )
        lines = [
            f"# Frontend: `{name}`",
            "",
            f"**Mô tả:** {desc}",
            "",
            f"**Source Shop:** `artifacts/pos-app/src/pages/{name}`",
            "",
            f"**URL (wouter):** `{route}`",
            f"**Component:** `{comp_name}`",
            f"**Độ lớn:** ~{line_count} dòng.",
            "",
            doc.strip(),
            "",
        ]
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
                if mod and (ROOT / "api-modules" / f"{mod}.md").is_file():
                    lines.append(f"- `{h}` → [`api-modules/{mod}.md`](../api-modules/{mod}.md)")
                else:
                    lines.append(f"- `{h}`")
            lines.append("")
        nv = ROUTE_NGHIEP_VU.get(route)
        if nv:
            lines.extend(
                [
                    "## Luồng nghiệp vụ (doc)",
                    "",
                    f"- `{nv}`",
                    "",
                ]
            )
        lines.extend(
            [
                "## File liên quan",
                "",
                "- Route khai báo: `artifacts/pos-app/src/App.tsx`",
                "- Layout/menu: `components/layout/app-layout.tsx`",
                "- Session: `lib/session-cache.ts`, `lib/use-session-user.ts`",
                "",
            ]
        )
        (ROOT / rel).write_text("\n".join(lines), encoding="utf-8")
        paths.append(rel)
    return paths


def write_schemas() -> list[str]:
    out_dir = ROOT / "schema"
    out_dir.mkdir(parents=True, exist_ok=True)
    paths: list[str] = []
    for f in sorted(SCHEMA_DIR.glob("*.ts")):
        if f.name in ("index.ts",):
            continue
        text = f.read_text(encoding="utf-8", errors="replace")
        tables = PG_TABLE_RE.findall(text)
        cols: list[str] = []
        for m in COL_RE.finditer(text):
            cols.append(f"- `{m.group(2)}` ({m.group(1)})")
        if not tables and not cols:
            continue
        rel = f"schema/{f.stem}.md"
        tbl = ", ".join(f"`{t}`" for t in tables[:3])
        if len(tables) > 3:
            tbl += f" (+{len(tables) - 3} bảng)"
        desc = register_desc(
            rel,
            f"Drizzle schema `{f.stem}.ts` — {len(cols)} cột trên {len(tables) or 0} bảng Postgres ({tbl or 'n/a'}).",
        )
        lines = [
            f"# Schema: `{f.stem}`",
            "",
            f"**Mô tả:** {desc}",
            "",
            f"**Source Shop:** `lib/db/src/schema/{f.name}`",
            "",
        ]
        if tables:
            lines.append("## Bảng Postgres")
            lines.append("")
            for t in tables:
                lines.append(f"- `{t}`")
            lines.append("")
        fks = sorted(set(FK_RE.findall(text)))
        if cols:
            lines.append("## Cột (trích từ schema TS)")
            lines.append("")
            lines.extend(cols)
            lines.append("")
        if fks:
            lines.append("## Tham chiếu (references → bảng Drizzle)")
            lines.append("")
            for fk in fks:
                lines.append(f"- `{fk}`")
            lines.append("")
        lines.append("Tổng quan quan hệ: `reference/database.md`.")
        lines.append("")
        (ROOT / rel).write_text("\n".join(lines), encoding="utf-8")
        paths.append(rel)
    return paths


def write_lib_modules() -> list[str]:
    out_base = ROOT / "lib-modules"
    paths: list[str] = []
    if not LIB_ROOT.is_dir():
        return paths
    for f in sorted(LIB_ROOT.rglob("*.ts")):
        rel_from_lib = f.relative_to(LIB_ROOT)
        rel = f"lib-modules/{rel_from_lib.with_suffix('').as_posix()}.md"
        text = f.read_text(encoding="utf-8", errors="replace")
        line_count = text.count("\n") + 1
        exports = [a or b for a, b in EXPORT_RE.findall(text)]
        imports_db = [ln.strip() for ln in text.splitlines() if "@workspace/db" in ln][:8]
        rel_shop = f"artifacts/api-server/src/lib/{rel_from_lib.as_posix()}"
        ex_preview = ", ".join(exports[:5]) if exports else "(không export tên rõ)"
        if exports and len(exports) > 5:
            ex_preview += ", …"
        desc = register_desc(
            rel,
            f"Logic backend `{rel_from_lib.as_posix()}` (~{line_count} dòng) — export: {ex_preview}.",
        )
        lines = [
            f"# Lib: `{rel_from_lib.as_posix()}`",
            "",
            f"**Mô tả:** {desc}",
            "",
            f"**Source Shop:** `{rel_shop}`",
            "",
            f"**Độ lớn:** ~{line_count} dòng.",
            "",
            "Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.",
            "",
        ]
        if exports:
            lines.append(f"## Export ({len(exports)} symbol)")
            lines.append("")
            for ex in exports[:40]:
                lines.append(f"- `{ex}`")
            if len(exports) > 40:
                lines.append(f"- … {len(exports) - 40} export khác")
            lines.append("")
        if imports_db:
            lines.append("## Import DB / schema")
            lines.append("")
            for imp in imports_db:
                lines.append(f"- `{imp}`")
            lines.append("")
        preview = "\n".join(text.splitlines()[:35])
        lines.extend(
            [
                "## Xem trước đầu file",
                "",
                "```typescript",
                preview,
                "```",
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
        p = ROOT / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        b = body.strip()
        desc = (
            HE_THONG_DESC.get(rel)
            or NGHIEP_VU_DESC.get(rel)
            or summary_from_markdown_body(b)
            or Path(rel).stem.replace("-", " ")
        )
        register_desc(rel, desc)
        if b.startswith("#"):
            lines = prepend_mo_ta_block(b.splitlines(), DOC_DESCRIPTIONS[rel])
            p.write_text("\n".join(lines) + "\n", encoding="utf-8")
        else:
            title = Path(rel).stem.replace("-", " ").title()
            lines = [
                f"# {title}",
                "",
                f"**Mô tả:** {DOC_DESCRIPTIONS[rel]}",
                "",
                b,
            ]
            p.write_text("\n".join(lines) + "\n", encoding="utf-8")
        paths.append(rel)
    return paths


def write_index(
    all_paths: list[str],
    flat_endpoints: list[tuple[str, str, str, str]],
) -> None:
    groups: dict[str, list[str]] = {
        "Hệ thống & workspace": [],
        "Nghiệp vụ (luồng chi tiết)": [],
        "API modules (từng file routes/*.ts)": [],
        "Thư viện backend (lib-modules, từng file lib/*.ts)": [],
        "Frontend pages (từng pages/*.tsx)": [],
        "Database schema (từng file schema/*.ts)": [],
        "Reference mirror Shop": [],
    }
    for p in sorted(all_paths):
        if p.startswith("he-thong/"):
            groups["Hệ thống & workspace"].append(p)
        elif p.startswith("nghiep-vu/"):
            groups["Nghiệp vụ (luồng chi tiết)"].append(p)
        elif p.startswith("api-modules/"):
            groups["API modules (từng file routes/*.ts)"].append(p)
        elif p.startswith("lib-modules/"):
            groups["Thư viện backend (lib-modules, từng file lib/*.ts)"].append(p)
        elif p.startswith("frontend-pages/"):
            groups["Frontend pages (từng pages/*.tsx)"].append(p)
        elif p.startswith("schema/"):
            groups["Database schema (từng file schema/*.ts)"].append(p)
        elif p.startswith("reference/"):
            groups["Reference mirror Shop"].append(p)

    ref_files = sorted((ROOT / "reference").glob("*.md")) if (ROOT / "reference").is_dir() else []
    for f in ref_files:
        groups["Reference mirror Shop"].append(f"reference/{f.name}")

    lines = [
        "# VietPOS-Map — Mục lục đầy đủ",
        "",
        "Tài liệu **chi tiết theo file code** trong Shop-Manager-System-Offline, "
        "cộng **luồng nghiệp vụ** và **mirror** doc gốc Shop.",
        "",
        "**Regenerate:** `python3 docs/gen.py` (sau khi đổi routes/pages/schema ở Shop).",
        "",
        "Mỗi file doc có dòng **Mô tả:** ở đầu; mục lục bên dưới lặp lại mô tả sau tên file.",
        "",
        "---",
        "",
        "## Sơ đồ kiến trúc",
        "",
        "```",
        "pos-app (React) ──/api──► api-server (Express) ──► PostgreSQL",
        "     │                         ▲",
        "  local-db/sync               cloud-sync → Railway",
        " Widget / ESP32 ──API key──► visitor-counts, widget",
        "```",
        "",
        "---",
        "",
    ]
    n = 0
    for group, items in groups.items():
        if not items:
            continue
        lines.append(f"## {group} ({len(items)} mục)")
        lines.append("")
        for item in sorted(set(items)):
            n += 1
            label = Path(item).name
            desc = DOC_DESCRIPTIONS.get(item, "")
            if desc:
                lines.append(f"{n}. [{label}]({item}) — {desc}")
            else:
                lines.append(f"{n}. [{label}]({item})")
        lines.append("")

    lines.extend(
        [
            "---",
            "",
            f"## Chỉ mục API đầy đủ ({len(flat_endpoints)} endpoint)",
            "",
            "Mỗi dòng trỏ tới file module; chi tiết handler nằm ở mục **Chi tiết từng endpoint** trong file đó.",
            "",
        ]
    )
    for i, (mod, method, api_path, doc_path) in enumerate(
        sorted(flat_endpoints, key=lambda x: (x[2], x[1])), start=1
    ):
        blurb = endpoint_index_blurb(mod, method, api_path)
        lines.append(
            f"{i}. `{method}` `/api{api_path}` — {blurb} — [`{mod}`]({doc_path})"
        )

    lines.extend(
        [
            "",
            "---",
            "",
            "## Lộ trình đọc gợi ý",
            "",
            "1. `he-thong/01-kien-truc-runtime.md` → `he-thong/04-docker-va-cloud-sync.md`",
            "2. `nghiep-vu/01-dang-nhap-va-shop-context.md` → … → `12-widget-va-dem-khach.md`",
            "3. Sửa API: `api-modules/<ten>.md` + `lib-modules/...` nếu logic nằm lib",
            "4. Sửa UI: `frontend-pages/<ten>.md`",
            "5. DB: `schema/<ten>.md` + `reference/database.md`",
            "6. HĐ đầu vào: `nghiep-vu/06`–`08`, `api-modules/vat-inbound.md`, `frontend-pages/vat-inbound.md`",
            "",
            f"**Tổng số mục file trong mục lục:** {n}",
            f"**Tổng endpoint REST (trích routes):** {len(flat_endpoints)}",
            "",
        ]
    )
    (ROOT / "00-muc-luc-va-kien-truc.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    if not SHOP.is_dir():
        raise SystemExit(f"Missing Shop: {SHOP}")
    DOC_DESCRIPTIONS.clear()
    clean_generated()
    mirror_shop()
    all_paths: list[str] = []
    all_paths.extend(write_dict_files(HE_THONG_FILES))
    all_paths.extend(write_dict_files(NGHIEP_VU_FILES))
    api_paths, flat_endpoints = write_api_modules()
    all_paths.extend(api_paths)
    all_paths.extend(write_lib_modules())
    all_paths.extend(write_pages())
    all_paths.extend(write_schemas())
    write_index(all_paths, flat_endpoints)
    print(
        f"Built {len(all_paths)} topic files + index; "
        f"endpoints: {len(flat_endpoints)}; "
        f"reference: {len(list((ROOT/'reference').glob('*.md')))}"
    )


if __name__ == "__main__":
    main()
