# Frontend: `login.tsx`

**Mô tả:** Đăng nhập email/PIN, lưu phiên thiết bị. (URL /login, Login, ~1080 dòng).

**Source Shop:** `artifacts/pos-app/src/pages/login.tsx`

**URL (wouter):** `/login`
**Component:** `Login`
**Độ lớn:** ~1080 dòng.

**Route:** `/login`

Email/password, PIN máy, tài khoản đã lưu trên thiết bị. JWT → `pos_token`.

## Quyền (phát hiện trong source)

- Có kiểm tra role **`super_admin`** (hoặc redirect dashboard).

## JSX component dùng trong file (PascalCase)

- `<Button />`
- `<Card />`
- `<CardContent />`
- `<CardDescription />`
- `<CardFooter />`
- `<CardHeader />`
- `<CardTitle />`
- `<DeviceBlockedScreen />`
- `<ForgotPinPasswordDialog />`
- `<Form />`
- `<FormControl />`
- `<FormField />`
- `<FormItem />`
- `<FormLabel />`
- `<FormMessage />`
- `<Input />`
- `<LoginFormValues />`
- `<PinCodeDialog />`
- `<SavedAccount />`
- `<SetPinWithPasswordDialog />`
- `<User />`
- `<UserCircle />`
- `<WifiOff />`

## Biểu thức quyền / guard trong file

- `requirePassword`
- `required`

## Import chính (đầu file)

- `import { useEffect, useRef, useState } from "react";`
- `import { useLocation } from "wouter";`
- `import { useForm } from "react-hook-form";`
- `import { zodResolver } from "@hookform/resolvers/zod";`
- `import * as z from "zod";`
- `import {`
- `import { useQueryClient } from "@tanstack/react-query";`
- `import { Button } from "@/components/ui/button";`
- `import { Input } from "@/components/ui/input";`
- `import { Card, CardContent, CardDescription, CardHeader, CardTitle, CardFooter } from "@/components/ui/card";`
- `import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from "@/components/ui/form";`
- `import { useToast } from "@/hooks/use-toast";`
- `import { UserCircle, WifiOff } from "lucide-react";`
- `import {`
- `import { syncAuthTokenGetter, clearAuthTokenGetter } from "@/lib/auth-session";`
- `import { isTauriRuntime } from "@/lib/tauri-runtime";`
- `import { roleRequiresPin, staffUsesDevicePin } from "@/lib/user-pin";`
- `import { hashDevicePin, verifyDevicePin } from "@/lib/staff-device-pin";`
- … 1 import khác

## Module `@/lib/...` được import

- `@/lib/auth-session`
- `@/lib/device/use-device-gate`
- `@/lib/home-path`
- `@/lib/offline`
- `@/lib/pin-lock`
- `@/lib/pin-reset-api`
- `@/lib/sales-api`
- `@/lib/session-cache`
- `@/lib/staff-device-pin`
- `@/lib/tauri-runtime`
- `@/lib/user-pin`

## Chuỗi `/api/...` (page + component con, 2 mục)

- `/api/auth/me` → [`api-modules/auth.md`](../api-modules/auth.md)
- `/api/auth/pin/set` → [`api-modules/auth.md`](../api-modules/auth.md)

## Luồng nghiệp vụ (doc)

- `nghiep-vu/01-dang-nhap-va-shop-context.md`

## File liên quan

- Route khai báo: `artifacts/pos-app/src/App.tsx`
- Layout/menu: `components/layout/app-layout.tsx`
- Session: `lib/session-cache.ts`, `lib/use-session-user.ts`
