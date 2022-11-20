<?php

function view($content, $data = [])
{
    extract($data);
    extract([
        'content' => $content . '.php'
    ]);
    require __DIR__ . '/../view/base.php';
    return;
}

function safe($value) 
{
	return htmlspecialchars(strip_tags($value));
}