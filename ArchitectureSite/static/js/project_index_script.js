console.log("Working")
var x = document.getElementsByClassName("gallery__item");

$(document).ready(function() {
    $(".gallery__item").each(function() {
        $(this)
            .mouseover(function() {
                thechild = this.children[1]
                thechild.classList.add("my-class")
            })
            .mouseleave(function() {
                thechild = this.children[1]
                thechild.classList.remove("my-class")
            });
    })
});