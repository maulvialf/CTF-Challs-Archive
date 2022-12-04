<?php
namespace App\Service;

class MapExportService
{
    public $uuid;
    public $map_url;
    public $stamp_url;
    public $export_file;
    public $x_coordinate;
    public $y_coordinate;

    public function __construct($uuid, $map_url, $stamp_url, $export_file, $x_coordinate, $y_coordinate)
    {
        $this->uuid         = $uuid;
        $this->map_url      = $map_url;
        $this->stamp_url    = $stamp_url;
        $this->export_file  = $export_file;
        $this->x_coordinate = $x_coordinate;
        $this->y_coordinate = $y_coordinate;
    }

    public function fetch_image($url)
    {
        if (strpos($url, "http") !== 0) return false;

        $exportFile = '/tmp/'.md5($url);

        @file_put_contents($exportFile, @file_get_contents($url));

        return $exportFile;
    }

    public function is_image($path)
    {
        $a = getimagesize($path);
        $image_type = $a[2];

        if (in_array($image_type , array(IMAGETYPE_GIF , IMAGETYPE_JPEG ,IMAGETYPE_PNG)))
        {
            return true;
        }
        return false;
    }

    public function generateMap()
    {
        // Fetch resources
        $mapFile = $this->fetch_image($this->map_url);
        $stampFile = $this->fetch_image($this->stamp_url);

        if (!$this->is_image($mapFile) || !$this->is_image($stampFile)) return false;

        // Create Image instances
        $map = imagecreatefrompng($mapFile);
        $stamp = imagecreatefrompng($stampFile);

        // add stamp to the tracker coordinates
        imagecopymerge(
            $map,
            $stamp,
            $this->x_coordinate,
            $this->y_coordinate,
            0,
            0,
            imagesx($stamp),
            imagesy($stamp),
            100
        );

        // create watermark with details
        $stamp = imagecreatetruecolor(420, 115);

        imagefilledrectangle($stamp, 0, 0, 419, 115, 0x0000FF);
        imagefilledrectangle($stamp, 9, 9, 410, 105, 0xFFFFFF);

        imagestring($stamp, 5, 20, 20, 'Track: ' . $this->uuid, 0x0000FF);
        imagestring($stamp, 5, 20, 40, 'X-Coordinate: ' . $this->x_coordinate, 0x0000FF);
        imagestring($stamp, 5, 20, 60, 'Y-Coordinate: ' . $this->y_coordinate, 0x0000FF);
        imagestring($stamp, 5, 20, 80, 'Last Updated: ' . date("Y/m/d H:i:s"), 0x0000FF);

        // Set the margins for the stamp and get the height/width of the stamp image
        $marge_right = 10;
        $marge_bottom = 10;
        $sx = imagesx($stamp);
        $sy = imagesy($stamp);

        // Merge the stamp onto our map
        imagecopymerge($map, $stamp, imagesx($map) - 450, 10, 0, 0, imagesx($stamp), imagesy($stamp), 50);

        // Save exported map
        $savePath = '/www/public/static/exports/' . $this->export_file;
        imagepng($map, $savePath);
    }

    public function getExportedMap()
    {
        $savePath = '/www/public/static/exports/' . $this->export_file;
        $mapData = base64_encode(file_get_contents($savePath));

        return $mapData;
    }

}