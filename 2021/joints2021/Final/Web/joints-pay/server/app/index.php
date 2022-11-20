<?php
require 'config.php';
$username = getUsername();

$db = new Database();
$conn = $db->getConnection();

if ($username != null) {
    $sql = 'SELECT * FROM transactions;';
    $stmt = $conn->prepare($sql);
    $stmt->execute();

    $transactions = $stmt->fetchAll();
    $balance = 0;
    foreach ($transactions as $transaction) {
        if ($transaction['to_username'] == $username) {
            $balance += intval($transaction['balance']);
        }
        if ($transaction['from_username'] == $username) {
            $balance -= intval($transaction['balance']);
        }
    }

    $receivedTransactions = [];
    foreach ($transactions as $transaction) {
        if ($transaction['to_username'] == $username && $transaction['has_read'] == 0) {
            $receivedTransactions[] = $transaction;
            $sql = "UPDATE transactions SET has_read = 1 where id = :id";
            $stmt = $conn->prepare($sql);
            $stmt->execute(['id' => $transaction['id']]);
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <title>Joints Pay</title>
    <style>
        .w3-half {
            padding: 0px 32px;
        }
    </style>
</head>
<body>
    <div class="w3-row">
        <div class="w3-container">
            <h1 class="w3-center">Joints Pay</h1>
            <p class="w3-center">Dapatkan bonus 100.000 setelah registrasi pertama!</p>
            <?php if ($username == null): ?>
                <a href="/auth.php"><p class="w3-center">Login dengan discord</p></a>
            <?php else: ?>
                <p class="w3-center">Selamat datang, <b><span id="username"></span></b></p>
            <?php endif; ?>

            <div class="w3-half">
                <div class="w3-card-4">
                    <header class="w3-container w3-blue">
                        <h4>Pengumuman</h4>
                    </header>
                    <div class="w3-container">
                        <p>Tolong kepada para hekel, webnya jangan dirusak - <i>Author: joints-pay#8174</i></p>
                        <p>Untuk sekarang web kami telah diintegrasikan dengan discord agar lebih memudahkan transaksi :) - <i>Author: joints-pay#8174</i></p>
                    </div>
                </div>
            </div>
            <?php if($username != null): ?>
                <div class="w3-half">
                    <div class="w3-card-4">
                        <header class="w3-container w3-blue">
                            <h4>Aplikasi Joints Pay</h4>
                        </header>
                        <div class="w3-container">
                            <p>Balance: <?php echo $balance; ?></p>
                            <br>
                            <b><p>Kirim Dana:</p></b>
                            <p>Username Discord Tujuan: <input type="text" id="to_username"></p>
                            <p>Pesan Singkat: <input type="text" id="messages"></p>
                            <p>Jumlah Saldo: <input type="number" id="balance"> <input type="submit" value="kirim" onclick="send()"></p>
                            <br>
                            <b><p>Notifikasi Penerimaan Dana:</p></b>
                            <?php foreach($receivedTransactions as $transaction): ?>
                                <div class="w3-card">
                                    <div class="w3-container">
                                        <p>Dari: <input type='text' value='<?php echo htmlentities($transaction['from_username']); ?>'></p>
                                        <p>Jumlah: <input type='number' value='<?php echo htmlentities($transaction['balance']); ?>'></p>
                                        <p>Pesan: <input type='text' value='<?php echo htmlentities($transaction['messages']); ?>'></p>
                                    </div>
                                </div>
                            <?php endforeach; ?>
                            <p></p>
                        </div>
                    </div>
                </div>
            <?php endif; ?>
        </div>
    </div>
    <script>
        function fetchUsername() {
            fetch('/discord.php?url=%2Fusers%2F%40me')
            .then(response => response.json())
            .then(data => {
                document.querySelector('#username').innerHTML = data.username + '#' + data.discriminator
            });
        }

        function send() {
            let to_username = document.querySelector('#to_username').value
            let messages = document.querySelector('#messages').value
            let balance = document.querySelector('#balance').value

            let formData = new FormData()
            formData.append('to_username', to_username)
            formData.append('messages', messages)
            formData.append('balance', balance)

            fetch('/send.php', {
                body: formData,
                method: 'POST'
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Pengiriman berhasil')
                } else {
                    alert('Pengiriman gagal')
                }
                location.reload()
            });
        }

        fetchUsername()
    </script>
</body>
</html>