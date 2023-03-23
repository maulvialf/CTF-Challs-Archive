<?php
class ProductController extends Controller
{
    public function __construct()
    {
        $privileged = True;
        parent::__construct($privileged);
    }

    public function index($router)
    {
        return $router->view('products', ['access' => $this->access]);
    }

    public function list($router)
    {
        $router->jsonify(['products' => $this->product->getProducts()]);
    }
}