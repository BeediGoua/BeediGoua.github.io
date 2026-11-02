(function () {
  var year = document.getElementById("year");
  if (year) {
    year.textContent = String(new Date().getFullYear());
  }

  var menu = document.querySelector(".mobile-menu");
  if (menu) {
    menu.addEventListener("toggle", function () {
      var summary = menu.querySelector("summary");
      if (summary) {
        summary.setAttribute("aria-expanded", menu.open ? "true" : "false");
      }
    });
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && menu.open) {
        menu.open = false;
      }
    });
    menu.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        menu.open = false;
      });
    });
  }
})();
