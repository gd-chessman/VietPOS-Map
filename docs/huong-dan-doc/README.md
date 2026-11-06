# Hướng dẫn đọc VietPOS-Map

**Mô tả:** Ba bước đọc Map — không cần lướt ~250 file trên một trang.

---

## Cách đọc (3 bước)

| Bước | Làm gì | Mở thư mục |
|------|--------|------------|
| **1** | Xem **bản đồ hình** + kiến trúc | [README.md](../ban-do-kien-truc/) (ASCII) · [kien-truc-he-thong](../chuyen-de/kien-truc-he-thong/) (Mermaid) |
| **2** | Chọn **một chủ đề** gần việc bạn làm | [Danh sách chủ đề](../README.md#chủ-đề-chuyen-de) |
| **3** | Sửa code → tra **chỉ mục kỹ thuật** | [chi-muc/danh-sach-api](../chi-muc/danh-sach-api/) và các chỉ mục cùng cấp |

**Không nên:** mở `thu-vien/` và đọc lần lượt mọi README — mỗi hub chủ đề chỉ liệt kê lib **liên quan**.

---

## Trong mỗi hub chủ đề (`chuyen-de/…/README.md`)

Thứ tự gợi ý:

1. **Luồng nghiệp vụ** (`nghiep-vu/…`) — *tại sao / quy trình*
2. **Màn hình** (`trang/…`) — *người dùng thao tác ở đâu*
3. **Module API** (`module-api/…`) — *endpoint nào*
4. **Schema** (`co-so-du-lieu/…`) — *bảng Postgres*
5. **Thư viện** (`thu-vien/…`) — *logic phức tạp* (subset)

---

## Tài liệu gốc tiếng Anh

`tham-chieu/…/README.md` = bản sao doc Shop. Dùng khi cần RBAC, database tổng thể, Docker — xem mục tham chiếu trên [bản đồ chính](../README.md).

---

## Tạo lại Map

```bash
python3 docs/gen.py
```

→ [Bản đồ chính](../README.md)
