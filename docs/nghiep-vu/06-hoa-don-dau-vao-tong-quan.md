# Hóa đơn đầu vào — tổng quan

**Mô tả:** Vòng đời HĐ mua vào: import, ghép SP, nhập kho, trạng thái stockStatus.

## Nguồn dữ liệu

| Kênh | UI / API | Ghi chú |
|------|----------|---------|
| PDF | Nhập PDF → parse local → upsert server | Revision parse `VAT_INBOUND_PARSE_REVISION` |
| Excel | Mẫu + import | `vat-inbound-excel-import.ts` |
| CQT | Lấy hóa đơn → `POST /vat-inbound/sync-tax` | GDT direct / Viettel tùy org |
| Viettel | Verify từng HĐ | `verify-viettel` endpoint |

## Vòng đời (happy path)

1. HĐ vào DB `vat_inbound_invoices` (shop hub).
2. Nếu MST trùng **MST lọc** → `archivedAt`, tab **Khác** (xem mục 07).
3. Kế toán mở HĐ → ghép từng dòng SP (`stock-receipt`) — tạo/cập nhật `stockLines`, có thể tạo SP/NCC.
4. **Nhập kho** (`receive-stock`) — cộng tồn, giá vốn BQ.
5. Trạng thái: `mapped` → `partial`/`received` hoặc `closed_short`.

## Trạng thái `stockStatus`

- `mapped`: đã ghép, chưa nhập kho
- `partial`: nhập một phần
- `received`: đủ
- `closed_short`: chốt thiếu
- `rollback_requested`: chờ duyệt hoàn tác nhập kho

## Offline / IndexedDB

- Máy client giữ bản copy + PDF bytes; sync khi online.
- `listPendingVatInboundInvoices` push lên server.

## Đọc tiếp

- API đầy đủ: `api-modules/vat-inbound.md`
- UI: `frontend-pages/vat-inbound.md`
- DB: `schema/vatInboundInvoices.md`
