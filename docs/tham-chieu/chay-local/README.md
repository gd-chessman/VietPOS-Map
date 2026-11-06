<!-- Mirror: Shop-Manager-System-Offline/docs/running-local.md -->

# Running locally (Windows + Docker)

**Mô tả:** Tài liệu tham chiếu gốc Shop docs/running-local.md — Running locally (Windows + Docker) (nội dung dưới thường tiếng Anh).

> **Ghi chú:** Phần dưới giữ nguyên tiếng Anh từ repo Shop (tham chiếu kỹ thuật). Luồng tiếng Việt ưu tiên đọc `nghiep-vu/` và `he-thong/`.

## Prerequisites

- Node.js (LTS recommended)
- `pnpm`
- Docker Desktop (must be running for the Postgres container)

## 1) Install dependencies

From repo root:

```powershell
pnpm install
```

## 2) Start Postgres (Docker)

The repo includes `docker-compose.yml` which starts Postgres 16.

```powershell
cd "C:\Users\Hp Omen\Shop-Manager-System-AI"
docker compose up -d
docker compose ps
```

Expected:

- container `shop-manager-postgres-ai` is **healthy**
- Postgres is exposed on host port **5434**

Connection string used by the app:

```
postgres://shop_manager:shop_manager@127.0.0.1:5434/shop_manager
```

## 3) Push schema (Drizzle)

```powershell
$env:DATABASE_URL="postgres://shop_manager:shop_manager@127.0.0.1:5434/shop_manager"
pnpm --filter @workspace/db run push
```

## 4) Seed data

### Minimal setup (one shop + super admin)

```powershell
$env:DATABASE_URL="postgres://shop_manager:shop_manager@127.0.0.1:5434/shop_manager"
pnpm --filter @workspace/scripts run seed:local
```

Default admin:

- email: `admin@pos.com`
- password: `admin123`

### Full dataset for Local Shop (`SHOP1`)

After minimal `seed:local` (or standalone), seeds products, inventory, staff, orders (14 days), shifts, and stock requests for org `LOCAL` / shop `SHOP1`. **Idempotent**.

```powershell
$env:DATABASE_URL="postgres://shop_manager:shop_manager@127.0.0.1:5434/shop_manager"
pnpm --filter @workspace/scripts run seed:local-full
```

Uses same env vars as `seed:local` (`SEED_ORG_CODE`, `SEED_SHOP_CODE`, `SEED_ADMIN_EMAIL`, `SEED_ADMIN_PASSWORD`).

Local shop accounts (password `admin123` unless `SEED_ADMIN_PASSWORD` is set):

| Email | Role |
|-------|------|
| `admin@pos.com` | super_admin |
| `admin.local@local.demo` | admin |
| `manager.local@local.demo` | manager |
| `warehouse.local@local.demo` | warehouse_keeper |
| `accountant.local@local.demo` | accountant |
| `staff.local@local.demo` | staff |

Login as `admin@pos.com` after this seed to see dashboard charts and orders for Local Shop.

### Full demo dataset (multi-branch chain)

Creates org `VIETPOS` with 3 branches (HUB, HN, CN), products, inventory, staff, orders (14 days), and stock requests. **Idempotent** — safe to run multiple times.

```powershell
$env:DATABASE_URL="postgres://shop_manager:shop_manager@127.0.0.1:5434/shop_manager"
pnpm --filter @workspace/scripts run seed:demo
```

Optional: `$env:SEED_DEMO_PASSWORD="yourpassword"` (min 6 chars; default `admin123`).

Demo accounts (password `admin123` unless overridden):

| Email | Role | Branch |
|-------|------|--------|
| `admin@pos.com` | super_admin | HUB |
| `admin.hub@vietpos.demo` | admin | HUB (chi nhánh chính) |
| `manager.hub@vietpos.demo` | manager | HUB |
| `warehouse.hub@vietpos.demo` | warehouse_keeper | HUB |
| `accountant.hub@vietpos.demo` | accountant | HUB |
| `staff.hub@vietpos.demo` | staff | HUB |
| `admin.hn@vietpos.demo` | admin | HN |
| `staff.hn@vietpos.demo` | staff | HN |
| `admin.cn@vietpos.demo` | admin | CN |

Branch admin emails must be **unique** within the organization (do not reuse `admin@pos.com` for branch admins).

## 5) Start backend API server

Recommended local env:

```powershell
$env:NODE_ENV="development"
$env:PORT="3003"
$env:SESSION_SECRET="dev-session-secret"
$env:DATABASE_URL="postgres://shop_manager:shop_manager@127.0.0.1:5434/shop_manager"
pnpm --filter @workspace/api-server run dev:win
```

Health check:

- `http://127.0.0.1:3003/api/healthz`

## 6) Start frontend POS app

Use a **separate terminal** (do not reuse `$env:PORT` from the API — Vite used to listen on 3003 and break `/api` proxy).

```powershell
pnpm --filter @workspace/pos-app run dev:win
```

Open:

- `http://127.0.0.1:5175/`

Proxy check (frontend → backend):

- `http://127.0.0.1:5175/api/healthz` should return `{"status":"ok"}`

## Common issues

### Cannot stop backend / Vite with Ctrl+C

```powershell
cd "C:\Users\Hp Omen\Shop-Manager-System-AI"
.\scripts\stop-dev-ports.ps1
```

### ERR_CONNECTION_REFUSED on `http://localhost:5175`

The frontend server is not running (or was stopped by `Ctrl+C`). Restart `pnpm --filter @workspace/pos-app run dev`.

### Vite shows `Local: http://localhost:3003/` (wrong port)

You still have `$env:PORT="3003"` in the same PowerShell session. Clear it and restart the frontend:

```powershell
Remove-Item Env:PORT -ErrorAction SilentlyContinue
pnpm --filter @workspace/pos-app run dev
```

Frontend must be on **5175**; API stays on **3003**.

### Vite proxy ECONNREFUSED / ENOBUFS `127.0.0.1:3003`

Backend is not running on port 3003, or frontend accidentally listens on 3003 (see above). Start the API server (step 5) and keep the terminal running.

### HTTP 500 on login with “Failed query … from users …”

The database is not reachable (Docker Desktop not running, Postgres container not started, wrong `DATABASE_URL`).

