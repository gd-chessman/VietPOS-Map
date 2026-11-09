# An ninh và chặn truy cập

**Mô tả:** Chặn IP/thiết bị, quan sát truy cập, super_admin.

**Về trang chủ Map:** [README.md](../../README.md) · [Hướng dẫn đọc](../../huong-dan-doc/)

Denylist chạy **trước** router API — 403 ngay nếu bị chặn.

## 1. Luồng nghiệp vụ (đọc trước)

- [10-truy-cap-an-ninh](../../nghiep-vu/10-truy-cap-an-ninh/) — Chặn IP/thiết bị, quan sát truy cập và RBAC liên quan.

## 2. Màn hình (giao diện)

- [chan-truy-cap](../../trang/chan-truy-cap/) — Chặn IP/thiết bị và tab tổng quan truy cập bất thường.

## 3. Module API

- [chan-ip-api](../../module-api/chan-ip-api/) — Module API blocked-ips.ts — 3 endpoint. Danh sách IP bị chặn toàn cục trên mọi request /api/*. -…
- [chan-thiet-bi-api](../../module-api/chan-thiet-bi-api/) — Module API blocked-devices.ts — 3 endpoint. Danh sách Device ID (header client) bị chặn mọi…
- [quan-sat-truy-cap](../../module-api/quan-sat-truy-cap/) — Module API access-observations.ts — 1 endpoint. Tổng hợp cặp (deviceId, IP) đã gọi API…

## 4. Bảng dữ liệu (schema)

- [ip-bi-chan](../../co-so-du-lieu/ip-bi-chan/) — Drizzle blockedIps.ts — 1 bảng, 5 cột, 1 index (blocked_ips).
- [thiet-bi-bi-chan](../../co-so-du-lieu/thiet-bi-bi-chan/) — Drizzle blockedDevices.ts — 1 bảng, 5 cột, 1 index (blocked_devices).

## 5. Thư viện backend (một số file quan trọng)

Tra cứu đủ: [README.md](../../chi-muc/thu-vien-backend/)

- [api-access-observations](../../thu-vien/api-access-observations/) — [An ninh] api-access-observations.ts — recordApiAccessObservation…
- [device-denylist](../../thu-vien/device-denylist/) — [An ninh] device-denylist.ts — blockedDeviceCount, normalizeDeviceId…
- [ip-denylist](../../thu-vien/ip-denylist/) — [An ninh] ip-denylist.ts — normalizeClientIp, blockedIpCount, clientIpFromRequest…

---

*Sinh tự động — `python3 docs/gen.py`*
