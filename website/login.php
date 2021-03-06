<?php
session_start();

if(isset($_SESSION["loggedin"]) && $_SESSION["loggedin"] === true){
    header("location: index.php");
    exit;
}

$err = "";

if ($_SERVER["REQUEST_METHOD"] == "POST"){
    $gebruiksnaam = $_POST['username'];
    $wachtwoord = $_POST['password'];
    
    if (empty($wachtwoord) || empty($gebruiksnaam)) {
        $err = '<div class="alert alert-danger" role="alert">
        Gebruiksnaam of wachtwoord is onjuist!
      </div>';
    }
    if ($wachtwoord == "SmartPlant" && $gebruiksnaam == "Admin"){
        $_SESSION["loggedin"] = true;
        $_SESSION["username"] = $gebruiksnaam;                            
        header("location: index.php");
    }
}


?>




<!DOCTYPE >
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Jekyll v3.8.5">
    <title>Signin Template · Bootstrap</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/4.3/examples/sign-in/">

    <!-- Bootstrap core CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">


    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }
    </style>
    <!-- Custom styles for this template -->
    <link href="inc/css/login.css" rel="stylesheet">
  </head>
  <body class="text-center">
     
    <form class="form-signin" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
  <img class="mb-4" src="img/logo.svg" alt="" width="72" height="72">
  <h1 class="h3 mb-3 font-weight-normal">Inloggen</h1>
  <?php  echo $err; ?>
  <label for="inputEmail" class="sr-only">Gebruikersnaam</label>
  <input type="text" name="username" value="" id="inputEmail" class="form-control" placeholder="Gebruikersnaam" autofocus>
  <span class="help-block"></span>
  <label for="inputPassword" class="sr-only">Wachtwoord</label>
  <input type="password" name="password" id="inputPassword" class="form-control" placeholder="Password">
  <button class="btn btn-lg btn-primary btn-block" type="submit" name="login" value="Login">Inloggen</button>

</form>


</body>
</html>