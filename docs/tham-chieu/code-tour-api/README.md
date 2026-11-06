<!-- Mirror: Shop-Manager-System-Offline/docs/code-tour/api-server.md -->

# Code tour — API server (`artifacts/api-server`)

**Mô tả:** Tài liệu tham chiếu gốc Shop docs/code-tour/api-server.md — Code tour — API server (artifacts/api-server) (nội dung dưới thường tiếng Anh).

> **Ghi chú:** Phần dưới giữ nguyên tiếng Anh từ repo Shop (tham chiếu kỹ thuật). Luồng tiếng Việt ưu tiên đọc `nghiep-vu/` và `he-thong/`.

## What this package does

Implements the REST API under `/api/*` used by the POS web app.

## Entry points

- `src/index.ts`
  - Starts the server and binds to `PORT`.
- `src/app.ts`
  - Configures middleware and mounts routes at `/api`.

## Authentication & RBAC

File: `src/middlewares/auth.ts`

Key responsibilities:

- `requireAuth()`: validates `Authorization: Bearer <jwt>` and sets `req.auth`.
- `signToken()`: creates JWT for login response.
- `requireAdmin()`, `requireManagerOrAdmin()`, `requireRole()`: role gating.
- `isShopAdminRole()`: “admin-equivalent” roles (currently `admin` + `super_admin`).

Operational notes:

- Most data access is scoped by `req.auth.shopId` (shop context comes from token).
- JWT signing key is `SESSION_SECRET` (must be set in production).

## Route modules (business meaning)

### Auth — `src/routes/auth.ts`

- `POST /api/auth/login`: email/password login (bcrypt compare), returns JWT.
- `GET /api/auth/me`: returns current user identity for UI gating.

### Orders (POS core) — `src/routes/orders.ts`

Highlights:

- `POST /api/orders` creates order + order items and decrements inventory in **one DB transaction**.
- Inventory checks are performed before decrement. The inventory row is locked with `FOR UPDATE` to prevent race conditions.
- Cancel workflow:
  - Non-admin roles can request cancellation (note required).
  - Admin-equivalent roles can cancel directly and restore inventory.
  - Admin-equivalent roles can approve/reject cancel requests.

### Products — `src/routes/products.ts`

- Catalog CRUD + shop-level quantity updates.
- API may hide `costPrice` for some roles (controls margin visibility).

### Inventory (shop-level) — `src/routes/inventory.ts`

- List and adjust shop inventory.

### Stock requests (import/export) — `src/routes/stock-requests.ts`

Defines the internal import/export request process:

- Create request with items
- Approve/reject (org-aware permissions)
- Complete request (updates inventory)

Business-critical helper:

- `canApproveRequest()` encodes who may approve across shops within the same organization.

### Chain / multi-branch — `src/routes/chain.ts`

Implements “chain-level” operations:

- Organizations
- Shops + create/reset admin
- Warehouses
- Warehouse adjustments (movement log)
- Transfers lifecycle: draft → approve → ship → receive

Pay attention to:

- Warehouse inventory lookups and fallbacks
- Movement logging when adjusting stock

### Staff — `src/routes/staff.ts`

- Shop staff CRUD (admin-equivalent only).

### Dashboard / Statistics / Reports — `src/routes/dashboard.ts`, `statistics.ts`, `reports.ts`

Operational reporting for managers/admins (sales, staff performance, reprints, etc.).

## Where to look first when debugging

- Login failing: `src/routes/auth.ts` and DB connectivity (`lib/db`).
- POS cannot submit orders: `src/routes/orders.ts` (inventory checks/transaction).
- “I can’t see buttons” in UI: usually frontend role gating, but confirm API RBAC too.

