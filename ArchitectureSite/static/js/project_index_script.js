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

/* break */
const SELECTOR = 'fade-on-scroll';
const ANIMATE_CLASS_NAME = 'animate';

const animate = element =>  (
    element.classList.add(ANIMATE_CLASS_NAME)
)

const isAnimated = element => (
    element.classList.contains(ANIMATE_CLASS_NAME)
)
console.log("Running")

const intersectionObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {


        if(entry.intersectionRatio > 0) {
            animate(entry.target);
        }

    });
});

const elements = [].filter.call(
    document.getElementsByClassName(SELECTOR),
    element => !isAnimated(element, ANIMATE_CLASS_NAME)
)

elements.forEach((element) => intersectionObserver.observe(element));