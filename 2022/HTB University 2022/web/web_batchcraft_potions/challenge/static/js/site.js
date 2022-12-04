$(document).ready(function(){
    loadPotionImages();

    $('.owl-carousel').owlCarousel({
        loop:true,
        center:true,
        margin:10,
        nav:false,
        dots: false,
        URLhashListener:true,
        startPosition: 'URLHash',
        responsive:{
            0:{
                items:3
            },
            600:{
                items:5
            },
            1000:{
                items:5
            }
        }
    })
})

const loadPotionImages = () => {
    let products = $('.potion-items');

    products.each(function() {
        for(i=0; i < potionTypes.length; i++) {
            if ($( this ).data('category') == potionTypes[i].id) {
                $( this ).prepend(`<img src='${potionTypes[i].src}' class='category-img'>`);
            }
        }
    })

}
