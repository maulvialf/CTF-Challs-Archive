<?php

namespace App\Entity;

use App\Repository\SpellServiceRepository;
use Doctrine\ORM\Mapping as ORM;

#[ORM\Entity(repositoryClass: SpellServiceRepository::class)]
class SpellService
{
    #[ORM\Id]
    #[ORM\GeneratedValue]
    #[ORM\Column]
    private ?int $id = null;

    #[ORM\Column(length: 255, nullable: true)]
    private ?string $email = null;

    #[ORM\Column(length: 255, nullable: true)]
    private ?string $track_uuid = null;

    public function getId(): ?int
    {
        return $this->id;
    }

    public function getEmail(): ?string
    {
        return $this->email;
    }

    public function setEmail(?string $email): self
    {
        $this->email = $email;

        return $this;
    }

    public function getTrackUUID(): ?string
    {
        return $this->track_uuid;
    }

    public function setTrackUUID(?string $track_uuid): self
    {
        $this->track_uuid = $track_uuid;

        return $this;
    }
}
