# Kiến trúc runtime

**Mô tả:** Sơ đồ runtime: client React → Express API → PostgreSQL; tùy chọn cloud-sync Railway.

```
Client (Browser / Tauri)
  → pos-app (React, Vite)
  → /api/* → api-server (Express 5)
  → @workspace/db (Drizzle) → PostgreSQL 16
  → (optional) cloud-sync → Railway Postgres
```

**Build prod:** web static trong container nginx; API node dist/index.mjs.

**Auth:** JWT middleware; cookie/session tùy endpoint public.

Xem thêm: `reference/architecture.md`.
