$(document).ready(function() {
    loadInfo();
    $('#follow-btn').click(function(){follow();});
});

function loadInfo(){
    uid = window.location.search.substr(1).split("=")[1];
    $("#profile-pic").css("background", 'url("../static/IMG/' + uid + '.png") no-repeat center center'); 
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

function follow() {
    uid = window.location.search.substr(1).split("=")[1];
    $.ajax({
        url : "../user/follow?uid=" + uid,
        type : "POST",
        success : function(data) {
            if (data) {
                location.reload();
            } else {
                alert("You already followed this person.");
            }
        }
    });
}