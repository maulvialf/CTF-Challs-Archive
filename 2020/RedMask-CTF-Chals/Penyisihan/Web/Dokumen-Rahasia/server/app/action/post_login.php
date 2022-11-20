<?php 
    if(isset($_POST['username']) && isset($_POST['password'])){
        $username = $_POST['username'];
        $password = $_POST['password'];

        $loginQuery = $conn->query("select * from users where username='$username' limit 1");

        $user = $loginQuery->fetch();

        if(password_verify($password, $user["password"])){
            $_SESSION['login'] =  array(
                "auth" => true,
                "username" => $user["username"]
            );

            header("Location: /");
            return;
        }else{
            $error = base64_encode("Username/Password Salah");
            header("Location: /login?error=" . $error);
            return;
        }
    }
