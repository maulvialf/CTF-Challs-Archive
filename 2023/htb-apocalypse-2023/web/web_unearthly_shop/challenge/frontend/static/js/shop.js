window.onload = () => {
    listProducts();
}

const listProducts = async () => {
    let query = [{
        "$match":{
            "instock":true
        }
    }]

    await fetch('/api/products', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(query)
    })
    .then(async (response) => {
            if (response.status == 200) {
                result = await response.json();

                if (Array.isArray(result)) {
                    for (let product of result) {
                        addSlider(product);
                    }
                    initSlider();
                }
            }
    })
    .catch((e) => {
        console.log(e);
    });
}

const addSlider = (product) => {
    let content = `
    <div class="product-slider__item swiper-slide" data-target="img${product._id}">
        <div class="product-slider__card">
            <div class="product-slider__cover">
                <img src="/static/images/pattern.jpg" alt="">
            </div>
            <div class="product-slider__content">
                <h1 class="product-slider__title">
                    ${product.name}
                </h1>
                <span class="product-slider__price">bid starts at - $<span class="number">${product.price}</span> mill</span>
                <div class="product-ctr">
                    <p>${product.description}</p>
                </div>
                <div class="product-slider__bottom">
                    <button class="product-slider__cart" onclick="orderForm(${product._id})">
                    Place Order
                    </button>
                    <button class="product-slider__fav js-fav"><span class="heart"></span> ADD TO WISHLIST</button>
                </div>
            </div>
        </div>
    </div>
    `;

    let imagePlaceholder = `
        <div class="product-img__item" id="img${product._id}">
            <img src="/static/images/${product.image}" class="product-img__img">
        </div>
    `;
    $('#product-img-container').append(imagePlaceholder);
    $('#slider-container').append(content);
}

const initSlider = () => {
    var swiper = new Swiper('.product-slider', {
        spaceBetween: 30,
        effect: 'fade',
        initialSlide: 0,
        loop: false,
        navigation: {
            nextEl: '.next',
            prevEl: '.prev'
        },
        // mousewheel: {
        //     // invert: false
        // },
        on: {
            init: function(){
                var index = this.activeIndex;

                var target = $('.product-slider__item').eq(index).data('target');

                console.log(target);

                $('.product-img__item').removeClass('active');
                $('.product-img__item#'+ target).addClass('active');
            }
        }

    });

    swiper.on('slideChange', function () {
        var index = this.activeIndex;

        var target = $('.product-slider__item').eq(index).data('target');

        console.log(target);

        $('.product-img__item').removeClass('active');
        $('.product-img__item#'+ target).addClass('active');

        if(swiper.isEnd) {
            $('.prev').removeClass('disabled');
            $('.next').addClass('disabled');
        } else {
            $('.next').removeClass('disabled');
        }

        if(swiper.isBeginning) {
            $('.prev').addClass('disabled');
        } else {
            $('.prev').removeClass('disabled');
        }
    });

    $(".js-fav").on("click", function() {
        $(this).find('.heart').toggleClass("is-active");
    });
}

const orderForm = (oid) => {
    $('.modal-container').removeClass('hidden');
    $('.order-form').removeClass('hidden');
    $('.modal-container').off();
    $('.modal-container').on('click', () => {
        $('.modal-container').addClass('hidden');
        $('.order-form').addClass('hidden');
    });
    $('#order-item-id').val(oid);
}

const placeOrder = async () => {
    let card = $('#resp-msg');
    card.hide();

    if (!parseFloat($('#order-bid').val())) {
        card.text('Bid must be a number!');
        card.show();
        return;
    }

    await fetch('/api/order', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name:     $('#order-name').val(),
            email:    $('#order-email').val(),
            bid:      $('#order-bid').val(),
            item_id:  $('#order-item-id').val()
        })
    })
    .then(response => response.json())
    .then(response => {
        card.text(response.message);
        card.show();
        setTimeout(() => {
            location.reload();
        }, 1000);
    })
    .catch((e) => {
        console.log(e);
        card.text('Internal error');
        card.show();
    });
}