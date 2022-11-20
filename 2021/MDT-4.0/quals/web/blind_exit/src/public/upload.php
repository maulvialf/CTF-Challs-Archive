<?php

if($_POST['upload'] && $_POST["comment"]){
    $comment = $_POST["comment"];
    $allowed_ext = array('png','jpg','jpeg');
    $filename = $_FILES['file']['name'];
    $x = explode('.', $filename);
    $ext = strtolower(end($x));
    $size	= $_FILES['file']['size'];
    $file_tmp = $_FILES['file']['tmp_name'];
    $outfilename = sha1($filename . time() . 'out'. 'randomgan');
    $outpath = 'uploads/'.$outfilename.".".$ext;

    if(in_array($ext, $allowed_ext) === true){
        
        if(mime_content_type($file_tmp) != "image/png" && mime_content_type($file_tmp) != "image/jpg" && mime_content_type($file_tmp) != "image/jpeg"){
            die("Only allowed image/jpg or image/png MIME type !");
        }

        if($size < 7000){			
            move_uploaded_file($file_tmp, $outpath);

            $check_cmd = escapeshellcmd("./exiftool $outpath");
            $write_cmd = escapeshellcmd("./exiftool -Comment='$comment' $outpath");
            shell_exec($check_cmd.";".$write_cmd);

            $image_info = getimagesize($outpath);

            header('Content-Type: ' . $image_info['mime']);
            header('Content-Length: ' . filesize($outpath));

            readfile($outpath);

        }else{
            die('Size too big !');
        }
    }else{
        die('Not allowed extension !') ;
    }
}