# VietPOS-Map — Bản đồ tài liệu

**Mô tả:** Trang chủ Map — mỗi chủ đề nằm trong **một thư mục**, file **`README.md`**.

**Cửa vào (index.html):** [../index.html](../index.html)
**Bản đồ hình (ASCII + Mermaid):** [README.md](ban-do-kien-truc/README.md)

1. [Hướng dẫn đọc (3 bước)](huong-dan-doc/README.md)
2. [Kiến trúc — Mermaid](chuyen-de/kien-truc-he-thong/README.md)

**Tạo lại:** `python3 docs/gen.py`

---

## Chủ đề (chuyen-de)

Mỗi thư mục gom link **nghiệp vụ → màn hình → API → schema → lib** theo một việc.

- [Kiến trúc hệ thống](chuyen-de/kien-truc-he-thong/README.md) — Sơ đồ tổng thể: pos-app, api-server, Postgres, offline, cloud-sync — đọc đầu tiên.
- [Đăng nhập và phiên làm việc](chuyen-de/dang-nhap-va-phien/README.md) — JWT, shop đang chọn, hub shop, quyền menu.
- [POS và đơn hàng](chuyen-de/pos-va-don-hang/README.md) — Quầy bán, giỏ hàng, thanh toán, ca làm việc, hủy đơn.
- [Sản phẩm và tồn kho](chuyen-de/san-pham-va-kho/README.md) — Danh mục SP, tồn shop, phiếu nhập/xuất, PO.
- [Hóa đơn đầu vào (VAT mua vào)](chuyen-de/hoa-don-dau-vao/README.md) — Import PDF/Excel, kéo CQT, MST lọc, ghép hàng, nhập kho.
- [Hóa đơn bán ra (Viettel)](chuyen-de/hoa-don-ban-ra/README.md) — Phát hành HĐ VAT từ POS, tra cứu, form công khai.
- [Chuỗi và nhiều cửa hàng](chuyen-de/chuoi-cua-hang/README.md) — Tổ chức, shop, kho, điều chuyển, dashboard chuỗi.
- [An ninh và chặn truy cập](chuyen-de/an-ninh-truy-cap/README.md) — Chặn IP/thiết bị, quan sát truy cập, super_admin.
- [Offline và đồng bộ](chuyen-de/offline-dong-bo/README.md) — IndexedDB, checkout offline, API sync.
- [Trợ lý AI, widget, đếm khách](chuyen-de/tro-ly-widget/README.md) — Agent chat, widget Android, ESP32 visitor-counts.

---

## Mười hai chương nghiệp vụ

1. [01-dang-nhap-va-shop-context](nghiep-vu/01-dang-nhap-va-shop-context/README.md) — Đăng nhập, JWT gắn shop/role, hub shop và ngữ cảnh vận hành API.
2. [02-pos-ban-hang](nghiep-vu/02-pos-ban-hang/README.md) — Luồng POS: ca làm việc, giỏ hàng, thanh toán, in bill, hủy đơn và audit.
3. [03-san-pham-va-ton](nghiep-vu/03-san-pham-va-ton/README.md) — Quản lý sản phẩm, import Excel, tồn shop và điều chỉnh inventory.
4. [04-phieu-nhap-xuat-chuyen-kho](nghiep-vu/04-phieu-nhap-xuat-chuyen-kho/README.md) — Phiếu stock-request, chuyển kho chuỗi, PO và liên kết nhập hàng.
5. [05-hoa-don-vat-xuat](nghiep-vu/05-hoa-don-vat-xuat/README.md) — Hóa đơn VAT bán ra qua Viettel SInvoice và cấu hình org.
6. [06-hoa-don-dau-vao-tong-quan](nghiep-vu/06-hoa-don-dau-vao-tong-quan/README.md) — Vòng đời HĐ mua vào: import, ghép SP, nhập kho, trạng thái stockStatus.
7. [07-hd-dau-vao-mst-loc](nghiep-vu/07-hd-dau-vao-mst-loc/README.md) — MST lọc tự archive HĐ; tab Khác / Lưu trữ / Đang dùng; modal trên trang HĐ đầu vào.
8. [08-hd-dau-vao-cqt-sync](nghiep-vu/08-hd-dau-vao-cqt-sync/README.md) — Kéo HĐ từ CQT (GDT direct): captcha, sync-tax, map XML vào DB.
9. [09-chuoi-va-da-chi-nhanh](nghiep-vu/09-chuoi-va-da-chi-nhanh/README.md) — Organization, nhiều shop, kho trung tâm, dashboard chuỗi và heartbeat.
10. [10-truy-cap-an-ninh](nghiep-vu/10-truy-cap-an-ninh/README.md) — Chặn IP/thiết bị, quan sát truy cập và RBAC liên quan.
11. [11-offline-va-sync-client](nghiep-vu/11-offline-va-sync-client/README.md) — IndexedDB local-db, checkout offline, pull/push sync với server.
12. [12-widget-va-dem-khach](nghiep-vu/12-widget-va-dem-khach/README.md) — App widget Android, ESP32 visitor-counts và shop API keys.

---

## Hệ thống (chi tiết kỹ thuật)

- [01-kien-truc-runtime](he-thong/01-kien-truc-runtime/README.md) — Sơ đồ runtime: client React → Express API → PostgreSQL; tùy chọn cloud-sync Railway.
- [02-workspace-luu-niem](he-thong/02-workspace-luu-niem/README.md) — Các repo trong LuuNiem (Shop, Widget, Map, ESP32, HDSD) và vai trò từng thư mục.
- [03-monorepo-packages](he-thong/03-monorepo-packages/README.md) — Cấu trúc pnpm workspace: artifacts, lib, scripts trong Shop-Manager.
- [04-docker-va-cloud-sync](he-thong/04-docker-va-cloud-sync/README.md) — Docker Compose local, biến CLOUD_DATABASE_URL, worker cloud-sync và Trợ lý AI.

---

## Tra cứu kỹ thuật (chi-muc)

Dùng **sau** hub chủ đề — danh sách dài, không đọc từ đầu đến cuối.

| Chỉ mục | Nội dung |
|---------|----------|
| [danh-sach-api](chi-muc/danh-sach-api/README.md) | 39 module API |
| [danh-sach-trang](chi-muc/danh-sach-trang/README.md) | 36 trang UI |
| [thu-vien-backend](chi-muc/thu-vien-backend/README.md) | 99 file lib |
| [co-so-du-lieu](chi-muc/co-so-du-lieu/README.md) | 43 schema |
| [endpoint-http](chi-muc/endpoint-http/README.md) | 235 endpoint HTTP |

---

## Tài liệu tham chiếu gốc Shop (tiếng Anh)

- [audit-offline](tham-chieu/audit-offline/README.md) — Tài liệu tham chiếu gốc Shop docs/offline-first-audit.md…
- [chay-local](tham-chieu/chay-local/README.md) — Tài liệu tham chiếu gốc Shop docs/running-local.md…
- [chu-thich-ma](tham-chieu/chu-thich-ma/README.md) — Tài liệu tham chiếu gốc Shop docs/code-annotations.md…
- [co-so-du-lieu-goc](tham-chieu/co-so-du-lieu-goc/README.md) — Tài liệu tham chiếu gốc Shop docs/database.md — Database schema overview (Postgres + Drizzle)…
- [code-tour-api](tham-chieu/code-tour-api/README.md) — Tài liệu tham chiếu gốc Shop docs/code-tour/api-server.md — Code tour…
- [code-tour-db](tham-chieu/code-tour-db/README.md) — Tài liệu tham chiếu gốc Shop docs/code-tour/db.md — Code tour…
- [code-tour-pos](tham-chieu/code-tour-pos/README.md) — Tài liệu tham chiếu gốc Shop docs/code-tour/pos-app.md — Code tour…
- [danh-sach-api-goc](tham-chieu/danh-sach-api-goc/README.md) — Tài liệu tham chiếu gốc Shop docs/api-routes.md — API routes (nội dung dưới thường tiếng Anh).
- [docker-may-chu](tham-chieu/docker-may-chu/README.md) — Tài liệu tham chiếu gốc Shop docs/docker-may-chu.md…
- [kien-truc](tham-chieu/kien-truc/README.md) — Tài liệu tham chiếu gốc Shop docs/architecture.md — Architecture (nội dung dưới thường tiếng Anh).
- [lo-trinh-offline](tham-chieu/lo-trinh-offline/README.md) — Tài liệu tham chiếu gốc Shop docs/offline-first-roadmap.md…
- [luong-nghiep-vu-goc](tham-chieu/luong-nghiep-vu-goc/README.md) — Tài liệu tham chiếu gốc Shop docs/business-flows.md…
- [offline-first](tham-chieu/offline-first/README.md) — Tài liệu tham chiếu gốc Shop docs/offline-first.md…
- [phan-quyen-rbac](tham-chieu/phan-quyen-rbac/README.md) — Tài liệu tham chiếu gốc Shop docs/rbac.md — RBAC (roles & permissions) (nội dung dưới thường…
- [truy-cap-cong-khai](tham-chieu/truy-cap-cong-khai/README.md) — Tài liệu tham chiếu gốc Shop docs/public-access.md…

---

## Thống kê

- Hub chủ đề: 10
- README sinh tự động: ~265
- Endpoint HTTP: 235

