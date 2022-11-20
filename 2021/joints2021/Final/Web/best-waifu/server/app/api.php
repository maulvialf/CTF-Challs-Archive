<?php

require_once 'config.php';

function str_random($length) 
{ 
    $string = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'; 
    return substr(str_shuffle($string),  
                        0, $length); 
} 

function verifyWaifu($chara) 
{
    $waifu = [
        'keqing', 'jean', 'hutao', 'ganyu'
    ];

    if (!in_array($chara, $waifu)) {
        header('Content-Type: application/json');
        $response = [
            'success' => false,
            'error' => 'karakter tidak ditemukan'
        ];
        echo json_encode($response);
        exit;
    }
}

// Insert vote
if (isset($_POST['character'])) {
    $chara = $_POST['character'];
    verifyWaifu($chara);

    $charactersCollection = $db->characters;
    $charactersCollection->insertOne([
        'name' => $chara
    ]);
    header('Content-Type: application/json');
    $response = [
        'success' => true
    ];
    echo json_encode($response);
    exit;
}

// Get votes count
if (isset($_GET['character'])) {
    $chara = $_GET['character'];

    // filter
    $chara = str_replace(';', '', $chara);
    $chara = str_replace('/', '', $chara);
    $chara = str_replace('eval', '', $chara);
    $chara = str_replace('require', '', $chara);
    $chara = str_replace('`', '', $chara);

    $charactersCollection = $db->characters;
    $totalData = $charactersCollection->count([
        '$where' => "this.name == '$chara'"
    ]);

    header('Content-Type: application/json');
    $response = [
        'success' => true,
        'data' => [
            'name' => $chara,
            'vote_count' => $totalData
        ]
    ];
    echo json_encode($response);
    exit;
}
?>
