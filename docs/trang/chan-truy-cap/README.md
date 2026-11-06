# Trang giao diện: `access-block.tsx`

**Mô tả:** Chặn IP/thiết bị và tab tổng quan truy cập bất thường. (URL /access-block, AccessBlockPage, ~78 dòng).

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/access-block.tsx`

**Đường dẫn URL:** `/access-block`
**Tên component React:** `AccessBlockPage`
**Quy mô:** ~78 dòng.

## Thông tin hiển thị

Nội dung người dùng **nhìn thấy** trên màn hình (trích nhãn từ TSX; số liệu động từ API).

### `access-block.tsx`

**Tiêu đề trang:** “Chặn truy cập”
**Tab / khu vực:**
- Tổng quan
- Chặn IP
- Chặn thiết bị

### `@/pages/ip-ban`

**Thẻ / chỉ số (CardTitle):**
- Thêm IP bị chặn
- Danh sách đang chặn
**Cột bảng:**
- IP
- Ghi chú
- Thêm lúc
- Người thêm
**Nhãn lọc / preset / placeholder:**
- Địa chỉ IP
- Ghi chú (tuỳ chọn)
- Ô nhập: Spam login, bot quét…
**Tooltip / mô tả ngắn (title=):**
- Bỏ chặn

### `@/pages/device-ban`

**Thẻ / chỉ số (CardTitle):**
- Thêm thiết bị bị chặn
- Danh sách đang chặn
**Cột bảng:**
- Tên thiết bị
- Device ID
- Ghi chú
- Thêm lúc
- Người thêm
**Nhãn lọc / preset / placeholder:**
- Device ID
- Ghi chú (tuỳ chọn)
- Ô nhập: pos-…
- Ô nhập: Máy lạ, đã thu hồi…
**Tooltip / mô tả ngắn (title=):**
- Bỏ chặn

### `@/pages/access-overview-section`

**Thẻ / chỉ số (CardTitle):**
- Thiết bị & IP gần đây
**Cột bảng:**
- Tên thiết bị
- Device ID
- IP
- Hôm nay
- 48h
- Lần cuối
- Thao tác

## Thao tác người dùng

Hành động chính (nút, menu, mục dialog) — không liệt kê mọi nút icon-only.

### `@/pages/ip-ban`

**Thao tác:**
- Chặn IP
- setConfirmRemove( )} >
- ); }} > Bỏ chặn
- Huỷ

**Hộp thoại (tiêu đề):**
- Bỏ chặn IP này?

### `@/pages/device-ban`

**Thao tác:**
- Chặn thiết bị
- setConfirmRemove( ) } >
- ); }} > Bỏ chặn
- Huỷ

**Hộp thoại (tiêu đề):**
- Bỏ chặn thiết bị này?

### `@/pages/access-overview-section`

**Thao tác:**
- void refetch()} > Làm mới
- Đã chặn IP
- setConfirmBlock( ) } > Chặn IP
- Đã chặn thiết bị
- setConfirmBlock( ) } > Chặn thiết bị
- Huỷ

**Đường dẫn:** `/access-block` (query `?tab=overview|ip|device`)

## Vai trò

Trang **quản trị hệ thống** gom ba màn con thành một: quan sát truy cập bất thường, quản lý denylist IP, denylist thiết bị.
Mọi denylist áp dụng **trước** handler API — client bị chặn nhận 403 trên `/api/*`.

## Quyền

| Điều kiện | Hành vi |
|-----------|---------|
| `user.role === "super_admin"` | Hiển thị đủ 3 tab |
| Role khác | `<Redirect to="/dashboard" />` ngay khi mount |

Menu sidebar: mục **Chặn truy cập** (`app-layout.tsx`, icon `Ban`) — `show: isSuperAdmin`.

## Cấu trúc UI

1. **Header:** tiêu đề + mô tả ngắn (mọi request `/api` bị từ chối nếu nằm trong denylist).
2. **Tabs (3 cột):**
   - **Tổng quan** → `<AccessOverviewSection />` — bảng quan sát, chặn nhanh.
   - **Chặn IP** → `<IpBanSection />` — CRUD `blocked_ips`.
   - **Chặn thiết bị** → `<DeviceBanSection />` — CRUD `blocked_devices`.

Tab mặc định: `initialTabFromSearch()` đọc `?tab=` (`ip` | `device` | mặc định `overview`).

## Route legacy (App.tsx)

| URL cũ | Chuyển tới |
|--------|------------|
| `/ip-ban` | `/access-block?tab=ip` |
| `/device-ban` | `/access-block?tab=device` |
| `/access-block/overview` | `/access-block?tab=overview` |

File `ip-ban.tsx` / `device-ban.tsx` vẫn tồn tại như **section export** (không còn route riêng).

## Luồng nghiệp vụ (tóm tắt)

```
Request /api/*
  → accessObservationMiddleware (ghi hit device+IP, RAM)
  → ipDenylistMiddleware (403 nếu IP trong DB/env)
  → deviceDenylistMiddleware (403 nếu device id trong DB)
  → router handlers
```

Super admin mở **Tổng quan** → thấy IP/device lạ → bấm **Chặn** → POST blocked-* → middleware refresh cache.

## API (spec đầy đủ trong Map)

Mỗi module có bảng endpoint + **body/response/mã lỗi** từng route:

- `module-api/chan-ip-api/README.md` — blocked-ips
- `module-api/chan-thiet-bi-api/README.md` — blocked-devices
- `module-api/quan-sat-truy-cap/README.md` — access-observations

## Đọc tiếp

- Nghiệp vu: `nghiep-vu/10-truy-cap-an-ninh/README.md`
- Lib: `thu-vien/ip-denylist/README.md`, `thu-vien/device-denylist/README.md`, `thu-vien/api-access-observations/README.md`
- Schema: `co-so-du-lieu/ip-bi-chan/README.md`, `co-so-du-lieu/thiet-bi-bi-chan/README.md`

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

## Quyền (phát hiện trong source)

- Có kiểm tra role **`super_admin`** (hoặc redirect dashboard).

## Tab UI (`TabsTrigger` value)

- `device`
- `ip`
- `overview`

## Query string URL

- Tab qua `?tab=` — xem `initialTabFromSearch` trong file.

## Redirect trong component

- → `/dashboard`

## JSX component dùng trong file (PascalCase)

- `<AccessOverviewSection />`
- `<Ban />`
- `<DeviceBanSection />`
- `<IpBanSection />`
- `<LayoutDashboard />`
- `<Smartphone />`
- `<Tabs />`
- `<TabsContent />`
- `<TabsList />`
- `<TabsTrigger />`

## Import chính (đầu file)

- `import { useMemo } from "react";`
- `import { Ban, LayoutDashboard, Smartphone } from "lucide-react";`
- `import { Redirect } from "wouter";`
- `import { useSessionUser } from "@/lib/use-session-user";`
- `import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";`
- `import { IpBanSection } from "@/pages/ip-ban";`
- `import { DeviceBanSection } from "@/pages/device-ban";`
- `import { AccessOverviewSection } from "@/pages/access-overview-section";`

## Module `@/lib/...` được import

- `@/lib/use-session-user`

## Chuỗi `/api/...` (page + component con, 5 mục)

- `/api/access-observations?limit=200`
- `/api/blocked-devices` → [`blocked-devices`](../../module-api/chan-thiet-bi-api/)
- `/api/blocked-devices/${id}` → [`blocked-devices`](../../module-api/chan-thiet-bi-api/)
- `/api/blocked-ips` → [`blocked-ips`](../../module-api/chan-ip-api/)
- `/api/blocked-ips/${id}` → [`blocked-ips`](../../module-api/chan-ip-api/)

## Luồng nghiệp vụ (doc)

- [10-truy-cap-an-ninh](../../nghiep-vu/10-truy-cap-an-ninh/)

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
