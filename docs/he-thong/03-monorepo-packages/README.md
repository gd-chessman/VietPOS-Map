# Gói trong monorepo Shop

**Mô tả:** Cấu trúc pnpm workspace: artifacts, lib, scripts trong Shop-Manager.

Monorepo **pnpm** — một repo chứa API, giao diện, thư viện dùng chung.

| Nhóm | Thành phần |
|------|------------|
| **artifacts** | `api-server`, `pos-app`, `pos-desktop`, `mockup-sandbox` |
| **lib** | `db`, `local-db`, `sync`, `api-zod`, `api-spec`, `api-client-react` |
| **scripts** | seed DB, helper Docker |

Khai báo workspace: `Shop-Manager-System-Offline/pnpm-workspace.yaml`.

**Đọc tiếp:** [04-docker-va-cloud-sync](04-docker-va-cloud-sync.md) · Tour code: `tham-chieu/api-server/README.md`, `tham-chieu/pos-app/README.md`
