<!DOCTYPE html>
<html lang="en">
   <head>
      <meta charset="UTF-8" />
      <title>UnEarthly Shop | Users</title>
      <link rel="icon" href="/static/images/logo_small.png" />
      <link rel="stylesheet" type="text/css" href="/static/css/bootstrap.min.css" />
      <link rel="stylesheet" type="text/css" href="/static/css/main.css" />
   </head>
   <body>
   <nav class="navbar navbar-expand-lg navbar-dark bg-unearth">
          <div class="container-fluid">
          <a class="navbar-brand" href="#"><img src="/static/images/logo_small.png" class="navbar-logo ms-2 me-2">UnEarthly Shop</a>
            <div class="collapse navbar-collapse" id="navbarMain">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item">
                            <a class="nav-link" href="/admin/dashboard">Dashboard</a>
                    </li>
                    <?php if($access['Product']): ?>
                     <li class="nav-item">
                            <a class="nav-link" href="/admin/products">Products</a>
                    </li>
                    <?php endif; ?>
                    <?php if($access['Order']): ?>
                     <li class="nav-item">
                            <a class="nav-link" href="/admin/orders">Orders</a>
                    </li>
                    <?php endif; ?>
                    <?php if($access['User']): ?>
                     <li class="nav-item">
                            <a class="nav-link" href="/admin/users">Users</a>
                    </li>
                    <?php endif; ?>
                </ul>
               <ul class="navbar-nav ms-auto">
                  <li class="nav-item">
                     <a class="nav-link" href="/admin/logout">Logout</a>
                  </li>
               </ul>
            </div>
         </div>
      </nav>
      <div class="container-lg mt-5" id="users-container">
         <div class="card">
            <h5 class="card-header text-uppercase">
                Users
            </h5>
            <div class="card-body">
               <p id="users-stat"></p>
               <div class="table-responsive" id="users-table">
                  <table class="table table-stripped">
                     <thead>
                        <tr>
                           <th> ID </th>
                           <th> Username </th>
                           <th style="width: 150px"> Action </th>
                        </tr>
                     </thead>
                     <tbody>
                     </tbody>
                  </table>
               </div>
            </div>
         </div>
      </div>

      <div class="container-lg mt-5 hidden" id="user-view-container">
            <div class="row g-0 w-100 mb-2">
                <div class="row g-0 w-100 mb-1">
                    <div class="col text-start">
                    <button class="btn btn-secondary" id="back-user-btn">← Users</button>
                    </div>
                </div>
            </div>
        <div class="card" id="user-card">

        </div>
       </div>


   </body>
   <script type="text/javascript" src="/static/js/jquery.min.js"></script>
   <script type="text/javascript" src="/static/js/users.js"></script>
</html>