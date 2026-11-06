# Thư viện: `session-cookie.ts`

**Mô tả:** [Đăng nhập & phiên] session-cookie.ts — SESSION_COOKIE_NAME, setSessionCookie, clearSessionCookie.

**Chủ đề:** [Đăng nhập & phiên](../../chuyen-de/dang-nhap-va-phien/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/session-cookie.ts` · **Quy mô:** ~27 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (3)

- `SESSION_COOKIE_NAME`
- `setSessionCookie`
- `clearSessionCookie`

## Trích mã (tham khảo)

```typescript
import type { Response } from "express";

export const SESSION_COOKIE_NAME = "pos_session";

const MAX_AGE_MS = 7 * 24 * 60 * 60 * 1000;

export function setSessionCookie(res: Response, jwt: string): void {
  const secure = process.env.NODE_ENV === "production";
  res.cookie(SESSION_COOKIE_NAME, jwt, {
    httpOnly: true,
    secure,
    sameSite: secure ? "none" : "lax",
    maxAge: MAX_AGE_MS,
    path: "/",
  });
}

export function clearSessionCookie(res: Response): void {
  const secure = process.env.NODE_ENV === "production";
  res.clearCookie(SESSION_COOKIE_NAME, {
    httpOnly: true,
    secure,
    sameSite: secure ? "none" : "lax",
    path: "/",
  });
}
```

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Đăng nhập & phiên](../../chuyen-de/dang-nhap-va-phien/)
