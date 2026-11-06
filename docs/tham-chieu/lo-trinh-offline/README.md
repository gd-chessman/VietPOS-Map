<!-- Mirror: Shop-Manager-System-Offline/docs/offline-first-roadmap.md -->

# Roadmap: Offline-first toàn bộ ứng dụng

**Mô tả:** Tài liệu tham chiếu gốc Shop docs/offline-first-roadmap.md — Roadmap: Offline-first toàn bộ ứng dụng (nội dung dưới thường tiếng Anh).

> **Ghi chú:** Phần dưới giữ nguyên tiếng Anh từ repo Shop (tham chiếu kỹ thuật). Luồng tiếng Việt ưu tiên đọc `nghiep-vu/` và `he-thong/`.

Kế hoạch đầu việc để mở rộng offline-first ra toàn bộ `pos-app`, dựa trên hiện trạng đã kiểm kê tại [offline-first-audit.md](offline-first-audit.md).

## Giả định phạm vi

App dùng nội bộ cho 1 cửa hàng — **bỏ qua bài toán 2 thiết bị cùng ghi song song** (không cần cơ chế merge/conflict phức tạp giữa nhiều thiết bị). Chỉ cần **hàng đợi offline (outbox)** áp dụng tuần tự khi có mạng trở lại, theo đúng pattern đã chứng minh hiệu quả với đơn hàng (`pendingOrders` + `Idempotency-Key` + `order_sync_keys`), tổng quát hóa để tái dùng cho các tính năng còn lại thay vì viết riêng lẻ từng cái.

## Phase 0 — Hạ tầng dùng chung

Làm trước, mọi phase sau phụ thuộc vào đây.

1. **Bảng outbox tổng quát** trong `lib/local-db`: bảng `pendingActions` (thay vì tạo bảng riêng cho từng loại thao tác) — field: `id` (uuid), `type` (`shift_close` | `order_cancel` | `order_cancel_approve` | `payment_change` | `product_upsert` | `product_delete` | `inventory_adjust` | `staff_upsert`...), `payload` (json), `shopId`, `userId`, `createdAt`, `syncStatus`, `syncError`, `resultRef`.
2. Hàm CRUD cho outbox: `enqueueAction()`, `listPendingActions()`, `markActionSynced()`, `markActionConflict()` — cùng file `local-db`.
3. Mở rộng `lib/sync`: `pushPendingActions()` — xử lý theo đúng thứ tự tạo (FIFO), map `type` → đúng API endpoint, gửi kèm `Idempotency-Key` = action id.
4. **Server**: thêm bảng `sync_action_keys` (idempotency tổng quát, giống `order_sync_keys` nhưng dùng chung cho mọi loại action, không chỉ order).
5. **Server**: rà soát từng endpoint sẽ offline hóa (cancel, approve/reject, payment-change, product CRUD, inventory adjust, staff CRUD...) — hiện chỉ `POST /orders` hỗ trợ `Idempotency-Key`, cần bổ sung cho các endpoint còn lại theo cùng pattern.
6. **Client**: hook dùng chung `useOfflineAwareMutation()` — online thì gọi API như cũ (không đổi hành vi hiện tại); offline thì `enqueueAction()` + cập nhật UI lạc quan (optimistic) + toast "sẽ đồng bộ khi có mạng".
7. **Client**: helper `useOfflineAwareQuery()` — đọc cache trước, gọi API làm mới cache khi có mạng, hiển thị badge "dữ liệu lúc HH:mm" khi đang phục vụ từ cache.

## Phase 1 — Tại quầy POS

Ưu tiên cao nhất, rủi ro thấp nhất vì cùng nằm trên màn hình POS đã offline sẵn.

8. Đóng ca offline — dùng outbox mới, đóng local ngay, đồng bộ server khi có mạng. File: `lib/sales-api.ts:67-76`, `lib/offline/logout.ts`.
9. Hủy đơn / duyệt hủy / hoàn tác hủy — chuyển `lib/cancel-order.ts` sang `useOfflineAwareMutation`.
10. Đổi phương thức thanh toán tại POS — `lib/payment-change.ts` tương tự.
11. Sửa ghi chú đơn hàng (nếu có thao tác sửa ngoài lúc tạo) — `lib/order-note.ts`.

## Phase 2 — Quản lý tại cửa hàng (Products / Inventory / Staff)

12. Cache đọc **toàn bộ** danh sách sản phẩm cho trang Products (khác cache rút gọn hiện dùng cho POS — cần đủ field để sửa).
13. CRUD sản phẩm offline (create/update/delete) → outbox + cập nhật danh sách local lạc quan.
14. Điều chỉnh tồn kho (Inventory) offline → outbox tương tự.
15. Cache đọc + CRUD offline cho Staff.
16. Mở rộng bảng `salesStaff` (hiện chỉ đọc-only cho POS) thành CRUD offline cho trang Sales Staff.
17. Trang Orders toàn cửa hàng: mở rộng phạm vi cache đơn hàng ra ngoài ca hiện tại (hiện `shiftOrders` chỉ giới hạn theo ca).

## Phase 3 — Hóa đơn VAT, Dashboard/Statistics/Reports

18. Hóa đơn VAT: cache đọc danh sách; **khuyến nghị KHÔNG offline hóa bước phát hành/sửa** — cần xác thực real-time (mã số thuế, cổng thuế), chỉ nên cho xem lại offline.
19. Dashboard/Statistics: cache snapshot kết quả API gần nhất (không tính lại local vì thiếu dữ liệu lịch sử đầy đủ), hiển thị badge "dữ liệu lúc HH:mm".
20. Reports: cache kết quả các báo cáo đã xem gần nhất tương tự; export Excel giữ nguyên yêu cầu mạng.

## Phase 4 — Stock Requests & Chain (cân nhắc riêng)

21. Stock Requests: chỉ offline hóa bước **tạo yêu cầu** (create-only, giống bản chất "thêm mới" của order); bước duyệt/từ chối giữ online vì cần tồn kho real-time từ kho/chi nhánh khác — đây không phải vấn đề đa-thiết-bị mà là đa-chi-nhánh, nằm ngoài phạm vi "1 cửa hàng offline".
22. Chain / Chain Dashboard: khuyến nghị **giữ network-only** — màn hình tổng hợp đa chi nhánh, bản chất luôn cần dữ liệu real-time từ nhiều cửa hàng khác nhau.
