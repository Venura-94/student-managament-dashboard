document.addEventListener("DOMContentLoaded", function () {
  // Sidebar submenu toggle
  document.querySelectorAll(".sidebar-menu > li.has-submenu > a").forEach(function (link) {
    link.addEventListener("click", function (e) {
      e.preventDefault();
      var parent = link.parentElement;
      var wasOpen = parent.classList.contains("open");

      document.querySelectorAll(".sidebar-menu > li.has-submenu.open").forEach(function (item) {
        if (item !== parent) item.classList.remove("open");
      });

      parent.classList.toggle("open", !wasOpen);
    });
  });

  // Mobile sidebar toggle
  var toggleBtn = document.querySelector(".menu-toggle");
  var sidebar = document.querySelector(".sidebar");
  if (toggleBtn && sidebar) {
    toggleBtn.addEventListener("click", function () {
      sidebar.classList.toggle("show");
    });
  }
});
