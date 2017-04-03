$(document).ready(function() {
    loadInfo();
});

function loadInfo(){
    uid = window.location.search.substr(1).split("=")[1];
    
    $.ajax({
        url : "../user/profileinfo?uid=" + uid,
        type : "GET",
        success : function(data) {
            var obj = JSON.parse(data);
            $('#profile-name').html(obj.name);
            if (obj.followed) {
                $('#follow-btn').html('Followed');
            } else {
                $('#follow-btn').html('Follow now');
            }
        }
    });
}