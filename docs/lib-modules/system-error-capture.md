# Lib: `system-error-capture.ts`

**Mô tả:** Logic backend system-error-capture.ts (~125 dòng) — export: markSystemEventLogged, captureUnhandledProcessError, captureHttpServerError, systemErrorCaptureMiddleware, systemExpressErrorHandler.

**Source Shop:** `artifacts/api-server/src/lib/system-error-capture.ts`

**Độ lớn:** ~125 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (5 symbol)

- `markSystemEventLogged`
- `captureUnhandledProcessError`
- `captureHttpServerError`
- `systemErrorCaptureMiddleware`
- `systemExpressErrorHandler`

## Xem trước đầu file

```typescript
import type { NextFunction, Request, Response, RequestHandler } from "express";
import { recordApiSystemEvent } from "./system-event-log";

const DEDUPE_MS = 2 * 60 * 1000;
const recentKeys = new Map<string, number>();

function captureEnabled(): boolean {
  const v = process.env.SYSTEM_EVENT_CAPTURE_HTTP?.trim().toLowerCase();
  if (v === "0" || v === "false" || v === "off") return false;
  return true;
}

function normalizePath(url: string | undefined): string {
  const raw = (url ?? "").split("?")[0] || "/";
  return raw.replace(/\/\d+(?=\/|$)/g, "/:id");
}

function shouldSkipPath(path: string): boolean {
  if (path === "/healthz" || path.endsWith("/healthz")) return true;
  return false;
}

function dedupeKey(parts: string[]): string {
  return parts.join("|");
}

function shouldDedupe(key: string): boolean {
  const now = Date.now();
  const last = recentKeys.get(key);
  if (last != null && now - last < DEDUPE_MS) return true;
  recentKeys.set(key, now);
  if (recentKeys.size > 5000) {
    for (const [k, t] of recentKeys) {
      if (now - t > DEDUPE_MS) recentKeys.delete(k);
    }
```
