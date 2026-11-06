# Lib: `ip-denylist.ts`

**Mô tả:** Logic backend ip-denylist.ts (~159 dòng) — export: normalizeClientIp, blockedIpCount, clientIpFromRequest, describeSeenClientIp, refreshIpDenylistFromDb, ….

**Source Shop:** `artifacts/api-server/src/lib/ip-denylist.ts`

**Độ lớn:** ~159 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (8 symbol)

- `normalizeClientIp`
- `blockedIpCount`
- `clientIpFromRequest`
- `describeSeenClientIp`
- `refreshIpDenylistFromDb`
- `startIpDenylistRefreshScheduler`
- `ipDenylistMiddleware`
- `isValidBlockedIp`

## Import DB / schema

- `import { db, blockedIpsTable } from "@workspace/db";`
- `"[ip-denylist] Bảng blocked_ips chưa có — chạy: pnpm --filter @workspace/db run apply:blocked-ips",`

## Xem trước đầu file

```typescript
import type { Request, RequestHandler } from "express";
import { db, blockedIpsTable } from "@workspace/db";
import { logger } from "./logger";
import { isTrustProxyEnabled } from "./rate-limit";

const DEFAULT_REFRESH_MS = 10 * 60 * 1000;

function ipDenylistRefreshMs(): number {
  const raw = process.env.IP_DENYLIST_REFRESH_MS;
  if (raw == null || raw.trim() === "") return DEFAULT_REFRESH_MS;
  const n = Number(raw);
  if (!Number.isFinite(n) || n < 0) return DEFAULT_REFRESH_MS;
  return Math.floor(n);
}

/** Chuẩn hóa địa chỉ (IPv4 mapped, khoảng trắng). */
export function normalizeClientIp(raw: string | undefined | null): string {
  if (raw == null) return "";
  let ip = raw.trim();
  if (ip.startsWith("::ffff:")) ip = ip.slice("::ffff:".length);
  return ip;
}

function parseDenylistEnv(): Set<string> {
  const raw = process.env.IP_DENYLIST ?? process.env.BLOCKED_IPS ?? "";
  const set = new Set<string>();
  for (const part of raw.split(/[,;\s]+/)) {
    const ip = normalizeClientIp(part);
    if (ip) set.add(ip);
  }
  return set;
}

const envBlockedIps = parseDenylistEnv();
/** Gộp env + DB; cập nhật khi refresh / sau CRUD. */
```
