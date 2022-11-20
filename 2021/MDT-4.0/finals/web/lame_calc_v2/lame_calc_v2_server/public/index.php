<html>
  <head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
    <style>
      .divx {
        width: 60%;
        margin: auto;
      }

      .output_res {
        background-color: rgb(231, 224, 224);
        height: 600px;
        overflow: auto;
        border: indigo;
        border-width: medium;
        border-style: bold;
      }
    </style>
    <title>Calc App</title>
    <h1 style="text-align: center;">Caculate your equation</h1>
  </head>

  <body>
    <div class="divx">
      <form id="fetch_form" action="/" method="POST">
        <div class="form-group">
          <label for="eq_input">Equation</label>
          <input type="text" class="form-control" name="equation" id="eq_input" aria-describedby="" placeholder="Enter Equation">
        </div>
        <br>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
      <br>
      <p id="output_fetch" class="output_res">
        <?php

        if (isset($_POST["equation"])){
            $eq = $_POST["equation"];

            if (strlen($eq) > 265){
                die("Too long !");
            }

            if(preg_match("/\~|\||\[|\]|\`|\'|\||\^|}|{|;|@|&|#|!|\>|\?|\</i",$eq)){
                die("Bad Char !");
            }

            $blacklist = "include|read|all|open|file|dir|opt|glob|object|iter|eval|return|field|close|set|require";

            if (preg_match("/$blacklist/i", $eq)){
                die("Bad Word !");
            }

            eval("echo " . $eq . " ;");

        }

        ?>

      </p>
    </div>
  </body>

  <footer>

  </footer>

</html>

