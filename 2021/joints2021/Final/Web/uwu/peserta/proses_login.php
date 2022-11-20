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
    if (count($results) != 1) {
        echo 'username atau password salah';
        exit();
    }

    $user = $results[0];

    if (!password_verify($password, $user['password'])) {
        echo 'username atau password salah';
        exit();
    }

    if ($redis->exists($username)) {
        $_SESSION['user'] = json_decode($redis->get($username), true);
    } else {
        $_SESSION['user'] = [
            'username' => $username,
            'is_admin' => false
        ];
        $redis->set($username, json_encode($_SESSION['user']));
    }

    header('Location: /index.php');
}