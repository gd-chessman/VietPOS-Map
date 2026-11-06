# Sản phẩm và tồn kho

**Mô tả:** CRUD sản phẩm, import Excel, tồn shop và điều chỉnh inventory.

- SP scoped **shop_id**; internal_code, vat_name, giá, giá vốn, VAT rate.
- Import Excel: trùng mã nội bộ → **cộng tồn**; có thể kích hoạt lại SP discontinued.
- Tồn shop: bảng `inventory` (`warehouse_id` NULL cho POS).
- Điều chỉnh tồn: PATCH inventory; warehouse riêng cho chuỗi/kho tổng.

**API:** `products.ts`, `inventory.ts`. **UI:** `products.tsx`, `inventory.tsx`.
