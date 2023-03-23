<?php
class OrderModel extends Model
{
    public function __construct()
    {
        parent::__construct();
    }

    public function getOrders()
    {

        $orders = $this->database->query('orders',
        [
            [
                '$sort' => ['_id' => 1]
            ]
        ]);

        return $orders;
    }

    public function total_orders()
    {
        $orders = $this->database->query('orders', []);

        return count($orders) ?? 0;
    }
}