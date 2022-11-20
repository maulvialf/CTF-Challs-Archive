<?php

require __DIR__ . '/vendor/autoload.php';

$client = new MongoDB\Client("mongodb://waifu-terbaik-mongo:27017");
$db = $client->joints;