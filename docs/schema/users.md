# Schema: `users`

**Mô tả:** Drizzle schema users.ts — 13 cột trên 1 bảng Postgres (users).

**Source Shop:** `lib/db/src/schema/users.ts`

## Bảng Postgres

- `users`

## Cột (trích từ schema TS)

- `id` (id)
- `name` (name)
- `email` (email)
- `password` (password)
- `role` (role)
- `status` (status)
- `organization_id` (organizationId)
- `shop_id` (shopId)
- `pin_hash` (pinHash)
- `pin_set_at` (pinSetAt)
- `pin_failed_attempts` (pinFailedAttempts)
- `pin_locked_until` (pinLockedUntil)
- `agent_assistant_enabled` (agentAssistantEnabled)

## Tham chiếu (references → bảng Drizzle)

- `organizationsTable`
- `shopsTable`

Tổng quan quan hệ: `reference/database.md`.
