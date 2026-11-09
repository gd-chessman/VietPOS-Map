# Trang giao diện: `lan-devices.tsx`

**Mô tả:** Thiết bị LAN peer (in, widget nội bộ).

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/lan-devices.tsx`

**Đường dẫn URL:** `/lan-devices`
**Tên component React:** `LanDevicesPage`
**Quy mô:** ~382 dòng.

## Thông tin hiển thị

Nội dung người dùng **nhìn thấy** trên màn hình (trích nhãn từ TSX; số liệu động từ API).

### `lan-devices.tsx`

**Tiêu đề trang:** “Thiết bị LAN”, “Thiết bị của bạn”, “Máy khác trên Wi‑Fi )}”
**Tab / khu vực:**
- Máy quầy
- Điện thoại
**Tooltip / mô tả ngắn (title=):**
- Đang trên LAN

## Thao tác người dùng

Hành động chính (nút, menu, mục dialog) — không liệt kê mọi nút icon-only.

**Đường dẫn:** `/lan-devices`

Thiết bị LAN peer (in, widget nội bộ).

## Component con (logic UI chính)

- `@/components/ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `@/components/ui/badge` → `artifacts/pos-app/src/components/ui/badge.tsx`
- `@/components/ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `@/components/ui/tabs` → `artifacts/pos-app/src/components/ui/tabs.tsx`
- `@/components/lan/LanDevicesPhoneTab` → `artifacts/pos-app/src/components/lan/LanDevicesPhoneTab.tsx`

## Cách đọc code

- API: tìm `useQuery`, `useMutation`, `apiFetch`, hoặc mục **Chuỗi `/api/...`** bên dưới.
- Quyền: `lib/session-permissions.ts`, biểu thức trong `app-layout.tsx` và file page.
- Offline: các trang POS có thể gọi Dexie qua `@/lib/offline/...`.

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

## Tab UI (`TabsTrigger` value)

- `desktops`
- `phones`

## Redirect trong component

- → `/dashboard`

## JSX component dùng trong file (PascalCase)

- `<Badge />`
- `<Button />`
- `<Card />`
- `<CardContent />`
- `<CardHeader />`
- `<CardTitle />`
- `<CircleDot />`
- `<Copy />`
- `<DetailRow />`
- `<Icon />`
- `<Info />`
- `<LanDevicesPhoneTab />`
- `<LanPeer />`
- `<Laptop />`
- `<Monitor />`
- `<NetworkHero />`
- `<PeerCard />`
- `<Radio />`
- `<Router />`
- `<Smartphone />`
- `<Sparkles />`
- `<Tabs />`
- `<TabsContent />`
- `<TabsList />`
- `<TabsTrigger />`
- … 3 component khác

## Import chính (đầu file)

- `import { useEffect, useMemo, useState } from "react";`
- `import { Redirect } from "wouter";`
- `import {`
- `import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";`
- `import { Badge } from "@/components/ui/badge";`
- `import { Button } from "@/components/ui/button";`
- `import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";`
- `import { LanDevicesPhoneTab } from "@/components/lan/LanDevicesPhoneTab";`
- `import { cn } from "@/lib/utils";`
- `import { getOrCreateDeviceId } from "@/lib/device/device-id";`
- `import { isTauriRuntime } from "@/lib/tauri-runtime";`
- `import { LAN_DISCOVERY_PORT, lanPeerList, lanPlatformLabel, type LanPeer } from "@/lib/tauri-lan-peers";`
- `import { LAN_PEER_PING_INTERVAL_MS, LAN_PEER_TTL_SECS } from "@/hooks/useLanPeerAnnounce";`
- `import { useToast } from "@/hooks/use-toast";`

## Module `@/lib/...` được import

- `@/lib/device/device-id`
- `@/lib/tauri-lan-peers`
- `@/lib/tauri-runtime`
- `@/lib/utils`

## Component `@/components/...` (đã quét API lớp 1)

- `ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `ui/badge` → `artifacts/pos-app/src/components/ui/badge.tsx`
- `ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `ui/tabs` → `artifacts/pos-app/src/components/ui/tabs.tsx`
- `lan/LanDevicesPhoneTab` → `artifacts/pos-app/src/components/lan/LanDevicesPhoneTab.tsx`

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
