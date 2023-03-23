<?php
class Controller
{
    public $user;
    public $access;
    public $username;

    public function __construct($privileged = False, $required_access = [])
    {
        $this->database = Database::getDatabase();
        $this->user     = new UserModel;
        $this->product  = new ProductModel;
        $this->order    = new OrderModel;

        if ($privileged) {
            if (empty($this->user->username)) {
                header('Location: /admin/');
                exit;
            }

            $this->username = $this->user->username;
            $this->email    = $this->user->email;
            $this->access   = $this->user->access;

            $controller = preg_replace('/Controller/','',get_called_class());

            if (!$this->access[$controller]) {
                header('Location: /admin/?msg=Access+Denied');
                exit;
            }
        }

    }
}