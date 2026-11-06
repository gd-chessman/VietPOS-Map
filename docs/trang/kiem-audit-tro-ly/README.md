# Trang giao diện: `agent-chat-audit.tsx`

**Mô tả:** Xem lịch sử hội thoại Trợ lý AI đã lưu. (URL /agent-chat-audit, AgentChatAuditPage, ~269 dòng).

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/agent-chat-audit.tsx`

**Đường dẫn URL:** `/agent-chat-audit`
**Tên component React:** `AgentChatAuditPage`
**Quy mô:** ~269 dòng.

## Thông tin hiển thị

Nội dung người dùng **nhìn thấy** trên màn hình (trích nhãn từ TSX; số liệu động từ API).

### `agent-chat-audit.tsx`

**Tiêu đề trang:** “Lịch sử chat Trợ lý AI”
**Thẻ / chỉ số (CardTitle):**
- Theo tài khoản

## Thao tác người dùng

Hành động chính (nút, menu, mục dialog) — không liệt kê mọi nút icon-only.

### `agent-chat-audit.tsx`

**Thao tác:**
- Trợ lý AI
- setPage((p) => Math.max(0, p - 1))} > Trước
- = pageCount} onClick= > Sau
- setDeleteConfirmOpen(true)} > Xóa hẳn
- setOpenThreadId(null)}> Đóng
- Huỷ

**Hộp thoại (tiêu đề):**
- Xóa vĩnh viễn hội thoại #{openThreadId}?

**Đường dẫn:** `/agent-chat-audit`

Xem lịch sử hội thoại Trợ lý AI đã lưu.

## Component con (logic UI chính)

- `@/components/ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `@/components/ui/alert-dialog` → `artifacts/pos-app/src/components/ui/alert-dialog.tsx`
- `@/components/ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `@/components/ui/dialog` → `artifacts/pos-app/src/components/ui/dialog.tsx`

## Cách đọc code

- API: tìm `useQuery`, `useMutation`, `apiFetch`, hoặc mục **Chuỗi `/api/...`** bên dưới.
- Quyền: `lib/session-permissions.ts`, biểu thức trong `app-layout.tsx` và file page.
- Offline: các trang POS có thể gọi Dexie qua `@/lib/offline/...`.

## Module API liên quan (trong Map)

- [`agent`](../../module-api/tro-ly-ai-api/) — nhóm `/api/agent`

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

## Quyền (phát hiện trong source)

- Có kiểm tra role **`super_admin`** (hoặc redirect dashboard).

## Redirect trong component

- → `/dashboard`

## JSX component dùng trong file (PascalCase)

- `<AlertDialog />`
- `<AlertDialogAction />`
- `<AlertDialogCancel />`
- `<AlertDialogContent />`
- `<AlertDialogDescription />`
- `<AlertDialogFooter />`
- `<AlertDialogHeader />`
- `<AlertDialogTitle />`
- `<ArrowLeft />`
- `<Bot />`
- `<Button />`
- `<Card />`
- `<CardContent />`
- `<CardDescription />`
- `<CardHeader />`
- `<CardTitle />`
- `<Dialog />`
- `<DialogContent />`
- `<DialogFooter />`
- `<DialogHeader />`
- `<DialogTitle />`
- `<Link />`
- `<ScrollText />`
- `<Trash2 />`

## Dialog / modal (tiêu đề)

- Xóa vĩnh viễn hội thoại #{openThreadId}?

## Import chính (đầu file)

- `import { useState } from "react";`
- `import { Link, Redirect } from "wouter";`
- `import { useQuery, useQueryClient } from "@tanstack/react-query";`
- `import { format } from "date-fns";`
- `import { ArrowLeft, Bot, ScrollText, Trash2 } from "lucide-react";`
- `import { Button } from "@/components/ui/button";`
- `import {`
- `import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";`
- `import {`
- `import { useSessionUser } from "@/lib/use-session-user";`
- `import { useToast } from "@/hooks/use-toast";`
- `import { apiDelete, apiGet } from "@/lib/sales-api";`
- `import { renderAssistantContent } from "@/lib/agent-assistant-content";`
- `import { cn } from "@/lib/utils";`

## Module `@/lib/...` được import

- `@/lib/agent-assistant-content`
- `@/lib/sales-api`
- `@/lib/use-session-user`
- `@/lib/utils`

## Component `@/components/...` (đã quét API lớp 1)

- `ui/button` → `artifacts/pos-app/src/components/ui/button.tsx`
- `ui/alert-dialog` → `artifacts/pos-app/src/components/ui/alert-dialog.tsx`
- `ui/card` → `artifacts/pos-app/src/components/ui/card.tsx`
- `ui/dialog` → `artifacts/pos-app/src/components/ui/dialog.tsx`

## Chuỗi `/api/...` (page + component con, 3 mục)

- `/api/agent/chat/audit/threads/${openThreadId}` → [`agent`](../../module-api/tro-ly-ai-api/)
- `/api/agent/chat/audit/threads/${openThreadId}/messages?limit=500` → [`agent`](../../module-api/tro-ly-ai-api/)
- `/api/agent/chat/audit/threads?limit=${limit}&offset=${page * limit}` → [`agent`](../../module-api/tro-ly-ai-api/)

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
