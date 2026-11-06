# Schema: `customerFeedback`

**Mô tả:** Drizzle schema customerFeedback.ts — 8 cột trên 1 bảng Postgres (customer_feedback).

**Mã nguồn Shop:** `lib/db/src/schema/customerFeedback.ts`

## Bảng Postgres

- `customer_feedback`

## Cột (trích từ schema TS)

- `id` (id)
- `shop_id` (shopId)
- `customer_name` (customerName)
- `phone` (phone)
- `rating` (rating)
- `content` (content)
- `image_urls` (imageUrls)
- `created_at` (createdAt)

## Tham chiếu (references → bảng Drizzle)

- `shopsTable`

Tổng quan quan hệ: `tham-chieu/co-so-du-lieu-goc/README.md`.
