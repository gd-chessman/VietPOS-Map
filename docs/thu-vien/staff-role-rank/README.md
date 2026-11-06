# Thư viện: `staff-role-rank.ts`

**Mô tả:** [Kiến trúc / dùng chung] staff-role-rank.ts — roleRank, callerCanManageTargetRole.

**Chủ đề:** [Kiến trúc / dùng chung](../../chuyen-de/kien-truc-he-thong/)

**Mã nguồn Shop:** `artifacts/api-server/src/lib/staff-role-rank.ts` · **Quy mô:** ~18 dòng

File này là **tra cứu** khi đã đọc hub chủ đề và module API tương ứng. Thuật toán đầy đủ nằm trong mã TypeScript gốc.

## Hàm/hằng export (2)

- `roleRank`
- `callerCanManageTargetRole`

## Trích mã (tham khảo)

```typescript
const ROLE_RANK: Record<string, number> = {
  super_admin: 0,
  admin: 1,
  manager: 2,
  accountant: 3,
  warehouse_keeper: 4,
  staff: 5,
};

export function roleRank(role: string): number {
  return ROLE_RANK[role] ?? 99;
}

/** Người gọi chỉ quản lý được tài khoản có vai trò thấp hơn (rank lớn hơn). */
export function callerCanManageTargetRole(callerRole: string, targetRole: string): boolean {
  return roleRank(targetRole) > roleRank(callerRole);
}
```

← [Chỉ mục lib](../../chi-muc/thu-vien-backend/) · [Hub Kiến trúc / dùng chung](../../chuyen-de/kien-truc-he-thong/)
