# Thư viện: `dashboard-visitor-stats.ts`

**Mô tả:** [Chuỗi cửa hàng] dashboard-visitor-stats.ts — visitDateString, visitorsPerBuyer, sumVisitorsForShopOnDate, visitorsByShopOnDate, sumVisitorsForShopsOnDate, ….

**Chủ đề:** [Chuỗi cửa hàng](../../chuyen-de/chuoi-cua-hang/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/dashboard-visitor-stats.ts` · **Quy mô:** ~240 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (12)

- `visitDateString`
- `visitorsPerBuyer`
- `sumVisitorsForShopOnDate`
- `visitorsByShopOnDate`
- `sumVisitorsForShopsOnDate`
- `sumVisitorsForChainScopeOnDate`
- `visitDateRangeFromChartBuckets`
- `sumVisitorsForShopBetweenVisitDates`
- `visitorsGroupedByVisitDateForShop`
- `visitorsGroupedByVisitDateForChainScope`
- `sumVisitorsForChartBucket`
- `sumVisitorsForChainScopeBetweenVisitDates`

## Import cơ sở dữ liệu

- `import { db, shopDailyVisitorCountsTable } from "@workspace/db";`

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Chuỗi cửa hàng](../../chuyen-de/chuoi-cua-hang/)
