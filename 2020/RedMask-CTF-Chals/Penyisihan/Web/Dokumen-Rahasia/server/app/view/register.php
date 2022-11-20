<h1>Form Registrasi</h1>
<div class="row">
    <div class="col-12">
    <form action="/register" method="POST">
        Username: <input type="text" class="form-control" name="username"><br>
        Password: <input type="password" class="form-control" name="password"><br>
        <input class="btn btn-primary" type="submit" name="register" value="register">
        <?php if(isset($_GET['error'])): ?>
            <?php echo "<p>".safe(base64_decode($_GET['error']))."</p>"; ?>
        <?php endif; ?>
    </form>
    </div>
</div>