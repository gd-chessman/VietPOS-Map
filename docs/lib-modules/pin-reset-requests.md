# Lib: `pin-reset-requests.ts`

**Mô tả:** Logic backend pin-reset-requests.ts (~98 dòng) — export: upsertPendingPinResetRequest, canSetPinWithoutPasswordAfterUserSetsReset, clearUserPin, setUserPin, markPinResetRequestResolved, ….

**Source Shop:** `artifacts/api-server/src/lib/pin-reset-requests.ts`

**Độ lớn:** ~98 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (6 symbol)

- `upsertPendingPinResetRequest`
- `canSetPinWithoutPasswordAfterUserSetsReset`
- `clearUserPin`
- `setUserPin`
- `markPinResetRequestResolved`
- `markPinResetRequestCancelled`

## Import DB / schema

- `import { db, pinResetRequestsTable, usersTable, type User } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { db, pinResetRequestsTable, usersTable, type User } from "@workspace/db";
import { and, desc, eq } from "drizzle-orm";
import { hashPin, validatePinFormat } from "./user-pin";

export async function upsertPendingPinResetRequest(user: Pick<User, "id" | "shopId">): Promise<{ created: boolean }> {
  const [existing] = await db
    .select({ id: pinResetRequestsTable.id })
    .from(pinResetRequestsTable)
    .where(and(eq(pinResetRequestsTable.userId, user.id), eq(pinResetRequestsTable.status, "pending")))
    .limit(1);
  if (existing) return { created: false };
  await db.insert(pinResetRequestsTable).values({
    userId: user.id,
    shopId: user.shopId,
    status: "pending",
  });
  return { created: true };
}

/** Quản trị đã duyệt «user tự đặt PIN» — cho phép /auth/pin/set không cần mật khẩu (kể cả cache PIN cũ trên DB). */
export async function canSetPinWithoutPasswordAfterUserSetsReset(userId: number): Promise<boolean> {
  const [row] = await db
    .select({ resolvedAt: pinResetRequestsTable.resolvedAt })
    .from(pinResetRequestsTable)
    .where(
      and(
        eq(pinResetRequestsTable.userId, userId),
        eq(pinResetRequestsTable.status, "resolved"),
        eq(pinResetRequestsTable.resolutionMode, "user_sets"),
      ),
    )
    .orderBy(desc(pinResetRequestsTable.resolvedAt))
    .limit(1);
  if (!row?.resolvedAt) return false;
  const ageMs = Date.now() - row.resolvedAt.getTime();
```
