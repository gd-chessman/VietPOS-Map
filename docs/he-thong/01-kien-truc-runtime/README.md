# Kiến trúc runtime

**Mô tả:** Sơ đồ runtime: client React → Express API → PostgreSQL; tùy chọn cloud-sync Railway.

Trình duyệt hoặc app desktop (Tauri) chạy **pos-app** (React). Mọi thao tác nghiệp vụ gọi **api-server** (Express) qua prefix `/api`, server đọc/ghi **PostgreSQL** qua Drizzle (`@workspace/db`).

```
Trình duyệt / Tauri
  → pos-app (React, Vite)
  → /api/* → api-server (Express 5)
  → @workspace/db (Drizzle) → PostgreSQL 16
  → (tùy chọn) cloud-sync → Postgres trên Railway
```

- **Production:** web build tĩnh phục vụ nginx; API chạy `dist/index.mjs`.
- **Xác thực:** JWT trên hầu hết route; một số route công khai (form HĐ, feedback) dùng cookie/session riêng.

**Đọc tiếp:** [02-workspace](02-workspace-luu-niem.md) · Tham chiếu gốc: `tham-chieu/architecture/README.md`
