<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Tag !</title>
</head>
<body>
    <h1>Tag your comment on an Image !</h1>
    <h3>Upload file</h3>
    <form action="/upload.php" method="POST" enctype="multipart/form-data">
        <input type="file" name="file"><br>
        Your Comment :
        <input type="text" name="comment"><br>
        <input type="submit" name="upload" value="Upload">
    </form>
    <p>*Only accept file image jpg/jpeg/png</p>
</body>
</html>
