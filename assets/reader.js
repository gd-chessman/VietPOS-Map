/* VietPOS-Map — render README.md đã nhúng (trang index.html) */
(function () {
  if (typeof marked === "undefined") return;

  marked.setOptions({ gfm: true, breaks: false, headerIds: true, mangle: false });

  function resolveMdHref(href, basePath) {
    if (/^https?:\/\//i.test(href)) return href;
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

  function mdToPageUrl(resolvedMd) {
    if (resolvedMd.endsWith("/README.md")) {
      return resolvedMd.slice(0, -"README.md".length) + "index.html";
    }
    if (resolvedMd.endsWith(".md")) {
      return resolvedMd.slice(0, -3) + ".html";
    }
    return resolvedMd;
  }

  function fixLinks(root, basePath) {
    root.querySelectorAll("a[href]").forEach((a) => {
      const href = a.getAttribute("href");
      if (!href || href.startsWith("#") || /^https?:/i.test(href)) return;
      const hash = href.includes("#") ? "#" + href.split("#").slice(1).join("#") : "";
      const pathOnly = href.split("#")[0];
      if (pathOnly.endsWith(".md") || pathOnly.includes(".md/")) {
        const resolved = resolveMdHref(pathOnly, basePath);
        a.setAttribute("href", mdToPageUrl(resolved) + hash);
      }
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
    const basePath = document.body.getAttribute("data-md-path") || "";
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
