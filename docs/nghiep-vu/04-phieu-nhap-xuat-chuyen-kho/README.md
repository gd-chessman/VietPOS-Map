# Phiếu nhập/xuất và chuyển kho

**Mô tả:** Phiếu stock-request, chuyển kho chuỗi, PO và liên kết nhập hàng.

**Stock requests:** CN con xin hàng từ hub — duyệt tại hub; vận chuyển trừ tồn nguồn; nhận cộng đích.

**Transfers (chain):** draft → approve → ship → receive; `inventory_movements` audit.

**Purchase orders:** liên kết HĐ đầu vào khi ghép hàng (không bắt buộc PO riêng cho mọi flow).

**API:** `stock-requests.ts`, `purchase-orders.ts`, `chain.ts` (transfers).
