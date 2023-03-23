<?php

require __DIR__ . "/vendor/autoload.php";

spl_autoload_register(function ($name) {
    if (preg_match('/Controller$/', $name)) {
        $name = "controllers/${name}";
    } elseif (preg_match('/Model$/', $name)) {
        $name = "models/${name}";
    } elseif (preg_match('/_/', $name)) {
        $name = preg_replace('/_/', '/', $name);
    }

    $filename = "/${name}.php";

    if (file_exists($filename)) {
        require $filename;
    }
    elseif (file_exists(__DIR__ . $filename)) {
        require __DIR__ . $filename;
    }
});

$database = new Database("mongodb://localhost:27017/");
$database->connect("unearthly_shop");

session_start();

$router = new Router();
$router->new('GET', '/admin/', 'AuthController@index');
$router->new('GET', '/admin/login', 'AuthController@index');
$router->new('GET', '/admin/logout', 'AuthController@logout');

$router->new('POST', '/admin/api/auth/login', 'AuthController@login');
$router->new('POST', '/admin/api/auth/register', 'AuthController@register');

$router->new('GET', '/admin/dashboard', 'DashboardController@index');

$router->new('GET', '/admin/users', 'UserController@index');
$router->new('GET', '/admin/api/users/list', 'UserController@list');
$router->new('POST', '/admin/api/users/update', 'UserController@update');
$router->new('GET', '/admin/api/users/{param}', 'UserController@view');

$router->new('GET', '/admin/orders', 'OrderController@index');
$router->new('GET', '/admin/api/orders/list', 'OrderController@list');

$router->new('GET', '/admin/products', 'ProductController@index');
$router->new('GET', '/admin/api/products/list', 'ProductController@list');

die($router->match());