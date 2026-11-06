# Frontend: `access-block.tsx`

**Mô tả:** Chặn IP/thiết bị và tab tổng quan truy cập bất thường. (URL /access-block, AccessBlockPage, ~78 dòng).

**Source Shop:** `artifacts/pos-app/src/pages/access-block.tsx`

**URL (wouter):** `/access-block`
**Component:** `AccessBlockPage`
**Độ lớn:** ~78 dòng.

**Route:** `/access-block` (query `?tab=overview|ip|device`)

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

## Đọc tiếp

- Nghiệp vụ: `nghiep-vu/10-truy-cap-an-ninh.md`
- API: `api-modules/blocked-ips.md`, `blocked-devices.md`, `access-observations.md`
- Lib: `lib-modules/ip-denylist.md`, `device-denylist.md`, `api-access-observations.md`
- Schema: `schema/blockedIps.md`, `schema/blockedDevices.md`

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

## Luồng nghiệp vụ (doc)

- `nghiep-vu/10-truy-cap-an-ninh.md`

## File liên quan

- Route khai báo: `artifacts/pos-app/src/App.tsx`
- Layout/menu: `components/layout/app-layout.tsx`
- Session: `lib/session-cache.ts`, `lib/use-session-user.ts`
