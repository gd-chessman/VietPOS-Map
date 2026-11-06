<!-- Mirror: Shop-Manager-System-Offline/docs/architecture.md -->

# Architecture

**Mô tả:** Bản mirror doc Shop docs/architecture.md — Architecture.

## Monorepo layout

This repository is a `pnpm` workspace (see `pnpm-workspace.yaml`) with these key packages:

- **Frontend**: `artifacts/pos-app` — the POS + admin web app (React + Vite)
- **Backend**: `artifacts/api-server` — REST API server (Express)
- **Database library**: `lib/db` — Drizzle ORM schema + DB access (`pg` Pool)
- **API schema**: `lib/api-zod` — shared Zod request/response schemas/types
- **API client**: `lib/api-client-react` — shared React Query client/hooks for the frontend
- **Scripts**: `scripts` — local scripts (e.g. seeding)

## Runtime topology (local)

Typical local stack:

- **Postgres**: Docker container from `docker-compose.yml` (host port `5433`)
- **API server**: `http://127.0.0.1:3002` (Express)
- **POS web app**: `http://127.0.0.1:5174` (Vite dev server)
  - Vite dev server proxies `/api/*` → API server (config in `artifacts/pos-app/vite.config.ts`).

## Request flow (web)

1. Browser loads the POS web app from Vite (dev) or static build (prod).
2. Frontend makes requests to `/api/...` (relative).
3. In dev, Vite proxies those to the API server.
4. API server validates auth (JWT) and uses `lib/db` to query Postgres.

## Backend layering

Backend entrypoints:

- `artifacts/api-server/src/index.ts`: HTTP server listens on `PORT` (defaults to 3001 in code; locally you often run 3002)
- `artifacts/api-server/src/app.ts`: Express app middleware + router mount under `/api`
- `artifacts/api-server/src/routes/*`: REST endpoints grouped by domain
- `artifacts/api-server/src/middlewares/auth.ts`: JWT auth + role helpers

Build:

- `artifacts/api-server/build.mjs` bundles the server using `esbuild` into `dist/*.mjs`.

## Frontend layering

Frontend entrypoints:

- `artifacts/pos-app/src/App.tsx`: routes + providers
- `artifacts/pos-app/src/pages/*`: business pages (POS, products, inventory, orders, chain, etc.)
- `artifacts/pos-app/src/components/*`: UI components (Radix/shadcn style)

State/data:

- React Query for server state.
- Authentication token stored in `localStorage` as `pos_token`.

