# Schema: `customerFeedback`

**Mô tả:** Drizzle customerFeedback.ts — 1 bảng, 8 cột, 2 index (customer_feedback).

**Mã nguồn Shop:** `lib/db/src/schema/customerFeedback.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [phan-hoi-api](../../module-api/phan-hoi-api/) (`routes/feedback.ts`)
- **Giao diện:** [phan-hoi-khach](../../trang/phan-hoi-khach/)

## Bảng `customer_feedback`

- **Biến Drizzle:** `customerFeedbackTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `shop_id` | `shopId` | integer | — | `shops` | — |
| `customer_name` | `customerName` | text | NOT NULL | — | — |
| `phone` | `phone` | text | — | — | — |
| `rating` | `rating` | integer | NOT NULL | — | — |
| `content` | `content` | text | NOT NULL | — | — |
| `image_urls` | `imageUrls` | jsonb | JSON typed | — | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |

**Index:**

- `customer_feedback_created_idx` on `createdAt`
- `customer_feedback_shop_idx` on `shopId`

## Kiểu & Zod (insert)

- `insertCustomerFeedbackSchema` — `createInsertSchema` (xem file TS)
- `export type InsertCustomerFeedback`
- `export type CustomerFeedback`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
