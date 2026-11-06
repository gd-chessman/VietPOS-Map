# Thư viện: `user-email.ts`

**Mô tả:** [Đăng nhập & phiên] user-email.ts — normalizeEmail, EMAIL_ALREADY_USED_MSG, ORG_EMAIL_TAKEN_MSG, findUserByNormalizedEmail, findUserByOrgEmail.

**Chủ đề:** [Đăng nhập & phiên](../../chuyen-de/dang-nhap-va-phien/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/user-email.ts` · **Quy mô:** ~50 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (5)

- `normalizeEmail`
- `EMAIL_ALREADY_USED_MSG`
- `ORG_EMAIL_TAKEN_MSG`
- `findUserByNormalizedEmail`
- `findUserByOrgEmail`

## Import cơ sở dữ liệu

- `import { db, usersTable } from "@workspace/db";`

## Trích mã (tham khảo)

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
  const normalized = normalizeEmail(email);
  if (organizationId != null) {
    const where = excludeUserId != null
      ? and(
          eq(usersTable.organizationId, organizationId),
          emailEqualsNormalized(normalized),
          ne(usersTable.id, excludeUserId),
        )
      : and(eq(usersTable.organizationId, organizationId), emailEqualsNormalized(normalized));
    const [existing] = await db.select({ id: usersTable.id }).from(usersTable).where(where).limit(1);
```

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Đăng nhập & phiên](../../chuyen-de/dang-nhap-va-phien/)
