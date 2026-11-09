# Chuỗi và nhiều cửa hàng

**Mô tả:** Tổ chức, shop, kho, điều chuyển, dashboard chuỗi.

**Về trang chủ Map:** [README.md](../../README.md) · [Hướng dẫn đọc](../../huong-dan-doc/)

Một **organization** nhiều **shop**; hub shop cho HĐ đầu vào.

## 1. Luồng nghiệp vụ (đọc trước)

- [09-chuoi-va-da-chi-nhanh](../../nghiep-vu/09-chuoi-va-da-chi-nhanh/) — Organization, nhiều shop, kho trung tâm, dashboard chuỗi và heartbeat.

## 2. Màn hình (giao diện)

- [chuoi-cua-hang](../../trang/chuoi-cua-hang/) — Sửa tổ chức: shop, Viettel, CQT, Trợ lý AI, URL feedback.
- [bang-dieu-khiem-chuoi](../../trang/bang-dieu-khiem-chuoi/) — Dashboard tổng hợp chuỗi cửa hàng theo quyền.
- [khoa-api-chuoi](../../trang/khoa-api-chuoi/) — Tạo API key shop cho widget và thiết bị ESP32.

## 3. Module API

- [chuoi-api](../../module-api/chuoi-api/) — Tổ chức, shop, kho, điều chuyển hàng.
- [bang-dieu-khiem-api](../../module-api/bang-dieu-khiem-api/) — Số liệu tổng quan: doanh thu, đơn, tồn thấp.
- [khoa-api-cua-hang](../../module-api/khoa-api-cua-hang/) — API key shop (widget, ESP32).

## 4. Bảng dữ liệu (schema)

- [to-chuc](../../co-so-du-lieu/to-chuc/) — Drizzle organizations.ts — 1 bảng, 39 cột (organizations).
- [kho-hang](../../co-so-du-lieu/kho-hang/) — Drizzle warehouses.ts — 1 bảng, 7 cột (warehouses).
- [chuyen-kho](../../co-so-du-lieu/chuyen-kho/) — Drizzle stockTransfers.ts — 2 bảng, 17 cột (stock_transfers, stock_transfer_items).

## 5. Thư viện backend (một số file quan trọng)

Tra cứu đủ: [README.md](../../chi-muc/thu-vien-backend/)

- [chain-shop-scope](../../thu-vien/chain-shop-scope/) — [Chuỗi cửa hàng] chain-shop-scope.ts — parseOptionalShopId, resolveChainShopScope…
- [dashboard-period](../../thu-vien/dashboard-period/) — [Chuỗi cửa hàng] dashboard-period.ts — resolveDashboardPeriodRange…
- [dashboard-visitor-stats](../../thu-vien/dashboard-visitor-stats/) — [Chuỗi cửa hàng] dashboard-visitor-stats.ts — visitDateString, visitorsPerBuyer…
- [shop-presence-sweep](../../thu-vien/shop-presence-sweep/) — [Chuỗi cửa hàng] shop-presence-sweep.ts — startShopPresenceSweepScheduler.
- [shop-presence](../../thu-vien/shop-presence/) — [Chuỗi cửa hàng] shop-presence.ts — SHOP_PRESENCE_TIMEOUT_MS, isShopOnline…

---

*Sinh tự động — `python3 docs/gen.py`*
