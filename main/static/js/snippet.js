function copyElementText(id) {
    var elem = document.createElement("textarea");
    var host = window.location.host;
    document.body.appendChild(elem);
    elem.value = host + id;
    elem.select();
    document.execCommand("copy");
    document.body.removeChild(elem);
}