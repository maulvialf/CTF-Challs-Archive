<?php
    $servername = "db";
    $username = "root";
    $password = "bajigur1337hekel";
    try {
        $conn = new PDO("mysql:host=$servername;dbname=yangbacawibu", $username, $password);
        // set the PDO error mode to exception
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    }catch(PDOException $e){
        die();
    }