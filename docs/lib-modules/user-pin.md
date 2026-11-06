# Lib: `user-pin.ts`

**Mô tả:** Logic backend user-pin.ts (~35 dòng) — export: PIN_LENGTH, roleRequiresPin, normalizePin, validatePinFormat, hashPin, ….

**Source Shop:** `artifacts/api-server/src/lib/user-pin.ts`

**Độ lớn:** ~35 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (9 symbol)

- `PIN_LENGTH`
- `roleRequiresPin`
- `normalizePin`
- `validatePinFormat`
- `hashPin`
- `verifyPinHash`
- `PIN_LOCK_MAX_ATTEMPTS`
- `PIN_LOCK_MS`
- `isPinLocked`

## Xem trước đầu file

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
