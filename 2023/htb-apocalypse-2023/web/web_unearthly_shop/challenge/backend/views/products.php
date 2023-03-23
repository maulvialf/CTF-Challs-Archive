<!DOCTYPE html>
<html lang="en">
   <head>
      <meta charset="UTF-8" />
      <title>UnEarthly Shop | Products</title>
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
      <div class="container-lg mt-5" id="products-container">
         <div class="card">
            <h5 class="card-header text-uppercase">
                Products
            </h5>
            <div class="card-body">
               <p id="products-stat"></p>
               <div class="table-responsive" id="products-table">
                  <table class="table table-stripped">
                     <thead>
                        <tr>
                           <th> ID </th>
                           <th> Name </th>
                           <th> price </th>
                           <th> in stock </th>
                           <th class="text-center"> image </th>
                           <th style="width: 250px"> Action </th>
                        </tr>
                     </thead>
                     <tbody>
                     </tbody>
                  </table>
               </div>
            </div>
         </div>
      </div>

   </body>
   <script type="text/javascript" src="/static/js/jquery.min.js"></script>
   <script type="text/javascript" src="/static/js/products.js"></script>
</html>