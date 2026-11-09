# Mười hai chương nghiệp vụ

**Mô tả:** Luồng nghiệp vụ POS theo chương.

- [01 dang nhap va shop context](01-dang-nhap-va-shop-context/) — Đăng nhập, JWT gắn shop/role, hub shop và ngữ cảnh vận hành API.
- [02 pos ban hang](02-pos-ban-hang/) — Luồng POS: ca làm việc, giỏ hàng, thanh toán, in bill, hủy đơn và audit.
- [03 san pham va ton](03-san-pham-va-ton/) — Quản lý sản phẩm, import Excel, tồn shop và điều chỉnh inventory.
- [04 phieu nhap xuat chuyen kho](04-phieu-nhap-xuat-chuyen-kho/) — Phiếu stock-request, chuyển kho chuỗi, PO và liên kết nhập hàng.
- [05 hoa don vat xuat](05-hoa-don-vat-xuat/) — Hóa đơn VAT bán ra qua Viettel SInvoice và cấu hình org.
- [06 hoa don dau vao tong quan](06-hoa-don-dau-vao-tong-quan/) — Vòng đời HĐ mua vào: import, ghép SP, nhập kho, trạng thái stockStatus.
- [07 hd dau vao mst loc](07-hd-dau-vao-mst-loc/) — MST lọc tự archive HĐ; tab Khác / Lưu trữ / Đang dùng; modal trên trang HĐ đầu vào.
- [08 hd dau vao cqt sync](08-hd-dau-vao-cqt-sync/) — Kéo HĐ từ CQT (GDT direct): captcha, sync-tax, map XML vào DB.
- [09 chuoi va da chi nhanh](09-chuoi-va-da-chi-nhanh/) — Organization, nhiều shop, kho trung tâm, dashboard chuỗi và heartbeat.
- [10 truy cap an ninh](10-truy-cap-an-ninh/) — Chặn IP/thiết bị, quan sát truy cập và RBAC liên quan.
- [11 offline va sync client](11-offline-va-sync-client/) — IndexedDB local-db, checkout offline, pull/push sync với server.
- [12 widget va dem khach](12-widget-va-dem-khach/) — App widget Android, ESP32 visitor-counts và shop API keys.
