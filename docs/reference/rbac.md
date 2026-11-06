<!-- Mirror: Shop-Manager-System-Offline/docs/rbac.md -->

# RBAC (roles & permissions)

**Mô tả:** Bản mirror doc Shop docs/rbac.md — RBAC (roles & permissions).

## Roles (database)

Defined in `lib/db/src/schema/users.ts` enum `user_role`:

- `super_admin`
- `admin`
- `manager`
- `staff`
- `accountant`
- `warehouse_keeper`

## Authentication model

- Login: `POST /api/auth/login`
- The server returns a JWT (`token`) containing: `userId`, `shopId`, `role`, `email`, `organizationId`
- Frontend stores token in `localStorage` under key `pos_token`
- Requests attach `Authorization: Bearer <token>`

JWT signing key:

- `SESSION_SECRET` (required in production; local dev uses a fallback in code, but you should still set it explicitly for predictable behavior)

## Authorization helpers (backend)

Implemented in `artifacts/api-server/src/middlewares/auth.ts`:

- `requireAuth`: requires bearer token and verifies JWT
- `requireAdmin`: allows `admin` and `super_admin` (via `isShopAdminRole`)
- `requireManagerOrAdmin`: allows `manager`, `admin`, `super_admin`
- `requireRole(...roles)`: generic role whitelist

### Stock requests (phiếu nhập/xuất)

- Mỗi phiếu có **`fromShopId` → `toShopId`**
- **Nhập:** chỉ `kho tổng → chi nhánh` (CN con xin nhập; kho tổng có thể tạo hộ CN đích)
- **Xuất:** `CN/kho tổng → CN/kho tổng` khác trong cùng tổ chức
- **Vận chuyển:** trừ tồn tại `fromShopId`
- **Hoàn thành:** nhập — kho tổng + admin/thủ kho CN đích; xuất — chỉ CN đích (`toShopId`)
- **Huỷ** `in_transit` / `completed`: chỉ admin tổng hoặc admin chi nhánh chính
- **Xem danh sách:** kho tổng xem cả org; CN con chỉ phiếu có mình ở Từ hoặc Đến

JWT `/auth/me` exposes `canApproveStock`, `canCompleteStock`, `canViewChainDashboard`, `canViewChainStatistics`, `canViewOrgInventory`, `hubShopId` (re-login after permission changes).

### Hóa đơn VAT tại POS (bước 2 — lưu yêu cầu)

- Checkbox **Xuất hóa đơn GTGT (công ty)** trên POS **mọi chi nhánh**; khi tick: tên công ty, MST, email, địa chỉ, **SĐT** (bắt buộc).
- Giá bán **đã gồm VAT** — tổng tiền **không đổi** khi tick/không tick.
- Dữ liệu lưu trên `orders`; đơn có badge **HĐ VAT** tại trang Đơn hàng (chờ xuất HĐĐT — bước 3 sau).
- **Kho tổng** (`canViewOrgInventory` / nhân sự CN chính): `GET /api/orders?shopId=&invoiceRequested=true|false` — xem đơn **cả chuỗi**, lọc có/không yêu cầu HĐ. CN con chỉ xem đơn tại shop mình.

### Tồn kho (inventory)

- **CN con:** chỉ xem/sửa tồn tại `shopId` đăng nhập (`GET /api/inventory`).
- **Kho tổng** (admin / manager / thủ kho tại CN chính): `GET /api/inventory?shopId=` — xem tồn mọi CN trong tổ chức; **sửa** (`PATCH`) chỉ tại CN đăng nhập, UI chỉ bật sửa khi đang xem CN của mình.
- **Giá trị tồn (giá bán):** **admin** và **manager**; **thủ kho** chỉ thấy số lượng (API trả `price` = null).
- **Giá trị tồn (giá vốn):** chỉ **kho tổng** / quản trị danh mục (`canManageCatalog`); CN con không xem (`costPrice` = null).

### Chain dashboard

- **Platform master admin** (`super_admin` / `admin` without `organizationId`): all shops
- **Cửa hàng tổng** `admin` or `manager` with `userCanManageCatalog` and `shopId === hubShopId` (`userCanViewChainDashboard`); **quản lý chi nhánh** không xem Dashboard chuỗi / Shop status

### Chain statistics (`/statistics`)

- **Hub** (`userCanViewChainDashboard`) and **accountant at hub**: full org scope (`resolveStatisticsShopScope` → `resolveChainShopScope`)
- **Manager / admin at a branch**: `userCanViewChainStatistics` + API locked to `auth.shopId` only (no “all branches”)
- Giá vốn / lợi nhuận on statistics still follow `canSeeDashboardSalesProfit` (hub toggle for accountant)
- Cột **lượt bán** on catalog & statistics follows `canSeeCatalogSalesCount` (hub toggles; chỉ quản lý/kế toán **đăng nhập tại cửa hàng tổng**; quản lý chi nhánh không xem; staff never; admin/warehouse always)
- **Giá vốn** trên API danh mục/sync: `userCanSeeProductCostPrice` — quản lý chỉ tại hub; chi nhánh không nhận `costPrice` (lợi nhuận dashboard vẫn `canSeeDashboardSalesProfit`, chỉ hub)

## UI gating (frontend)

UI menus and actions are shown/hidden based on `me.role` returned by `/api/auth/me`.

Important: UI gating is not a security boundary by itself. API endpoints must also enforce RBAC.

