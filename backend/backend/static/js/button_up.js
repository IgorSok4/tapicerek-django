document.addEventListener('DOMContentLoaded', (event) => {
    window.onscroll = function() {
        scrollFunction();
    };

    function scrollFunction() {
        var scrollTopBtn = document.getElementById("scrollTopBtn");
        scrollTopBtn.style.display = "none";
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            scrollTopBtn.style.display = "block";
        } else {
            scrollTopBtn.style.display = "none";
        }
    }

    // when button clicked, roll up
    var scrollTopBtn = document.getElementById("scrollTopBtn");
    if (scrollTopBtn) {
        scrollTopBtn.onclick = function() {
            document.body.scrollTop = 0; // Safari
            document.documentElement.scrollTop = 0; // Chrome, Firefox, IE and Opera
        };
    }
});
