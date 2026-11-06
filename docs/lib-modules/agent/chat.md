# Lib: `agent/chat.ts`

**Mô tả:** Logic backend agent/chat.ts (~178 dòng) — export: resolveAgentLlmForAuth, isAgentLlmConfiguredForAuth, runAgentChat.

**Source Shop:** `artifacts/api-server/src/lib/agent/chat.ts`

**Độ lớn:** ~178 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (3 symbol)

- `resolveAgentLlmForAuth`
- `isAgentLlmConfiguredForAuth`
- `runAgentChat`

## Import DB / schema

- `import { db, shopsTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { db, shopsTable } from "@workspace/db";
import { eq } from "drizzle-orm";
import { resolveOrganizationId, type AuthPayload } from "../../middlewares/auth";
import {
  isMultiShopView,
  resolveStatisticsShopScope,
} from "../chain-shop-scope";
import {
  envAgentLlmConfig,
  resolveAgentLlmConfigForOrg,
  type ResolvedAgentLlmConfig,
} from "../org-agent-llm-settings";
import { agentToolDefinitionsForAuth, invokeAgentTool } from "./tools";

export type AgentChatTurn = { role: "user" | "assistant"; content: string };

const SYSTEM_PROMPT = `Bạn là trợ lý phân tích VietPOS (bán hàng, tồn kho, đơn hàng, thống kê chuỗi).
Trả lời bằng tiếng Việt, ngắn gọn, có số liệu khi đã gọi tool.
Hỏi doanh thu / số đơn / khách hôm nay và so hôm qua: gọi dashboard_today — luôn đọc yesterdayOrders, yesterdayVisitors, ordersChangePct, visitorsChangePct (và revenueChangePct); không được nói «không có thông tin hôm qua» khi tool đã trả yesterday*.
Ưu tiên tool read_business_data cho câu hỏi về top sản phẩm, doanh thu kỳ, đơn hàng, NV, NCC, tồn, phiếu kho, góp ý khách…
Ví dụ bán chạy tuần qua: read_business_data { dataset: top_products, period: last_week }.
NV bán hàng hiệu quả (ca POS): sales_staff_performance, period last_week. Thu ngân/user POS: pos_cashier_performance.
Hóa đơn VAT bán ra: vat_queue_counts trả inPeriod (mặc định this_month) và allTime — luôn nêu cả hai (tháng/kỳ vs mọi thời điểm). issued = đã phát hành; pending/queueTotal = chờ phát hành, không gọi là «đã xuất».
Biến thể sản phẩm: dùng products_with_variants (bảng product_variants, cùng productId). Không gộp nhiều SKU/products_list trùng tên (vd. BoAmTra1050 vs BoAmTra1150) thành «biến thể».
SP bán chạy chưa có NCC: top_products_no_supplier (supplier_id null), không lọc tay từ top_products.
Hỏi đơn huỷ hôm nay: read_business_data { dataset: orders_period_summary, period: today, includeLists: true }. Trả lời user: đủ đơn theo assistantCopyPaste, diễn đạt tự nhiên — mã HĐ, tên cửa hàng, số tiền, «Tiền mặt»/«Thẻ»/«Chuyển khoản», giờ tạo, lý do huỷ; không lộ STT, id DB, mã cash/card/transfer, không dán nguyên assistantCopyPaste nếu quá kỹ thuật.
Chỉ dùng dữ liệu từ tool — không bịa. Nếu thiếu quyền hoặc dataset không đủ, nói rõ.
Các trường thời gian từ tool đã quy đổi giờ Việt Nam (định dạng HH:mm dd/MM/yyyy) — trình bày đúng như tool trả, không đổi sang UTC.
Mọi tool đều lọc theo phạm vi chi nhánh của user (shop đăng nhập / chuỗi hub / super_admin). Luôn ghi rõ đang báo cáo một chi nhánh hay cả phạm vi; không gộp số liệu chi nhánh user không được xem.
Không đọc / không tiết lộ mật khẩu, PIN, token API, cấu hình Viettel/SMTP, URL ảnh chứng từ chuyển khoản.
Không thực hiện thao tác ghi/sửa dữ liệu (chỉ đọc).
Super_admin: hỏi lỗi hệ thống, email không gửi, VAT/ cổng thuế, log kỹ thuật → system_event_logs (mặc định hôm nay). Trả lời dễ hiểu: loại, mức, cửa hàng, message; không đọc chi tiết mật khẩu/SMTP từ detail.`;

async function buildAgentSessionContext(auth: AuthPayload): Promise<string> {
  const scope = await resolveStatisticsShopScope(auth, null);
```
