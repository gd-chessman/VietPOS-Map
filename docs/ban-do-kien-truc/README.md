# Bản đồ kiến trúc (hình)

**Mô tả:** Sơ đồ **vẽ bằng ký tự** — hiển thị trực tiếp trong Cursor/GitHub, không cần plugin Mermaid.

← [Trang chủ Map](README.md) · [Hướng dẫn đọc](huong-dan-doc/README.md)

---

## 1. Hệ thống VietPOS (runtime)

```
┌─────────────────────────────────────────────────────────────────┐
│                     MÁY NGƯỜI DÙNG                            │
│  ┌──────────────┐      ┌──────────────────┐                     │
│  │ Trình duyệt  │      │ IndexedDB        │                     │
│  │ hoặc Tauri   │─────▶│ (offline: đơn,   │                     │
│  │              │      │  HĐ chờ sync)    │                     │
│  └──────┬───────┘      └────────▲─────────┘                     │
│         │                       │ pull / push                   │
│         │  HTTPS  /api/*        │                               │
│         ▼                       │                               │
└─────────┼───────────────────────┼───────────────────────────────┘
          │                       │
          ▼                       │
┌─────────────────────────────────┴───────────────────────────────┐
│                      api-server (Express)                        │
│   JWT · quyền shop · Viettel/CQT · nghiệp vụ POS/kho/HĐ VAT      │
└─────────┬───────────────────────────────┬───────────────────────┘
          │ Drizzle                         │ cloud-sync (tùy chọn)
          ▼                                 ▼
┌──────────────────┐              ┌──────────────────┐
│ PostgreSQL       │              │ Postgres cloud   │
│ (máy chủ shop)   │─────────────▶│ (Railway, ops)   │
└──────────────────┘   mirror     └──────────────────┘

     Widget Android / ESP32 ──API key──▶ visitor-counts, widget/home
```

| Thành phần | Ghi chú |
|------------|---------|
| **pos-app** | React — POS, kho, HĐ, cấu hình chuỗi |
| **api-server** | Một cửa `/api` cho mọi nghiệp vụ |
| **local-db + sync** | Quầy vẫn bán khi mất mạng |
| **cloud-sync** | Sao chép DB lên cloud (không thay thế DB local) |

*Phiên bản Mermaid (nếu IDE hỗ trợ):* [chuyen-de/kien-truc-he-thong/README.md](chuyen-de/kien-truc-he-thong/README.md)

---

## 2. Bản đồ tài liệu VietPOS-Map (cách đi)

```
                    ┌─────────────────────────────┐
                    │  ban-do-kien-truc/README.md (đây)  │
                    │  sơ đồ hình + hướng dẫn     │
                    └──────────────┬──────────────┘
                                   │
         ┌─────────────────────────┼─────────────────────────┐
         ▼                         ▼                         ▼
┌─────────────────┐    ┌──────────────────────┐    ┌─────────────────┐
│ 00-huong-dan    │    │ 00-muc-luc (trang    │    │ chuyen-de/      │
│ (3 bước đọc)    │    │ chủ Map)             │    │ 10 hub chủ đề   │
└────────┬────────┘    └──────────┬───────────┘    └────────┬────────┘
         │                        │                         │
         │            chọn 1 chủ đề (POS, HĐ đầu vào…)     │
         │                        └────────────┬────────────┘
         │                                     ▼
         │              ┌──────────────────────────────────────────┐
         │              │  Trên mỗi hub, đọc theo thứ tự:           │
         │              │  ① nghiep-vu/  →  ② frontend-pages/      │
         │              │  →  ③ api-modules/  →  ④ schema/        │
         │              │  →  ⑤ lib-modules/ (một phần)             │
         │              └────────────────────┬─────────────────────┘
         │                                   │
         │         cần tra hết URL / file    ▼
         │              ┌──────────────────────────────────────────┐
         └─────────────▶│  chi-muc/  (danh sách dài, tách riêng)   │
                        │  · api-modules · trang-giao-dien          │
                        │  · thu-vien-backend · schema · endpoint   │
                        └──────────────────────────────────────────┘

   reference/  = doc gốc Shop (tiếng Anh) — RBAC, database, Docker
```

---

## 3. Hub chủ đề (chọn một nhánh)

```
                    [00-muc-luc / chuyen-de]
                              │
    ┌────────────┬────────────┼────────────┬────────────┐
    ▼            ▼            ▼            ▼            ▼
 Đăng nhập     POS &       Sản phẩm    HĐ đầu vào   HĐ bán ra
 & phiên       đơn hàng    & kho       (VAT mua)    (Viettel)
    │            │            │            │            │
    └────────────┴────────────┴────────────┴────────────┘
                              │
         Chuỗi shop · An ninh · Offline · Trợ lý/widget
```

Danh sách link: [00-muc-luc → Chủ đề](README.md)

---

## 4. Luồng dữ liệu HĐ đầu vào (tóm tắt)

```
 PDF / Excel / CQT sync
         │
         ▼
  vat_inbound_invoices (Postgres)
         │
         ├── MST lọc? ──▶ archived → tab "Khác"
         │
         ▼
  Ghép dòng SP (stock-receipt) → nhập kho (receive-stock) → tồn + giá vốn
```

Chi tiết: [hoa-don-dau-vao](../chuyen-de/hoa-don-dau-vao/README.md)
