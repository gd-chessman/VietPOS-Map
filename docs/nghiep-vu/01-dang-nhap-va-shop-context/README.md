# Đăng nhập và ngữ cảnh shop

**Mô tả:** Đăng nhập, JWT gắn shop/role, hub shop và ngữ cảnh vận hành API.

- User đăng nhập email/mật khẩu (`POST /api/auth/login`).
- JWT gắn **shop_id**, **role**, **organization_id** (nếu có).
- Hầu hết API dùng `requireOperationalContext` — mọi thao tác gắn shop đang chọn.
- **Hub shop** (chi nhánh chính): HĐ đầu vào, một số cấu hình chuỗi.
- Offline: không login user mới; checkout vẫn ghi local nếu đã có session.

**Code:** `middlewares/auth.ts`, `pages/login.tsx`, `lib/session-cache.ts`.
