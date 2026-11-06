# Thư viện: `payment-revenue.ts`

**Mô tả:** [POS & đơn hàng] payment-revenue.ts — emptyPaymentRevenue, addOrderPaymentRevenue, sumOrdersPaymentRevenue.

**Chủ đề:** [POS & đơn hàng](../../chuyen-de/pos-va-don-hang/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/payment-revenue.ts` · **Quy mô:** ~31 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (3)

- `emptyPaymentRevenue`
- `addOrderPaymentRevenue`
- `sumOrdersPaymentRevenue`

## Import cơ sở dữ liệu

- `} from "@workspace/db";`

## Trích mã (tham khảo)

```typescript
import {
  resolveOrderPayments,
  type OrderPaymentSplit,
  type PaymentMethodCode,
} from "@workspace/db";

export type PaymentRevenueTotals = Record<PaymentMethodCode, number>;

export function emptyPaymentRevenue(): PaymentRevenueTotals {
  return { cash: 0, card: 0, transfer: 0 };
}

export function addOrderPaymentRevenue(
  totals: PaymentRevenueTotals,
  order: { paymentMethod?: string | null; payments?: unknown; totalAmount: number | string },
): void {
  const total = typeof order.totalAmount === "number" ? order.totalAmount : parseFloat(String(order.totalAmount));
  const splits = resolveOrderPayments(order.payments, order.paymentMethod, total);
  for (const s of splits) totals[s.method] += s.amount;
}

export function sumOrdersPaymentRevenue(
  orders: Array<{ paymentMethod?: string | null; payments?: unknown; totalAmount: number | string }>,
): PaymentRevenueTotals {
  const totals = emptyPaymentRevenue();
  for (const o of orders) addOrderPaymentRevenue(totals, o);
  return totals;
}

export type { OrderPaymentSplit };
```

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub POS & đơn hàng](../../chuyen-de/pos-va-don-hang/)
