# Lib: `pin-challenge.ts`

**Mô tả:** Logic backend pin-challenge.ts (~56 dòng) — export: PIN_CHALLENGE_PURPOSE, signPinChallengeToken, verifyPinChallengeToken, isPinChallengeJwtPayload.

**Source Shop:** `artifacts/api-server/src/lib/pin-challenge.ts`

**Độ lớn:** ~56 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (4 symbol)

- `PIN_CHALLENGE_PURPOSE`
- `signPinChallengeToken`
- `verifyPinChallengeToken`
- `isPinChallengeJwtPayload`

## Import DB / schema

- `import type { User } from "@workspace/db";`

## Xem trước đầu file

```typescript
import jwt from "jsonwebtoken";
import type { User } from "@workspace/db";

function getJwtSecret(): string {
  const secret = process.env.SESSION_SECRET;
  if (!secret) {
    if (process.env.NODE_ENV !== "production") return "dev-session-secret";
    throw new Error("SESSION_SECRET is required");
  }
  return secret;
}

export const PIN_CHALLENGE_PURPOSE = "pin_challenge" as const;
const PIN_CHALLENGE_TTL = "10m";

export type PinChallengePayload = {
  purpose: typeof PIN_CHALLENGE_PURPOSE;
  userId: number;
  email: string;
  role: string;
  shopId: number;
  organizationId: number | null;
};

/** Sau email+mật khẩu đúng — chưa cấp JWT app; chỉ dùng cho /auth/pin/verify và /auth/pin/setup. */
export function signPinChallengeToken(user: Pick<User, "id" | "email" | "role" | "shopId" | "organizationId">): string {
  const payload: PinChallengePayload = {
    purpose: PIN_CHALLENGE_PURPOSE,
    userId: user.id,
    email: user.email,
    role: user.role,
    shopId: user.shopId,
    organizationId: user.organizationId ?? null,
  };
  return jwt.sign(payload, getJwtSecret(), { expiresIn: PIN_CHALLENGE_TTL });
```
