# Schema: `orgGdtTaxSessions`

**Mô tả:** Drizzle orgGdtTaxSessions.ts — 1 bảng, 8 cột (org_gdt_tax_sessions).

**Mã nguồn Shop:** `lib/db/src/schema/orgGdtTaxSessions.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Liên kết nhanh

- **HTTP API:** [cong-cqt](../../module-api/cong-cqt/) (`routes/org-gdt-portal.ts`)

## Bảng `org_gdt_tax_sessions`

*Phiên JWT cổng hoadondientu.gdt.gov.vn theo tổ chức (sau «Kiểm tra kết nối»).*

- **Biến Drizzle:** `orgGdtTaxSessionsTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `id` | `id` | serial | **PK** | — | — |
| `organization_id` | `organizationId` | integer | NOT NULL | `organizations` | — |
| `gdt_access_token_enc` | `gdtAccessTokenEnc` | text | — | — | — |
| `gdt_token_expires_at` | `gdtTokenExpiresAt` | timestamp("gdt_token_expires_at", { withTimezone: true }) | — | — | — |
| `connected_at` | `connectedAt` | timestamp("connected_at", { withTimezone: true }) | — | — | — |
| `last_test_at` | `lastTestAt` | timestamp("last_test_at", { withTimezone: true }) | — | — | — |
| `last_test_ok` | `lastTestOk` | boolean | — | — | — |
| `updated_at` | `updatedAt` | timestamp("updated_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |

## Kiểu & Zod (insert)

- `export type OrgGdtTaxSessionRow`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
