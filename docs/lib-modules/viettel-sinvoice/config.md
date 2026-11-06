# Lib: `viettel-sinvoice/config.ts`

**Mô tả:** Logic backend viettel-sinvoice/config.ts (~163 dòng) — export: toGdtPortalTaxCode, loadOrgViettelRow, resolveOrganizationIdForShop, getViettelInboundConfig, getViettelSinvoiceConfig, ….

**Source Shop:** `artifacts/api-server/src/lib/viettel-sinvoice/config.ts`

**Độ lớn:** ~163 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (8 symbol)

- `toGdtPortalTaxCode`
- `loadOrgViettelRow`
- `resolveOrganizationIdForShop`
- `getViettelInboundConfig`
- `getViettelSinvoiceConfig`
- `resolveGdtTaxCodeForOrganization`
- `viettelConfigErrorMessage`
- `viettelInboundConfigErrorMessage`

## Import DB / schema

- `import { db, organizationsTable, shopsTable } from "@workspace/db";`

## Xem trước đầu file

```typescript
import { db, organizationsTable, shopsTable } from "@workspace/db";
import { eq } from "drizzle-orm";

export type ViettelAuthConfig = {
  /** Invoice API base, e.g. …/services/einvoiceapplication/api */
  apiBaseUrl: string;
  /** Auth API base (login), e.g. https://api-vinvoice.viettel.vn */
  authBaseUrl: string;
  username: string;
  password: string;
};

export type ViettelSinvoiceConfig = ViettelAuthConfig & {
  supplierTaxCode: string;
  templateCode: string;
  invoiceSeries: string;
  invoiceType: string;
};

export type ViettelInboundConfig = ViettelAuthConfig & {
  supplierTaxCode: string;
  /** MST tài khoản CQT (hoadondientu) — có thể khác mã chi nhánh Viettel. */
  gdtTaxCode: string;
};

const DEFAULT_API_BASE_URL =
  "https://api-vinvoice.viettel.vn/services/einvoiceapplication/api";

const orgViettelSelect = {
  viettelInvoiceApiUrl: organizationsTable.viettelInvoiceApiUrl,
  viettelInvoiceAuthUrl: organizationsTable.viettelInvoiceAuthUrl,
  viettelInvoiceUsername: organizationsTable.viettelInvoiceUsername,
  viettelInvoicePassword: organizationsTable.viettelInvoicePassword,
  viettelInvoiceTaxCode: organizationsTable.viettelInvoiceTaxCode,
  viettelInvoiceTemplateCode: organizationsTable.viettelInvoiceTemplateCode,
```
