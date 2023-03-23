<?php
class ProductModel extends Model
{
    public function __construct()
    {
        parent::__construct();
    }

    public function getProducts()
    {

        $products = $this->database->query('products',
        [
            [
                '$sort' => ['_id' => 1]
            ]
        ]);

        return $products;
    }

    public function total_products()
    {
        $products = $this->database->query('products', []);

        return count($products) ?? 0;
    }
}