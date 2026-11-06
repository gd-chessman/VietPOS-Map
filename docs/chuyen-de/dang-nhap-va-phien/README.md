# Đăng nhập và phiên làm việc

**Mô tả:** JWT, shop đang chọn, hub shop, quyền menu.

**Về trang chủ Map:** [README.md](../../README.md) · [Hướng dẫn đọc](../../huong-dan-doc/)

Mọi API gần như đều gắn **shop_id** và **role** sau khi đăng nhập.

## 1. Luồng nghiệp vụ (đọc trước)

- [01-dang-nhap-va-shop-context](../../nghiep-vu/01-dang-nhap-va-shop-context/) — Đăng nhập, JWT gắn shop/role, hub shop và ngữ cảnh vận hành API.

## 2. Màn hình (giao diện)

- [dang-nhap](../../trang/dang-nhap/) — Đăng nhập email/PIN, lưu phiên thiết bị. (URL /login, Login, ~1080 dòng).
- [quyen-cua-toi](../../trang/quyen-cua-toi/) — Giải thích quyền role và menu hiện tại. (URL /my-permissions, MyPermissions, ~767 dòng).

## 3. Module API

- [xac-thuc](../../module-api/xac-thuc/) — Module API auth.ts — 8 endpoint. Đăng nhập, JWT, PIN, phiên người dùng.
- [cua-hang](../../module-api/cua-hang/) — Module API shops.ts — 3 endpoint. Danh sách shop user được truy cập.

## 4. Bảng dữ liệu (schema)

- [nguoi-dung](../../co-so-du-lieu/nguoi-dung/) — Drizzle schema users.ts — 13 cột trên 1 bảng Postgres (users).
- [cua-hang-db](../../co-so-du-lieu/cua-hang-db/) — Drizzle schema shops.ts — 31 cột trên 1 bảng Postgres (shops).

## 5. Thư viện backend (một số file quan trọng)

Tra cứu đủ: [README.md](../../chi-muc/thu-vien-backend/)

- [pin-challenge](../../thu-vien/pin-challenge/) — [Đăng nhập & phiên] pin-challenge.ts — PIN_CHALLENGE_PURPOSE, signPinChallengeToken, veri…
- [pin-reset-requests](../../thu-vien/pin-reset-requests/) — [Đăng nhập & phiên] pin-reset-requests.ts — upsertPendingPinResetRequest, canSetPinWithou…
- [session-cookie](../../thu-vien/session-cookie/) — [Đăng nhập & phiên] session-cookie.ts — SESSION_COOKIE_NAME, setSessionCookie, clearSessi…
- [user-pin](../../thu-vien/user-pin/) — [Đăng nhập & phiên] user-pin.ts — PIN_LENGTH, roleRequiresPin, normalizePin, validatePinF…

---

*Sinh tự động — `python3 docs/gen.py`*
