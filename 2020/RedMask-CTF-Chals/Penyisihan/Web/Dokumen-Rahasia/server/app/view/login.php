<h1>Login</h1>
<div class="row">
    <div class="col-12">
    <form action="/login" method="POST">
        Username: <input type="text" class="form-control" name="username"><br>
        Password: <input type="password" class="form-control" name="password"><br>
        <input class="btn btn-primary" type="submit" name="login" value="login">
        <?php if(isset($_GET['error'])): ?>
            <?php echo "<p>".safe(base64_decode($_GET['error']))."</p>"; ?>
        <?php endif; ?>
    </form>
    </div>
</div>