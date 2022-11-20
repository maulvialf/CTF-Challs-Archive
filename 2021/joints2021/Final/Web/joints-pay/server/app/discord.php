<?php

require 'config.php';

$accessToken = getCreds()['access_token'];
$url = $_REQUEST['url'];
$method = $_SERVER['REQUEST_METHOD'];
if (isset($_REQUEST['data'])) {
    $data = json_decode(base64_decode($_REQUEST['data']), true);
} else {
    $data = [];
}


$client = new GuzzleHttp\Client();
if ($method == 'GET') {
    $response = json_decode($client->request('GET', $_ENV['DISCORD_API_ENDPOINT'].$url, [
        'headers' => ['Authorization' => "Bearer $accessToken"]
    ])->getBody(), true);
} else {
    $response = json_decode($client->request($method, $_ENV['DISCORD_API_ENDPOINT'].$url, [
        'headers' => ['Authorization' => "Bearer $accessToken"],
        'json' => $data
    ])->getBody(), true);
}

header('Content-Type: application/json');
echo json_encode($response);