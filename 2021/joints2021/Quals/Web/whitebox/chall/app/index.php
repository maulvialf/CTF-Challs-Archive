<?php
    $whitebox = '/tmp/whitebox/' . md5('s4ltmD5d' . $_SERVER['REMOTE_ADDR']);
    @mkdir($whitebox);
    @chdir($whitebox);
    if (isset($_GET['echo']) && strlen($_GET['echo']) <= 1) {
        $cmd = 'echo -n ' . '"' . $_GET['echo'] . '" ';
        if (isset($_GET['echo1']) && strlen($_GET['echo1']) <= 3) {
            echo $cmd . $_GET['echo1'];
            exec($cmd . $_GET['echo1']);
        }
        echo $cmd;
        exec($cmd);
    } elseif (isset($_GET['sh']) && strlen($_GET['sh']) <= 1) {
        exec('sh ' . $_GET['sh']);
        echo "Command Executed";
    } elseif (isset($_GET['reset'])) {
        exec('/bin/rm -rf ' . $whitebox);
        echo "Reset Successfully";
    } else{
        highlight_file(__FILE__);
    }
