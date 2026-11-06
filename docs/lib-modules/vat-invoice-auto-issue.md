# Lib: `vat-invoice-auto-issue.ts`

**Mô tả:** Logic backend vat-invoice-auto-issue.ts (~172 dòng) — export: AUTO_ISSUE_BATCH_MINUTE_OF_DAY_VN, minutesOfDayVN, orderPurchaseAt, isEligiblePurchaseDayForAutoIssue, isPurchaseTodayVN, ….

**Source Shop:** `artifacts/api-server/src/lib/vat-invoice-auto-issue.ts`

**Độ lớn:** ~172 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (12 symbol)

- `AUTO_ISSUE_BATCH_MINUTE_OF_DAY_VN`
- `minutesOfDayVN`
- `orderPurchaseAt`
- `isEligiblePurchaseDayForAutoIssue`
- `isPurchaseTodayVN`
- `endOfPurchaseDayIssueCutoffVN`
- `isLateNightPurchaseVN`
- `isDayBatchIssueWindow`
- `computeAutoIssueAt`
- `isReadyForAutoIssue`
- `runVatInvoiceAutoIssueBatch`
- `startVatInvoiceAutoIssueScheduler`

## Import DB / schema

- `import { db, ordersTable, shopsTable, usersTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { db, ordersTable, shopsTable, usersTable } from "@workspace/db";
import { and, eq, isNull, sql } from "drizzle-orm";
import { VAT_INVOICE_PUBLIC_EDIT_WINDOW_MS } from "./vat-invoice-public-window";
import { validateBuyerInvoiceForIssue, resolveInvoiceStatus, isActivelyIssuing } from "./vat-invoice";
import { issueViettelInvoiceForOrder } from "./viettel-sinvoice/issue";
import { logger } from "./logger";

const VN_TZ = "Asia/Ho_Chi_Minh";
const TICK_MS = 60_000;
/** Từ 23:55 (VN): quét xuất hết đơn trong ngày mua; đơn tạo 23:55–24:00 xuất ngay. */
export const AUTO_ISSUE_BATCH_MINUTE_OF_DAY_VN = 23 * 60 + 55;
let timer: ReturnType<typeof setInterval> | null = null;
let running = false;

function vnCalendarDay(d: Date): string {
  return d.toLocaleDateString("en-CA", { timeZone: VN_TZ });
}

/** Phút trong ngày theo giờ VN (0–1439). */
export function minutesOfDayVN(d: Date): number {
  const parts = new Intl.DateTimeFormat("en-US", {
    timeZone: VN_TZ,
    hour: "numeric",
    minute: "numeric",
    hour12: false,
  }).formatToParts(d);
  const hour = Number(parts.find((p) => p.type === "hour")?.value ?? 0);
  const minute = Number(parts.find((p) => p.type === "minute")?.value ?? 0);
  return hour * 60 + minute;
}

export function orderPurchaseAt(order: { clientCreatedAt: Date | null; createdAt: Date }): Date {
  return order.clientCreatedAt ?? order.createdAt;
}

```
