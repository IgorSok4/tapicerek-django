document.addEventListener('DOMContentLoaded', (event) => {
    window.onscroll = function() { stickyNav(); };

    var navbar = document.getElementById("nav-sec");
    var sticky = navbar.offsetTop;
    var navbarLogo = document.getElementById("navbar-logo"); // Pobranie elementu logo

    function stickyNav() {
        if (window.pageYOffset >= sticky) {
            navbar.classList.add("sticky");
            navbarLogo.style.display = "block"; // Pokazanie logo
        } else {
            navbar.classList.remove("sticky");
            navbarLogo.style.display = "none"; // Ukrycie logo
        }
    }
});