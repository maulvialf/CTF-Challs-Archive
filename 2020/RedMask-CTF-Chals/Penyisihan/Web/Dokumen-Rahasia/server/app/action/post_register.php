<?php 
    if(isset($_POST['username']) && isset($_POST['password'])){
        $username = $_POST['username'];
        $password = $_POST['password'];

        $ifUserExistsQuery = $conn->query("SELECT 1 FROM users WHERE username='$username'");

        if($ifUserExistsQuery->fetchColumn())
            $error = "Username sudah terdaftar";
        elseif($username == "")
            $error = "Kolom username harus diisi";
        elseif($password == "")
            $error = "Kolom password harus diisi";

        if(!empty($errors)){
            header("location: /?error=".base64_encode($error));
            return;
        }

        $passwordHash = password_hash($password, PASSWORD_DEFAULT);

        $insertQuery = $conn->query("insert into users (username, password) values ('$username', '$passwordHash')");

        $_SESSION['login'] = array(
            "auth" => true,
            "username" => $username
        );

        header("Location: /");
    }
