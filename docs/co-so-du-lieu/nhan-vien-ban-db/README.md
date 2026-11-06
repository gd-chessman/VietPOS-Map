# Schema: `salesStaff`

**Mô tả:** Drizzle salesStaff.ts — 1 bảng, 13 cột, 1 enum, 2 index (sales_staff).

**Mã nguồn Shop:** `lib/db/src/schema/salesStaff.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [nhan-vien-ban-api](../../module-api/nhan-vien-ban-api/) (`routes/sales-staff.ts`)
- **Giao diện:** [nhan-vien-ban-hang](../../trang/nhan-vien-ban-hang/)

## Enum Postgres

### `sales_staff_status` (`salesStaffStatusEnum`)

- Giá trị: `["active", "on_leave", "resigned"]`

## Bảng `sales_staff`

- **Biến Drizzle:** `salesStaffTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `full_name` | `fullName` | text | NOT NULL | — | — |
| `id_number` | `idNumber` | text | — | — | — |
| `date_of_birth` | `dateOfBirth` | date | — | — | — |
| `address` | `address` | text | — | — | — |
| `phone` | `phone` | text | — | — | — |
| `start_date` | `startDate` | date | — | — | — |
| `end_date` | `endDate` | date | — | — | — |
| `status` | `status` | enum `sales_staff_status` | NOT NULL, default `active` | — | — |
| `notes` | `notes` | text | — | — | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |
| `updated_at` | `updatedAt` | timestamp("updated_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |

**Index:**

- `sales_staff_shop_id_number_uidx` on `shopId`, `idNumber`
- `sales_staff_shop_status_idx` on `shopId`, `status`

## Kiểu & Zod (insert)

- `insertSalesStaffSchema` — `createInsertSchema` (xem file TS)
- `export type InsertSalesStaff`
- `export type SalesStaff`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
