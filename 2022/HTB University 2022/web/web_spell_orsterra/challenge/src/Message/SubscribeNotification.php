<?php

namespace App\Message;

class SubscribeNotification
{
    public function __construct(string $email, string $uuid, string $x_coordinate, string $y_coordinate)
    {
        $this->email = $email;
        $this->uuid = $uuid;
        $this->x_coordinate = $x_coordinate;
        $this->y_coordinate = $y_coordinate;
    }

    public function getEmail(): string
    {
        return $this->email;
    }
    public function getUUID(): string
    {
        return $this->uuid;
    }
    public function getXCoordinate(): string
    {
        return $this->x_coordinate;
    }
    public function getYCoordinate(): string
    {
        return $this->y_coordinate;
    }
}