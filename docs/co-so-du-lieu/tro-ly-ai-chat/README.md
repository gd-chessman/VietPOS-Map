# Schema: `agentChat`

**Mô tả:** Drizzle agentChat.ts — 2 bảng, 12 cột, 3 index (agent_chat_threads, agent_chat_messages).

**Mã nguồn Shop:** `lib/db/src/schema/agentChat.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [tro-ly-ai-api](../../module-api/tro-ly-ai-api/) (`routes/agent.ts`)

## Bảng `agent_chat_threads`

- **Biến Drizzle:** `agentChatThreadsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `user_id` | `userId` | integer | NOT NULL | `users` | — |
| `organization_id` | `organizationId` | integer | — | `organizations` | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |
| `updated_at` | `updatedAt` | timestamp("updated_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |
| `user_cleared_at` | `userClearedAt` | timestamp("user_cleared_at", { withTimezone: true }) | — | — | — |

**Index:**

- `agent_chat_threads_user_id_uidx` on `userId`
- `agent_chat_messages_thread_created_idx` on `threadId`, `createdAt`

## Bảng `agent_chat_messages`

- **Biến Drizzle:** `agentChatMessagesTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `thread_id` | `threadId` | integer | NOT NULL | `agent_chat_threads` | — |
| `role` | `role` | text | NOT NULL | — | — |
| `content` | `content` | text | NOT NULL | — | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |

**Index:**

- `agent_chat_messages_thread_created_idx` on `threadId`, `createdAt`

## Kiểu & Zod (insert)

- `export type AgentChatThread`
- `export type AgentChatMessageRow`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
