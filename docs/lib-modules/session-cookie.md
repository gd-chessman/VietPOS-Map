# Lib: `session-cookie.ts`

**Mô tả:** Logic backend session-cookie.ts (~27 dòng) — export: SESSION_COOKIE_NAME, setSessionCookie, clearSessionCookie.

**Source Shop:** `artifacts/api-server/src/lib/session-cookie.ts`

**Độ lớn:** ~27 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (3 symbol)

- `SESSION_COOKIE_NAME`
- `setSessionCookie`
- `clearSessionCookie`

## Xem trước đầu file

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
