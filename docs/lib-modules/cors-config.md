# Lib: `cors-config.ts`

**Mô tả:** Logic backend cors-config.ts (~30 dòng) — export: parseFrontendUrls, getCorsOptions.

**Source Shop:** `artifacts/api-server/src/lib/cors-config.ts`

**Độ lớn:** ~30 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (2 symbol)

- `parseFrontendUrls`
- `getCorsOptions`

## Xem trước đầu file

```typescript
import type { CorsOptions } from "cors";

/** Origin trình duyệt được phép (phân tách dấu phẩy). Bắt buộc set — không set = chặn mọi Origin. */
export function parseFrontendUrls(raw: string | undefined): string[] {
  if (!raw?.trim()) return [];
  return raw
    .split(",")
    .map((s) => s.trim())
    .filter(Boolean);
}

export function getCorsOptions(): CorsOptions {
  const set = new Set(parseFrontendUrls(process.env.FRONTEND_URLS));
  return {
    credentials: true,
    origin(origin, callback) {
      // curl / server-side — không có Origin.
      if (!origin) {
        callback(null, true);
        return;
      }
      if (set.size > 0 && set.has(origin)) {
        callback(null, true);
        return;
      }
      callback(null, false);
    },
  };
}
```
