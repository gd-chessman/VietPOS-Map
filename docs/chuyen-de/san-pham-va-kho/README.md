# Sản phẩm và tồn kho

**Mô tả:** Danh mục SP, tồn shop, phiếu nhập/xuất, PO.

**Về trang chủ Map:** [README.md](../../README.md) · [Hướng dẫn đọc](../../huong-dan-doc/)

Dữ liệu master + tồn trước khi bán hoặc nhập HĐ.

## 1. Luồng nghiệp vụ (đọc trước)

- [03-san-pham-va-ton](../../nghiep-vu/03-san-pham-va-ton/) — Quản lý sản phẩm, import Excel, tồn shop và điều chỉnh inventory.
- [04-phieu-nhap-xuat-chuyen-kho](../../nghiep-vu/04-phieu-nhap-xuat-chuyen-kho/) — Phiếu stock-request, chuyển kho chuỗi, PO và liên kết nhập hàng.

## 2. Màn hình (giao diện)

- [san-pham](../../trang/san-pham/) — Danh mục sản phẩm, variant, import Excel, giá.
- [ton-kho](../../trang/ton-kho/) — Tồn kho shop, điều chỉnh số lượng, cảnh báo sắp hết.
- [phieu-nhap-xuat](../../trang/phieu-nhap-xuat/) — Phiếu yêu cầu nhập/xuất nội bộ giữa shop.
- [dat-hang](../../trang/dat-hang/) — Phiếu đặt mua (PO) và trạng thái nhận hàng.
- [nha-cung-cap](../../trang/nha-cung-cap/) — Danh mục nhà cung cấp.

## 3. Module API

- [san-pham-api](../../module-api/san-pham-api/) — Sản phẩm: thêm/sửa/xóa, import Excel, biến thể.
- [ton-kho-api](../../module-api/ton-kho-api/) — Tồn kho cấp shop (số lượng POS).
- [phieu-nhap-xuat](../../module-api/phieu-nhap-xuat/) — Phiếu yêu cầu nhập/xuất nội bộ.
- [dat-hang](../../module-api/dat-hang/) — Phiếu đặt mua (PO).
- [nha-cung-cap-api](../../module-api/nha-cung-cap-api/) — Nhà cung cấp.

## 4. Bảng dữ liệu (schema)

- [san-pham-db](../../co-so-du-lieu/san-pham-db/) — Drizzle products.ts — 1 bảng, 21 cột, 1 enum, 4 index (products).
- [ton-kho-db](../../co-so-du-lieu/ton-kho-db/) — Drizzle inventory.ts — 1 bảng, 6 cột, 2 index (inventory).
- [phieu-yeu-cau-kho](../../co-so-du-lieu/phieu-yeu-cau-kho/) — Drizzle stockRequests.ts — 3 bảng, 32 cột (stock_requests, stock_request_logs, stock_request_items).

## 5. Thư viện backend (một số file quan trọng)

Tra cứu đủ: [README.md](../../chi-muc/thu-vien-backend/)

- [inventory-variant](../../thu-vien/inventory-variant/) — [Sản phẩm & kho] inventory-variant.ts — upsertShopStockByProduct…
- [product-audit](../../thu-vien/product-audit/) — [Sản phẩm & kho] product-audit.ts — recordProductAudit, buildProductFieldChanges.
- [product-category](../../thu-vien/product-category/) — [Sản phẩm & kho] product-category.ts — findCategoryByName, resolveProductCategory…
- [product-supplier](../../thu-vien/product-supplier/) — [Sản phẩm & kho] product-supplier.ts — parseSupplierImportStatus, findSupplierByName…
- [product-variants](../../thu-vien/product-variants/) — [Sản phẩm & kho] product-variants.ts — suggestVariantCode, getVariant0…
- [product-vat-name](../../thu-vien/product-vat-name/) — [Sản phẩm & kho] product-vat-name.ts — normalizeVatNameKey…
- [product-vat](../../thu-vien/product-vat/) — [Sản phẩm & kho] product-vat.ts — DEFAULT_UNIT, DEFAULT_VAT_RATE, DEFAULT_TNCN_RATE…
- [vat-inbound-product-code](../../thu-vien/vat-inbound-product-code/) — [Hóa đơn đầu vào] vat-inbound-product-code.ts…
- [weighted-average-cost](../../thu-vien/weighted-average-cost/) — [Sản phẩm & kho] weighted-average-cost.ts — roundMoney2, weightedAverageCost…

---

*Sinh tự động — `python3 docs/gen.py`*
