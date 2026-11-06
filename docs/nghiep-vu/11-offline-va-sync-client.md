# Offline và sync client

**Mô tả:** IndexedDB local-db, checkout offline, pull/push sync với server.

- IndexedDB (`local-db`): orders pending, vat inbound local copy, outbox.
- `lib/sync`: pull/push theo endpoint `sync.ts`.
- POS checkout **không** chờ sync worker — ghi local trước.

**Mirror:** `reference/offline-first.md`, `offline-first-audit.md`.
