/* Đầu <body> trên trang doc — inject github-markdown đúng theme (sau khi có body) */
(function () {
  const MD_CSS = {
    dark: "https://cdn.jsdelivr.net/npm/github-markdown-css@5.6.1/github-markdown-dark.min.css",
    light:
      "https://cdn.jsdelivr.net/npm/github-markdown-css@5.6.1/github-markdown-light.min.css",
  };
  const theme =
    document.documentElement.getAttribute("data-theme") === "light"
      ? "light"
      : document.documentElement.getAttribute("data-theme") === "dark"
        ? "dark"
        : window.matchMedia("(prefers-color-scheme: light)").matches
          ? "light"
          : "dark";

  if (!document.body?.getAttribute("data-md-path")) return;

  let link = document.getElementById("md-theme-css");
  if (!link) {
    link = document.createElement("link");
    link.id = "md-theme-css";
    link.rel = "stylesheet";
    document.head.appendChild(link);
  }
  link.href = MD_CSS[theme];
})();
