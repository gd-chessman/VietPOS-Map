# Trang giao diện: `agent-assistant.tsx`

**Mô tả:** Trợ lý AI chat + panel trạng thái hệ thống (DB, cloud sync, shop online). (URL /agent-assistant, AgentAssistantPage, ~419 dòng).

**Mã nguồn Shop:** `artifacts/pos-app/src/pages/agent-assistant.tsx`

**Đường dẫn URL:** `/agent-assistant`
**Tên component React:** `AgentAssistantPage`
**Quy mô:** ~419 dòng.

**Đường dẫn:** `/agent-assistant`

Trợ lý AI + panel hệ thống (DB, cloud sync URL, shops online). Chat khi đã cấu hình LLM org.

**Đọc tiếp:** [Hướng dẫn đọc Map](../../huong-dan-doc/)

## Quyền (phát hiện trong source)

- Có kiểm tra role **`super_admin`** (hoặc redirect dashboard).

## Redirect trong component

- → `/dashboard`

## JSX component dùng trong file (PascalCase)

- `<Activity />`
- `<AgentAssistantSettingsDialog />`
- `<AgentChatPanel />`
- `<AgentSystemInfo />`
- `<AlertDialog />`
- `<AlertDialogAction />`
- `<AlertDialogCancel />`
- `<AlertDialogContent />`
- `<AlertDialogDescription />`
- `<AlertDialogFooter />`
- `<AlertDialogHeader />`
- `<AlertDialogTitle />`
- `<AlertTriangle />`
- `<Badge />`
- `<Bot />`
- `<Button />`
- `<Card />`
- `<CardContent />`
- `<CardDescription />`
- `<CardHeader />`
- `<CardTitle />`
- `<CheckCircle2 />`
- `<Cloud />`
- `<Database />`
- `<HTMLTextAreaElement />`
- … 9 component khác

## Dialog / modal (tiêu đề)

- Ẩn hội thoại trên màn hình?

## Import chính (đầu file)

- `import { useEffect, useState } from "react";`
- `import { Link, Redirect } from "wouter";`
- `import { useQuery } from "@tanstack/react-query";`
- `import {`
- `import { AgentAssistantSettingsDialog } from "@/components/AgentAssistantSettingsDialog";`
- `import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";`
- `import { Badge } from "@/components/ui/badge";`
- `import { Button } from "@/components/ui/button";`
- `import {`
- `import { AgentChatPanel } from "@/components/AgentChatPanel";`
- `import { useAgentChat } from "@/hooks/use-agent-chat";`
- `import { useSessionUser } from "@/lib/use-session-user";`
- `import { apiGet } from "@/lib/sales-api";`
- `import { canUseAgentAssistant, getAgentQuickPrompts } from "@/lib/agent-assistant-access";`
- `import { cn } from "@/lib/utils";`
- `import { AGENT_ASSISTANT_FOCUS_CHAT_EVENT } from "@/lib/pos-keyboard-shortcuts";`

## Module `@/lib/...` được import

- `@/lib/agent-assistant-access`
- `@/lib/pos-keyboard-shortcuts`
- `@/lib/sales-api`
- `@/lib/use-session-user`
- `@/lib/utils`

## Chuỗi `/api/...` (page + component con, 6 mục)

- `/api/agent/assistant-access` → [`agent`](../../module-api/tro-ly-ai-api/)
- `/api/agent/assistant-access?organizationId=${selectedOrgId}` → [`agent`](../../module-api/tro-ly-ai-api/)
- `/api/agent/chat/system` → [`agent`](../../module-api/tro-ly-ai-api/)
- `/api/organizations`
- `/api/organizations/${selectedOrgId}`
- `/api/organizations/current`

## Liên kết mã

- Khai báo URL: `artifacts/pos-app/src/App.tsx`
- Menu/layout: `components/layout/app-layout.tsx`
- Phiên đăng nhập: `lib/session-cache.ts`, `lib/use-session-user.ts`
