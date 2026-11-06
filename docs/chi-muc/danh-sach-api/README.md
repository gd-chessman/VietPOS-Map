# Chỉ mục module API

**Mô tả:** Danh sách 39 module routes — dùng khi đã biết cần sửa API nào.

← [Bản đồ chính](../../README.md) · [Hướng dẫn đọc](../../huong-dan-doc/)

---

1. [audit-gio-hang-pos](../../module-api/audit-gio-hang-pos/) — Module API pos-cart-audit.ts — 3 endpoint. Audit thao tác giỏ hàng POS.
2. [bang-dieu-khiem-api](../../module-api/bang-dieu-khiem-api/) — Module API dashboard.ts — 17 endpoint. Số liệu tổng quan: doanh thu, đơn, tồn thấp.
3. [bao-cao-api](../../module-api/bao-cao-api/) — Module API reports.ts — 4 endpoint. Báo cáo nhân viên, in lại bill.
4. [bao-cao-audit-dat-hang](../../module-api/bao-cao-audit-dat-hang/) — Module API purchase-order-audit-reports.ts — 2 endpoint. Báo cáo audit phiếu mua.
5. [bao-cao-audit-don](../../module-api/bao-cao-audit-don/) — Module API order-audit-reports.ts — 2 endpoint. Báo cáo audit đơn hàng.
6. [bao-cao-audit-phieu-kho](../../module-api/bao-cao-audit-phieu-kho/) — Module API stock-request-audit-reports.ts — 2 endpoint. Báo cáo audit phiếu nhập/xuất.
7. [bao-cao-audit-san-pham](../../module-api/bao-cao-audit-san-pham/) — Module API product-audit-reports.ts — 2 endpoint. Báo cáo thay đổi sản phẩm.
8. [ca-lam-viec](../../module-api/ca-lam-viec/) — Module API shift-sessions.ts — 3 endpoint. Ca làm việc mở/đóng.
9. [cau-hinh-thong-bao-api](../../module-api/cau-hinh-thong-bao-api/) — Module API notification-settings.ts — 2 endpoint. Cấu hình thông báo platform/org.
10. [cau-hinh-viettel](../../module-api/cau-hinh-viettel/) — Module API org-viettel-settings.ts — 2 endpoint. Cấu hình Viettel SInvoice theo org.
11. [chan-ip-api](../../module-api/chan-ip-api/) — Module API blocked-ips.ts — 3 endpoint. Danh sách IP bị chặn toàn cục trên mọi request /api/*. - Quyền: requireAuth + role super_…
12. [chan-thiet-bi-api](../../module-api/chan-thiet-bi-api/) — Module API blocked-devices.ts — 3 endpoint. Danh sách Device ID (header client) bị chặn mọi /api/*. - Quyền: super_admin (giống b…
13. [chuoi-api](../../module-api/chuoi-api/) — Module API chain.ts — 29 endpoint. Tổ chức, shop, kho, điều chuyển (transfers). Cấu hình org (Viettel, CQT, feedback URL, agent L…
14. [cong-cqt](../../module-api/cong-cqt/) — Module API org-gdt-portal.ts — 4 endpoint. Session CQT trực tiếp (captcha, connect) — dùng chung org với HĐ đầu vào.
15. [cua-hang](../../module-api/cua-hang/) — Module API shops.ts — 3 endpoint. Danh sách shop user được truy cập.
16. [danh-muc-san-pham](../../module-api/danh-muc-san-pham/) — Module API product-categories.ts — 3 endpoint. Danh mục sản phẩm.
17. [dat-hang](../../module-api/dat-hang/) — Module API purchase-orders.ts — 9 endpoint. Phiếu đặt mua (PO).
18. [don-hang-api](../../module-api/don-hang-api/) — Module API orders.ts — 21 endpoint. Đơn hàng POS: tạo, hủy, duyệt hủy, in lại, thông báo reprint. Gắn ca (shift-sessions), audit…
19. [dong-bo-du-lieu](../../module-api/dong-bo-du-lieu/) — Module API sync.ts — 2 endpoint. API đồng bộ client (kéo/đẩy) cho IndexedDB offline.
20. [hoa-don-dau-vao](../../module-api/hoa-don-dau-vao/) — Module API vat-inbound.ts — 28 endpoint. Module lớn nhất về HĐ mua vào VAT: import PDF/Excel, kéo CQT/Viettel, ghép SP, nhập kho,…
21. [hoa-don-vat-cong-khai](../../module-api/hoa-don-vat-cong-khai/) — Module API public-vat-invoice.ts — 3 endpoint. API/form HĐ VAT công khai.
22. [khach-vang-lai](../../module-api/khach-vang-lai/) — Module API walk-in-customers.ts — 2 endpoint. Khách vãng lai (walk-in).
23. [khoa-api-cua-hang](../../module-api/khoa-api-cua-hang/) — Module API shop-api-keys.ts — 8 endpoint. API key cho widget / thiết bị (ESP32 visitor-counts). Giao diện: pages/chain-api-keys.t…
24. [kiem-tra-suc-khoe](../../module-api/kiem-tra-suc-khoe/) — Module API health.ts — 1 endpoint. Kiểm tra service còn sống (healthz).
25. [media-api](../../module-api/media-api/) — Module API media.ts — 1 endpoint. Upload và quản lý file media.
26. [nha-cung-cap-api](../../module-api/nha-cung-cap-api/) — Module API suppliers.ts — 4 endpoint. Nhà cung cấp.
27. [nhan-vien-ban-api](../../module-api/nhan-vien-ban-api/) — Module API sales-staff.ts — 4 endpoint. Nhân viên bán hàng gắn quầy.
28. [nhan-vien](../../module-api/nhan-vien/) — Module API staff.ts — 7 endpoint. Quản lý tài khoản nhân viên (admin).
29. [phan-hoi-api](../../module-api/phan-hoi-api/) — Module API feedback.ts — 5 endpoint. Phản hồi khách và form công khai.
30. [phieu-nhap-xuat](../../module-api/phieu-nhap-xuat/) — Module API stock-requests.ts — 14 endpoint. Phiếu yêu cầu nhập/xuất nội bộ: tạo → duyệt → hoàn tất → cập nhật tồn. Giao diện: pag…
31. [quan-sat-truy-cap](../../module-api/quan-sat-truy-cap/) — Module API access-observations.ts — 1 endpoint. Tổng hợp cặp (deviceId, IP) đã gọi API — lưu in-memory (TTL giờ, xem accessObserv…
32. [san-pham-api](../../module-api/san-pham-api/) — Module API products.ts — 11 endpoint. Quản lý sản phẩm (thêm/sửa/xóa), import Excel, biến thể, ẩn/hiện SP, giá/giá vốn theo role.…
33. [su-kien-he-thong](../../module-api/su-kien-he-thong/) — Module API system-events.ts — 1 endpoint. Sự kiện / lỗi hệ thống.
34. [thong-bao](../../module-api/thong-bao/) — Module API notifications.ts — 2 endpoint. Thông báo in-app cho user.
35. [thong-ke-api](../../module-api/thong-ke-api/) — Module API statistics.ts — 6 endpoint. Thống kê bán theo sản phẩm.
36. [ton-kho-api](../../module-api/ton-kho-api/) — Module API inventory.ts — 2 endpoint. Tồn kho cấp shop (số lượng POS).
37. [tro-ly-ai-api](../../module-api/tro-ly-ai-api/) — Module API agent.ts — 10 endpoint. Trợ lý AI: chat, thông tin hệ thống (DB, đồng bộ cloud, shop online), cấp quyền agent_assistan…
38. [widget-quay](../../module-api/widget-quay/) — Module API widget.ts — 1 endpoint. API phục vụ app Android widget: thống kê quầy (JWT / shop context). Repo: VietPOS-Widget/.
39. [xac-thuc](../../module-api/xac-thuc/) — Module API auth.ts — 8 endpoint. Đăng nhập, JWT, PIN, phiên người dùng.
