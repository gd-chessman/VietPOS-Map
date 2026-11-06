<!-- Mirror: Shop-Manager-System-Offline/docs/public-access.md -->

# Public site local ra internet (cho người khác truy cập/test)

**Mô tả:** Tài liệu tham chiếu gốc Shop docs/public-access.md — Public site local ra internet (cho người khác truy cập/test) (nội dung dưới thường tiếng Anh).

> **Ghi chú:** Phần dưới giữ nguyên tiếng Anh từ repo Shop (tham chiếu kỹ thuật). Luồng tiếng Việt ưu tiên đọc `nghiep-vu/` và `he-thong/`.

Hướng dẫn này dùng cho mục đích **demo/test tạm thời** — cho người khác (ngoài mạng LAN) truy cập vào app đang chạy trên máy bạn, không cần deploy lên server thật.

> ⚠️ Chỉ dùng để demo/test. Không dùng cách này để vận hành cửa hàng thật lâu dài — xem phần [Khi nào cần deploy thật](#khi-nào-cần-deploy-thật-thay-vì-tunnel) ở cuối bài.

## Điều kiện cần trước

App phải đang chạy local theo hướng dẫn ở [README.md](../README.md):

- Backend API ở cổng **3003**
- Frontend POS app ở cổng **5175**

Kiểm tra 2 tiến trình đang chạy (PowerShell):

```powershell
netstat -ano | findstr ":3003 :5175"
```

Frontend (`vite.config.ts`) đã cấu hình sẵn `host: "0.0.0.0"`, `allowedHosts: true` và proxy `/api` → backend nội bộ. Vì vậy **chỉ cần public cổng 5175** — không cần expose cổng 3003 hay 5434 (Postgres) ra ngoài.

## Cách 1 — localtunnel (không cần cài đặt, chạy ngay)

Nhanh nhất, chạy trực tiếp qua `npx`, không cần tạo tài khoản.

```powershell
npx --yes localtunnel --port 5175
```

Output sẽ có dạng:

```
your url is: https://<random-name>.loca.lt
```

Gửi link này cho người cần test.

**Lưu ý:** người truy cập lần đầu sẽ thấy trang cảnh báo "Friendly Reminder" của localtunnel, yêu cầu nhập **Tunnel Password** — đó chính là **IP public** của máy đang chạy tunnel. Lấy IP này bằng:

```powershell
curl https://ipv4.icanhazip.com
```

Gửi kèm IP này cho người test (chỉ cần nhập 1 lần, trình duyệt sẽ nhớ).

Muốn cố định subdomain (để link không đổi mỗi lần chạy lại):

```powershell
npx --yes localtunnel --port 5175 --subdomain ten-shop-cua-ban
```

(Subdomain có thể bị người khác chiếm nếu đã có ai dùng trước — không đảm bảo 100%.)

## Cách 2 — Cloudflare Tunnel (ổn định hơn, không có trang cảnh báo)

Cài 1 lần:

```powershell
winget install --id Cloudflare.cloudflared
```

Chạy tunnel:

```powershell
cloudflared tunnel --url http://localhost:5175
```

Output sẽ in ra 1 link dạng `https://<random-name>.trycloudflare.com` — gửi link này cho người test. Không cần password, không giới hạn thời gian chạy.

**Tên miền thật** (tunnel cố định + DNS): xem [cloudflare-tunnel-domain.md](./cloudflare-tunnel-domain.md).

## Cách 3 — ngrok

Cần tạo tài khoản miễn phí tại ngrok.com và lấy authtoken trước khi dùng.

```powershell
ngrok config add-authtoken <your-authtoken>
ngrok http 5175
```

## Dừng public site

Chỉ cần dừng tiến trình tunnel đang chạy (`Ctrl+C` trong terminal đó, hoặc đóng terminal). Link public sẽ ngừng hoạt động ngay — 2 server local (3003, 5175) vẫn tiếp tục chạy bình thường cho bạn dùng.

## Lưu ý bảo mật

- **Không** chia sẻ file `.env` — chứa `DATABASE_URL`, `SESSION_SECRET` thật.
- `SESSION_SECRET` dùng trong lệnh dev (`dev-session-secret`) chỉ nên dùng cho local. Nếu để người ngoài truy cập, cân nhắc đổi sang giá trị ngẫu nhiên mạnh hơn.
- Tuyệt đối không expose cổng Postgres **5434** ra ngoài (không chạy `cloudflared`/`ngrok`/`localtunnel` trỏ vào cổng này).
- Máy bạn phải bật và giữ kết nối mạng trong suốt thời gian người khác cần truy cập — tunnel chết khi bạn tắt máy hoặc mất mạng.
- Dữ liệu nhập vào trong lúc test (đơn hàng, sản phẩm...) nằm trên Postgres local của bạn — không phải môi trường production riêng biệt.

## Khi nào cần deploy thật thay vì tunnel

Tunnel chỉ phù hợp demo ngắn hạn (link tạm, tốc độ phụ thuộc đường truyền máy bạn, máy phải luôn bật). Nếu cần chạy ổn định lâu dài cho nhiều người dùng:

1. Build production: `pnpm run build`
2. Deploy `api-server` + `pos-app` (static) lên VPS hoặc PaaS (Render, Railway, Fly.io...)
3. Đặt sau reverse proxy (Nginx/Caddy) với domain riêng + HTTPS
4. Postgres chạy riêng, **không** expose ra internet, chỉ backend kết nối được
