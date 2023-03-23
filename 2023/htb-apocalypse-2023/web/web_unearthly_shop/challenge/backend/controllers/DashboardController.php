<?php
class DashboardController extends Controller
{
    public function __construct()
    {
        $privileged = True;
        parent::__construct($privileged);
    }

    public function index($router)
    {
        $users = $this->user->total_users();
        $products = $this->product->total_products();
        $orders = $this->order->total_orders();

        $router->view('dashboard', [
            'username' => $this->username,
            'access'   => $this->access,
            'users'    => $users,
            'products' => $products,
            'orders'   => $orders
        ]);
    }
}