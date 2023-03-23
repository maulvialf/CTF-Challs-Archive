<?php
class Controller
{
    public function __construct($privileged = False, $required_access = [])
    {
        $this->database = Database::getDatabase();
        $this->product  = new ProductModel;
        $this->order    = new OrderModel;
    }
}