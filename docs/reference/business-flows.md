<!-- Mirror: Shop-Manager-System-Offline/docs/business-flows.md -->

# Business flows (how the system operates)

**Mô tả:** Bản mirror doc Shop docs/business-flows.md — Business flows (how the system operates).

This document describes the current business workflows supported by the system (as implemented).

## 1) Login & working context

- Users login with email/password.
- Each user belongs to a **shop** (`shop_id`).
- Most operational workflows (products, POS orders, inventory, staff list) are scoped to the user’s `shop_id`.

## 2) POS sales flow

**Goal:** create a completed retail order and decrement stock for the shop.

High-level flow:

1. Cashier opens POS screen.
2. Cashier searches/selects products and builds a cart.
3. Cashier confirms payment method (cash/card/transfer).
4. System creates an order:
   - `orders.shop_id = current shop`
   - `orders.user_id = cashier`
   - `orders.status = completed`
   - order items inserted to `order_items`
5. Inventory is decremented for the shop-level inventory row (`inventory.shop_id = shop`, `warehouse_id` NULL).
6. Receipt can be displayed/printed; reprints may be tracked in `reprint_logs`.

### Order cancelation workflow

- Non-admin roles can submit a **cancel request** (requires a note).
- Admin-equivalent roles can approve/reject cancel requests.
- When a cancel is finalized, inventory is restored back to the shop stock.

## 3) Product lifecycle

Supported operations:

- Create product (with price and cost price)
- Update product fields (name, prices, internal codes, thumbnail, quantity adjustments)
- Soft-discontinue product (mark as `discontinued`)
- Reactivate discontinued product
- Import products from Excel (bulk): tạo mới; **trùng Mã nội bộ** (cùng shop) → **cộng tồn** (không đổi giá); SP ngừng KD được kích hoạt lại khi cộng tồn

Notes:

- Product records are scoped by `shop_id`.
- Cost price may be hidden from certain roles in API responses.

## 4) Inventory management (shop-level)

Supported operations:

- List shop inventory and quantities.
- Adjust quantity for a product at the shop level.

## 5) Stock requests (import/export requests)

These represent internal requests to bring stock in / take stock out, with a basic approval lifecycle.

Typical flow:

1. A user creates a request (type import/export) with line items.
2. Authorized roles approve or reject (optional note on reject).
3. Completing the request updates inventory accordingly.

## 6) Chain / multi-branch operations

Supported operations:

- Manage organizations (chain/company).
- Manage shops (branches) under an organization.
- Create shop admin users when setting up new shops.
- Manage warehouses (store backroom, central, transit).
- Adjust warehouse stock and track movements.
- Create and manage warehouse transfers (draft → approve → ship → receive).

The goal is to support stock distribution across multiple shops and central warehouses.

