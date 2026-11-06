# Lib: `gdt-portal/http-session.ts`

**Mô tả:** Logic backend gdt-portal/http-session.ts (~53 dòng) — export: (không export tên rõ).

**Source Shop:** `artifacts/api-server/src/lib/gdt-portal/http-session.ts`

**Độ lớn:** ~53 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Xem trước đầu file

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
```
