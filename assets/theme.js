/* VietPOS-Map — sáng/tối (nút, Mermaid); boot sớm: inline head trong index.html */
window.VietPOSTheme = (function () {
  const KEY = "vietpos-map-theme";
  const MD_CSS = {
    dark: "https://cdn.jsdelivr.net/npm/github-markdown-css@5.6.1/github-markdown-dark.min.css",
    light:
      "https://cdn.jsdelivr.net/npm/github-markdown-css@5.6.1/github-markdown-light.min.css",
  };

  function get() {
    const saved = localStorage.getItem(KEY);
    if (saved === "light" || saved === "dark") return saved;
    return window.matchMedia("(prefers-color-scheme: light)").matches
      ? "light"
      : "dark";
  }

  function ensureMdLink(theme) {
    let mdLink = document.getElementById("md-theme-css");
    if (!mdLink && document.body?.getAttribute("data-md-path")) {
      mdLink = document.createElement("link");
      mdLink.id = "md-theme-css";
      mdLink.rel = "stylesheet";
      const docCss = document.querySelector('link[href="/assets/doc.css"]');
      if (docCss) docCss.before(mdLink);
      else document.head.appendChild(mdLink);
    }
    if (mdLink) mdLink.href = MD_CSS[theme];
  }

  function apply(theme) {
    const root = document.documentElement;
    root.setAttribute("data-theme", theme);
    root.style.colorScheme = theme;
    root.classList.remove("theme-light", "theme-dark");
    root.classList.add(theme === "light" ? "theme-light" : "theme-dark");
    localStorage.setItem(KEY, theme);

    ensureMdLink(theme);

    const btn = document.getElementById("theme-toggle");
    if (btn) btn.textContent = theme === "dark" ? "☀ Sáng" : "☾ Tối";

    const portalBtn = document.getElementById("portal-theme-toggle");
    if (portalBtn) {
      portalBtn.textContent =
        theme === "dark" ? "☀ Giao diện sáng" : "☾ Giao diện tối";
    }

    if (typeof mermaid !== "undefined") {
      mermaid.initialize({
        startOnLoad: false,
        theme: theme === "dark" ? "dark" : "neutral",
        securityLevel: "loose",
      });
    }

    document.dispatchEvent(
      new CustomEvent("vietpos-theme", { detail: { theme } }),
    );
  }

  function toggle() {
    const cur = document.documentElement.getAttribute("data-theme") || get();
    const next = cur === "dark" ? "light" : "dark";
    apply(next);
    return next;
  }

  function sync() {
    apply(get());
  }

  return { KEY, get, apply, toggle, sync, MD_CSS };
})();
