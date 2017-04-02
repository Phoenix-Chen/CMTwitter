var curtime;
var lasttime;

$(document).ready(function() {
    //curtime = new Date().getTime();
    loadStatus();
});

function loadStatus() {
    $.ajax({
        url : "status/getstatus",
        type : "GET",
        success : function(data) {
            var obj = JSON.parse(data);
            for (var i = 0; i < obj.length; i++) {
                var card = '<div class="col-sm-6 col-md-4"><div class="thumbnail"><img src="/static/IMG/' + obj[i].author_id + '.png"><div class="caption"><p>' + obj[i].text + '</p><p><a href="#" class="btn btn-primary glyphicon glyphicon-thumbs-up" role="button"></a></p></div></div></div>'
                $('#status-container').prepend(card);
            }
        }
    });
}

function makeCard() {
    
}