# Thư viện: `pin-challenge.ts`

**Mô tả:** [Đăng nhập & phiên] pin-challenge.ts — PIN_CHALLENGE_PURPOSE, signPinChallengeToken, verifyPinChallengeToken, isPinChallengeJwtPayload.

**Chủ đề:** [Đăng nhập & phiên](../../chuyen-de/dang-nhap-va-phien/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/pin-challenge.ts` · **Quy mô:** ~56 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (4)

- `PIN_CHALLENGE_PURPOSE`
- `signPinChallengeToken`
- `verifyPinChallengeToken`
- `isPinChallengeJwtPayload`

## Import cơ sở dữ liệu

- `import type { User } from "@workspace/db";`

## Trích mã (tham khảo)

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
}

export function verifyPinChallengeToken(token: string): PinChallengePayload | null {
  try {
    const payload = jwt.verify(token, getJwtSecret()) as PinChallengePayload;
    if (payload.purpose !== PIN_CHALLENGE_PURPOSE) return null;
    if (payload.userId == null || payload.shopId == null) return null;
    return payload;
  } catch {
    return null;
```

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Đăng nhập & phiên](../../chuyen-de/dang-nhap-va-phien/)
