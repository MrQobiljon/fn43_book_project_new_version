document.addEventListener("DOMContentLoaded", () => {
  const toggles = document.querySelectorAll("[data-dropdown-toggle]");

  toggles.forEach((toggle) => {
    toggle.addEventListener("click", (e) => {
      e.stopPropagation();
      const menuId = toggle.getAttribute("data-dropdown-toggle");
      const targetMenu = document.getElementById(menuId);

      document.querySelectorAll(".custom-dropdown-menu").forEach((menu) => {
        if (menu !== targetMenu) menu.classList.remove("show");
      });

      if (targetMenu) {
        targetMenu.classList.toggle("show");
      }
    });
  });

  document.addEventListener("click", () => {
    document.querySelectorAll(".custom-dropdown-menu").forEach((menu) => {
      menu.classList.remove("show");
    });
  });
});