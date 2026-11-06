# Schema: `shopApiKeys`

**Mô tả:** Drizzle schema shopApiKeys.ts — 9 cột trên 1 bảng Postgres (shop_api_keys).

**Mã nguồn Shop:** `lib/db/src/schema/shopApiKeys.ts`

## Bảng Postgres

- `shop_api_keys`

## Cột (trích từ schema TS)

- `id` (id)
- `shop_id` (shopId)
- `label` (label)
- `count_mode` (countMode)
- `beam_carry` (beamCarry)
- `beam_carry_visit_date` (beamCarryVisitDate)
- `api_key` (apiKey)
- `status` (status)
- `created_at` (createdAt)

## Tham chiếu (references → bảng Drizzle)

- `shopsTable`

Tổng quan quan hệ: `tham-chieu/co-so-du-lieu-goc/README.md`.
