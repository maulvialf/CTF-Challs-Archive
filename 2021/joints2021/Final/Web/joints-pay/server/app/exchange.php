<?php

require 'config.php';

$data = [
    'client_id' => $_ENV["DISCORD_CLIENT_ID"],
    'client_secret' => $_ENV['DISCORD_CLIENT_SECRET'],
    'grant_type'=> 'authorization_code',
    'code' => $_GET['code'],
    'redirect_uri' => $_ENV['OAUTH_REDIRECT_URL'],
    'scope' => 'identify guilds messages.read'
];

$url = $_ENV['DISCORD_API_ENDPOINT'] . '/oauth2/token';
$response = $client->request('POST', $url, [
    'form_params' => $data
]);

$token = base64_encode($response->getBody());
setcookie('token', $token, time() + 604800, "/", null, null, true);
$_COOKIE['token'] = $token;

$db = new Database();
$conn = $db->getConnection();
$conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

try {
    $username = getUsername();

    $sql = "INSERT INTO users (username) VALUES (:username)";
    $stmt = $conn->prepare($sql);
    $stmt->bindParam(':username', $username);
    $stmt->execute();

    $sql = "INSERT INTO transactions (from_username, to_username, messages, balance, has_read) VALUES ('', :to_username, '', 100000, 1)";
    $stmt = $conn->prepare($sql);
    $stmt->bindParam(':to_username', $username);
    $stmt->execute();
} catch (Exception $e) {

}

header("Location: /index.php", true, 301);
exit();