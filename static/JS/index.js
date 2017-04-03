$(document).ready(function() {
    loadStatus();
});

function loadStatus() {
    $.ajax({
        url : "status/getstatus",
        type : "GET",
        success : function(data) {
            var obj = JSON.parse(data);
            for (var i = 0; i < obj.length; i++) {
                var card = '<div class="col-md-offset-1 col-md-10">\
                                <div class="card col-md-12">\
                                    <img class="col-md-2" src="/static/IMG/' + obj[i].author_id + '.png">\
                                    <div class="col-md-9 status-info">\
                                        <p class="author-name">' + obj[i].author_name + '</p>\
                                        <p class="post-time">Posted on: ' + obj[i].time + '</p>\
                                    </div>\
                                    <div class="col-md-1">\
                                        <i onclick="likeStatus(' + obj[i].post_id + ')" class="glyphicon glyphicon-heart like-btn ';
                if (obj[i].liked == 'True') {
                    card += 'liked';
                }
                card += '"></i>\
                                    </div>\
                                    <div class="col-md-12 status-text-container">\
                                        <p>' + obj[i].text + '</p>\
                                    </div>\
                                </div>\
                            </div>';
                $('#status-container').prepend(card);
            }
        }
    });
}

function likeStatus(pid) {
    $.ajax({
        url : "status/likestatus?pid=" + pid,
        type : "POST",
        success : function(data) {
            if (data) {
                location.reload();
            } else {
                alert("You already liked this status.");
            }
        }
    });
}