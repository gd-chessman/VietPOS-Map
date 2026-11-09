(function () {
  const hero = document.querySelector(".hero");
  if (!hero || document.getElementById("portal-theme-toggle")) return;
  const btn = document.createElement("button");
  btn.type = "button";
  btn.id = "portal-theme-toggle";
  btn.className = "theme-toggle";
  btn.style.cssText =
    "margin-top:.75rem;border:1px solid var(--border);background:var(--bg2);color:var(--text);border-radius:8px;padding:.4rem .75rem;cursor:pointer;font-size:.85rem";
  btn.addEventListener("click", () => {
    window.VietPOSTheme.toggle();
  });
  const t = document.documentElement.getAttribute("data-theme") || "dark";
  btn.textContent = t === "dark" ? "☀ Giao diện sáng" : "☾ Giao diện tối";
  hero.appendChild(btn);
})();
