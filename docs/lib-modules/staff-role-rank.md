# Lib: `staff-role-rank.ts`

**Mô tả:** Logic backend staff-role-rank.ts (~18 dòng) — export: roleRank, callerCanManageTargetRole.

**Source Shop:** `artifacts/api-server/src/lib/staff-role-rank.ts`

**Độ lớn:** ~18 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (2 symbol)

- `roleRank`
- `callerCanManageTargetRole`

## Xem trước đầu file

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
