<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>UnEarthly Shop | Admin</title>
        <link rel="icon" href="/static/images/logo_small.png" />
        <link rel="stylesheet" type="text/css" href="/static/css/bootstrap.min.css" />
        <link rel="stylesheet" type="text/css" href="/static/css/login.css" />
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-dark bg-unearth">
          <div class="container-fluid">
          <a class="navbar-brand" href="#"><img src="/static/images/logo_small.png" class="navbar-logo ms-2 me-2">UnEarthly Shop</a>
          </div>
        </nav>

        <div class="auth-container card">
          <img src="/static/images/logo_small.png">
          <p id="auth-p1">Sign in to continue</p>
          <form class="login-form" id="form">
              <label for="username">Username</label>
              <input name="username" type="text" id="username" class="form-control" />
              <label for="password">Password</label>
              <input name="password" type="password" id="password" class="form-control" />
              <div class="submit-btns">
                  <button type="submit" id="login-btn" class="btn btn-info">Login</button>
              </div>
              <p class="alert alert-info mt-3" id="alerts"></p>
            </form>
        </div>
    </body>
    <script type="text/javascript" src="/static/js/login.js"></script>
</html>
