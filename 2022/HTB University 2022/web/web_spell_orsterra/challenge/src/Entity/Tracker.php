<?php

namespace App\Entity;

use App\Repository\TrackerRepository;
use Doctrine\ORM\Mapping as ORM;

#[ORM\Entity(repositoryClass: TrackerRepository::class)]
class Tracker
{
    #[ORM\Id]
    #[ORM\GeneratedValue]
    #[ORM\Column]
    private ?int $id = null;

    #[ORM\Column(length: 255)]
    private ?string $uuid = null;

    #[ORM\Column(length: 255)]
    private ?string $x_coordinate = null;

    #[ORM\Column(length: 255)]
    private ?string $y_coordinate = null;

    #[ORM\Column]
    private ?int $live_spell = null;

    public function getId(): ?int
    {
        return $this->id;
    }

    public function getUUID(): ?string
    {
        return $this->uuid;
    }

    public function setUUID(string $uuid): self
    {
        $this->uuid = $uuid;

        return $this;
    }

    public function getXCoordinate(): ?string
    {
        return $this->x_coordinate;
    }

    public function setXCoordinate(string $x_coordinate): self
    {
        $this->x_coordinate = $x_coordinate;

        return $this;
    }

    public function getYCoordinate(): ?string
    {
        return $this->y_coordinate;
    }

    public function setYCoordinate(string $y_coordinate): self
    {
        $this->y_coordinate = $y_coordinate;

        return $this;
    }

    public function getLiveSpell(): ?int
    {
        return $this->live_spell;
    }

    public function setLiveSpell(int $live_spell): self
    {
        $this->live_spell = $live_spell;

        return $this;
    }

}
