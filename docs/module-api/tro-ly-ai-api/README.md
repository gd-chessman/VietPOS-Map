# Module API: `agent`

**Mô tả:** Module API agent.ts — 10 endpoint. Trợ lý AI: chat, thông tin hệ thống (DB, đồng bộ cloud, shop online), cấp quyền agent_assistant_enabled. Giao diện: pag…

**Mã nguồn Shop:** `artifacts/api-server/src/routes/agent.ts`

Trợ lý AI: chat, thông tin hệ thống (DB, đồng bộ cloud, shop online), cấp quyền `agent_assistant_enabled`.

**Giao diện:** `pages/agent-assistant.tsx`, `agent-chat-audit.tsx`.

**Số endpoint:** 10

## Bảng endpoint (tóm tắt)

| Method | Path | Mô tả ngắn |
|--------|------|------------|
| GET | `/agent/assistant-access` | Đường dẫn đầy đủ `/api/agent/assistant-access` |
| PATCH | `/agent/assistant-access` | Đường dẫn đầy đủ `/api/agent/assistant-access` |
| GET | `/agent/chat/system` | Đường dẫn đầy đủ `/api/agent/chat/system` |
| GET | `/agent/chat/history` | Đường dẫn đầy đủ `/api/agent/chat/history` |
| DELETE | `/agent/chat/history` | Đường dẫn đầy đủ `/api/agent/chat/history` |
| GET | `/agent/chat/audit/threads` | Đường dẫn đầy đủ `/api/agent/chat/audit/threads` |
| DELETE | `/agent/chat/audit/threads/:threadId` | Đường dẫn đầy đủ `/api/agent/chat/audit/threads/:threadId`… |
| GET | `/agent/chat/audit/threads/:threadId/messages` | Đường dẫn đầy đủ `/api/agent/chat/audit/threads/:threadId/messages`… |
| GET | `/agent/chat/status` | Đường dẫn đầy đủ `/api/agent/chat/status` |
| POST | `/agent/chat` | Đường dẫn đầy đủ `/api/agent/chat` |

## Chi tiết từng endpoint

### `GET /agent/assistant-access` {#get-agent-assistant-access}

Đường dẫn đầy đủ `/api/agent/assistant-access`. Lớp kiểm tra: `requireAuth, requireSuperAdminForAgentAccess`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireSuperAdminForAgentAccess`

### `PATCH /agent/assistant-access` {#patch-agent-assistant-access}

Đường dẫn đầy đủ `/api/agent/assistant-access`. Lớp kiểm tra: `requireAuth, requireSuperAdminForAgentAccess`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireSuperAdminForAgentAccess`

### `GET /agent/chat/system` {#get-agent-chat-system}

Đường dẫn đầy đủ `/api/agent/chat/system`. Lớp kiểm tra: `requireAgentChatRole, requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAgentChatRole`, `requireAuth`

### `GET /agent/chat/history` {#get-agent-chat-history}

Đường dẫn đầy đủ `/api/agent/chat/history`. Lớp kiểm tra: `requireAgentChatRole, requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAgentChatRole`, `requireAuth`

### `DELETE /agent/chat/history` {#delete-agent-chat-history}

Đường dẫn đầy đủ `/api/agent/chat/history`. Lớp kiểm tra: `requireAgentChatRole, requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAgentChatRole`, `requireAuth`

### `GET /agent/chat/audit/threads` {#get-agent-chat-audit-threads}

Đường dẫn đầy đủ `/api/agent/chat/audit/threads`. Lớp kiểm tra: `requireAuth, requireSuperAdminForAgentAccess`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireSuperAdminForAgentAccess`

### `DELETE /agent/chat/audit/threads/:threadId` {#delete-agent-chat-audit-threads--threadId}

Đường dẫn đầy đủ `/api/agent/chat/audit/threads/:threadId`. Lớp kiểm tra: `requireAuth, requireSuperAdminForAgentAccess`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireSuperAdminForAgentAccess`

### `GET /agent/chat/audit/threads/:threadId/messages` {#get-agent-chat-audit-threads--threadId-messages}

Đường dẫn đầy đủ `/api/agent/chat/audit/threads/:threadId/messages`. Lớp kiểm tra: `requireAuth, requireSuperAdminForAgentAccess`.

- **Lớp kiểm tra (middleware):** `requireAuth`, `requireSuperAdminForAgentAccess`

### `GET /agent/chat/status` {#get-agent-chat-status}

Đường dẫn đầy đủ `/api/agent/chat/status`. Lớp kiểm tra: `requireAgentChatRole, requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAgentChatRole`, `requireAuth`

### `POST /agent/chat` {#post-agent-chat}

Đường dẫn đầy đủ `/api/agent/chat`. Lớp kiểm tra: `requireAgentChatRole, requireAuth`.

- **Lớp kiểm tra (middleware):** `requireAgentChatRole`, `requireAuth`

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./agent.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
