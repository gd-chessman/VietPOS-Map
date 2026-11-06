# Thư viện: `shop-vat-settings.ts`

**Mô tả:** [Kiến trúc / dùng chung] shop-vat-settings.ts — isVatInvoicePublicEnabledForShop.

**Chủ đề:** [Kiến trúc / dùng chung](../../chuyen-de/kien-truc-he-thong/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/shop-vat-settings.ts` · **Quy mô:** ~11 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (1)

- `isVatInvoicePublicEnabledForShop`

## Import cơ sở dữ liệu

- `import { db, shopsTable } from "@workspace/db";`

## Trích mã (tham khảo)

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

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Kiến trúc / dùng chung](../../chuyen-de/kien-truc-he-thong/)
