# Hóa đơn bán ra (Viettel)

**Mô tả:** Phát hành HĐ VAT từ POS, tra cứu, form công khai.

**Về trang chủ Map:** [README.md](../../README.md) · [Hướng dẫn đọc](../../huong-dan-doc/)

Tích hợp Viettel SInvoice — cấu hình tại Chuỗi → Sửa tổ chức.

## 1. Luồng nghiệp vụ (đọc trước)

- [05-hoa-don-vat-xuat](../../nghiep-vu/05-hoa-don-vat-xuat/) — Hóa đơn VAT bán ra qua Viettel SInvoice và cấu hình org.

## 2. Màn hình (giao diện)

- [hoa-don-xuat-vat](../../trang/hoa-don-xuat-vat/) — Phát hành và quản lý HĐ VAT bán ra (Viettel).
- [tra-cuu-hoa-don-cong-khai](../../trang/tra-cuu-hoa-don-cong-khai/) — Form công khai tra cứu/xem HĐ VAT /vat-invoice.

## 3. Module API

- [cau-hinh-viettel](../../module-api/cau-hinh-viettel/) — Cấu hình Viettel SInvoice theo org.
- [hoa-don-vat-cong-khai](../../module-api/hoa-don-vat-cong-khai/) — API/form HĐ VAT công khai.

## 4. Bảng dữ liệu (schema)

- [to-chuc](../../co-so-du-lieu/to-chuc/) — Drizzle organizations.ts — 1 bảng, 39 cột (organizations).

## 5. Thư viện backend (một số file quan trọng)

Tra cứu đủ: [README.md](../../chi-muc/thu-vien-backend/)

- [org-viettel-settings](../../thu-vien/org-viettel-settings/) — [Hóa đơn bán ra] org-viettel-settings.ts — viettelConfigReadiness…
- [vat-invoice-auto-issue](../../thu-vien/vat-invoice-auto-issue/) — [Hóa đơn bán ra] vat-invoice-auto-issue.ts — AUTO_ISSUE_BATCH_MINUTE_OF_DAY_VN…
- [vat-invoice-buyer-email](../../thu-vien/vat-invoice-buyer-email/) — [Hóa đơn bán ra] vat-invoice-buyer-email.ts — deliverVatInvoiceEmailToBuyer.
- [vat-invoice-public-window](../../thu-vien/vat-invoice-public-window/) — [Hóa đơn bán ra] vat-invoice-public-window.ts…
- [vat-invoice](../../thu-vien/vat-invoice/) — [Hóa đơn bán ra] vat-invoice.ts — normalizeTaxCode, isValidTaxCode, isNumericTaxCode…

---

*Sinh tự động — `python3 docs/gen.py`*
