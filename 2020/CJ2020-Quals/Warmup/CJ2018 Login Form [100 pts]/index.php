<?php

require_once 'flag.php';

function login($username, $hash) {
    if ($username === 'cyber'
        && $hash === 'ac3821b0bd0b0a9a130db104248f1a140c2ab439') {
        return true;
    } else {
        return false;
    }
}

function render_login_page() {
    $template = file_get_contents('template.html');
    print $template;
}

function init($flag) {
    $query = array();
    if (!empty($_SERVER['QUERY_STRING'])) {
        $query_str = $_SERVER['QUERY_STRING'];
        $query = parse_str($query_str);
    }

    if (!empty($query['action'])) {
        $action = $query['action'];
    }

    if ($action === 'login') {
        if (!empty($query['username'])) {
            $username = $query['username'];
        }

        if (!empty($query['password'])) {
            $password = $query['password'];
        }

        if (!empty($username) && !empty($password)) {
            $hash_password = sha1($password);
        }

        if (!empty($hash_password) && login($username, $hash_password)) {
            print "<h1>Welcome!</h1><br>";
            print $flag;
        } else {
            print 'Wrong!';
        }
    } else {
        render_login_page();
    }
}

init($flag);

