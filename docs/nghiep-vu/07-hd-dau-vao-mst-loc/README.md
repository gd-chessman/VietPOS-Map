# HĐ đầu vào — MST lọc (tab Khác)

**Mô tả:** MST lọc tự archive HĐ; tab Khác / Lưu trữ / Đang dùng; modal trên trang HĐ đầu vào.

## Mục đích

Tự động **lưu trữ** hóa đơn mua vào có MST người bán/người mua nằm trong danh sách loại trừ
(công ty nội bộ, đối tác không cần nhập kho, v.v.) để kế toán không thấy ở tab **Đang dùng**.

## Cấu hình

| Lớp | Chi tiết |
|-----|----------|
| DB | `organizations.vat_inbound_auto_archive_tax_codes` — chuỗi text, nhiều MST (xuống dòng hoặc phân tách) |
| API GET | `/api/vat-inbound/marked-mst-archive` |
| API PATCH | `/api/vat-inbound/marked-mst-archive` body `{ codes }` (string hoặc null) |
| Quyền sửa | Admin / manager (`canEditVatInboundMarkedMst`) |

**Không** cấu hình trong Chuỗi → Sửa tổ chức (đã chuyển về trang HĐ đầu vào).

## Hành vi UI

- Tab **Khác:** HĐ đã `archivedAt` **và** MST khớp danh sách lọc.
- Tab **Lưu trữ:** archived nhưng **không** khớp MST lọc (lưu trữ thủ công / lý do khác).
- Tab **Đang dùng:** chưa archive, không thuộc Khác.
- Nút **MST lọc** trên toolbar (trước Mẫu Excel): modal textarea → **Lưu** → PATCH + backfill.

## Backfill

- Khi PATCH danh sách: `backfillVatInboundArchiveByMarkedMst(orgId)`.
- Khi insert/update HĐ / sau sync thuế: helper `syncVatInboundTaxArchivesForInvoice` (xem lib auto-archive).

## Code map

- `lib/vat-inbound-auto-archive-mst.ts` — normalize MST, so khớp
- `lib/vat-inbound-marked-mst-backfill.ts` — quét HĐ org
- `routes/vat-inbound.ts` — endpoint marked-mst-archive
- `pages/vat-inbound.tsx` — modal, tab lọc `other`
