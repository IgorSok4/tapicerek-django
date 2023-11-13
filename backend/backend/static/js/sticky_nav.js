document.addEventListener('DOMContentLoaded', (event) => {
    window.onscroll = function() { stickyNav(); };

    var navbar = document.getElementById("nav-sec");
    var mainContent = document.querySelector('main'); // Upewnij się, że ten selektor odpowiada elementowi na stronie.
    var sticky = navbar ? navbar.offsetTop : 0;

    function stickyNav() {
        if (window.pageYOffset >= sticky) {
            navbar.classList.add("sticky");
            navbar.style.top = '0px';
            if (mainContent) mainContent.style.paddingTop = navbar.offsetHeight + 'px';
        } else {
            navbar.classList.remove("sticky");
            navbar.style.top = '';
            if (mainContent) mainContent.style.paddingTop = '0';
        }
    }
});
