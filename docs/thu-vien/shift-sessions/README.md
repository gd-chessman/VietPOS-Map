# Thư viện: `shift-sessions.ts`

**Mô tả:** [POS & đơn hàng] shift-sessions.ts — getActiveShiftSession, isShiftSessionRestrictedRole, assertStaffOrderInActiveShiftSession.

**Chủ đề:** [POS & đơn hàng](../../chuyen-de/pos-va-don-hang/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/shift-sessions.ts` · **Quy mô:** ~40 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (3)

- `getActiveShiftSession`
- `isShiftSessionRestrictedRole`
- `assertStaffOrderInActiveShiftSession`

## Import cơ sở dữ liệu

- `import { db, shiftSessionsTable } from "@workspace/db";`

## Trích mã (tham khảo)

```typescript
import { db, shiftSessionsTable } from "@workspace/db";
import { eq, and, isNull, desc } from "drizzle-orm";
import { isShopAdminRole } from "../middlewares/auth";

export async function getActiveShiftSession(shopId: number, userId: number) {
  const [session] = await db
    .select()
    .from(shiftSessionsTable)
    .where(and(
      eq(shiftSessionsTable.shopId, shopId),
      eq(shiftSessionsTable.userId, userId),
      isNull(shiftSessionsTable.endedAt),
    ))
    .orderBy(desc(shiftSessionsTable.startedAt))
    .limit(1);
  return session ?? null;
}

/** Shift-session guard applies to floor staff only (`staff` role). */
export function isShiftSessionRestrictedRole(role: string): boolean {
  return role === "staff";
}

/** Returns an error message when staff may not act on this order. */
export async function assertStaffOrderInActiveShiftSession(
  auth: { role: string; shopId: number; userId: number },
  orderShiftSessionId: number | null,
): Promise<string | null> {
  if (!isShiftSessionRestrictedRole(auth.role)) return null;

  const activeSession = await getActiveShiftSession(auth.shopId, auth.userId);
  if (!activeSession) {
    return "Không có phiên làm việc đang mở. Chỉ được xem, ghi chú và in lại hoá đơn.";
  }
  if (orderShiftSessionId == null || orderShiftSessionId !== activeSession.id) {
    return "Chỉ được thao tác với đơn hàng thuộc phiên làm việc đang mở.";
  }
  return null;
}
```

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub POS & đơn hàng](../../chuyen-de/pos-va-don-hang/)
