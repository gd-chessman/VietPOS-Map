# Schema: `inventoryMovements`

**Mô tả:** Drizzle inventoryMovements.ts — 1 bảng, 9 cột (inventory_movements).

**Mã nguồn Shop:** `lib/db/src/schema/inventoryMovements.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [ton-kho-api](../../module-api/ton-kho-api/) (`routes/inventory.ts`)

## Bảng `inventory_movements`

- **Biến Drizzle:** `inventoryMovementsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `product_id` | `productId` | integer | NOT NULL | — | — |
| `warehouse_id` | `warehouseId` | integer | NOT NULL | `warehouses` | — |
| `movement_type` | `movementType` | text | NOT NULL | — | — |
| `quantity_delta` | `quantityDelta` | integer | NOT NULL | — | — |
| `reference_type` | `referenceType` | text | — | — | — |
| `reference_id` | `referenceId` | integer | — | — | — |
| `note` | `note` | text | — | — | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
