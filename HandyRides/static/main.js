function getCookie(c_name) {

    var i,x,y,ARRcookies=document.cookie.split(";");
    for (i=0;i<ARRcookies.length;i++){
        x=ARRcookies[i].substr(0,ARRcookies[i].indexOf("="));
        y=ARRcookies[i].substr(ARRcookies[i].indexOf("=")+1);
        x=x.replace(/^\s+|\s+$/g,"");
        if (x==c_name) {
            return unescape(y);
        }
    }
}
function setCookie(c_name, value, exdays) {
    var exdate = new Date();
    exdate.setDate(exdate.getDate() + exdays);
    var c_value = escape(value) + ((exdays == null) ? "" : "; expires=" + exdate.toUTCString());
    document.cookie = c_name + "=" + c_value;
}

function checkForm() {

    var searchOrig = document.getElementById('id_search_orig').value.trim();
    var searchDest = document.getElementById('id_search_dest').value.trim();

    if (searchOrig === '' && searchDest === '') {
        alert('Please fill in at least one field.');
        return false;
    }

    if (searchOrig.toLowerCase() === 'elon musk' || searchDest.toLowerCase() === 'elon musk') {
        alert("He's not here");
        return false;
    }

    return true;
}

document.addEventListener("DOMContentLoaded", function() {
    if (!getCookie('firstVisit')) {
        setCookie('firstVisit', 'true', 365);
        if (window.location.pathname !== "/") {
            window.location.href = "/";
        }
    }
});
