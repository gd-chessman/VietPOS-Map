# Lib: `user-email.ts`

**Mô tả:** Logic backend user-email.ts (~50 dòng) — export: normalizeEmail, EMAIL_ALREADY_USED_MSG, ORG_EMAIL_TAKEN_MSG, findUserByNormalizedEmail, findUserByOrgEmail.

**Source Shop:** `artifacts/api-server/src/lib/user-email.ts`

**Độ lớn:** ~50 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (5 symbol)

- `normalizeEmail`
- `EMAIL_ALREADY_USED_MSG`
- `ORG_EMAIL_TAKEN_MSG`
- `findUserByNormalizedEmail`
- `findUserByOrgEmail`

## Import DB / schema

- `import { db, usersTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { db, usersTable } from "@workspace/db";
import { and, eq, ne, sql } from "drizzle-orm";

function emailEqualsNormalized(normalized: string) {
  return sql`lower(${usersTable.email}) = ${normalized}`;
}

export function normalizeEmail(email: string): string {
  return email.trim().toLowerCase();
}

export const EMAIL_ALREADY_USED_MSG =
  "Email này đã được sử dụng. Mỗi email chỉ được gán cho một tài khoản (không dùng chung).";

/** @deprecated alias — cùng nội dung, dùng ở chain admin */
export const ORG_EMAIL_TAKEN_MSG = EMAIL_ALREADY_USED_MSG;

export async function findUserByNormalizedEmail(
  email: string,
  excludeUserId?: number,
): Promise<{ id: number } | null> {
  const normalized = normalizeEmail(email);
  const where =
    excludeUserId != null
      ? and(emailEqualsNormalized(normalized), ne(usersTable.id, excludeUserId))
      : emailEqualsNormalized(normalized);
  const [row] = await db.select({ id: usersTable.id }).from(usersTable).where(where).limit(1);
  return row ?? null;
}

export async function findUserByOrgEmail(
  organizationId: number | null,
  email: string,
  excludeUserId?: number,
): Promise<{ id: number } | null> {
```
