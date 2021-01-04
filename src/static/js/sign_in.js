$(document).ready(function() {
	$('button').click(function() {
		$.ajax({
			data : {
				username : $('#username').val(),
				password : $('#password').val()
			},
			type : 'POST',
			url : '/auth/sign-in'
		})
		.done(function(data) {
			if (data.success == true) {
                console.log(data.message)
                sessionStorage.setItem("user", $('#username').val());
                console.log(data.cookie.expires)
                expire_date = new Date(data.cookie.expires[0],data.cookie.expires[1], data.cookie.expires[2],
                              data.cookie.expires[3], data.cookie.expires[4], data.cookie.expires[5],
                              data.cookie.expires[6], data.cookie.expires[7])
                document.cookie = data.cookie.name + "=" + data.cookie.value + "; " + "expires=" + expire_date.toUTCString() + "; path=/";
                window.location.href = data.redirect
			}
			else {
				alert(data.message)
			}
		});
	});
});