<?php

require 'config.php';

$conn = Database::getConnection();

$sql = "CREATE TABLE IF NOT EXISTS users (
	id integer PRIMARY KEY,
	username text NOT NULL,
    password text NOT NULL
);";
$conn->exec($sql);