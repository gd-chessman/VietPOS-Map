# Lib: `vietnam-calendar.ts`

**Mô tả:** Logic backend vietnam-calendar.ts (~105 dòng) — export: VN_TZ, formatVnDateTime, vnCalendarDay, vnAddCalendarDays, vnDayStartFromInstant, ….

**Source Shop:** `artifacts/api-server/src/lib/vietnam-calendar.ts`

**Độ lớn:** ~105 dòng.

Thư viện backend dùng chung giữa nhiều route handler — đọc file gốc để biết thuật toán đầy đủ.

## Export (11 symbol)

- `VN_TZ`
- `formatVnDateTime`
- `vnCalendarDay`
- `vnAddCalendarDays`
- `vnDayStartFromInstant`
- `vnDayEndInclusiveFromInstant`
- `vnWeekday`
- `vnYmdToParts`
- `vnDaysBetweenInclusive`
- `vnDayBoundsExclusive`
- `buildVietnamCalendarDayHourBuckets`

## Xem trước đầu file

```typescript
export const VN_TZ = "Asia/Ho_Chi_Minh";

type VnDateTimeInput = string | Date | null | undefined;

/** `HH:mm dd/MM/yyyy` theo múi giờ Việt Nam (email, báo cáo server). */
export function formatVnDateTime(input: VnDateTimeInput): string {
  if (input == null || input === "") return "—";
  const d = input instanceof Date ? input : new Date(input);
  if (Number.isNaN(d.getTime())) return "—";
  const parts = new Intl.DateTimeFormat("en-GB", {
    timeZone: VN_TZ,
    hour: "2-digit",
    minute: "2-digit",
    day: "2-digit",
    month: "2-digit",
    year: "numeric",
    hour12: false,
  }).formatToParts(d);
  const pick = (type: Intl.DateTimeFormatPartTypes) =>
    parts.find((p) => p.type === type)?.value ?? "";
  return `${pick("hour")}:${pick("minute")} ${pick("day")}/${pick("month")}/${pick("year")}`;
}

/** yyyy-MM-dd theo lịch Việt Nam. */
export function vnCalendarDay(d = new Date()): string {
  return d.toLocaleDateString("en-CA", { timeZone: VN_TZ });
}

/** Cộng/trừ ngày trên lịch VN (yyyy-MM-dd). */
export function vnAddCalendarDays(ymd: string, days: number): string {
  const anchor = new Date(`${ymd}T12:00:00.000+07:00`);
  anchor.setTime(anchor.getTime() + days * 86_400_000);
  return vnCalendarDay(anchor);
}

```
