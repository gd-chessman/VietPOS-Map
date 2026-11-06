# Thư viện: `weighted-average-cost.ts`

**Mô tả:** [Sản phẩm & kho] weighted-average-cost.ts — roundMoney2, weightedAverageCost, reverseWeightedAverageCost.

**Chủ đề:** [Sản phẩm & kho](../../chuyen-de/san-pham-va-kho/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/weighted-average-cost.ts` · **Quy mô:** ~47 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (3)

- `roundMoney2`
- `weightedAverageCost`
- `reverseWeightedAverageCost`

## Trích mã (tham khảo)

```typescript
/** Làm tròn tiền 2 chữ số — khớp cột numeric(12, 2). */
export function roundMoney2(n: number): number {
  return Math.round((n + Number.EPSILON) * 100) / 100;
}

/**
 * Bình quân gia quyền giá vốn khi nhập kho:
 * (tồn cũ × giá vốn cũ + SL nhập × giá nhập) / (tồn cũ + SL nhập).
 *
 * Tồn âm (bán vượt) được coi là 0 — lần nhập đó lấy giá nhập làm giá vốn.
 */
export function weightedAverageCost(
  oldQty: number,
  oldCost: number,
  inboundQty: number,
  inboundCost: number,
): number {
  const inbound = Math.max(0, inboundQty);
  const onHand = Number.isFinite(oldQty) ? Math.max(0, oldQty) : 0;
  const prevCost = Number.isFinite(oldCost) ? oldCost : 0;
  const nextCost = Number.isFinite(inboundCost) ? inboundCost : 0;
  if (inbound <= 0) return roundMoney2(prevCost);
  const denom = onHand + inbound;
  if (denom <= 0) return roundMoney2(nextCost);
  return roundMoney2((onHand * prevCost + inbound * nextCost) / denom);
}

/**
 * Đảo ngược BQGQ khi rollback nhập kho (ước lượng khi không có sổ giá vốn).
 * prevCost ≈ (tồn hiện tại × giá vốn hiện tại − SL rollback × giá nhập) / (tồn − SL).
 */
export function reverseWeightedAverageCost(
  currentQty: number,
  currentCost: number,
  rollbackQty: number,
  inboundCost: number,
): number {
  const qty = Number.isFinite(currentQty) ? currentQty : 0;
  const cost = Number.isFinite(currentCost) ? currentCost : 0;
  const delta = Math.max(0, rollbackQty);
  const inbound = Number.isFinite(inboundCost) ? inboundCost : 0;
  if (delta <= 0) return roundMoney2(cost);
  const prevQty = qty - delta;
  if (prevQty <= 0) return roundMoney2(inbound);
  return roundMoney2((qty * cost - delta * inbound) / prevQty);
```

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Sản phẩm & kho](../../chuyen-de/san-pham-va-kho/)
