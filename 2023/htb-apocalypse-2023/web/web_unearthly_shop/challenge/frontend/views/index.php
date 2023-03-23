<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>UnEarthly Shop</title>
        <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <meta name="author" content="rayhan0x01">
        <link rel="icon" href="/static/images/logo_small.png" />
        <link rel="stylesheet" type="text/css" href="/static/css/swiper.min.css" />
        <link rel="stylesheet" type="text/css" href="/static/css/shop.css" />
    </head>
    <body>
        <div class="wrapper">
            <div class="header">
                <div class="head-banner-container">
                    <p class="head-banner">UnEarthly Artifacts Shop</p>
                </div>
            </div>
            <div class="content">
                <div class="bg-shape">
                    <img src="/static/images/sculpture.png" alt="">
                </div>
                <div class="product-img" id="product-img-container">
                </div>
                <div class="product-slider">
                    <button class="prev disabled">
                        <span class="icon">
                            <svg class="icon icon-arrow-right">
                                <use xlink:href="#icon-arrow-left"></use>
                            </svg>
                        </span>
                    </button>
                    <button class="next">
                        <span class="icon">
                            <svg class="icon icon-arrow-right">
                                <use xlink:href="#icon-arrow-right"></use>
                            </svg>
                        </span>
                    </button>
                    <div class="product-slider__wrp swiper-wrapper" id="slider-container">
                    </div>
                </div>
            </div>
            <div class="footer">
                <span class="footer__item">Take home a piece of the universe with our unearthly artifacts.</span>
                <span class="footer__item"><span class="number">100% </span>&nbsp;verified extraterrestrial artifacts.</span>
            </div>
        </div>
        <div class="modal-container hidden"></div>
        <div class="order-form hidden">
            <p>Please submit your purchase bid request below:</p>
            <span class="cross"></span>
            <label>Name</label>
            <input type="text" class="form-group" id="order-name" placeholder="Your Name">
            <label>Email</label>
            <input type="email" class="form-group" id="order-email" placeholder="Your Email">
            <label>Bid</label>
            <input type="number" step="0.01" class="form-group" id="order-bid" placeholder="Your Bid">
            <input type="hidden" id="order-item-id" value="">
            <button type="button" class="form-group" onclick="placeOrder()">Submit Bid</button>
            <p id="resp-msg">Please wait for response...</p>
        </div>

        <svg class="hidden" hidden>
            <symbol id="icon-arrow-left" viewBox="0 0 32 32">
                <path d="M0.704 17.696l9.856 9.856c0.896 0.896 2.432 0.896 3.328 0s0.896-2.432 0-3.328l-5.792-5.856h21.568c1.312 0 2.368-1.056 2.368-2.368s-1.056-2.368-2.368-2.368h-21.568l5.824-5.824c0.896-0.896 0.896-2.432 0-3.328-0.48-0.48-1.088-0.704-1.696-0.704s-1.216 0.224-1.696 0.704l-9.824 9.824c-0.448 0.448-0.704 1.056-0.704 1.696s0.224 1.248 0.704 1.696z"></path>
            </symbol>
            <symbol id="icon-arrow-right" viewBox="0 0 32 32">
                <path d="M31.296 14.336l-9.888-9.888c-0.896-0.896-2.432-0.896-3.328 0s-0.896 2.432 0 3.328l5.824 5.856h-21.536c-1.312 0-2.368 1.056-2.368 2.368s1.056 2.368 2.368 2.368h21.568l-5.856 5.824c-0.896 0.896-0.896 2.432 0 3.328 0.48 0.48 1.088 0.704 1.696 0.704s1.216-0.224 1.696-0.704l9.824-9.824c0.448-0.448 0.704-1.056 0.704-1.696s-0.224-1.248-0.704-1.664z"></path>
            </symbol>
        </svg>
        <script type="text/javascript" src="/static/js/jquery.min.js"></script>
        <script type="text/javascript" src="/static/js/swiper.min.js"></script>
        <script type="text/javascript" src="/static/js/shop.js"></script>
    </body>
</html>