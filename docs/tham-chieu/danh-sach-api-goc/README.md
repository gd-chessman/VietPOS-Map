<!-- Mirror: Shop-Manager-System-Offline/docs/api-routes.md -->

# API routes

**Mô tả:** Tài liệu tham chiếu gốc Shop docs/api-routes.md — API routes (nội dung dưới thường tiếng Anh).

> **Ghi chú:** Phần dưới giữ nguyên tiếng Anh từ repo Shop (tham chiếu kỹ thuật). Luồng tiếng Việt ưu tiên đọc `nghiep-vu/` và `he-thong/`.

All endpoints are mounted under `/api` (see `artifacts/api-server/src/app.ts`).

## Health

- `GET /api/healthz`

## Auth

- `POST /api/auth/login`
- `GET /api/auth/me` (requires auth)

## Shops

- `GET /api/shops` (requires auth)

## Products

- `GET /api/products` (requires auth)
- `POST /api/products` (requires auth)
- `GET /api/products/:id` (requires auth)
- `PATCH /api/products/:id` (requires auth)
- `DELETE /api/products/:id` (requires auth; soft-discontinue)

## Inventory (shop-level)

- `GET /api/inventory` (requires auth)
- `PATCH /api/inventory/:productId` (requires auth)

## Orders (POS)

- `GET /api/orders` (requires auth)
- `POST /api/orders` (requires auth)
- `GET /api/orders/:id` (requires auth)
- `PATCH /api/orders/:id/cancel` (requires auth)
- `PATCH /api/orders/:id/approve-cancel` (requires auth)
- `PATCH /api/orders/:id/reject-cancel` (requires auth)
- `PATCH /api/orders/:id/uncancel` (requires auth)
- `POST /api/orders/:id/notify-reprint` (requires auth)

## Staff (user management)

These endpoints require `requireAdmin` (admin + super_admin).

- `GET /api/staff`
- `POST /api/staff`
- `PATCH /api/staff/:id`
- `DELETE /api/staff/:id`

## Dashboard

- `GET /api/dashboard`
- `GET /api/dashboard/revenue-chart`
- `GET /api/dashboard/top-products`
- `GET /api/dashboard/orders-today`
- `GET /api/dashboard/low-stock`

## Statistics

- `GET /api/statistics/products`
- `GET /api/statistics/product-sales`

## Reports

- `GET /api/reports/staff`
- `GET /api/reports/reprints`
- `GET /api/reports/staff/:userId/detail`

## Stock requests (import/export requests)

- `GET /api/stock-requests`
- `GET /api/stock-requests/pending-count`
- `GET /api/stock-requests/:id`
- `POST /api/stock-requests`
- `PATCH /api/stock-requests/:id/approve`
- `PATCH /api/stock-requests/:id/reject`
- `PATCH /api/stock-requests/:id/complete`
- `PATCH /api/stock-requests/:id/cancel`

## Chain (org/shops/warehouses/transfers)

This module contains “chain-level” operations such as:

- Organizations:
  - `GET /api/organizations`
  - `POST /api/organizations`
  - `PATCH /api/organizations/:id`
- Shops:
  - `POST /api/shops` (create shop; may create warehouse + admin)
  - `PATCH /api/shops/:id`
  - `POST /api/shops/:id/create-admin`
  - `PATCH /api/shops/:id/admin-email`
  - `PATCH /api/shops/:id/reset-password`
- Warehouses:
  - `GET /api/warehouses`
  - `POST /api/warehouses`
  - `PATCH /api/warehouses/:id`
  - `GET /api/warehouses/:id/products`
  - `GET /api/warehouses/:id/inventory`
  - `POST /api/warehouses/:id/adjust-stock`
  - `GET /api/warehouses/:id/movements`
- Transfers:
  - `GET /api/transfers`
  - `GET /api/transfers/:id/items`
  - `POST /api/transfers`
  - `PATCH /api/transfers/:id`
  - `DELETE /api/transfers/:id`
  - `POST /api/transfers/:id/approve`
  - `POST /api/transfers/:id/ship`
  - `POST /api/transfers/:id/receive`

