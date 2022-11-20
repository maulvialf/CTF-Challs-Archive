<form action="/" method="POST">
    Enter your equation : <br>
    <input type="text" name="equation"><br>
    <input type="submit" name="submit" value="Submit">
</form>

<?php

if (isset($_POST["equation"])){
    $eq = $_POST["equation"];

    if (strlen($eq) > 57){
        die("Too long !");
    }

    if(preg_match("/\~|\&|\||\[|\]|\.|\`|\'|\||\+|\-|\>|\?|\<|\//i",$eq)){
        die("Bad Char !");
    }

    eval("echo " . $eq . " ;");

}

?>