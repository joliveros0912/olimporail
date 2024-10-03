// owl carousel things

$('.home_carousel').owlCarousel({
    loop: true,
    margin: 0,
    dots: true,
    nav: false,
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 1
        },
        1000: {
            items: 1
        }
    }
});

//navbar

window.addEventListener('scroll', function(){
    let navbar = document.getElementById("navbar");
    navbar.classList.toggle("fixed", this.window.scrollY > 0);
})


let MenuBtn = document.querySelector("#menu-btn");

//menu section

let menutabs = document.querySelector(".menu-tabs");
menutabs.addEventListener("click", function(e){
    if(e.target.classList.contains("menu-tab-item") && !e.target.classList.contains("active"))
    {
        menutabs.querySelector(".active").classList.remove("active");

        e.target.classList.add("active");
    }
})