$(document).ready(function() {
    $('#logoutBtn').click(function(){logout();});
});

function logout() {
    $.ajax({
        url : "user/logout",
        type : "POST",
        success : function(data) {
            if (data) {
                location.reload();
            } else {
                alert("Sorry, something went wrong...");
            }
        }
    });
}