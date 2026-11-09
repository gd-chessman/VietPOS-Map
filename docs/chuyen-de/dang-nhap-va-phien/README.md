# Đăng nhập và phiên làm việc

**Mô tả:** JWT, shop đang chọn, hub shop, quyền menu.

**Về trang chủ Map:** [README.md](../../README.md) · [Hướng dẫn đọc](../../huong-dan-doc/)

Mọi API gần như đều gắn **shop_id** và **role** sau khi đăng nhập.

## 1. Luồng nghiệp vụ (đọc trước)

- [01-dang-nhap-va-shop-context](../../nghiep-vu/01-dang-nhap-va-shop-context/) — Đăng nhập, JWT gắn shop/role, hub shop và ngữ cảnh vận hành API.

## 2. Màn hình (giao diện)

- [dang-nhap](../../trang/dang-nhap/) — Đăng nhập email/PIN, lưu phiên thiết bị.
- [quyen-cua-toi](../../trang/quyen-cua-toi/) — Giải thích quyền role và menu hiện tại.

## 3. Module API

- [xac-thuc](../../module-api/xac-thuc/) — Đăng nhập, JWT, PIN, phiên người dùng.
- [cua-hang](../../module-api/cua-hang/) — Danh sách shop user được truy cập.

## 4. Bảng dữ liệu (schema)

- [nguoi-dung](../../co-so-du-lieu/nguoi-dung/) — Drizzle users.ts — 1 bảng, 13 cột, 2 enum, 2 index (users).
- [cua-hang-db](../../co-so-du-lieu/cua-hang-db/) — Drizzle shops.ts — 1 bảng, 31 cột (shops).

## 5. Thư viện backend (một số file quan trọng)

Tra cứu đủ: [README.md](../../chi-muc/thu-vien-backend/)

- [pin-challenge](../../thu-vien/pin-challenge/) — [Đăng nhập & phiên] pin-challenge.ts — PIN_CHALLENGE_PURPOSE, signPinChallengeToken…
- [pin-reset-requests](../../thu-vien/pin-reset-requests/) — [Đăng nhập & phiên] pin-reset-requests.ts — upsertPendingPinResetRequest…
- [session-cookie](../../thu-vien/session-cookie/) — [Đăng nhập & phiên] session-cookie.ts — SESSION_COOKIE_NAME, setSessionCookie…
- [user-pin](../../thu-vien/user-pin/) — [Đăng nhập & phiên] user-pin.ts — PIN_LENGTH, roleRequiresPin, normalizePin…

---

*Sinh tự động — `python3 docs/gen.py`*
