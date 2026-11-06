# Lib: `org-viettel-settings.ts`

**Mô tả:** Logic backend org-viettel-settings.ts (~126 dòng) — export: viettelConfigReadiness, stripOrgViettelPassword, toPublicViettelSettings, applyViettelSettingsFromBody.

**Source Shop:** `artifacts/api-server/src/lib/org-viettel-settings.ts`

**Độ lớn:** ~126 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (4 symbol)

- `viettelConfigReadiness`
- `stripOrgViettelPassword`
- `toPublicViettelSettings`
- `applyViettelSettingsFromBody`

## Xem trước đầu file

```typescript
export type OrgViettelDbFields = {
  viettelInvoiceApiUrl?: string | null;
  viettelInvoiceAuthUrl?: string | null;
  viettelInvoiceUsername?: string | null;
  viettelInvoicePassword?: string | null;
  viettelInvoiceTaxCode?: string | null;
  viettelInvoiceTemplateCode?: string | null;
  viettelInvoiceSeries?: string | null;
  viettelInvoiceType?: string | null;
  viettelInvoiceGdtTaxCode?: string | null;
};

export type ViettelInvoiceSettingsPublic = {
  apiUrl: string | null;
  authUrl: string | null;
  username: string | null;
  taxCode: string | null;
  templateCode: string | null;
  series: string | null;
  invoiceType: string | null;
  gdtTaxCode: string | null;
  passwordConfigured: boolean;
};

export type ViettelConfigReadiness = {
  /** Đủ để phát hành HĐĐT bán ra (Viettel SInvoice). */
  outboundReady: boolean;
  /** Đủ tài khoản/MST Viettel để gọi API (PDF đầu vào, kiểm tra HĐ). */
  inboundApiReady: boolean;
  /** Có MST cổng thuế (cấu hình Viettel hoặc MST tổ chức) để đồng bộ HĐ đầu vào. */
  inboundTaxPortalReady: boolean;
};

export function viettelConfigReadiness(
  settings: ViettelInvoiceSettingsPublic,
```
