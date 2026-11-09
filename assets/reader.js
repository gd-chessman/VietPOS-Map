/* VietPOS-Map — render README.md đã nhúng (trang index.html) */
(function () {
  if (typeof marked === "undefined") return;

  marked.setOptions({ gfm: true, breaks: false, headerIds: true, mangle: false });

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

  /** URL xem trên Vercel (cleanUrls → index.html trong thư mục). */
  function toViewUrl(resolvedPath) {
    let p = ensureDocsPrefix(resolvedPath.replace(/\/+$/, ""));
    if (p.endsWith("/README.md")) {
      p = p.slice(0, -"/README.md".length);
    } else if (p.endsWith(".md")) {
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
      const resolved =
        pathOnly.startsWith("/") ? pathOnly : resolveMdHref(pathOnly, basePath);
      a.setAttribute("href", toViewUrl(resolved) + hash);
    });
  }

  async function renderMermaid(root) {
    if (typeof mermaid === "undefined") return;
    root.querySelectorAll("pre > code.language-mermaid").forEach((code) => {
      const pre = code.parentElement;
      const el = document.createElement("div");
      el.className = "mermaid";
      el.textContent = code.textContent;
      pre.replaceWith(el);
    });
    const nodes = root.querySelectorAll(".mermaid");
    if (nodes.length) await mermaid.run({ nodes });
  }

  function decodeMd() {
    const el = document.getElementById("md-b64");
    if (!el) return "";
    const b64 = el.textContent.trim();
    return new TextDecoder().decode(
      Uint8Array.from(atob(b64), (c) => c.charCodeAt(0)),
    );
  }

  async function boot() {
    const content = document.getElementById("content");
    const basePath = document.body.getAttribute("data-md-path") || "/docs/README.md";
    if (!content) return;
    try {
      const md = decodeMd();
      content.innerHTML = marked.parse(md);
      fixLinks(content, basePath);
      await renderMermaid(content);
    } catch (e) {
      content.innerHTML =
        '<p class="error">Lỗi render markdown: ' +
        (e && e.message ? e.message : e) +
        "</p>";
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
