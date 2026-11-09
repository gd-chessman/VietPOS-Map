/* VietPOS-Map — sáng/tối (nút, Mermaid); boot sớm: theme-boot.js */
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
      document.head.appendChild(mdLink);
    }
    if (mdLink) mdLink.href = MD_CSS[theme];
  }

  function apply(theme) {
    const root = document.documentElement;
    root.setAttribute("data-theme", theme);
    root.style.colorScheme = theme;
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
