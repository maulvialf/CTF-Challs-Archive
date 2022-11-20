<?php
    // error_reporting(0);
    session_start();

    require __DIR__ . "/../bootstrap/config.php";
    require __DIR__ . "/../bootstrap/middleware.php";
    require __DIR__ . "/../bootstrap/helper.php";


    $route = function ($method, $path, $action, $middleware = '') use ($conn) {
        $requestMethod = $_SERVER['REQUEST_METHOD'];
        $requestUri = explode('?', $_SERVER['REQUEST_URI'], 2)[0];

        if ($path == $requestUri) {
            if ($method == $requestMethod) {
                if ($middleware !== '') {
                    ('middleware_' . $middleware)();
                }
                require __DIR__ . "/../action/" . $action . ".php";
                exit();
            }
        }
    };

    $route('GET', '/', 'view_home', 'auth');
    $route('GET', '/login', 'view_login', 'guest');
    $route('POST', '/login', 'post_login', 'guest');
    $route('GET', '/register', 'view_register', 'guest');
    $route('POST', '/register', 'post_register', 'guest');
    $route('GET', '/logout', 'logout');

    require __DIR__ . "/../view/404.php";