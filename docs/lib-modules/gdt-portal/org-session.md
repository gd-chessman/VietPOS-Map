# Lib: `gdt-portal/org-session.ts`

**Mô tả:** Logic backend gdt-portal/org-session.ts (~153 dòng) — export: normalizeVatInboundProvider, getGdtSessionPublic, saveGdtSessionToken, markGdtTestFailed, clearGdtSession, ….

**Source Shop:** `artifacts/api-server/src/lib/gdt-portal/org-session.ts`

**Độ lớn:** ~153 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (8 symbol)

- `normalizeVatInboundProvider`
- `getGdtSessionPublic`
- `saveGdtSessionToken`
- `markGdtTestFailed`
- `clearGdtSession`
- `loadGdtPortalClientForOrg`
- `normalizeGdtPortalUsername`
- `resolveGdtPortalCredentials`

## Import DB / schema

- `import { db, orgGdtTaxSessionsTable, organizationsTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { db, orgGdtTaxSessionsTable, organizationsTable } from "@workspace/db";
import { eq } from "drizzle-orm";
import { decryptSecret, encryptSecret } from "../secret-box";
import { GdtPortalClient } from "./client";

const DEFAULT_TOKEN_TTL_MS = 20 * 60 * 60_000;

export type GdtSessionPublic = {
  connected: boolean;
  connectedAt: string | null;
  tokenExpiresAt: string | null;
  lastTestAt: string | null;
  lastTestOk: boolean | null;
};

export function normalizeVatInboundProvider(raw: string | null | undefined): "viettel" | "gdt_direct" {
  return raw === "gdt_direct" ? "gdt_direct" : "viettel";
}

export async function getGdtSessionPublic(orgId: number): Promise<GdtSessionPublic> {
  const [row] = await db
    .select()
    .from(orgGdtTaxSessionsTable)
    .where(eq(orgGdtTaxSessionsTable.organizationId, orgId))
    .limit(1);
  if (!row?.gdtAccessTokenEnc) {
    return {
      connected: false,
      connectedAt: null,
      tokenExpiresAt: null,
      lastTestAt: row?.lastTestAt?.toISOString() ?? null,
      lastTestOk: row?.lastTestOk ?? null,
    };
  }
  const expires = row.gdtTokenExpiresAt?.getTime() ?? 0;
```
