# Lib: `org-smtp-settings.ts`

**Mô tả:** Logic backend org-smtp-settings.ts (~119 dòng) — export: stripOrgSmtpPassword, smtpConfigFromOrgRow, loadOrgSmtpConfig, applySmtpSettingsFromBody.

**Source Shop:** `artifacts/api-server/src/lib/org-smtp-settings.ts`

**Độ lớn:** ~119 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (4 symbol)

- `stripOrgSmtpPassword`
- `smtpConfigFromOrgRow`
- `loadOrgSmtpConfig`
- `applySmtpSettingsFromBody`

## Import DB / schema

- `import { db, organizationsTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { db, organizationsTable } from "@workspace/db";
import { eq } from "drizzle-orm";

export type OrgSmtpDbFields = {
  smtpHost?: string | null;
  smtpPort?: number | null;
  smtpSecure?: boolean | null;
  smtpUser?: string | null;
  smtpPassword?: string | null;
  smtpFrom?: string | null;
};

export type SmtpTransportConfig = {
  host: string;
  port: number;
  secure: boolean;
  user: string;
  pass: string;
  from: string;
};

const orgSmtpSelect = {
  smtpHost: organizationsTable.smtpHost,
  smtpPort: organizationsTable.smtpPort,
  smtpSecure: organizationsTable.smtpSecure,
  smtpUser: organizationsTable.smtpUser,
  smtpPassword: organizationsTable.smtpPassword,
  smtpFrom: organizationsTable.smtpFrom,
};

function optText(v: unknown): string | null | undefined {
  if (v === undefined) return undefined;
  if (v === null || v === "") return null;
  if (typeof v !== "string") return undefined;
  const t = v.trim();
```
