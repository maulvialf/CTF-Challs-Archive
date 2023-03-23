<?php
class ProductModel extends Model
{
    public function __construct()
    {
        parent::__construct();
    }

    public function getProducts($query)
    {
        return $this->database->query('products', $query);
    }
}