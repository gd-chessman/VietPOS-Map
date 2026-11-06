# Lib: `payment-revenue.ts`

**Mô tả:** Logic backend payment-revenue.ts (~31 dòng) — export: emptyPaymentRevenue, addOrderPaymentRevenue, sumOrdersPaymentRevenue.

**Source Shop:** `artifacts/api-server/src/lib/payment-revenue.ts`

**Độ lớn:** ~31 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (3 symbol)

- `emptyPaymentRevenue`
- `addOrderPaymentRevenue`
- `sumOrdersPaymentRevenue`

## Import DB / schema

- `} from "@workspace/db";`

## Xem trước đầu file

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
