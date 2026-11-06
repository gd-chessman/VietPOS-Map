# Thư viện: `gdt-portal/http-session.ts`

**Mô tả:** [Hóa đơn đầu vào] gdt-portal/http-session.ts — (không export tên rõ).

**Chủ đề:** [Hóa đơn đầu vào](../../../chuyen-de/hoa-don-dau-vao/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/gdt-portal/http-session.ts` · **Quy mô:** ~53 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Trích mã (tham khảo)

```typescript
const USER_AGENT =
  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36";

export class GdtHttpSession {
  private cookies = new Map<string, string>();

  mergeSetCookie(headers: Headers): void {
    const raw = headers.getSetCookie?.() ?? [];
    const lines = raw.length ? raw : (headers.get("set-cookie") ? [headers.get("set-cookie")!] : []);
    for (const line of lines) {
      const part = line.split(";")[0]?.trim();
      if (!part || !part.includes("=")) continue;
      const eq = part.indexOf("=");
      const name = part.slice(0, eq);
      const value = part.slice(eq + 1);
      if (value) this.cookies.set(name, value);
      else this.cookies.delete(name);
    }
  }

  cookieHeader(): string | undefined {
    if (this.cookies.size === 0) return undefined;
    return [...this.cookies.entries()].map(([k, v]) => `${k}=${v}`).join("; ");
  }

  reset(): void {
    this.cookies.clear();
  }

  async request(
    url: string,
    init: RequestInit & { timeoutMs?: number } = {},
  ): Promise<Response> {
    const { timeoutMs = 120_000, ...rest } = init;
    const headers = new Headers(rest.headers);
    if (!headers.has("User-Agent")) headers.set("User-Agent", USER_AGENT);
    const cookie = this.cookieHeader();
    if (cookie && !headers.has("Cookie")) headers.set("Cookie", cookie);

    const ac = new AbortController();
    const timer = setTimeout(() => ac.abort(), timeoutMs);
    try {
      const res = await fetch(url, { ...rest, headers, signal: ac.signal });
      this.mergeSetCookie(res.headers);
      return res;
```

← [Chỉ mục lib](../../../chi-muc/thu-vien-backend/) · [Hub Hóa đơn đầu vào](../../../chuyen-de/hoa-don-dau-vao/)
