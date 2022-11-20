<?php

require 'config.php';

$db = new Database();
$conn = $db->getConnection();

$sql = "CREATE TABLE IF NOT EXISTS users (
	id integer PRIMARY KEY,
	username text NOT NULL UNIQUE
);";
$conn->exec($sql);

$sql = "CREATE TABLE IF NOT EXISTS transactions (
	id integer PRIMARY KEY,
	from_username text,
    to_username text NOT NULL,
    messages text,
    balance integer NOT NULL,
    has_read integer NOT NULL
);";
$conn->exec($sql);