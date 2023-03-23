<?php
class ShopController extends Controller
{
    public function __construct()
    {
        parent::__construct();
    }

    public function index($router)
    {
        $router->view('index');
    }

    public function products($router)
    {
        $json = file_get_contents('php://input');
        $query = json_decode($json, true);

        if (!$query)
        {
            $router->jsonify(['message' => 'Insufficient parameters!'], 400);
        }

        $products = $this->product->getProducts($query);

        $router->jsonify($products);
    }

    public function order($router)
    {
        $json = file_get_contents('php://input');
        $data = json_decode($json, true);

        if (!$data['name'] || !$data['email'] || !$data['bid'] || !$data['item_id'])
        {
            $router->jsonify(['message' => 'Insufficient parameters!'], 400);
        }

        $this->order->placeOrder($data['name'], $data['email'], $data['bid'], $data['item_id']);

        $router->jsonify(['message' => 'Order placed successfully!']);
    }
}