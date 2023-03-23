<?php
class OrderController extends Controller
{
    public function __construct()
    {
        $privileged = True;
        parent::__construct($privileged);
    }

    public function index($router)
    {
        return $router->view('orders', ['access' => $this->access]);
    }

    public function list($router)
    {
        $router->jsonify(['orders' => $this->order->getOrders()]);
    }
}