<?php

// error_reporting(0);
session_start();
require __DIR__ . "/../bootstrap/middleware.php";

middleware_auth();

if (!isset($_GET['name'])) {
    echo 'Parameter "name" not set.';
    die();
}

$doc = $_GET['name'];
include $doc . '.secret';