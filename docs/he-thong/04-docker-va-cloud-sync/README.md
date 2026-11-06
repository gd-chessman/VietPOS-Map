# Docker và đồng bộ cloud

**Mô tả:** Docker Compose local, biến CLOUD_DATABASE_URL, worker cloud-sync và Trợ lý AI.

Compose local thường gồm: Postgres (cổng **5434**), init schema, **api** (**3002**), **web** (**8080**), service **cloud-sync**.

- Worker **cloud-sync** chạy `scripts/cloud-sync.sh`, khóa `_sync_lock`, cần `CLOUD_DATABASE_URL` trỏ Postgres cloud (Railway).
- Trạng thái «đã cấu hình cloud» trên POS/Trợ lý AI đọc biến môi trường trên container **api** (không chỉ cloud-sync).

**Đọc tiếp:** `tham-chieu/docker-may-chu/README.md`, `tham-chieu/running-local/README.md` · Nghiệp vụ offline: [nghiep-vu/11](../nghiep-vu/11-offline-va-sync-client/README.md)
