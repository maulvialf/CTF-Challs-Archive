$(document).ready(function(){
    loadPotionImage();

})

const loadPotionImage = () => {

    let product = $('.potion-item');

    for (i=0; i < potionTypes.length; i++) {
        if (product.data('category') == potionTypes[i].id) {
            product.prepend(`<p class='reset-pos rpgui-container framed-golden-2'>Potion Type: ${potionTypes[i].name}</p>`);
            product.prepend(`<img src='${potionTypes[i].src}' class='category-img'>`);
        }
    }


}
