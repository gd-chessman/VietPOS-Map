# Lib: `user-notifications.ts`

**Mô tả:** Logic backend user-notifications.ts (~1266 dòng) — export: formatVatInboundInvoiceCode, clearVatInboundReceiptActiveNotifications, notifyVatInboundReceiptMapped, notifyVatInboundReceiptExcluded, noti…

**Source Shop:** `artifacts/api-server/src/lib/user-notifications.ts`

**Độ lớn:** ~1266 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (35 symbol)

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

## Import DB / schema

- `} from "@workspace/db";`
- `import type { Order } from "@workspace/db";`

## Xem trước đầu file

```typescript
import {
  db,
  userNotificationsTable,
  usersTable,
  shopsTable,
  formatPaymentSplitsLabel,
  resolveOrderPayments,
  type PaymentMethodCode,
} from "@workspace/db";
import { and, eq, inArray, isNull, sql } from "drizzle-orm";
import type { Order } from "@workspace/db";
import { getHubShopIdForOrg } from "../middlewares/auth";
import { resolveOrganizationIdForShop } from "./viettel-sinvoice/config";
import { sendOrderEmail, sendSimpleOperationalEmail } from "../email";
import { recordEmailSystemFailure } from "./system-event-log";
import {
  getNotificationChannelFlags,
  getRecipientRolesForNotification,
  type RecipientRoleKey,
} from "./platform-notification-settings";

export type ChainOrderEmailDetail = {
  items: Array<{ productName: string; quantity: number; price: number }>;
  note: string | null;
  createdAt: string;
  paymentMethod: string;
};

export type NotificationSeverity = "info" | "warning" | "error";

export type EmitNotificationInput = {
  userIds: number[];
  shopId: number;
  notificationKey: string;
  type: string;
```
