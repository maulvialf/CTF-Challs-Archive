<?php
class OrderModel extends Model
{
    public function __construct()
    {
        parent::__construct();
    }

    public function placeOrder($name, $email, $bid, $item_id)
    {
        return $this->database->insert('orders',
        [
            'name'    => $name,
            'email'   => $email,
            'bid'     => $bid,
            'item_id' => $item_id
        ]);
    }
}