# Lib: `gdt-portal/client.ts`

**Mô tả:** Logic backend gdt-portal/client.ts (~345 dòng) — export: captchaDataUrl.

**Source Shop:** `artifacts/api-server/src/lib/gdt-portal/client.ts`

**Độ lớn:** ~345 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (1 symbol)

- `captchaDataUrl`

## Xem trước đầu file

```typescript
import { randomUUID } from "node:crypto";
import { GdtHttpSession, USER_AGENT } from "./http-session";

const GDT_SITE = "https://hoadondientu.gdt.gov.vn";
const GDT_API_BASE = "https://hoadondientu.gdt.gov.vn/api/";

const PAGE_SIZE = 50;
const MAX_STATE_PAGES = 200;
/** Một request list có thể phủ nhiều ngày (auto-sync mặc định 3 ngày → 1 lần gọi). */
const FETCH_CHUNK_DAYS = 3;
const FETCH_RETRY_MAX = 4;
const FETCH_RETRY_DELAY_MS = 2500;
const FETCH_CHUNK_PAUSE_MS = 300;
const SESSION_WARM_TTL_MS = 90_000;
const VN_OFFSET = "+07:00";

export type GdtCaptcha = { key: string; rawContent: string };

function sleep(ms: number): Promise<void> {
  return new Promise((r) => setTimeout(r, ms));
}

function httpErrorMessage(status: number, text: string, context: string): string {
  if (status === 403 && text.includes("không hợp lệ")) {
    return `${context} HTTP 403 — WAF CQT. Thử lại captcha, tắt VPN. ${text.slice(0, 200)}`;
  }
  if (status === 401) {
    try {
      const j = JSON.parse(text) as { message?: string };
      const msg = String(j.message ?? "");
      if (/captcha/i.test(msg) || /captcha/i.test(text)) {
        return `${context}: mã captcha sai hoặc hết hạn — tải captcha mới.`;
      }
      if (msg) {
        return `${context}: ${msg} — kiểm tra MST/tài khoản và mật khẩu đúng như đăng nhập trên hoadondientu.gdt.gov.vn (bấm Lưu form nếu vừa đổi).`;
```
