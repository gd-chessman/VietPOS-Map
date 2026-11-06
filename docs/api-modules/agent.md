# API module: `agent`

**Mô tả:** File routes agent.ts — 10 endpoint HTTP cho /api/.... Trợ lý AI: chat, system info (DB, cloud sync, shops online), cấp quyền agent_assistant_enabled. Frontend: pages/agent-a…

**Source Shop:** `artifacts/api-server/src/routes/agent.ts`

Trợ lý AI: chat, system info (DB, cloud sync, shops online), cấp quyền `agent_assistant_enabled`.

**Frontend:** `pages/agent-assistant.tsx`, `agent-chat-audit.tsx`.

**Số endpoint trong file:** 10

## Danh sách endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/agent/assistant-access` | `/api/agent/assistant-access` |
| PATCH | `/agent/assistant-access` | `/api/agent/assistant-access` |
| GET | `/agent/chat/system` | `/api/agent/chat/system` |
| GET | `/agent/chat/history` | `/api/agent/chat/history` |
| DELETE | `/agent/chat/history` | `/api/agent/chat/history` |
| GET | `/agent/chat/audit/threads` | `/api/agent/chat/audit/threads` |
| DELETE | `/agent/chat/audit/threads/:threadId` | `/api/agent/chat/audit/threads/:threadId` |
| GET | `/agent/chat/audit/threads/:threadId/messages` | `/api/agent/chat/audit/threads/:threadId/messages` |
| GET | `/agent/chat/status` | `/api/agent/chat/status` |
| POST | `/agent/chat` | `/api/agent/chat` |

## Chi tiết từng endpoint

### `GET /agent/assistant-access` {#get-agent-assistant-access}

`/api/agent/assistant-access`. Middleware: `requireAuth, requireSuperAdminForAgentAccess`.

- **Middleware:** `requireAuth`, `requireSuperAdminForAgentAccess`

### `PATCH /agent/assistant-access` {#patch-agent-assistant-access}

`/api/agent/assistant-access`. Middleware: `requireAuth, requireSuperAdminForAgentAccess`.

- **Middleware:** `requireAuth`, `requireSuperAdminForAgentAccess`

### `GET /agent/chat/system` {#get-agent-chat-system}

`/api/agent/chat/system`. Middleware: `requireAgentChatRole, requireAuth`.

- **Middleware:** `requireAgentChatRole`, `requireAuth`

### `GET /agent/chat/history` {#get-agent-chat-history}

`/api/agent/chat/history`. Middleware: `requireAgentChatRole, requireAuth`.

- **Middleware:** `requireAgentChatRole`, `requireAuth`

### `DELETE /agent/chat/history` {#delete-agent-chat-history}

`/api/agent/chat/history`. Middleware: `requireAgentChatRole, requireAuth`.

- **Middleware:** `requireAgentChatRole`, `requireAuth`

### `GET /agent/chat/audit/threads` {#get-agent-chat-audit-threads}

`/api/agent/chat/audit/threads`. Middleware: `requireAuth, requireSuperAdminForAgentAccess`.

- **Middleware:** `requireAuth`, `requireSuperAdminForAgentAccess`

### `DELETE /agent/chat/audit/threads/:threadId` {#delete-agent-chat-audit-threads--threadId}

`/api/agent/chat/audit/threads/:threadId`. Middleware: `requireAuth, requireSuperAdminForAgentAccess`.

- **Middleware:** `requireAuth`, `requireSuperAdminForAgentAccess`

### `GET /agent/chat/audit/threads/:threadId/messages` {#get-agent-chat-audit-threads--threadId-messages}

`/api/agent/chat/audit/threads/:threadId/messages`. Middleware: `requireAuth, requireSuperAdminForAgentAccess`.

- **Middleware:** `requireAuth`, `requireSuperAdminForAgentAccess`

### `GET /agent/chat/status` {#get-agent-chat-status}

`/api/agent/chat/status`. Middleware: `requireAgentChatRole, requireAuth`.

- **Middleware:** `requireAgentChatRole`, `requireAuth`

### `POST /agent/chat` {#post-agent-chat}

`/api/agent/chat`. Middleware: `requireAgentChatRole, requireAuth`.

- **Middleware:** `requireAgentChatRole`, `requireAuth`

## Ghi chú đọc code

- Mount prefix `/api` qua `app.ts`; file này: `routes/index.ts` → `./agent.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (search theo path string).
- Quyền role: xem `reference/rbac.md` và middleware trong từng block.
