<!-- Mirror: Shop-Manager-System-Offline/docs/docker-may-chu.md -->

# Chạy VietPOS bằng Docker (DB + API + Web) và đóng gói `.tar`

**Mô tả:** Bản mirror doc Shop docs/docker-may-chu.md — Chạy VietPOS bằng Docker (DB + API + Web) và đóng gói .tar.

Repo đã có `docker-compose.yml` gồm:

| Service | Image | Cổng host |
|---------|--------|-----------|
| `postgres` | `postgres:16-alpine` | **5434** → 5432 |
| `init` | `vietpos-init:latest` | (chạy 1 lần rồi thoát) |
| `api` | `vietpos-api:latest` | **3002** |
| `web` | `vietpos-web:latest` (Nginx) | **8080** → 80 |
| `cloud-sync` | `vietpos-cloud-sync:latest` | (đẩy DB → cloud theo chu kỳ) |

Trình duyệt / tunnel chỉ cần **8080** (Nginx phục vụ POS và proxy `/api` → API).

## A. Build & chạy trên cùng máy

```bash
cd /path/to/Shop-Manager-System-Offline
# tùy chọn: SESSION_SECRET / SEED_ADMIN_EMAIL / SEED_ADMIN_PASSWORD trong .env
docker compose up -d --build
```

Service **`init`** tự chạy mỗi lần `up` (nếu chưa hoàn thành trước đó / DB mới):

1. Đẩy schema (drizzle push)  
2. Nếu **chưa có** user `admin` / `super_admin` → tạo 1 admin (mặc định `admin@pos.com` / `admin123`)  
3. **Không** seed sản phẩm / NV demo  

Service **`cloud-sync`**: nếu `.env` có `CLOUD_DATABASE_URL` (URL **public** Railway), mỗi `CLOUD_SYNC_INTERVAL_SECONDS` (mặc định 30):

- Chỉ đẩy khi DB local **đã có khóa** (`_sync_lock`). Docker mới / volume trống / máy mới **không đẩy**; nếu cloud còn data thì **tự kéo cloud → local** rồi cấp khóa.
- So sánh bảng/cột → CREATE / DROP / RECREATE khi lệch  
- Merge dữ liệu theo PK → DELETE / UPDATE / INSERT (không TRUNCATE toàn DB)  
- Không set URL → container idle  

Cấp khóa:

```bash
# Đổi máy hoặc Docker chạy lại từ đầu (DB trống): kéo cloud xuống rồi tự cấp khóa
./scripts/cloud-sync.sh pull

# Máy này đã đúng data, muốn tiếp tục đẩy lên cloud
./scripts/cloud-sync.sh enable

# Dừng đẩy
./scripts/cloud-sync.sh disable
```

Log: `docker compose logs -f cloud-sync`.

Đã có admin → bỏ qua tạo user.

Mở: http://127.0.0.1:8080  

Đổi email/mật khẩu admin **lần đầu** (trước khi tạo):

```bash
export SEED_ADMIN_EMAIL="admin@cuahang.com"
export SEED_ADMIN_PASSWORD="mat-khau-manh"
docker compose up -d --build
```

Mirror cloud (trong `.env`):

```env
CLOUD_DATABASE_URL=postgresql://postgres:...@....proxy.rlwy.net:PORT/railway
CLOUD_SYNC_INTERVAL_SECONDS=30
# CLOUD_SYNC_FORCE=1   # chỉ khi cố ý đẩy local trống/ít đè cloud
```

**Khóa đồng bộ:** chưa có `_sync_lock` + DB mới (chưa đơn/SP) + cloud còn data → **tự kéo cloud → local**. Local đã có đơn/SP mà chưa khóa → không tự kéo, không đẩy (`enable` nếu máy đúng).

```bash
# 1) Postgres local đã chạy, có CLOUD_DATABASE_URL trong .env
./scripts/cloud-sync.sh pull    # kéo cloud → local và cấp khóa
# 2) cloud-sync (daemon) lần sau sẽ đẩy được
```

Chạy tay: `./scripts/cloud-sync.sh once` | `loop 30` | `pull` | `bootstrap`.

Chỉ bật Postgres (dev kiểu cũ):

```bash
docker compose up -d postgres
```

## B. Đóng image thành `.tar` mang sang máy khác

```bash
chmod +x scripts/docker-save-images.sh scripts/docker-load-images.sh
./scripts/docker-save-images.sh
```

Ra `dist-docker/`: api/web/init/cloud-sync + postgres tar + `docker-compose.yml`.

## C. Máy chủ: nạp tar và chạy

```bash
cd /path/to/dist-docker
./docker-load-images.sh .
```

Máy chủ **không cần** Node: `init` lo schema + admin nếu chưa có.

## D. Mạng

- LAN: `http://IP-máy-chủ:8080`
- Ngoài LAN: tunnel cổng **8080**
- **Không** public **5434**

## E. File liên quan

- `docker/Dockerfile.api` / `Dockerfile.web` / `Dockerfile.init` / `Dockerfile.cloud-sync`
- `docker/nginx.conf`
- `scripts/cloud-sync.sh` — mirror local → cloud (cùng logic Docker + chạy tay)
- `scripts/docker-save-images.sh` / `docker-load-images.sh`
