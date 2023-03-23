<?php
class Database
{
    private $uri;

    private static $database = null;

    private $client;
    private $db;

    public function __construct($uri)
    {
        $this->uri = $uri;

        self::$database = $this;
    }

    public static function getDatabase(): Database
    {
        return self::$database;
    }

    public function connect($database)
    {
        $this->client = new MongoDB\Client($this->uri);

        $this->db = $this->client->$database;
    }

    public function query($collection, $query)
    {
        $collection = $this->db->$collection;

        $cursor = $collection->aggregate($query);

        if (!$cursor) {
            return false;
        }

        $rows = [];

        foreach ($cursor as $row) {
            array_push($rows, $row->jsonSerialize());
        }

        return $rows;
    }

    public function insert($collection, $data)
    {
        $collection = $this->db->$collection;

        $insertOneResult = $collection->insertOne($data);

        if ($insertOneResult->getInsertedCount()) {
            return true;
        }

        return false;
    }
}
