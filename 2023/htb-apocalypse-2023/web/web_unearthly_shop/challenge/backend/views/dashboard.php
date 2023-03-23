<!DOCTYPE html>
<html lang="en">
   <head>
      <meta charset="UTF-8" />
      <title>BumpyPanda | User</title>
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
      <div class="container m-3">
        <h5>Welcome back <?php echo $username; ?></h5>
      </div>
      <div class="container-xl mt-4">
         <div class="row justify-content-center">
            <div class="col-3">
                <a class="text-decoration-none" href="/admin/products"><div class="card">
                    <h5 class="card-header text-uppercase text-center">
                        Products
                    </h5>
                    <div class="card-body">
                       <p class="stat-num" id="product-stat"><?php echo $products; ?></p>
                    </div>
                 </div>
                </a>
            </div>
            <div class="col-3">
                <a class="text-decoration-none" href="/admin/orders"><div class="card">
                    <h5 class="card-header text-uppercase text-center">
                        Orders
                    </h5>
                    <div class="card-body">
                       <p class="stat-num" id="product-stat"><?php echo $orders; ?></p>
                    </div>
                 </div>
                </a>
            </div>
            <div class="col-3">
                <a class="text-decoration-none" href="/admin/users"><div class="card">
                    <h5 class="card-header text-uppercase text-center">
                        Users
                    </h5>
                    <div class="card-body">
                       <p class="stat-num" id="product-stat"><?php echo $users; ?></p>
                    </div>
                 </div>
                </a>
            </div>
        </div>
      </div>


   </body>
</html>