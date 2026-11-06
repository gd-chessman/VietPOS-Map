# VietPOS-Map

Bản đồ tài liệu **VietPOS** — mục lục dài (gồm **chỉ mục ~235 endpoint**), **~250+ file** chi tiết theo code Shop.

**Bắt đầu:** [docs/00-muc-luc-va-kien-truc.md](docs/00-muc-luc-va-kien-truc.md) (~200 dòng mục lục)

| Thư mục | Nội dung |
|---------|----------|
| `docs/he-thong/` | Kiến trúc, workspace, Docker |
| `docs/nghiep-vu/` | Luồng POS, kho, HĐ VAT (12 chương) |
| `docs/api-modules/` | **Từng file** `routes/*.ts` + bảng endpoint |
| `docs/frontend-pages/` | **Từng file** `pages/*.tsx` + import/API trích |
| `docs/lib-modules/` | **Từng file** `api-server/src/lib/**/*.ts` |
| `docs/schema/` | **Từng file** Drizzle schema + cột + FK |
| `docs/reference/` | Mirror doc gốc Shop (architecture, rbac, …) |

Sau khi đổi code Shop: `python3 docs/gen.py`
