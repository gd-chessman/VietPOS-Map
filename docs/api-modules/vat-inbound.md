# API module: `vat-inbound`

**Mô tả:** File routes vat-inbound.ts — 28 endpoint HTTP cho /api/.... Module lớn nhất về HĐ mua vào VAT: import PDF/Excel, kéo CQT/Viettel, ghép SP, nhập kho, lưu trữ, MST lọc (tab Khác), a…

**Source Shop:** `artifacts/api-server/src/routes/vat-inbound.ts`

Module **lớn nhất** về HĐ mua vào VAT: import PDF/Excel, kéo **CQT/Viettel**, ghép SP, nhập kho,
lưu trữ, MST lọc (tab Khác), audit, hoàn tác nhập kho / bỏ ghép dòng.

**Lib quan trọng:** `lib/vat-inbound-tax-sync.ts`, `lib/gdt-portal/*`, `lib/vat-inbound-auto-archive-mst.ts`,
`lib/viettel-sinvoice/*`, `lib/inbound-stock-receive.ts`.

**Frontend:** `pages/vat-inbound.tsx`, `lib/vat-inbound-api.ts`, IndexedDB `@workspace/local-db`.

**Quyền:** hub shop + `requireVatInboundAccess` (admin, manager, accountant, warehouse_keeper tại CN chính).

**Số endpoint trong file:** 28

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/vat-inbound` | Danh sách HĐ mua vào của **hub shop**; không trả `pdfBase64` (chỉ cờ `hasPdf`); tự relink PO nếu thiếu; join trạng thái … |
| GET | `/vat-inbound/marked-mst-archive` | Đọc chuỗi MST lọc từ `organizations… |
| PATCH | `/vat-inbound/marked-mst-archive` | Lưu MST lọc (admin/manager); normalize input; **backfill** archive HĐ trùng MST ngay sau lưu… |
| POST | `/vat-inbound/backfill-marked-mst-archive` | Chạy lại backfill archive theo MST (ops / sau migration)… |
| POST | `/vat-inbound/gdt/captcha` | Lấy captcha CQT cho org `gdt_direct` — trả session tạm captcha store… |
| POST | `/vat-inbound/gdt/reconnect` | Đăng nhập lại CQT sau captcha; lưu session org GDT… |
| POST | `/vat-inbound/sync-tax` | Kéo HĐ từ CQT/Viettel theo `from`/`to`; map XML → DB; auto archive MST; có thể split khoảng dài… |
| GET | `/vat-inbound/:id/pdf` | Tải PDF base64 đã lưu hoặc fetch Viettel nếu thiếu… |
| GET | `/vat-inbound/:id` | Chi tiết một HĐ (metadata + stock lines, không full PDF trong list)… |
| POST | `/vat-inbound` | Upsert HĐ (import PDF/Excel từ client); parse fields; sync archive MST on write… |
| POST | `/vat-inbound/:id/verify-viettel` | Xác thực HĐ với Viettel SInvoice; cập nhật trạng thái verify… |
| POST | `/vat-inbound/:id/stock-receipt` | Ghép dòng HĐ ↔ SP; tạo/cập nhật `stockLines`; có thể tạo SP/NCC/PO inline… |
| GET | `/vat-inbound/:id/purchase-order` | Lấy PO gắn HĐ (nếu có) |
| POST | `/vat-inbound/:id/receive-stock` | Nhập kho theo dòng đã ghép; cập nhật tồn + giá vốn BQ; đổi `stockStatus`… |
| POST | `/vat-inbound/:id/restore-line` | Khôi phục dòng đã loại trừ khỏi ghép hàng… |
| POST | `/vat-inbound/:id/dismiss-excluded-lines` | Bỏ qua dòng không nhập (phí, dịch vụ…) — ghi audit… |
| POST | `/vat-inbound/:id/undo-dismiss-excluded-lines` | Hoàn tác bỏ qua dòng (nếu policy cho phép)… |
| POST | `/vat-inbound/:id/request-undo-dismiss-excluded` | NV gửi yêu cầu hoàn tác bỏ qua dòng |
| POST | `/vat-inbound/:id/approve-undo-dismiss-excluded` | Quản lý duyệt hoàn tác bỏ qua dòng |
| POST | `/vat-inbound/:id/reject-undo-dismiss-excluded` | Từ chối yêu cầu hoàn tác bỏ qua dòng |
| POST | `/vat-inbound/:id/close-short` | Chốt nhập **thiếu** — đóng phiếu với trạng thái `closed_short`… |
| POST | `/vat-inbound/:id/request-rollback` | Yêu cầu hoàn tác nhập kho (rollback inventory)… |
| POST | `/vat-inbound/:id/approve-rollback` | Duyệt rollback — trừ lại tồn đã nhập |
| POST | `/vat-inbound/:id/reject-rollback` | Từ chối yêu cầu rollback |
| GET | `/vat-inbound/:id/audit-logs` | Nhật ký thao tác trên HĐ (`vat_inbound_audit_logs`)… |
| POST | `/vat-inbound/:id/archive` | Lưu trữ thủ công (`archivedAt`) |
| POST | `/vat-inbound/:id/unarchive` | Bỏ lưu trữ |
| DELETE | `/vat-inbound/:id` | Xóa HĐ (policy + trạng thái kho); thường admin… |

## Chi tiết từng endpoint

### `GET /vat-inbound` {#get-vat-inbound}

Danh sách HĐ mua vào của **hub shop**; không trả `pdfBase64` (chỉ cờ `hasPdf`); tự relink PO nếu thiếu; join trạng thái PO. Middleware: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

- **Middleware:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

### `GET /vat-inbound/marked-mst-archive` {#get-vat-inbound-marked-mst-archive}

Đọc chuỗi MST lọc từ `organizations.vat_inbound_auto_archive_tax_codes`. Middleware: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

- **Middleware:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

### `PATCH /vat-inbound/marked-mst-archive` {#patch-vat-inbound-marked-mst-archive}

Lưu MST lọc (admin/manager); normalize input; **backfill** archive HĐ trùng MST ngay sau lưu. Middleware: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

- **Middleware:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

### `POST /vat-inbound/backfill-marked-mst-archive` {#post-vat-inbound-backfill-marked-mst-archive}

Chạy lại backfill archive theo MST (ops / sau migration). Middleware: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

- **Middleware:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

### `POST /vat-inbound/gdt/captcha` {#post-vat-inbound-gdt-captcha}

Lấy captcha CQT cho org `gdt_direct` — trả session tạm captcha store. Middleware: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

- **Middleware:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

### `POST /vat-inbound/gdt/reconnect` {#post-vat-inbound-gdt-reconnect}

Đăng nhập lại CQT sau captcha; lưu session org GDT. Middleware: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

- **Middleware:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

### `POST /vat-inbound/sync-tax` {#post-vat-inbound-sync-tax}

Kéo HĐ từ CQT/Viettel theo `from`/`to`; map XML → DB; auto archive MST; có thể split khoảng dài. Middleware: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

- **Middleware:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

### `GET /vat-inbound/:id/pdf` {#get-vat-inbound--id-pdf}

Tải PDF base64 đã lưu hoặc fetch Viettel nếu thiếu. Middleware: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

- **Middleware:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

### `GET /vat-inbound/:id` {#get-vat-inbound--id}

Chi tiết một HĐ (metadata + stock lines, không full PDF trong list). Middleware: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

- **Middleware:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

### `POST /vat-inbound` {#post-vat-inbound}

Upsert HĐ (import PDF/Excel từ client); parse fields; sync archive MST on write. Middleware: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

- **Middleware:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

### `POST /vat-inbound/:id/verify-viettel` {#post-vat-inbound--id-verify-viettel}

Xác thực HĐ với Viettel SInvoice; cập nhật trạng thái verify. Middleware: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

- **Middleware:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

### `POST /vat-inbound/:id/stock-receipt` {#post-vat-inbound--id-stock-receipt}

Ghép dòng HĐ ↔ SP; tạo/cập nhật `stockLines`; có thể tạo SP/NCC/PO inline. Middleware: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

- **Middleware:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

### `GET /vat-inbound/:id/purchase-order` {#get-vat-inbound--id-purchase-order}

Lấy PO gắn HĐ (nếu có). Middleware: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

- **Middleware:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

### `POST /vat-inbound/:id/receive-stock` {#post-vat-inbound--id-receive-stock}

Nhập kho theo dòng đã ghép; cập nhật tồn + giá vốn BQ; đổi `stockStatus`. Middleware: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

- **Middleware:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

### `POST /vat-inbound/:id/restore-line` {#post-vat-inbound--id-restore-line}

Khôi phục dòng đã loại trừ khỏi ghép hàng. Middleware: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

- **Middleware:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

### `POST /vat-inbound/:id/dismiss-excluded-lines` {#post-vat-inbound--id-dismiss-excluded-lines}

Bỏ qua dòng không nhập (phí, dịch vụ…) — ghi audit. Middleware: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

- **Middleware:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

### `POST /vat-inbound/:id/undo-dismiss-excluded-lines` {#post-vat-inbound--id-undo-dismiss-excluded-lines}

Hoàn tác bỏ qua dòng (nếu policy cho phép). Middleware: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

- **Middleware:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

### `POST /vat-inbound/:id/request-undo-dismiss-excluded` {#post-vat-inbound--id-request-undo-dismiss-excluded}

NV gửi yêu cầu hoàn tác bỏ qua dòng. Middleware: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

- **Middleware:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

### `POST /vat-inbound/:id/approve-undo-dismiss-excluded` {#post-vat-inbound--id-approve-undo-dismiss-excluded}

Quản lý duyệt hoàn tác bỏ qua dòng. Middleware: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

- **Middleware:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

### `POST /vat-inbound/:id/reject-undo-dismiss-excluded` {#post-vat-inbound--id-reject-undo-dismiss-excluded}

Từ chối yêu cầu hoàn tác bỏ qua dòng. Middleware: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

- **Middleware:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

### `POST /vat-inbound/:id/close-short` {#post-vat-inbound--id-close-short}

Chốt nhập **thiếu** — đóng phiếu với trạng thái `closed_short`. Middleware: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

- **Middleware:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

### `POST /vat-inbound/:id/request-rollback` {#post-vat-inbound--id-request-rollback}

Yêu cầu hoàn tác nhập kho (rollback inventory). Middleware: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

- **Middleware:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

### `POST /vat-inbound/:id/approve-rollback` {#post-vat-inbound--id-approve-rollback}

Duyệt rollback — trừ lại tồn đã nhập. Middleware: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

- **Middleware:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

### `POST /vat-inbound/:id/reject-rollback` {#post-vat-inbound--id-reject-rollback}

Từ chối yêu cầu rollback. Middleware: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

- **Middleware:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

### `GET /vat-inbound/:id/audit-logs` {#get-vat-inbound--id-audit-logs}

Nhật ký thao tác trên HĐ (`vat_inbound_audit_logs`). Middleware: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

- **Middleware:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

### `POST /vat-inbound/:id/archive` {#post-vat-inbound--id-archive}

Lưu trữ thủ công (`archivedAt`). Middleware: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

- **Middleware:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

### `POST /vat-inbound/:id/unarchive` {#post-vat-inbound--id-unarchive}

Bỏ lưu trữ. Middleware: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

- **Middleware:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

### `DELETE /vat-inbound/:id` {#delete-vat-inbound--id}

Xóa HĐ (policy + trạng thái kho); thường admin. Middleware: `requireAuth, requireOperationalContext, requireVatInboundAccess`.

- **Middleware:** `requireAuth`, `requireOperationalContext`, `requireVatInboundAccess`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./vat-inbound.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.

## Luồng nghiệp vụ liên quan

- `nghiep-vu/06-hoa-don-dau-vao-tong-quan.md`
- `nghiep-vu/07-hd-dau-vao-mst-loc.md`
- `nghiep-vu/08-hd-dau-vao-cqt-sync.md`
- UI: `frontend-pages/vat-inbound.md`
- Lib: `lib-modules/vat-inbound-tax-sync.md`, `lib-modules/gdt-portal/`…
