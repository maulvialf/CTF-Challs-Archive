<?php

    if(!isset($_SESSION['login']))
        $_SESSION['login'] = array(
            "auth" => false,
            "username" => null,
        );

    function middleware_guest(){
        if($_SESSION['login']["auth"]) {
            header("Location: /");
            exit();
        }       
    }

    function middleware_auth(){
        if(!$_SESSION['login']["auth"]) {
            header("Location: /login");
            exit();
        }
    }