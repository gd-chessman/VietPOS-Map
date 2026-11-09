# Module API: `agent`

**Mô tả:** Module API agent.ts — 10 endpoint. Trợ lý AI: chat, thông tin hệ thống (DB, đồng bộ cloud, shop online)…

**Mã nguồn Shop:** `artifacts/api-server/src/routes/agent.ts`

Trợ lý AI: chat, thông tin hệ thống (DB, đồng bộ cloud, shop online), cấp quyền `agent_assistant_enabled`.

**Giao diện:** `pages/agent-assistant.tsx`, `agent-chat-audit.tsx`.

**Số endpoint:** 10

**Contract API:** Mỗi endpoint có mục **URL**, body/query (từ code + schema Zod orval khi có), bảng lỗi `error`, và response (Zod hoặc trường `res.json`).

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

**URL:** `GET /api/agent/assistant-access`

**Lớp route:** `requireAuth`, `requireSuperAdminForAgentAccess`
- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).

**Query:** `organizationId`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `organizationId không hợp lệ` |

**Response 200** — trường top-level (trích `res.json`):

`agentAssistantEnabled`, `alwaysEnabled`, `email`, `id`, `name`, `role`, `shopName`, `true`, `users`

### `PATCH /agent/assistant-access` {#patch-agent-assistant-access}

Đường dẫn đầy đủ `/api/agent/assistant-access`. Lớp kiểm tra: `requireAuth, requireSuperAdminForAgentAccess`.

**URL:** `PATCH /api/agent/assistant-access`

**Lớp route:** `requireAuth`, `requireSuperAdminForAgentAccess`
- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).

**Request body** — schema `AssistantAccessBody` (`@workspace/api-zod`):

*(schema `AssistantAccessBody` — xem `lib/api-zod/src/generated/api.ts`)*

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `userIds có tài khoản không thuộc tổ chức` |

**Response 200** — trường top-level (trích `res.json`):

`ok`

### `GET /agent/chat/system` {#get-agent-chat-system}

Đường dẫn đầy đủ `/api/agent/chat/system`. Lớp kiểm tra: `requireAgentChatRole, requireAuth`.

**URL:** `GET /api/agent/chat/system`

**Lớp route:** `requireAgentChatRole`, `requireAuth`

**Response 200** — trường top-level (trích `res.json`):

`message`

### `GET /agent/chat/history` {#get-agent-chat-history}

Đường dẫn đầy đủ `/api/agent/chat/history`. Lớp kiểm tra: `requireAgentChatRole, requireAuth`.

**URL:** `GET /api/agent/chat/history`

**Lớp route:** `requireAgentChatRole`, `requireAuth`

*Handler không trích được contract tự động — mở file route TypeScript.*

### `DELETE /agent/chat/history` {#delete-agent-chat-history}

Đường dẫn đầy đủ `/api/agent/chat/history`. Lớp kiểm tra: `requireAgentChatRole, requireAuth`.

**URL:** `DELETE /api/agent/chat/history`

**Lớp route:** `requireAgentChatRole`, `requireAuth`

**Response 200** — trường top-level (trích `res.json`):

`ok`

### `GET /agent/chat/audit/threads` {#get-agent-chat-audit-threads}

Đường dẫn đầy đủ `/api/agent/chat/audit/threads`. Lớp kiểm tra: `requireAuth, requireSuperAdminForAgentAccess`.

**URL:** `GET /api/agent/chat/audit/threads`

**Lớp route:** `requireAuth`, `requireSuperAdminForAgentAccess`
- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).

**Query:** `from`, `limit`, `offset`, `organizationId`, `to`, `userId`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `from không hợp lệ` |
| **400** | `to không hợp lệ` |

### `DELETE /agent/chat/audit/threads/:threadId` {#delete-agent-chat-audit-threads--threadId}

Đường dẫn đầy đủ `/api/agent/chat/audit/threads/:threadId`. Lớp kiểm tra: `requireAuth, requireSuperAdminForAgentAccess`.

**URL:** `DELETE /api/agent/chat/audit/threads/:threadId`

**Lớp route:** `requireAuth`, `requireSuperAdminForAgentAccess`
- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).

**Path params:** `threadId`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `threadId không hợp lệ` |
| **404** | `Không tìm thấy hội thoại` |

**Response 200** — trường top-level (trích `res.json`):

`ok`

### `GET /agent/chat/audit/threads/:threadId/messages` {#get-agent-chat-audit-threads--threadId-messages}

Đường dẫn đầy đủ `/api/agent/chat/audit/threads/:threadId/messages`. Lớp kiểm tra: `requireAuth, requireSuperAdminForAgentAccess`.

**URL:** `GET /api/agent/chat/audit/threads/:threadId/messages`

**Lớp route:** `requireAuth`, `requireSuperAdminForAgentAccess`
- **Thêm trong handler:** role **`super_admin`** (403 nếu không đủ).

**Query:** `limit`, `offset`

**Path params:** `threadId`

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `threadId không hợp lệ` |

### `GET /agent/chat/status` {#get-agent-chat-status}

Đường dẫn đầy đủ `/api/agent/chat/status`. Lớp kiểm tra: `requireAgentChatRole, requireAuth`.

**URL:** `GET /api/agent/chat/status`

**Lớp route:** `requireAgentChatRole`, `requireAuth`

**Response 200** — trường top-level (trích `res.json`):

`enabled`, `tools`

### `POST /agent/chat` {#post-agent-chat}

Đường dẫn đầy đủ `/api/agent/chat`. Lớp kiểm tra: `requireAgentChatRole, requireAuth`.

**URL:** `POST /api/agent/chat`

**Lớp route:** `requireAgentChatRole`, `requireAuth`

**Request body** — schema `ChatBody` (`@workspace/api-zod`):

*(schema `ChatBody` — xem `lib/api-zod/src/generated/api.ts`)*

**Lỗi JSON** (`error` string):

| HTTP | Message |
|------|---------|
| **400** | `Tin nhắn cuối phải là câu hỏi của user` |

## Ghi chú đọc mã

- Gắn prefix `/api` trong `app.ts`; file route: `routes/index.ts` → `./agent.ts`.
- Handler đầy đủ: mở file TypeScript tại Shop (tìm theo chuỗi path).
- Quyền role: `tham-chieu/phan-quyen-rbac/README.md` (tiếng Anh gốc) + các `require*` trong từng endpoint.

**Đọc tiếp:** [Hướng dẫn Map](../../huong-dan-doc/) · [Mục lục](../../README.md)
