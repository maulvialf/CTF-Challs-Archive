<?php

require 'config.php';

$authURL = $_ENV['DISCORD_AUTH_URL'];
header("Location: $authURL", true, 301);
exit();