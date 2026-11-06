<!-- Mirror: Shop-Manager-System-Offline/docs/code-annotations.md -->

# Code annotations (high-signal)

**Mô tả:** Tài liệu tham chiếu gốc Shop docs/code-annotations.md — Code annotations (high-signal) (nội dung dưới thường tiếng Anh).

> **Ghi chú:** Phần dưới giữ nguyên tiếng Anh từ repo Shop (tham chiếu kỹ thuật). Luồng tiếng Việt ưu tiên đọc `nghiep-vu/` và `he-thong/`.

This is a “guided reading” document for the repo. It avoids line-by-line commentary and instead documents:

- what each key file is responsible for
- which functions are business-critical
- what to be careful about when changing them (business meaning / invariants)

For full per-package tours, see `docs/code-tour/*`.

## Top-level

- `pnpm-workspace.yaml`
  - Defines packages and workspace-wide dependency catalog.
  - Contains supply-chain hardening (`minimumReleaseAge`) and platform overrides.
- `docker-compose.yml`
  - Local Postgres for development (`shop-manager-postgres`) on host port `5433`.

## Backend (API): `artifacts/api-server`

**Purpose**: Provide the `/api/*` REST endpoints that the POS web app calls.

Key files:

- `src/index.ts`
  - Starts the HTTP server, reading `PORT`.
  - **Business impact**: wrong port/env means the POS cannot operate.
- `src/app.ts`
  - Express middleware + mounts router under `/api`.
  - **Important**: `FRONTEND_URLS` CORS whitelist; if unset, browser cross-origin requests are denied. No separate Origin middleware.
- `src/middlewares/auth.ts`
  - JWT verification and RBAC helpers.
  - **Business invariants**:
    - A request’s *shop context* comes from the token (`shopId`).
    - If RBAC helpers change, many admin/manager workflows change.
    - `SESSION_SECRET` is required in production; dev has fallback.
- `src/routes/index.ts`
  - Module router composition (auth, products, orders, stock-requests, chain, etc.).

Business-critical route modules:

- `src/routes/auth.ts`
  - Login and “who am I”.
  - **Critical**: the `users` query must be reliable; if DB is down, login fails.
- `src/routes/orders.ts`
  - Creates orders and updates inventory (POS core).
  - **Critical invariants**:
    - Inventory is checked and locked (`FOR UPDATE`) before decrement.
    - Order creation and inventory updates happen in a DB transaction.
    - Cancellation workflow: non-admin can request cancel (requires note), admin-equivalent can finalize cancel and restore inventory.
- `src/routes/products.ts`
  - Product catalog CRUD + shop-level quantity updates.
  - **Important**: API can hide `costPrice` for some roles.
- `src/routes/stock-requests.ts`
  - Import/export request workflow with org-aware approval logic.
  - **Important**: `canApproveRequest()` embodies the business rule for “who can approve across branches”.
- `src/routes/chain.ts`
  - Multi-branch admin operations: organizations, shops, warehouses, transfers, warehouse adjustments, movement logs.
  - **Critical invariants**:
    - Transfer lifecycle (draft → approve → ship → receive).
    - Warehouse inventory lookup prefers `(warehouseId)` but can fall back to `(shopId, warehouseId NULL)` for shop-linked warehouses.
- `src/routes/staff.ts`
  - Staff CRUD within a shop; protected by `requireAdmin` (admin + super_admin).
- `src/routes/reports.ts`, `src/routes/statistics.ts`, `src/routes/dashboard.ts`
  - Reporting and analytics endpoints. These shape operational visibility.

## Frontend (POS App): `artifacts/pos-app`

**Purpose**: The retail/POS web UI used by staff/admin roles.

Key files:

- `src/App.tsx`
  - Route map and global providers (React Query, Toaster).
- `src/components/layout/app-layout.tsx`
  - Sidebar navigation and role-based visibility.
  - **Business impact**: determines which modules each role can see.
- `src/pages/login.tsx`
  - Login flow; stores token in `localStorage` key `pos_token`.
- `src/pages/pos.tsx`
  - POS selling UI. (Core workflow: build cart → submit order.)
- `src/pages/products.tsx`
  - Product management UI (add/import/edit/discontinue/reactivate).
  - **Business impact**: who can add vs edit products is decided here.
- `src/pages/inventory.tsx`
  - Inventory listing and adjustment UI.
- `src/pages/stock-requests.tsx`
  - Import/export requests UI.
- `src/pages/chain.tsx`
  - Chain-level operations UI (org/shop/warehouse/transfers).
- `src/pages/orders.tsx`
  - Order review + cancel/approve flows.
- `src/pages/staff.tsx`
  - Staff CRUD UI (admin-only module).
- `src/pages/reports.tsx`, `src/pages/statistics.tsx`, `src/pages/dashboard.tsx`
  - Operational reporting and analytics pages.

Toast system:

- `src/hooks/use-toast.ts`
  - Controls toast timing (auto-dismiss duration, remove delay).
- `src/components/ui/toast.tsx`
  - Renders toast UI and the close “x”.

## Database library: `lib/db`

**Purpose**: Single source of truth for DB schema, used by API routes.

Key files:

- `src/index.ts`
  - Creates Postgres pool and Drizzle DB.
  - **Critical**: `DATABASE_URL` must be set.
- `src/schema/*.ts`
  - Tables and enums.
  - **Business-critical tables**:
    - `users`, `shops`, `organizations`
    - `products`, `inventory`
    - `orders`, `order_items`
    - `stock_requests`, `stock_request_items`
    - `stock_transfers`, `stock_transfer_items`
    - `warehouses`, `inventory_movements`
    - `reprint_logs`

