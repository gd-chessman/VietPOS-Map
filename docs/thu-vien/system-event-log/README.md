# Thư viện: `system-event-log.ts`

**Mô tả:** [Kiến trúc / dùng chung] system-event-log.ts — recordSystemEvent, recordEmailSystemFailure, recordEmailSmtpNotConfigured, recordVatSystemEvent, recordSyncSystemEvent, ….

**Chủ đề:** [Kiến trúc / dùng chung](../../chuyen-de/kien-truc-he-thong/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/system-event-log.ts` · **Quy mô:** ~177 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (6)

- `recordSystemEvent`
- `recordEmailSystemFailure`
- `recordEmailSmtpNotConfigured`
- `recordVatSystemEvent`
- `recordSyncSystemEvent`
- `recordApiSystemEvent`

## Import cơ sở dữ liệu

- `import { db, shopsTable, systemEventLogsTable, type SystemEventCategory, type SystemEventSeverity } from "@workspace/db";`

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Kiến trúc / dùng chung](../../chuyen-de/kien-truc-he-thong/)
