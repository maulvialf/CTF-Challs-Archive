<?php

require __DIR__ . '/vendor/autoload.php';

session_start();

$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->safeLoad();

$redis = new Predis\Client('unix:/tmp/redis.sock');

class Database
{
    private static $pdo;

    public static function getConnection() {
        if (self::$pdo == null) {
            self::$pdo = new PDO("sqlite:" . $_ENV['DB_NAME']);
        }
        return self::$pdo;
    }
}

function getUser()
{
    if (isset($_SESSION['user'])) {
        return $_SESSION['user'];
    } else {
        return false;
    }
}