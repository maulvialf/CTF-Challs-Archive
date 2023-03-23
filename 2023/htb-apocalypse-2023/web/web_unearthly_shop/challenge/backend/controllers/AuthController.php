<?php
class AuthController extends Controller
{
    public function __construct()
    {
        parent::__construct();
    }

    public function index($router)
    {
        $router->view('login');
    }

    public function login($router)
    {
        $username = $_POST['username'];
        $password = $_POST['password'];

        if (empty($username) || empty($password)) {
            $router->jsonify(['message' => 'Insufficient parameters!', 'status' => 'danger'], 400);
        }

        $login = $this->user->login($username, $password);

        if (empty($login)) {
            $router->jsonify(['message' => 'Wrong username or password!', 'status' => 'danger'], 400);
        }

        $_SESSION['username'] = $login->username;
        $_SESSION['access']   = $login->access;

        $router->jsonify(['message' => 'Login was successful!', 'status' => 'success']);
    }

    public function logout($router)
    {
        session_destroy();
        header('Location: /admin/');
        exit;
    }
}