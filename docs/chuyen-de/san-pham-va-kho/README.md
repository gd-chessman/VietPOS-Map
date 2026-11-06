# Sản phẩm và tồn kho

**Mô tả:** Danh mục SP, tồn shop, phiếu nhập/xuất, PO.

**Về trang chủ Map:** [README.md](../../README.md) · [Hướng dẫn đọc](../../huong-dan-doc/)

Dữ liệu master + tồn trước khi bán hoặc nhập HĐ.

## 1. Luồng nghiệp vụ (đọc trước)

- [03-san-pham-va-ton](../../nghiep-vu/03-san-pham-va-ton/) — Quản lý sản phẩm, import Excel, tồn shop và điều chỉnh inventory.
- [04-phieu-nhap-xuat-chuyen-kho](../../nghiep-vu/04-phieu-nhap-xuat-chuyen-kho/) — Phiếu stock-request, chuyển kho chuỗi, PO và liên kết nhập hàng.

## 2. Màn hình (giao diện)

- [san-pham](../../trang/san-pham/) — Danh mục sản phẩm, variant, import Excel, giá. (URL /products, Products, ~2689 dòng).
- [ton-kho](../../trang/ton-kho/) — Tồn kho shop, điều chỉnh số lượng, cảnh báo sắp hết. (URL /inventory, Inventory, ~1066 dòng).
- [phieu-nhap-xuat](../../trang/phieu-nhap-xuat/) — Phiếu yêu cầu nhập/xuất nội bộ giữa shop. (URL /stock-requests, StockRequestsPage, ~1874 dòng).
- [dat-hang](../../trang/dat-hang/) — Phiếu đặt mua (PO) và trạng thái nhận hàng. (URL /purchase-orders, PurchaseOrdersPage, ~2359 dòng).
- [nha-cung-cap](../../trang/nha-cung-cap/) — Danh mục nhà cung cấp. (URL /suppliers, SuppliersPage, ~593 dòng).

## 3. Module API

- [san-pham-api](../../module-api/san-pham-api/) — Module API products.ts — 11 endpoint. Quản lý sản phẩm (thêm/sửa/xóa), import Excel, biến thể, ẩn/h…
- [ton-kho-api](../../module-api/ton-kho-api/) — Module API inventory.ts — 2 endpoint. Tồn kho cấp shop (số lượng POS).
- [phieu-nhap-xuat](../../module-api/phieu-nhap-xuat/) — Module API stock-requests.ts — 14 endpoint. Phiếu yêu cầu nhập/xuất nội bộ: tạo → duyệt → hoàn tất…
- [dat-hang](../../module-api/dat-hang/) — Module API purchase-orders.ts — 9 endpoint. Phiếu đặt mua (PO).
- [nha-cung-cap-api](../../module-api/nha-cung-cap-api/) — Module API suppliers.ts — 4 endpoint. Nhà cung cấp.

## 4. Bảng dữ liệu (schema)

- [san-pham-db](../../co-so-du-lieu/san-pham-db/) — Drizzle schema products.ts — 21 cột trên 1 bảng Postgres (products).
- [ton-kho-db](../../co-so-du-lieu/ton-kho-db/) — Drizzle schema inventory.ts — 6 cột trên 1 bảng Postgres (inventory).
- [phieu-yeu-cau-kho](../../co-so-du-lieu/phieu-yeu-cau-kho/) — Drizzle schema stockRequests.ts — 32 cột trên 3 bảng Postgres (stock_requests, stock_request_logs,…

## 5. Thư viện backend (một số file quan trọng)

Tra cứu đủ: [README.md](../../chi-muc/thu-vien-backend/)

- [inventory-variant](../../thu-vien/inventory-variant/) — [Sản phẩm & kho] inventory-variant.ts — upsertShopStockByProduct, upsertShopExtraVariantS…
- [product-audit](../../thu-vien/product-audit/) — [Sản phẩm & kho] product-audit.ts — recordProductAudit, buildProductFieldChanges.
- [product-category](../../thu-vien/product-category/) — [Sản phẩm & kho] product-category.ts — findCategoryByName, resolveProductCategory, syncPr…
- [product-supplier](../../thu-vien/product-supplier/) — [Sản phẩm & kho] product-supplier.ts — parseSupplierImportStatus, findSupplierByName, res…
- [product-variants](../../thu-vien/product-variants/) — [Sản phẩm & kho] product-variants.ts — suggestVariantCode, getVariant0, ensureVariantColu…
- [product-vat-name](../../thu-vien/product-vat-name/) — [Sản phẩm & kho] product-vat-name.ts — normalizeVatNameKey, findSupplierVatNameConflict,…
- [product-vat](../../thu-vien/product-vat/) — [Sản phẩm & kho] product-vat.ts — DEFAULT_UNIT, DEFAULT_VAT_RATE, DEFAULT_TNCN_RATE, ALLO…
- [vat-inbound-product-code](../../thu-vien/vat-inbound-product-code/) — [Hóa đơn đầu vào] vat-inbound-product-code.ts — initialsFromVatName, vatLinePriceThousand…
- [weighted-average-cost](../../thu-vien/weighted-average-cost/) — [Sản phẩm & kho] weighted-average-cost.ts — roundMoney2, weightedAverageCost, reverseWeig…

---

*Sinh tự động — `python3 docs/gen.py`*
