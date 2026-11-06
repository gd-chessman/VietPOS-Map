# Thư viện: `cors-config.ts`

**Mô tả:** [Kiến trúc / dùng chung] cors-config.ts — parseFrontendUrls, getCorsOptions.

**Chủ đề:** [Kiến trúc / dùng chung](../../chuyen-de/kien-truc-he-thong/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/cors-config.ts` · **Quy mô:** ~30 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (2)

- `parseFrontendUrls`
- `getCorsOptions`

## Trích mã (tham khảo)

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

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Kiến trúc / dùng chung](../../chuyen-de/kien-truc-he-thong/)
