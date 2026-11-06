# Chuỗi và đa chi nhánh

**Mô tả:** Organization, nhiều shop, kho trung tâm, dashboard chuỗi và heartbeat.

- **Organization** → nhiều **shops**; warehouse central / transit / shop backroom.
- Dashboard chuỗi: aggregate theo scope quyền (`chain-dashboard.tsx`).
- Heartbeat shop: `last_seen_at` — Trợ lý AI báo offline/clock drift.

**API:** `chain.ts`, `dashboard.ts`, `statistics.ts`.
