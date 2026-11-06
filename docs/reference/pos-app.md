<!-- Mirror: Shop-Manager-System-Offline/docs/code-tour/pos-app.md -->

# Code tour — POS web app (`artifacts/pos-app`)

**Mô tả:** Bản mirror doc Shop docs/code-tour/pos-app.md — Code tour — POS web app (artifacts/pos-app).

## What this package does

Single-page application for POS + store/chain management.

## Routing

File: `src/App.tsx`

Routes map 1:1 to business modules:

- `/login`: login
- `/`: dashboard
- `/pos`: POS selling screen
- `/products`: product catalog
- `/inventory`: inventory list/adjust
- `/orders`: orders list + cancel workflows
- `/stock-requests`: import/export requests
- `/statistics`: analytics
- `/reports`: staff reports
- `/staff`: staff management
- `/chain`: chain/multi-branch operations

## Authentication model

- Token is stored in `localStorage` under `pos_token`.
- Requests attach token as `Authorization: Bearer <token>`.

## Navigation & role-based access

File: `src/components/layout/app-layout.tsx`

This is the “menu policy” of the app:

- Defines which role sees which module.
- Shows pending stock-request count badge for approver roles.

## Key pages (business meaning)

- `src/pages/pos.tsx`
  - Core selling workflow: select products → create order → show receipt.
- `src/pages/orders.tsx`
  - Review orders, request cancel, approve/reject cancels (admin).
- `src/pages/products.tsx`
  - Create/import products, edit fields, discontinue/reactivate.
  - Also enforces UI permissions (who can add vs edit).
- `src/pages/inventory.tsx`
  - Shop inventory visibility and quantity adjustments.
- `src/pages/stock-requests.tsx`
  - Create and manage import/export requests and approvals.
- `src/pages/staff.tsx`
  - Shop staff CRUD.
- `src/pages/chain.tsx`
  - Organization/shop/warehouse + transfer workflows.
- `src/pages/dashboard.tsx`, `statistics.tsx`, `reports.tsx`
  - Operational reporting.

## Toast notifications

- `src/hooks/use-toast.ts` controls toast lifecycle (duration, removal).
- `src/components/ui/toast.tsx` controls appearance (including close `x`).

