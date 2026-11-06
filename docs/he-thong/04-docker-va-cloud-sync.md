# Docker và cloud sync

**Mô tả:** Docker Compose local, biến CLOUD_DATABASE_URL, worker cloud-sync và Trợ lý AI.

Compose: postgres (5434), init, api (3002), web (8080), cloud-sync.

**cloud-sync:** `scripts/cloud-sync.sh`, khóa `_sync_lock`, CLOUD_DATABASE_URL public Railway.

POS hiển thị trạng thái: Trợ lý AI ← env trên container **api**.

Mirror: `reference/docker-may-chu.md`, `reference/running-local.md`.
