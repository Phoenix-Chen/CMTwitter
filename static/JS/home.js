$(document).ready(function() {
    $('#signupBtn').click(function(){signup();});
    $('#loginBtn').click(function(){login();});
});

function login() {
    email = $('#loginEmail').val();
    if (!emailValid(email)) {
        alert("Please input a valid email address");
        return;
    }

    password = $('#loginPassword').val();

    $.ajax({
        url : "user/login?email=" + email + "&password=" + password,
        type : "POST",
        success : function(data) {
            if (data) {
                location.reload();
            } else {
                alert("Email or password incorrect...");
            }
        }
    });
    
}

function signup() {
    
    name = $('signupName').val();
    
    email = $('#signupEmail').val();
    if (!emailValid(email)) {
        alert("Please input a valid email address");
        return;
    }

    password = $('#signupPassword').val();

    reenter = $('#reenterPassword').val();
    if (password != reenter) {
        alert("Passwords do not match.");
        return;
    }



}

function emailValid(email) {
    var filter = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
    if (filter.test(email)) {
        return true;
    }
    return false;
}