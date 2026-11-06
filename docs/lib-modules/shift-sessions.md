# Lib: `shift-sessions.ts`

**Mô tả:** Logic backend shift-sessions.ts (~40 dòng) — export: getActiveShiftSession, isShiftSessionRestrictedRole, assertStaffOrderInActiveShiftSession.

**Source Shop:** `artifacts/api-server/src/lib/shift-sessions.ts`

**Độ lớn:** ~40 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (3 symbol)

- `getActiveShiftSession`
- `isShiftSessionRestrictedRole`
- `assertStaffOrderInActiveShiftSession`

## Import DB / schema

- `import { db, shiftSessionsTable } from "@workspace/db";`

## Xem trước đầu file

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
```
