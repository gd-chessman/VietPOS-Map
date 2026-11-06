# Schema: `agentChat`

**Mô tả:** Drizzle schema agentChat.ts — 12 cột trên 2 bảng Postgres (agent_chat_threads, agent_chat_messages).

**Mã nguồn Shop:** `lib/db/src/schema/agentChat.ts`

## Bảng Postgres

- `agent_chat_threads`
- `agent_chat_messages`

## Cột (trích từ schema TS)

- `id` (id)
- `user_id` (userId)
- `organization_id` (organizationId)
- `shop_id` (shopId)
- `created_at` (createdAt)
- `updated_at` (updatedAt)
- `user_cleared_at` (userClearedAt)
- `id` (id)
- `thread_id` (threadId)
- `role` (role)
- `content` (content)
- `created_at` (createdAt)

## Tham chiếu (references → bảng Drizzle)

- `agentChatThreadsTable`
- `organizationsTable`
- `shopsTable`
- `usersTable`

Tổng quan quan hệ: `tham-chieu/co-so-du-lieu-goc/README.md`.
