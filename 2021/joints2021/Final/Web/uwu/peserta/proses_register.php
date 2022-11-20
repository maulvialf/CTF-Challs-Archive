<?php

require __DIR__ . '/config.php';

$conn = Database::getConnection();

if (isset($_POST['submit'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    if ($username == '' || $password == '') {
        echo 'username/password tidak boleh kosong';
        exit();
    }

    if (!preg_match("/^[a-zA-Z0-9]+$/", $username)) {
        echo 'username hanya dapat berupa alphanumeric';
        exit();
    }

    try {
        $stmt = $conn->prepare('SELECT * FROM users WHERE username = :username');
        $stmt->bindParam(':username', $username);
        $stmt->execute();
    } catch (Exception $e) {
        die('error');
    }

    $results = $stmt->fetchAll();
    if (count($results) > 0) {
        echo 'username telah terdaftar';
        exit();
    }

    try {
        $stmt = $conn->prepare('INSERT INTO users (username, password) VALUES (:username, :password)');
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':password', password_hash($password, PASSWORD_BCRYPT));
        $stmt->execute();
    } catch (Exception $e) {
        die('error');
    }

    header('Location: /login.php');
}