<?php

require 'config.php';

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    header('Content-Type: application/json');
    echo json_encode([
        'success' => 'false',
        'error' => 'Method not supported'
    ]);
    exit();
}

$db = new Database();
$conn = $db->getConnection();

$username = getUsername();
if ($username == null) {
    header('Content-Type: application/json');
    echo json_encode([
        'success' => 'false',
        'error' => 'Unauthorized'
    ]);
    exit();
}

try {
    $sql = "INSERT INTO transactions (from_username, to_username, messages, balance, has_read) values (:user_from, :user_to, :messages, :balance, 0)";
    $stmt = $conn->prepare($sql);
    $stmt->execute([
        'user_from' => $username,
        'user_to' => $_POST['to_username'],
        'messages' => $_POST['messages'],
        'balance' => $_POST['balance']
    ]);

    header('Content-Type: application/json');
    echo json_encode([
        'success' => 'true'
    ]);
    exit();
} catch (Exception $e) {
    header('Content-Type: application/json');
    echo json_encode([
        'success' => 'false',
        'error' => 'Terjadi kesalahan'
    ]);
    exit();
}