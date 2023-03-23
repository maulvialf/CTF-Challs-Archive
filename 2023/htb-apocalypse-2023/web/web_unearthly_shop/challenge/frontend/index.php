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

$router = new Router();
$router->new("GET", "/", "ShopController@index");
$router->new("POST", "/api/products", "ShopController@products");
$router->new("POST", "/api/order", "ShopController@order");

die($router->match());
