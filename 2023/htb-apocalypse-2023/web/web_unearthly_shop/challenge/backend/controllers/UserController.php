<?php
class UserController extends Controller
{
    public function __construct()
    {
        $privileged = True;
        parent::__construct($privileged);
    }

    public function index($router)
    {
        return $router->view('users', ['username' => $this->username, 'access' => $this->access]);
    }

    public function list($router)
    {
        $router->jsonify(['users' => $this->user->getUsers()]);
    }

    public function view($router, $params)
    {
        $id = $params[0] ?? '';

        if (empty($id)) {
            $router->jsonify(['message' => 'Insufficient Parameters!', 'status' => 'danger'], 400);
            exit;
        }

        $user  =  $this->user->getUserById($id);

        if ($user) {
            $router->jsonify(['user' => $user]);
            exit;
        }

        $router->jsonify(['message' => 'User does not exist', 'status' => 'danger'], 400);
    }

    public function update($router)
    {
        $json = file_get_contents('php://input');
        $data = json_decode($json, true);

        if (!$data['_id'] || !$data['username'] || !$data['password'])
        {
            $router->jsonify(['message' => 'Insufficient parameters!'], 400);
        }

        if ($this->user->updateUser($data)) {
            $router->jsonify(['message' => 'User updated successfully!']);
        }

        $router->jsonify(['message' => 'Something went wrong!', 'status' => 'danger'], 500);
    }

}