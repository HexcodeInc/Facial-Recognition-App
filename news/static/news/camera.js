var video = document.getElementById('video');

var canvas = document.getElementById('canvas');
canvas.style.display = "none"
var context = canvas.getContext('2d');
var video = document.getElementById('video');
console.log("Here baka");
var image = new Image();
var dt;
/*function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');*/
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});
// Get access to the camera!
if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    // Not adding `{ audio: true }` since we only want video now
    navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
        video.src = window.URL.createObjectURL(stream);
        //while(1){ context.drawImage(video, 0, 0, 640, 480);}       
       // video.play();
    });
}

// Trigger photo take
document.getElementById("snap").addEventListener("click", function() {
	
	image.src = video;
	context.drawImage(video, 0, 0, 640, 480);
	var dataURL = document.getElementById('canvas').toDataURL("image/jpeg",1.0);
	//console.log({% url 'imageupload' %});
	$.post("../news/classify/upload",{image : dataURL, csrfmiddlewaretoken: '{{ csrf_token }}'}); 
});

function download() {
	dt = canvas.toDataURL('image/jpeg');
    this.href = dt;
};
downloadLnk.addEventListener('click', download, false);