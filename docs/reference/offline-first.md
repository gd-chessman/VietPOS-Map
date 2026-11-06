<!-- Mirror: Shop-Manager-System-Offline/docs/offline-first.md -->

# Offline-first (PWA + IndexedDB)

**Mô tả:** Bản mirror doc Shop docs/offline-first.md — Offline-first (PWA + IndexedDB).

## Decision

VietPOS POS tại quầy chuyển sang **offline-first** với:

- **PWA** — cache shell app qua Service Worker
- **IndexedDB (Dexie)** — catalog, tồn kho, đơn pending, phiên ca
- **Sync outbox** — đẩy đơn lên Express API khi có mạng
- **Idempotency** — header `Idempotency-Key` + bảng `order_sync_keys` trên Postgres

Web admin (`artifacts/pos-app`) giữ nguyên; offline ưu tiên luồng **POS checkout**.

## Packages

| Package | Role |
|---------|------|
| `lib/local-db` | Dexie schema + helpers |
| `lib/sync` | Pull catalog, push pending orders, sync worker |
| `artifacts/pos-app` | PWA + UI banner + offline checkout |

## API

- `GET /api/sync/catalog?since=` — snapshot catalog + inventory
- `GET /api/sync/shift-orders?shiftSessionId=` — đơn trong ca (cache offline)
- `POST /api/orders` + `Idempotency-Key` — tạo đơn idempotent khi sync

## Phases

1. **Phase 0** — local-db, sync, PWA scaffold, banner
2. **Phase 1** — checkout offline + sync queue
3. **Phase 2** — phiên ca + lịch sử đơn trong ca offline

## Conflict policy (v1)

Server thắng trên tồn kho. Đơn conflict được đánh dấu `conflict` trong IndexedDB để xử lý thủ công.
