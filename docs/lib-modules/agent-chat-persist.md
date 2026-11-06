# Lib: `agent-chat-persist.ts`

**Mô tả:** Logic backend agent-chat-persist.ts (~262 dòng) — export: AGENT_CHAT_CONTEXT_LIMIT, getOrCreateAgentChatThread, appendAgentChatMessage, loadAgentChatContextForUser, clearAgentChatForUser, ….

**Source Shop:** `artifacts/api-server/src/lib/agent-chat-persist.ts`

**Độ lớn:** ~262 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (9 symbol)

- `AGENT_CHAT_CONTEXT_LIMIT`
- `getOrCreateAgentChatThread`
- `appendAgentChatMessage`
- `loadAgentChatContextForUser`
- `clearAgentChatForUser`
- `deleteAgentChatThreadHard`
- `persistAgentChatExchange`
- `listAgentChatThreadsForAudit`
- `loadAgentChatThreadMessagesForAudit`

## Import DB / schema

- `} from "@workspace/db";`

## Xem trước đầu file

```typescript
import {
  db,
  agentChatMessagesTable,
  agentChatThreadsTable,
  usersTable,
  shopsTable,
} from "@workspace/db";
import { and, asc, desc, eq, gt, gte, lte, sql, type SQL } from "drizzle-orm";
import type { AuthPayload } from "../middlewares/auth";
import { resolveOrganizationId } from "../middlewares/auth";

export const AGENT_CHAT_CONTEXT_LIMIT = 30;

export type AgentChatTurn = { role: "user" | "assistant"; content: string };

export async function getOrCreateAgentChatThread(auth: AuthPayload): Promise<number> {
  const userId = auth.userId;
  const [existing] = await db
    .select({ id: agentChatThreadsTable.id })
    .from(agentChatThreadsTable)
    .where(eq(agentChatThreadsTable.userId, userId))
    .limit(1);

  const organizationId = await resolveOrganizationId(auth);
  const now = new Date();

  if (existing) {
    await db
      .update(agentChatThreadsTable)
      .set({
        shopId: auth.shopId,
        organizationId: organizationId ?? null,
        updatedAt: now,
      })
      .where(eq(agentChatThreadsTable.id, existing.id));
```
