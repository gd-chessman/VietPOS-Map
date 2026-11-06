# Thư viện: `vat-invoice-auto-issue.ts`

**Mô tả:** [Hóa đơn bán ra] vat-invoice-auto-issue.ts — AUTO_ISSUE_BATCH_MINUTE_OF_DAY_VN, minutesOfDayVN, orderPurchaseAt, isEligiblePurchaseDayForAutoIssue, isPurchaseTodayVN, ….

**Chủ đề:** [Hóa đơn bán ra](../../chuyen-de/hoa-don-ban-ra/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/vat-invoice-auto-issue.ts` · **Quy mô:** ~172 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (12)

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

## Import cơ sở dữ liệu

- `import { db, ordersTable, shopsTable, usersTable } from "@workspace/db";`

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Hóa đơn bán ra](../../chuyen-de/hoa-don-ban-ra/)
