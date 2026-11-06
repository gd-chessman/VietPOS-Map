# Lib: `order-preprint.ts`

**Mô tả:** Logic backend order-preprint.ts (~170 dòng) — export: newInvoicePublicToken, upsertOrderPreprintReservation, loadPreprintForClientOrder, findPreprintByPublicToken.

**Source Shop:** `artifacts/api-server/src/lib/order-preprint.ts`

**Độ lớn:** ~170 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (4 symbol)

- `newInvoicePublicToken`
- `upsertOrderPreprintReservation`
- `loadPreprintForClientOrder`
- `findPreprintByPublicToken`

## Import DB / schema

- `} from "@workspace/db";`

## Xem trước đầu file

```typescript
import {
  db,
  orderPreprintReservationsTable,
  shopsTable,
  type OrderPreprintReservation,
} from "@workspace/db";
import { and, eq } from "drizzle-orm";
import crypto from "node:crypto";
import { formatOrderInvoiceCode } from "./order-invoice-code";
import { resolveShopOrderSequence } from "./order-shop-sequence";
import { isVatInvoicePublicEnabledForShop } from "./shop-vat-settings";

export function newInvoicePublicToken(): string {
  return crypto.randomUUID().replace(/-/g, "");
}

export type UpsertOrderPreprintInput = {
  shopId: number;
  userId: number;
  clientOrderId: string;
  shopSequence?: number | null;
  totalAmount?: number | null;
  clientCreatedAt?: Date | null;
};

export type OrderPreprintResponse = {
  clientOrderId: string;
  shopSequence: number;
  invoiceCode: string;
  invoicePublicToken: string | null;
  invoiceCodeAdjusted: boolean;
  requestedShopSequence: number | null;
};

export async function upsertOrderPreprintReservation(
```
