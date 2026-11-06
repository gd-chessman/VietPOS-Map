# Lib: `customer-public-urls.ts`

**Mô tả:** Logic backend customer-public-urls.ts (~92 dòng) — export: normalizePublicBaseUrl, buildPublicPageUrl, publicUrlsFromBase, normalizeFeedbackPublicUrl, applyCustomerPublicUrlFields.

**Source Shop:** `artifacts/api-server/src/lib/customer-public-urls.ts`

**Độ lớn:** ~92 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (5 symbol)

- `normalizePublicBaseUrl`
- `buildPublicPageUrl`
- `publicUrlsFromBase`
- `normalizeFeedbackPublicUrl`
- `applyCustomerPublicUrlFields`

## Xem trước đầu file

```typescript
/** URL gốc site công khai theo tổ chức — các trang (/feedback, /vat-invoice, …) ghép từ đây. */

export type PublicCustomerPage = "feedback" | "vat-invoice";

/** Chuẩn hoá URL gốc: origin + path (không /feedback, /vat-invoice, không query). */
export function normalizePublicBaseUrl(raw: string): string {
  const t = raw.trim();
  if (!t) throw new Error("URL trống");
  const withProto = /^https?:\/\//i.test(t) ? t : `https://${t}`;
  let u: URL;
  try {
    u = new URL(withProto);
  } catch {
    throw new Error("URL không hợp lệ");
  }
  if (u.protocol !== "http:" && u.protocol !== "https:") {
    throw new Error("URL phải bắt đầu bằng http:// hoặc https://");
  }
  u.search = "";
  u.hash = "";
  let path = u.pathname.replace(/\/+$/, "");
  path = path.replace(/\/(feedback|vat-invoice)$/i, "");
  u.pathname = path || "/";
  const out = u.toString().replace(/\/$/, "");
  if (u.pathname === "/" && !out.endsWith("/")) {
    return out;
  }
  return out;
}

export function buildPublicPageUrl(base: string, page: PublicCustomerPage): string {
  const u = new URL(normalizePublicBaseUrl(base));
  const segment = page === "feedback" ? "feedback" : "vat-invoice";
  const path = u.pathname.replace(/\/+$/, "");
  u.pathname = `${path}/${segment}`.replace(/\/{2,}/g, "/");
```
