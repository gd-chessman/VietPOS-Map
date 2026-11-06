# Schema: `changeLog`

**Mô tả:** Drizzle changeLog.ts — 1 bảng, 6 cột, 2 index (change_log).

**Mã nguồn Shop:** `lib/db/src/schema/changeLog.ts`

## Cách đọc trang này

Mỗi **bảng Postgres** có bảng cột: kiểu Drizzle, `NOT NULL` / **PK**, khóa ngoại (cột FK → tên bảng đích), và ghi chú JSDoc từ mã nguồn. Enum và index được liệt kê riêng khi có trong file.

## Bảng `change_log`

*Append-only cursor log used by incremental catalog sync (GET /sync/catalog) to diff since a client's last-seen seq.*

- **Biến Drizzle:** `changeLogTable`

| Cột SQL | Thuộc tính TS | Kiểu | Ràng buộc | FK → bảng | Ghi chú |
|---------|---------------|------|-----------|-----------|---------|
| `seq` | `seq` | bigserial | **PK** | — | — |
| `shop_id` | `shopId` | integer | NOT NULL | `shops` | — |
| `entity_type` | `entityType` | text | NOT NULL | — | — |
| `entity_id` | `entityId` | integer | NOT NULL | — | — |
| `change_type` | `changeType` | text | NOT NULL | — | — |
| `created_at` | `createdAt` | timestamp("created_at", { withTimezone: true }) | NOT NULL, default `now()` | — | — |

**Index:**

- `change_log_shop_seq_idx` on `shopId`, `seq`
- `change_log_created_at_idx` on `createdAt`

## Kiểu & Zod (insert)

- `export type ChangeLogEntry`

Tổng quan ER / naming: [../../tham-chieu/co-so-du-lieu-goc/](../../tham-chieu/co-so-du-lieu-goc/).
