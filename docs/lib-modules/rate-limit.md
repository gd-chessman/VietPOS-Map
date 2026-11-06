# Lib: `rate-limit.ts`

**Mô tả:** Logic backend rate-limit.ts (~83 dòng) — export: isRateLimitEnabled, isTrustProxyEnabled, configureTrustProxy.

**Source Shop:** `artifacts/api-server/src/lib/rate-limit.ts`

**Độ lớn:** ~83 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (3 symbol)

- `isRateLimitEnabled`
- `isTrustProxyEnabled`
- `configureTrustProxy`

## Xem trước đầu file

```typescript
import rateLimit, { type Options, type RateLimitRequestHandler } from "express-rate-limit";
import type { RequestHandler } from "express";

function envInt(name: string, fallback: number): number {
  const raw = process.env[name];
  if (raw == null || raw.trim() === "") return fallback;
  const n = Number(raw);
  return Number.isFinite(n) && n > 0 ? Math.floor(n) : fallback;
}

export function isRateLimitEnabled(): boolean {
  const raw = process.env.RATE_LIMIT_ENABLED;
  return raw !== "0" && raw !== "false";
}

const noop: RequestHandler = (_req, _res, next) => next();

function limiter(options: Partial<Options>): RateLimitRequestHandler | RequestHandler {
  if (!isRateLimitEnabled()) return noop;
  return rateLimit({
    standardHeaders: true,
    legacyHeaders: false,
    handler: (_req, res, _next, opts) => {
      res.status(429).json({
        error: "Quá nhiều yêu cầu — vui lòng thử lại sau.",
        retryAfterSec: Math.ceil(opts.windowMs / 1000),
      });
    },
    ...options,
  });
}

const TEN_MIN = 10 * 60 * 1000;
const ONE_HOUR = 60 * 60 * 1000;

```
