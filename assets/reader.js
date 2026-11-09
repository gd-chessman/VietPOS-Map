/* VietPOS-Map — render MD + sidebar + TOC + sáng/tối */
(function () {
  const THEME_KEY = "vietpos-map-theme";
  const MD_CSS = {
    dark: "https://cdn.jsdelivr.net/npm/github-markdown-css@5.6.1/github-markdown-dark.min.css",
    light: "https://cdn.jsdelivr.net/npm/github-markdown-css@5.6.1/github-markdown-light.min.css",
  };

  const DOC_ROOT_SEGMENTS = new Set([
    "trang",
    "chuyen-de",
    "co-so-du-lieu",
    "module-api",
    "nghiep-vu",
    "he-thong",
    "chi-muc",
    "tham-chieu",
    "thu-vien",
    "ban-do-kien-truc",
    "huong-dan-doc",
  ]);

  const SECTION_LABELS = {
    "chuyen-de": "Hub chủ đề",
    trang: "Màn hình",
    "module-api": "Module API",
    "co-so-du-lieu": "Schema DB",
    "nghiep-vu": "Nghiệp vụ",
    "he-thong": "Hệ thống",
    "chi-muc": "Chỉ mục",
    "thu-vien": "Thư viện",
    tham-chieu: "Tham chiếu Shop",
    "ban-do-kien-truc": "Bản đồ hình",
    "huong-dan-doc": "Hướng dẫn",
    _root: "Map",
  };

  if (typeof marked !== "undefined") {
    marked.setOptions({ gfm: true, breaks: false, headerIds: true, mangle: false });
  }

  function currentViewPath() {
    const p = window.location.pathname.replace(/\/index\.html$/, "").replace(/\/+$/, "");
    return p || "/docs";
  }

  function resolveMdHref(href, basePath) {
    if (/^https?:\/\//i.test(href)) return href;
    if (href.startsWith("/")) return href.replace(/\/+$/, "") || "/";
    const baseDir = basePath.replace(/\/[^/]*$/, "/");
    const parts = (baseDir + href).split("/").filter(Boolean);
    const out = [];
    for (const part of parts) {
      if (part === ".") continue;
      if (part === "..") {
        out.pop();
        continue;
      }
      out.push(part);
    }
    return "/" + out.join("/");
  }

  function ensureDocsPrefix(pathname) {
    const parts = pathname.replace(/^\//, "").split("/").filter(Boolean);
    if (parts[0] === "docs" || parts.length === 0) return pathname;
    if (DOC_ROOT_SEGMENTS.has(parts[0])) return "/docs" + pathname;
    return pathname;
  }

  function toViewUrl(resolvedPath) {
    let p = ensureDocsPrefix(resolvedPath.replace(/\/+$/, ""));
    if (p.endsWith("/README.md")) p = p.slice(0, -"/README.md".length);
    else if (p.endsWith(".md")) {
      p = p.slice(0, -3);
      if (p.endsWith("/README")) p = p.slice(0, -"/README".length);
    }
    return p || "/docs";
  }

  function fixLinks(root, basePath) {
    root.querySelectorAll("a[href]").forEach((a) => {
      const href = a.getAttribute("href");
      if (!href || href.startsWith("#") || /^https?:/i.test(href)) return;
      const hash = href.includes("#") ? "#" + href.split("#").slice(1).join("#") : "";
      const pathOnly = href.split("#")[0];
      const resolved = pathOnly.startsWith("/") ? pathOnly : resolveMdHref(pathOnly, basePath);
      a.setAttribute("href", toViewUrl(resolved) + hash);
    });
  }

  function getTheme() {
    const saved = localStorage.getItem(THEME_KEY);
    if (saved === "light" || saved === "dark") return saved;
    return window.matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark";
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    const link = document.getElementById("md-theme-css");
    if (link) link.href = MD_CSS[theme];
    const btn = document.getElementById("theme-toggle");
    if (btn) btn.textContent = theme === "dark" ? "☀ Sáng" : "☾ Tối";
    if (typeof mermaid !== "undefined") {
      mermaid.initialize({
        startOnLoad: false,
        theme: theme === "dark" ? "dark" : "neutral",
        securityLevel: "loose",
      });
    }
    localStorage.setItem(THEME_KEY, theme);
  }

  function toggleTheme() {
    const next = document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
    applyTheme(next);
    const content = document.getElementById("content");
    if (content) rerenderMermaid(content);
  }

  async function renderMermaid(root) {
    if (typeof mermaid === "undefined") return;
    root.querySelectorAll("pre > code.language-mermaid").forEach((code) => {
      const pre = code.parentElement;
      const el = document.createElement("div");
      el.className = "mermaid";
      const src = code.textContent || "";
      el.textContent = src;
      el.setAttribute("data-mermaid-src", src);
      pre.replaceWith(el);
    });
    const nodes = root.querySelectorAll(".mermaid");
    if (nodes.length) {
      try {
        await mermaid.run({ nodes });
      } catch (_) {
        /* ignore parse errors */
      }
    }
  }

  async function rerenderMermaid(root) {
    if (typeof mermaid === "undefined") return;
    const sources = [];
    root.querySelectorAll(".mermaid").forEach((el) => {
      sources.push({
        src: el.getAttribute("data-mermaid-src") || el.textContent || "",
        next: el.nextSibling,
        parent: el.parentNode,
      });
      el.remove();
    });
    const freshNodes = [];
    for (const { src, next, parent } of sources) {
      const el = document.createElement("div");
      el.className = "mermaid";
      el.textContent = src;
      el.setAttribute("data-mermaid-src", src);
      parent.insertBefore(el, next);
      freshNodes.push(el);
    }
    if (freshNodes.length) {
      try {
        await mermaid.run({ nodes: freshNodes });
      } catch (_) {
        /* ignore */
      }
    }
  }

  function decodeMd() {
    const el = document.getElementById("md-b64");
    if (!el) return "";
    const b64 = el.textContent.trim();
    return new TextDecoder().decode(Uint8Array.from(atob(b64), (c) => c.charCodeAt(0)));
  }

  function buildBreadcrumb(mdWebPath) {
    const el = document.getElementById("doc-breadcrumb");
    if (!el) return;
    const view = currentViewPath();
    const parts = view.replace(/^\/docs\/?/, "").split("/").filter(Boolean);
    const crumbs = [{ label: "Map", href: "/docs" }];
    let acc = "/docs";
    for (const part of parts) {
      acc += "/" + part;
      crumbs.push({
        label: part.replace(/-/g, " "),
        href: acc,
      });
    }
    el.innerHTML = crumbs
      .map((c, i) =>
        i === crumbs.length - 1
          ? `<span>${escapeHtml(c.label)}</span>`
          : `<a href="${escapeHtml(c.href)}">${escapeHtml(c.label)}</a>`,
      )
      .join(' <span aria-hidden="true">/</span> ');
  }

  function buildToc(content) {
    const toc = document.getElementById("doc-toc");
    if (!toc) return;
    const headings = content.querySelectorAll("h2, h3");
    if (!headings.length) {
      toc.innerHTML = "";
      return;
    }
    const items = [];
    headings.forEach((h) => {
      if (!h.id) {
        h.id =
          "h-" +
          (h.textContent || "")
            .toLowerCase()
            .replace(/[^\w\u00C0-\u024f]+/gi, "-")
            .replace(/^-|-$/g, "");
      }
      const depth = h.tagName === "H3" ? "depth-3" : "";
      items.push(
        `<li class="${depth}"><a href="#${escapeHtml(h.id)}">${escapeHtml(h.textContent || "")}</a></li>`,
      );
    });
    toc.innerHTML =
      '<p class="doc-toc-title">Trên trang này</p><ul>' + items.join("") + "</ul>";
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function normPath(href) {
    return (href || "").replace(/\/index\.html$/, "").replace(/\/+$/, "") || "/docs";
  }

  function renderNavTree(nav, current) {
    const sidebar = document.getElementById("doc-sidebar");
    if (!sidebar || !nav) return;
    const cur = normPath(current);
    let html = '<div class="doc-sidebar-inner nav-tree">';

    html += '<p class="nav-tree-title">Cửa vào</p><ul>';
    html += '<li><a href="/index.html">Bản đồ VietPOS</a></li>';
    html += '<li><a href="/docs"' + (cur === "/docs" ? ' class="active"' : "") + ">Mục lục Map</a></li>";
    html += "</ul>";

    if (nav.hubs && nav.hubs.length) {
      html += '<p class="nav-tree-title">Hub chủ đề</p><ul>';
      nav.hubs.forEach((h) => {
        const active = normPath(h.href) === cur ? ' class="active"' : "";
        html += `<li><a href="${escapeHtml(h.href)}"${active}>${escapeHtml(h.title)}</a></li>`;
      });
      html += "</ul>";
    }

    if (nav.quick && nav.quick.length) {
      html += '<p class="nav-tree-title">Tra cứu nhanh</p><ul>';
      nav.quick.forEach((q) => {
        const active = normPath(q.href) === cur ? ' class="active"' : "";
        html += `<li><a href="${escapeHtml(q.href)}"${active}>${escapeHtml(q.title)}</a></li>`;
      });
      html += "</ul>";
    }

    if (nav.groups) {
      const keys = Object.keys(nav.groups).sort();
      for (const key of keys) {
        const label = SECTION_LABELS[key] || key;
        const items = nav.groups[key];
        const hasActive = items.some((it) => normPath(it.href) === cur);
        html += `<details${hasActive ? " open" : ""}><summary>${escapeHtml(label)} (${items.length})</summary><ul>`;
        items.forEach((it) => {
          const active = normPath(it.href) === cur ? ' class="active"' : "";
          html += `<li><a href="${escapeHtml(it.href)}"${active}>${escapeHtml(it.title)}</a></li>`;
        });
        html += "</ul></details>";
      }
    }

    html += "</div>";
    sidebar.innerHTML = html;
  }

  async function loadNav() {
    try {
      const res = await fetch("/assets/site-nav.json", { cache: "no-cache" });
      if (!res.ok) return;
      const nav = await res.json();
      renderNavTree(nav, currentViewPath());
    } catch (_) {
      /* optional */
    }
  }

  function setupSidebarToggle() {
    const btn = document.getElementById("sidebar-toggle");
    const sidebar = document.getElementById("doc-sidebar");
    const backdrop = document.getElementById("sidebar-backdrop");
    if (!btn || !sidebar) return;
    const close = () => {
      sidebar.classList.remove("open");
      backdrop?.classList.remove("show");
    };
    btn.addEventListener("click", () => {
      sidebar.classList.toggle("open");
      backdrop?.classList.toggle("show", sidebar.classList.contains("open"));
    });
    backdrop?.addEventListener("click", close);
  }

  async function boot() {
    if (window.VietPOSTheme) {
      window.VietPOSTheme.apply(window.VietPOSTheme.get());
    } else {
      applyTheme(getTheme());
    }
    document.getElementById("theme-toggle")?.addEventListener("click", () => {
      if (window.VietPOSTheme) {
        window.VietPOSTheme.toggle();
      } else {
        toggleTheme();
      }
    });
    document.addEventListener("vietpos-theme", () => {
      const content = document.getElementById("content");
      if (content) rerenderMermaid(content);
    });
    setupSidebarToggle();

    const content = document.getElementById("content");
    const basePath = document.body.getAttribute("data-md-path") || "/docs/README.md";
    const mdWebPath = basePath;
    buildBreadcrumb(mdWebPath);
    await loadNav();

    if (!content) return;
    try {
      const md = decodeMd();
      content.innerHTML = marked.parse(md);
      fixLinks(content, basePath);
      buildToc(content);
      await renderMermaid(content);
    } catch (e) {
      content.innerHTML =
        '<p class="error">Lỗi render markdown: ' +
        escapeHtml(e && e.message ? e.message : e) +
        "</p>";
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
