# Thư viện: `user-notifications.ts`

**Mô tả:** [Đăng nhập & phiên] user-notifications.ts — formatVatInboundInvoiceCode, clearVatInboundReceiptActiveNotifications, notifyVatInboundReceiptMapped, notifyVatInboundReceiptExcluded…

**Chủ đề:** [Đăng nhập & phiên](../../chuyen-de/dang-nhap-va-phien/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/user-notifications.ts` · **Quy mô:** ~1266 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (35)

- `formatVatInboundInvoiceCode`
- `clearVatInboundReceiptActiveNotifications`
- `notifyVatInboundReceiptMapped`
- `notifyVatInboundReceiptExcluded`
- `notifyVatInboundReceiptPartial`
- `notifyVatInboundReceiptReceived`
- `notifyVatInboundReceiptClosedShort`
- `clearVatInboundReceiptProgressNotifications`
- `notifyVatInboundReceiptDeNghi`
- `clearVatInboundReceiptDeNghiNotification`
- `notifyVatInboundAutoSyncNewInvoices`
- `notifyVatInboundAutoProcessResults`
- `listChainOversightRecipientIds`
- `loadChainOversightEmails`
- `formatOrderOversightPaymentLabel`
- `notifySuperAdminNewOrder`
- `notifyOrderCancelRequested`
- `notifyOrderReprint`
- `notifyOrderPaymentChange`
- `notifyPosCartClear`
- `notifyPosCartItemRemove`
- `notifyProductDiscontinued`
- `emitUserNotifications`
- `removeNotificationsByKeys`
- `removeNotificationsByKeyPrefix`
- `ensureVatInvoicePendingNotification`
- `notifyVatInvoicePending`
- `notifyVatInvoiceFailed`
- `notifyVatInvoiceIssued`
- `clearVatOrderNotifications`
- `notifyStockRequestPending`
- `clearStockRequestNotification`
- `notifyInventoryManualAdjust`
- `scheduleManagerInventoryManualAdjust`
- `scheduleNotification`

## Import cơ sở dữ liệu

- `} from "@workspace/db";`
- `import type { Order } from "@workspace/db";`

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Đăng nhập & phiên](../../chuyen-de/dang-nhap-va-phien/)
