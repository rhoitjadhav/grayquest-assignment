
function getCookie(name) {
    // Split cookie string and get all individual name=value pairs in an array
    var cookieArr = document.cookie.split(";");

    // Loop through the array elements
    for(var i = 0; i < cookieArr.length; i++) {
        var cookiePair = cookieArr[i].split("=");

        /* Removing whitespace at the beginning of the cookie name
        and compare it with the given string */
        if(name == cookiePair[0].trim()) {
            // Decode the cookie value and return
            return decodeURIComponent(cookiePair[1]);
        }
    }

    // Return null if not found
    return null;
}

function cookie_info_auto_fade() {
    document.getElementById("cookie").innerHTML = "Cookie Information:<br />" + "SessionId => " + getCookie('sessionId');
    setTimeout(function(){
        document.getElementById("cookie").innerHTML = "";
    }, 5000);
}

//document.getElementById("cookie-msg").innerHTML = "SessionId: ";
//setTimeout(function(){
//    document.getElementById("cookie-msg").innerHTML = "SessionId: ";
//}, 3000);



$(document).ready(function() {
    $("button").click(function() {
        $.ajax({
			data : {
				consent : this.value,
				user: sessionStorage.getItem("user")
			},
			type : 'POST',
			url : '/dashboard/cookie-consent'
		})
		.done(function(data) {
			if (data.success == true) {
                console.log(data.message)
                window.location.href = data.redirect
			}
			else {
				alert(data.message)
				window.location.href = data.redirect
			}
		});
    });
});