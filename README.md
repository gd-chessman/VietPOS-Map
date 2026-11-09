# VietPOS-Map

Bản đồ tài liệu **VietPOS** (tiếng Việt) — mỗi chủ đề một **thư mục**, nội dung trong **`README.md`**.

## Đọc theo thứ tự

1. **[Bản đồ chính](docs/README.md)** — mục lục và hub chủ đề
2. **[index.html](index.html)** — cửa vào: bản đồ runtime + lộ trình đọc + 10 hub (gốc VietPOS-Map)
3. [Bản đồ hình ASCII + Mermaid click](docs/ban-do-kien-truc/README.md)
4. [Hướng dẫn 3 bước](docs/huong-dan-doc/README.md)
5. [Kiến trúc Mermaid (click node)](docs/chuyen-de/kien-truc-he-thong/README.md)
6. Chọn **hub** trong `docs/chuyen-de/…/` (POS, HĐ đầu vào, chuỗi…)
7. Tra cứu sâu: [chi-muc/danh-sach-api](docs/chi-muc/danh-sach-api/README.md) và các chỉ mục cùng cấp

| Thư mục | Ý nghĩa |
|---------|---------|
| `docs/chuyen-de/` | Hub theo chủ đề |
| `docs/nghiep-vu/` | Luồng nghiệp vụ 01→12 |
| `docs/trang/` | Màn hình POS/admin |
| `docs/module-api/` | Module HTTP `/api` |
| `docs/co-so-du-lieu/` | Schema Postgres |
| `docs/thu-vien/` | Thư viện backend |
| `docs/chi-muc/` | Chỉ mục dài |
| `docs/tham-chieu/` | Doc gốc Shop (tiếng Anh) |

```bash
python3 docs/gen.py
```

Tạo lại toàn bộ README sau khi sửa code Shop.
