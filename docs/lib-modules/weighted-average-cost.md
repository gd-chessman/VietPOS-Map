# Lib: `weighted-average-cost.ts`

**Mô tả:** Logic backend weighted-average-cost.ts (~47 dòng) — export: roundMoney2, weightedAverageCost, reverseWeightedAverageCost.

**Source Shop:** `artifacts/api-server/src/lib/weighted-average-cost.ts`

**Độ lớn:** ~47 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (3 symbol)

- `roundMoney2`
- `weightedAverageCost`
- `reverseWeightedAverageCost`

## Xem trước đầu file

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
```
