<?php

session_start();
include __DIR__ . '/vendor/autoload.php';

class Database
{
    private $pdo;

    public function getConnection() {
        if ($this->pdo == null) {
            $this->pdo = new PDO("sqlite:" . __DIR__ . "/bank_joints_jaya.db");
        }
        return $this->pdo;
    }
}

$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();

$client = new GuzzleHttp\Client();

function getCreds()
{
    if (!isset($_COOKIE['token'])) {
        return null;
    }
    return json_decode(base64_decode($_COOKIE['token']), true);
}

function getUser()
{
    if (getCreds() == null) {
        return [];
    }

    $client = new GuzzleHttp\Client();
    $accessToken = getCreds()['access_token'];
    $user = json_decode($client->request('GET', $_ENV['DISCORD_API_ENDPOINT'].'/users/@me', [
        'headers' => ['Authorization' => "Bearer $accessToken"]
    ])->getBody(), true);
    return $user;
}

function getUsername()
{
    if (getCreds() == null) {
        return null;
    }

    $user = getUser();
    return $user['username'] . '#' . $user['discriminator'];
}