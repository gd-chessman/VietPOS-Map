# Thư viện: `user-pin.ts`

**Mô tả:** [Đăng nhập & phiên] user-pin.ts — PIN_LENGTH, roleRequiresPin, normalizePin, validatePinFormat, hashPin, ….

**Chủ đề:** [Đăng nhập & phiên](../../chuyen-de/dang-nhap-va-phien/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/user-pin.ts` · **Quy mô:** ~35 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (9)

- `PIN_LENGTH`
- `roleRequiresPin`
- `normalizePin`
- `validatePinFormat`
- `hashPin`
- `verifyPinHash`
- `PIN_LOCK_MAX_ATTEMPTS`
- `PIN_LOCK_MS`
- `isPinLocked`

## Trích mã (tham khảo)

```typescript
import bcrypt from "bcryptjs";

export const PIN_LENGTH = 4;

export function roleRequiresPin(role: string): boolean {
  return role !== "staff";
}

export function normalizePin(pin: string): string {
  return pin.trim();
}

export function validatePinFormat(pin: string): string | null {
  const p = normalizePin(pin);
  if (!/^\d{4}$/.test(p)) return "Mã PIN phải là 4 chữ số.";
  return null;
}

export async function hashPin(pin: string): Promise<string> {
  return bcrypt.hash(normalizePin(pin), 10);
}

export async function verifyPinHash(pin: string, pinHash: string | null | undefined): Promise<boolean> {
  if (!pinHash) return false;
  return bcrypt.compare(normalizePin(pin), pinHash);
}

export const PIN_LOCK_MAX_ATTEMPTS = 5;
export const PIN_LOCK_MS = 5 * 60 * 1000;

export function isPinLocked(lockedUntil: Date | null | undefined): boolean {
  if (!lockedUntil) return false;
  return lockedUntil.getTime() > Date.now();
}
```

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Đăng nhập & phiên](../../chuyen-de/dang-nhap-va-phien/)
