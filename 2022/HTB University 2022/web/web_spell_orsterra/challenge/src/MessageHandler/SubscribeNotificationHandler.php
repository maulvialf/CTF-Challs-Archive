<?php

namespace App\MessageHandler;

use App\Service\MapExportService;
use App\Message\SubscribeNotification;
use Symfony\Component\Messenger\Handler\MessageHandlerInterface;
use App\Repository\TrackerRepository;
use App\Entity\Tracker;

class SubscribeNotificationHandler implements MessageHandlerInterface
{
    public $email;
    public $uuid;
    public $export_file;
    public $x_coordinate;
    public $y_coordinate;

    public $map = 'http://localhost/static/images/clean_map.png';
    public $stamp = 'http://localhost/static/images/stamp.png';

    public function __invoke(SubscribeNotification $notification)
    {
        $this->email = $notification->getEmail();
        $this->uuid = $notification->getUUID();
        $this->x_coordinate = $notification->getXCoordinate();
        $this->y_coordinate = $notification->getYCoordinate();

        $this->export_file = md5($this->uuid) . '.png';
    }

    public function __destruct()
    {
        $exportMap = new MapExportService(
            $this->uuid,
            $this->map,
            $this->stamp,
            $this->export_file,
            $this->x_coordinate,
            $this->y_coordinate
        );

        $exportMap->generateMap();

        $mapImage = $exportMap->getExportedMap();

        $email_content = '
        <div style="background: #006b86; color: #fff; margin:0; padding: 0;">
            <p>&nbsp;</p>
            <p style="text-align: center;"><strong>Live Tracker Update</strong></p>
            <p style="text-align: center;">&nbsp;</p>
        </div>
        <img src="data:image/png;base64,'.$mapImage.'" style="width:100%; margin:0; padding: 0;">
        <div style="background: #0a7191; color: #fff">
            <p>&nbsp;</p>
            <p style="text-align: center;"><strong>&copy; Spell Orsterra</strong></p>
            <p>&nbsp;</p>
        </div>
        ';

        @mail($this->email, 'Live Tracker Update', $this->body);
    }
}