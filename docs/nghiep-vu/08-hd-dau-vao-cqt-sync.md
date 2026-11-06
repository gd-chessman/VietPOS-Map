# HĐ đầu vào — kéo CQT

**Mô tả:** Kéo HĐ từ CQT (GDT direct): captcha, sync-tax, map XML vào DB.

- Org `vat_inbound_provider = gdt_direct` → captcha + login CQT (`/vat-inbound/gdt/*`).
- `POST /vat-inbound/sync-tax` body `{ from, to }` — tối đa 3 tháng/lần, split dài.
- Map row GDT → insert/update DB; VAT rate label 0.08 → 8%; auto archive MST.

**Lib:** `gdt-portal/`, `vat-inbound-tax-sync.ts`, `map-inbound.ts`.

**Tool dev:** `gdt-cqt-tester/` (ngoài monorepo).
