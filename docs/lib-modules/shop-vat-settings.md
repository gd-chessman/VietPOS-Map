# Lib: `shop-vat-settings.ts`

**Mô tả:** Logic backend shop-vat-settings.ts (~11 dòng) — export: isVatInvoicePublicEnabledForShop.

**Source Shop:** `artifacts/api-server/src/lib/shop-vat-settings.ts`

**Độ lớn:** ~11 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (1 symbol)

- `isVatInvoicePublicEnabledForShop`

## Import DB / schema

- `import { db, shopsTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { db, shopsTable } from "@workspace/db";
import { eq } from "drizzle-orm";

export async function isVatInvoicePublicEnabledForShop(shopId: number): Promise<boolean> {
  const [shop] = await db
    .select({ vatInvoicePublicEnabled: shopsTable.vatInvoicePublicEnabled })
    .from(shopsTable)
    .where(eq(shopsTable.id, shopId));
  return shop?.vatInvoicePublicEnabled !== false;
}
```
