# Lib: `product-supplier.ts`

**Mô tả:** Logic backend product-supplier.ts (~200 dòng) — export: parseSupplierImportStatus, findSupplierByName, resolveProductSupplier, syncProductManufacturerFromSupplier.

**Source Shop:** `artifacts/api-server/src/lib/product-supplier.ts`

**Độ lớn:** ~200 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (4 symbol)

- `parseSupplierImportStatus`
- `findSupplierByName`
- `resolveProductSupplier`
- `syncProductManufacturerFromSupplier`

## Import DB / schema

- `import { db, productsTable, suppliersTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { db, productsTable, suppliersTable } from "@workspace/db";
import { and, eq, sql } from "drizzle-orm";

type DbLike = Pick<typeof db, "select" | "insert" | "update">;

export type ResolvedProductSupplier = {
  supplierId: number | null;
  manufacturer: string | null;
};

/** Chi tiết NCC từ import Excel (không gồm ghi chú). */
export type SupplierImportDetails = {
  phone?: string;
  email?: string;
  address?: string;
  taxCode?: string;
  contactPerson?: string;
  status?: "active" | "inactive";
};

export function parseSupplierImportStatus(v: unknown): "active" | "inactive" | undefined {
  const s = String(v ?? "").trim().toLowerCase();
  if (!s) return undefined;
  if (
    s === "inactive" ||
    s.includes("ngừng") ||
    s.includes("ngung") ||
    s.includes("dừng") ||
    s.includes("dung")
  ) {
    return "inactive";
  }
  if (
    s === "active" ||
    s.includes("hợp tác") ||
```
