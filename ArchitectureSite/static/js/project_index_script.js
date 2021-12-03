console.log("Working")
var x = document.getElementsByClassName("gallery__item");
var y = document.getElementsByClassName("centered");

$(document).ready(function() {
    $(".gallery__item").each(function() {
        $(this)
            .mouseover(function() {
                console.log("Over")
            })
            .mouseleave(function() {
                console.log("Not Overs")
            });
    })
});