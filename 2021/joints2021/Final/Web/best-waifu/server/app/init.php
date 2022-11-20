<?php

require_once '/var/www/config.php';

$charactersCollection = $db->characters;
$charactersCollection->insertOne([
	'name' => "JOINTS21{regex_wangy_wangy}"
]);

unlink(__FILE__);