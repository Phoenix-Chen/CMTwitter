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

function searchUser() {
    keyword = $('#searchbar').val();
    if (keyword != null && keyword != '') {
        $.ajax({
            url : "http://localhost:8000/user/finduser?keyword=" + keyword,
            type : "GET",
            success : function(data) {
                var obj = jQuery.parseJSON(data);
                var inner = "";
                for (var i = 0; i < obj.length; i++){
                    inner = inner +  "<option value='" + obj[i].u_id + "'>" + obj[i].name + "</option>";
                }
                $('#userlist').html(inner);
            }
        });
    }
    var opts = document.getElementById('userlist').childNodes;
    for (var i = 0; i < opts.length; i++) {
      if (opts[i].value === document.getElementById("searchbar").value) {
        toProfile(opts[i].value);
        break;
      }
    }
}

function toProfile(uid) {
    window.location.href = "/profile?uid="+uid;
}

function toIndex() {
    window.location.href = "/";
}
