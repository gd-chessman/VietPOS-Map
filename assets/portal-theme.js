(function () {
  const KEY = "vietpos-map-theme";
  function get() {
    const s = localStorage.getItem(KEY);
    if (s === "light" || s === "dark") return s;
    return matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark";
  }
  function apply(t) {
    document.documentElement.setAttribute("data-theme", t);
    localStorage.setItem(KEY, t);
    const root = document.documentElement;
    if (t === "light") {
      root.style.setProperty("--bg", "#f3f4f6");
      root.style.setProperty("--bg2", "#ffffff");
      root.style.setProperty("--panel", "#ffffff");
      root.style.setProperty("--border", "#d0d7de");
      root.style.setProperty("--text", "#1f2328");
      root.style.setProperty("--muted", "#656d76");
    } else {
      root.style.setProperty("--bg", "#0b0f14");
      root.style.setProperty("--bg2", "#111827");
      root.style.setProperty("--panel", "#151d2e");
      root.style.setProperty("--border", "#2a3548");
      root.style.setProperty("--text", "#eef2f7");
      root.style.setProperty("--muted", "#94a3b8");
    }
  }
  apply(get());
  const hero = document.querySelector(".hero");
  if (hero) {
    const btn = document.createElement("button");
    btn.type = "button";
    btn.className = "theme-toggle";
    btn.style.cssText =
      "margin-top:.75rem;border:1px solid var(--border);background:var(--bg2);color:var(--text);border-radius:8px;padding:.4rem .75rem;cursor:pointer;font-size:.85rem";
    const sync = () => {
      const t = document.documentElement.getAttribute("data-theme") || "dark";
      btn.textContent = t === "dark" ? "☀ Giao diện sáng" : "☾ Giao diện tối";
    };
    btn.addEventListener("click", () => {
      const next =
        document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark";
      apply(next);
      sync();
    });
    sync();
    hero.appendChild(btn);
  }
})();
