<?php
class UserModel extends Model
{
    public function __construct()
    {
        parent::__construct();
        $this->username = $_SESSION['username'] ?? '';
        $this->email    = $_SESSION['email'] ?? '';
        $this->access   = unserialize($_SESSION['access'] ?? '');
    }

    public function login($username, $password)
    {
        $login = $this->database->query('users',
        [
            [
                '$match' => [
                    'username' => strval($username),
                    'password' => strval($password)
                ]
            ]
        ]);

        return $login[0] ?? [];
    }

    public function total_users()
    {
        $users = $this->database->query('users', []);

        return count($users) ?? 0;
    }

    public function getUsers()
    {

        $users = $this->database->query('users',
        [
            [
                '$project' => [
                    '_id' => 1,
                    'username' => 1
                ]
            ]
        ]);

        return $users;
    }

    public function getUserById($id)
    {
        $user = $this->database->query('users',
        [
            [
                '$match' => [
                    '_id' => intval($id)
                ],
            ],
            [
                '$project' => [
                    '_id' => 1,
                    'username' => 1,
                    'access' => 1
                ]
            ]
        ]);

        return $user[0] ?? [];
    }

    public function updateUser($data)
    {
        return $this->database->update('users', $data['_id'], $data);
    }

}