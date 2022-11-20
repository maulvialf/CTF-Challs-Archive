<?php

$password = "8682a65aa7f080e0d8511018a9f64d77";
if ($_GET['p'] === $password) {
    $token = "";
    setcookie('token', $token, time() + 604800, "/", null, null, true);
    $_COOKIE['token'] = $token;

    header('Location: /index.php');
} else {
    header('Location: /index.php');
}
