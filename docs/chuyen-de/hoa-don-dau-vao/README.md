# Hóa đơn đầu vào (VAT mua vào)

**Mô tả:** Import PDF/Excel, kéo CQT, MST lọc, ghép hàng, nhập kho.

**Về trang chủ Map:** [README.md](../../README.md) · [Hướng dẫn đọc](../../huong-dan-doc/)

Chủ đề phức tạp nhất — đọc **06 → 07 → 08** trước khi mở file API/UI.

## 1. Luồng nghiệp vụ (đọc trước)

- [06-hoa-don-dau-vao-tong-quan](../../nghiep-vu/06-hoa-don-dau-vao-tong-quan/) — Vòng đời HĐ mua vào: import, ghép SP, nhập kho, trạng thái stockStatus.
- [07-hd-dau-vao-mst-loc](../../nghiep-vu/07-hd-dau-vao-mst-loc/) — MST lọc tự archive HĐ; tab Khác / Lưu trữ / Đang dùng; modal trên trang HĐ đầu vào.
- [08-hd-dau-vao-cqt-sync](../../nghiep-vu/08-hd-dau-vao-cqt-sync/) — Kéo HĐ từ CQT (GDT direct): captcha, sync-tax, map XML vào DB.

## 2. Màn hình (giao diện)

- [hoa-don-dau-vao](../../trang/hoa-don-dau-vao/) — HĐ đầu vào VAT: import, kéo CQT, MST lọc, ghép SP, nhập kho.

## 3. Module API

- [hoa-don-dau-vao](../../module-api/hoa-don-dau-vao/) — Hóa đơn mua vào VAT (lớn nhất).
- [cong-cqt](../../module-api/cong-cqt/) — Phiên đăng nhập CQT (captcha).

## 4. Bảng dữ liệu (schema)

- [hoa-don-dau-vao-db](../../co-so-du-lieu/hoa-don-dau-vao-db/) — Drizzle vatInboundInvoices.ts — 1 bảng, 55 cột, 3 index (vat_inbound_invoices).
- [audit-hoa-don-dau-vao](../../co-so-du-lieu/audit-hoa-don-dau-vao/) — Drizzle vatInboundAuditLogs.ts — 1 bảng, 8 cột, 2 index (vat_inbound_audit_logs).
- [phien-thue-cqt](../../co-so-du-lieu/phien-thue-cqt/) — Drizzle orgGdtTaxSessions.ts — 1 bảng, 8 cột (org_gdt_tax_sessions).

## 5. Thư viện backend (một số file quan trọng)

Tra cứu đủ: [README.md](../../chi-muc/thu-vien-backend/)

- [inbound-stock-receive](../../thu-vien/inbound-stock-receive/) — [Hóa đơn đầu vào] inbound-stock-receive.ts — applyInvoiceInventoryReceive…
- [vat-inbound-audit](../../thu-vien/vat-inbound-audit/) — [Hóa đơn đầu vào] vat-inbound-audit.ts — insertVatInboundAuditLog…
- [vat-inbound-auto-archive-mst](../../thu-vien/vat-inbound-auto-archive-mst/) — [Hóa đơn đầu vào] vat-inbound-auto-archive-mst.ts…
- [vat-inbound-auto-process](../../thu-vien/vat-inbound-auto-process/) — [Hóa đơn đầu vào] vat-inbound-auto-process.ts…
- [vat-inbound-auto-sync](../../thu-vien/vat-inbound-auto-sync/) — [Hóa đơn đầu vào] vat-inbound-auto-sync.ts — isVatInboundAutoSyncWindow…
- [vat-inbound-excluded](../../thu-vien/vat-inbound-excluded/) — [Hóa đơn đầu vào] vat-inbound-excluded.ts — listExcludedLineIndexes.
- [vat-inbound-mapped-products](../../thu-vien/vat-inbound-mapped-products/) — [Hóa đơn đầu vào] vat-inbound-mapped-products.ts…
- [vat-inbound-marked-mst-backfill](../../thu-vien/vat-inbound-marked-mst-backfill/) — [Hóa đơn đầu vào] vat-inbound-marked-mst-backfill.ts…
- [vat-inbound-product-code](../../thu-vien/vat-inbound-product-code/) — [Hóa đơn đầu vào] vat-inbound-product-code.ts…
- [vat-inbound-tax-sync](../../thu-vien/vat-inbound-tax-sync/) — [Hóa đơn đầu vào] vat-inbound-tax-sync.ts — syncVatInboundInvoicesFromTax.

---

*Sinh tự động — `python3 docs/gen.py`*
