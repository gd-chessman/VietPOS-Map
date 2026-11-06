<!-- Mirror: Shop-Manager-System-Offline/docs/offline-first-audit.md -->

# Đánh giá mức độ Offline-First (audit)

**Mô tả:** Bản mirror doc Shop docs/offline-first-audit.md — Đánh giá mức độ Offline-First (audit).

Tài liệu này kiểm kê từng tính năng của `pos-app` theo mức độ hoạt động được khi thiết bị **mất mạng tới API server**. Xem [offline-first.md](offline-first.md) cho quyết định kiến trúc gốc (phạm vi ban đầu: checkout + phiên ca), và [offline-first-roadmap.md](offline-first-roadmap.md) cho kế hoạch đầu việc mở rộng offline-first ra toàn bộ ứng dụng.

Ngày đánh giá: 2026-08-04.

## Nền tảng offline hiện có

- `artifacts/pos-app/src/lib/offline/` — hạ tầng offline phía client: `checkout.ts`, `products.ts`, `shift.ts`, `shift-session.ts`, `status.ts` (`useOfflineStatus`/`useSyncWorker`), `logout.ts`.
- `@workspace/local-db` (`lib/local-db/src/`) — Dexie/IndexedDB, chỉ có các bảng: `products` (cache danh mục), `pendingOrders`, `syncMeta`, `shiftSession`, `shiftOrders`, `salesStaff`. **Đây là giới hạn cứng** cho những gì có thể hoạt động offline — ngoài phạm vi này không có gì được lưu local.
- `@workspace/sync` (`lib/sync/src/`) — kéo catalog, đẩy đơn pending, kéo phiên ca hiện tại + nhân viên bán hàng active + đơn trong ca.
- VitePWA `runtimeCaching` (`artifacts/pos-app/vite.config.ts`, NetworkFirst trên `/api/*` trừ `/api/auth/login`, cache 5 phút) — **chỉ cache tài nguyên/response cuối cùng**, không phải data layer offline thật sự, không mở rộng khả năng offline cho các trang network-only bên dưới.

## ✅ Đã offline-first hoàn chỉnh

| Tính năng | Cơ chế | Bằng chứng |
|---|---|---|
| Tạo đơn hàng (checkout) tại POS | Ghi `pendingOrders` local, trừ tồn kho local, tự sync khi có mạng | `pos.tsx:850-901`, `lib/offline/checkout.ts:41-76` |
| Danh mục sản phẩm hiển thị trong POS | Cache-first, fallback khi mất mạng | `lib/offline/products.ts` (`usePosProducts`, `resolvePosProducts`) |
| Mở ca làm việc (shift session) | Ghi cache local, không cần mạng | `lib/offline/shift-session.ts:20-39` (`openOfflineShiftSession`) |
| Đăng nhập lại tài khoản đã lưu trên máy | Đọc localStorage, không gọi API | `session-cache.ts:92-98` (`switchToSavedAccount`) |
| Duy trì phiên đăng nhập khi rớt mạng giữa chừng | JWT cache + decode phía client | `session-cache.ts:104-136`, `use-session-user.ts:12-35` |
| Đăng xuất (trừ phần đóng ca) | Xoá session local ngay, không phụ thuộc mạng | `app-layout.tsx:114-126` |
| Xem lại đơn trong ca hiện tại (chỉ xem) | Đọc cache `shiftOrders`, read-only | `components/OfflineShiftOrdersList.tsx`, `lib/offline/shift.ts:37-49` |

## ⚠️ Offline-first một phần (có lỗ hổng)

| Tính năng | Vấn đề | Dự kiến cần sửa |
|---|---|---|
| **Đóng ca khi logout offline** | `endCurrentShiftSession()` gọi API, lỗi bị **nuốt âm thầm** (`try/catch` best-effort) — ca vẫn "mở" trên server dù máy đã logout local | Thêm bảng cache "pending shift close" (tương tự `pendingOrders`); đóng ca local ngay, đẩy trạng thái lên server lúc sync — cùng pattern với đơn hàng offline. File liên quan: `lib/sales-api.ts:67-76`, `lib/offline/logout.ts:4-7` |
| **Hủy đơn / duyệt hủy / hoàn tác hủy** (trong lịch sử đơn tại POS) | Gọi API trực tiếp, không có nhánh offline | Thêm bảng `pendingOrderActions` (loại action: cancel/approve/reject), áp dụng optimistic UI local, đồng bộ khi có mạng, xử lý xung đột nếu đơn đã bị máy khác sửa trước. File: `lib/cancel-order.ts:34-42`, `components/OrdersPanel.tsx:141,305-323` |
| **Xuất/sửa hoá đơn VAT tại POS** | Gọi API trực tiếp, không cache | Có thể thêm queue tương tự, nhưng **cần cân nhắc pháp lý**: phát hành hóa đơn VAT thường cần xác thực real-time (mã số thuế, cổng thuế) — không nên cho phép hoàn toàn offline. File: `components/EditInvoiceDialog.tsx:134,147,187` |
| **Xuất báo cáo Excel (trang Reports)** | Chỉ chặn nút bấm khi offline, không có gì thực sự offline | Không có dữ liệu local để export; muốn hỗ trợ cần cache kết quả báo cáo gần nhất + nhãn "dữ liệu cũ lúc X". File: `pages/reports.tsx:434,585-593` |

## ❌ Hoàn toàn phụ thuộc mạng (network-only)

| Trang / tính năng | Ghi chú |
|---|---|
| Dashboard (`/`) | Biểu đồ doanh thu, sản phẩm bán chạy — toàn bộ query API (`useGetDashboard`, `useGetRevenueChart`, `useGetTopProducts`) |
| Products (`/products`) — CRUD sản phẩm | Khác với danh mục hiển thị trong POS (đã cache); đây là trang thêm/sửa/xoá sản phẩm gốc |
| Inventory (`/inventory`) | Điều chỉnh tồn kho |
| Orders (`/orders`) — danh sách đơn toàn cửa hàng | Khác với lịch sử đơn trong ca tại POS (mục đã offline ở trên) |
| VAT Invoices (`/vat-invoices`) | Trang quản lý hóa đơn VAT tổng |
| Statistics (`/statistics`) | Thống kê tổng hợp |
| Staff (`/staff`), Sales Staff (`/sales-staff`) | Quản lý nhân viên / nhân viên bán hàng |
| Stock Requests (`/stock-requests`) | Yêu cầu chuyển kho giữa các chi nhánh |
| Chain Dashboard, Chain (`/chain-dashboard`, `/chain`) | Bảng điều khiển chuỗi cửa hàng đa chi nhánh |
| Đăng nhập bằng tài khoản **mới** (chưa từng đăng nhập trên máy) | Bắt buộc có mạng để lấy JWT — hệ thống đã chủ động chặn + báo rõ (`login.tsx:80,131-139,213,246`), đây là giới hạn hợp lý, không phải lỗi |

## Bản đồ nơi `isOfflineMode`/`useOfflineStatus` được dùng

Chỉ những file sau thực sự có nhánh xử lý theo trạng thái offline; mọi trang khác trong `pages/*` và `components/*` **không biết gì** về trạng thái mạng:

- `lib/offline/status.ts` (định nghĩa)
- `lib/offline/products.ts`, `shift-session.ts`
- `pages/pos.tsx`, `pages/login.tsx`, `pages/reports.tsx` (chỉ chặn nút export)
- `components/ShiftSessionBar.tsx`, `PosOrderHistoryDialog.tsx`, `OfflineShiftOrdersList.tsx`, `OfflineStatusBanner.tsx`, `SyncBootstrap.tsx`

## Khuyến nghị ưu tiên triển khai

Không phải mọi mục ❌ đều nên/cần offline hóa — rủi ro xung đột dữ liệu và giá trị mang lại khác nhau rất nhiều:

- **Nên ưu tiên** (rủi ro thấp, giá trị cao vì diễn ra ngay tại quầy bán hàng đang offline): đóng ca offline, hủy đơn offline, đổi phương thức thanh toán offline — cùng nằm trên màn hình POS.
- **Cân nhắc kỹ trước khi làm offline**: sửa hóa đơn VAT (ràng buộc pháp lý), điều chỉnh tồn kho/sửa giá sản phẩm (rủi ro 2 máy sửa đè giá cùng lúc), yêu cầu chuyển kho giữa chi nhánh (liên quan 2 cửa hàng, xung đột phức tạp hơn đơn hàng vốn chỉ "thêm mới" chứ không "sửa đè").
- **Không nên làm offline**: các trang quản trị tổng hợp (Dashboard, Statistics, Chain Dashboard, Staff CRUD) — bản chất là tổng hợp dữ liệu real-time từ server; "offline" khả thi nhất ở đây chỉ là cache-and-show-stale, không thể tạo/sửa thật sự offline mà không rủi ro.
