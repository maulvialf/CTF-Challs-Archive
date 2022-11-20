<?php
require __DIR__ . '/config.php';
if (getUser() == null) {
    header('Location: /login.php');
    exit();
}
?> 

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>uwu</h1>
    <img src="/static/irisan-kentang/uwu/cute_bomber.png" alt="" width="200px">
    <?php if (getUser()['is_admin']): ?>
        <p>FLAG: JOINTS21{redacted_ehe}</p>
    <?php else: ?>
        <p>Hanya admin yang dapat melihat flag</p>
    <?php endif; ?>
</body>
</html>