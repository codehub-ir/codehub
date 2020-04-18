// scroll functions
$(window).scroll(function (e) {

    // add/remove class to navbar when scrolling to hide/show
    var scroll = $(window).scrollTop();
    if (scroll >= 150) {
        $('.navbar').addClass("navbar-hide");
    } else {
        $('.navbar').removeClass("navbar-hide");
    }

});

function copyElementText(id) {
    var text = document.getElementById(id).innerText;
    var elem = document.createElement("textarea");
    var website_snippet_address = 'http://codehub.pythonanywhere.com/snippet/';
    document.body.appendChild(elem);
    elem.value = website_snippet_address + text;
    elem.select();
    document.execCommand("copy");
    document.body.removeChild(elem);
    window.alert('آدرس اسنیپت کپی شد!')
}