# Lib: `org-agent-llm-settings.ts`

**Mô tả:** Logic backend org-agent-llm-settings.ts (~167 dòng) — export: maskAgentApiKeyForDisplay, stripOrgAgentLlmSecret, envAgentLlmConfig, resolveAgentLlmConfigForOrg, isAgentLlmConfiguredForOrg, ….

**Source Shop:** `artifacts/api-server/src/lib/org-agent-llm-settings.ts`

**Độ lớn:** ~167 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (6 symbol)

- `maskAgentApiKeyForDisplay`
- `stripOrgAgentLlmSecret`
- `envAgentLlmConfig`
- `resolveAgentLlmConfigForOrg`
- `isAgentLlmConfiguredForOrg`
- `applyAgentLlmSettingsFromBody`

## Import DB / schema

- `import { db, organizationsTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { db, organizationsTable } from "@workspace/db";
import { eq } from "drizzle-orm";
import { decryptSecret, encryptSecret } from "./secret-box";

export type OrgAgentLlmDbFields = {
  agentOpenAiApiKeyEnc?: string | null;
  agentOpenAiApiKeyEnabled?: boolean | null;
  agentOpenAiBaseUrl?: string | null;
  agentOpenAiModel?: string | null;
};

export type ResolvedAgentLlmConfig = {
  apiKey: string;
  baseUrl: string;
  model: string;
  modelDisplay: string | null;
  source: "organization" | "env";
};

const orgAgentLlmSelect = {
  agentOpenAiApiKeyEnc: organizationsTable.agentOpenAiApiKeyEnc,
  agentOpenAiApiKeyEnabled: organizationsTable.agentOpenAiApiKeyEnabled,
  agentOpenAiBaseUrl: organizationsTable.agentOpenAiBaseUrl,
  agentOpenAiModel: organizationsTable.agentOpenAiModel,
};

function optText(v: unknown): string | null | undefined {
  if (v === undefined) return undefined;
  if (v === null || v === "") return null;
  if (typeof v !== "string") return undefined;
  const t = v.trim();
  return t ? t : null;
}

/** Hiển thị gợi ý key — không gửi full secret ra client. */
```
