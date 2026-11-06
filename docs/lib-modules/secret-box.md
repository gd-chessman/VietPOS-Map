# Lib: `secret-box.ts`

**Mô tả:** Logic backend secret-box.ts (~37 dòng) — export: encryptSecret, decryptSecret.

**Source Shop:** `artifacts/api-server/src/lib/secret-box.ts`

**Độ lớn:** ~37 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (2 symbol)

- `encryptSecret`
- `decryptSecret`

## Xem trước đầu file

```typescript
import { createCipheriv, createDecipheriv, createHash, randomBytes } from "node:crypto";

const ALGO = "aes-256-gcm";
const IV_LEN = 12;

function deriveKey(): Buffer {
  const secret = process.env.SESSION_SECRET;
  if (!secret?.trim()) {
    throw new Error("SESSION_SECRET is required to encrypt GDT tokens");
  }
  return createHash("sha256").update(secret, "utf8").digest();
}

/** Mã hoá chuỗi nhạy cảm (JWT CQT) — lưu DB. */
export function encryptSecret(plain: string): string {
  const key = deriveKey();
  const iv = randomBytes(IV_LEN);
  const cipher = createCipheriv(ALGO, key, iv);
  const enc = Buffer.concat([cipher.update(plain, "utf8"), cipher.final()]);
  const tag = cipher.getAuthTag();
  return `v1:${iv.toString("base64url")}:${tag.toString("base64url")}:${enc.toString("base64url")}`;
}

export function decryptSecret(payload: string): string {
  const parts = payload.split(":");
  if (parts.length !== 4 || parts[0] !== "v1") {
    throw new Error("Invalid encrypted secret format");
  }
  const iv = Buffer.from(parts[1]!, "base64url");
  const tag = Buffer.from(parts[2]!, "base64url");
  const data = Buffer.from(parts[3]!, "base64url");
  const key = deriveKey();
  const decipher = createDecipheriv(ALGO, key, iv);
  decipher.setAuthTag(tag);
  return Buffer.concat([decipher.update(data), decipher.final()]).toString("utf8");
```
