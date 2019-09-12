<?php

session_start();
 
// Check if the user is logged in, if not then redirect him to login page
if(!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true){
    header("location: login.php");
    exit;
}

?>

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="inc/css/style.css">
    
    <title>SmartPlant Project</title>
  </head>
  <body class="bg-gainsboro">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
                <a class="navbar-brand text-white" href="index.php">
                <img src="img/logo.svg" width="30" height="30" class="d-inline-block align-top mr-2" alt="">SmartPlant</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                  <span class="navbar-toggler-icon"></span>
                </button>
              
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                  <ul class="navbar-nav mr-auto">
                    <li class="nav-item active">
                      <a class="nav-link text-white" href="index.php">Home <span class="sr-only">(current)</span></a>
                    </li>
                    <li class="nav-item">
                      <a class="nav-link text-white" href="toevoegen.php">Plant toevoegen</a>
                    </li>
                  </ul>
                  <span id="Timestamp" class="text-white mr-3"><small>Laatste refresh: 00:00:00</small></span>
                  <button class="btn btn-success my-2 my-sm-0 mr-2" onclick="refresh()">Refresh</button>
                  <a href="logout.php" class="btn btn-danger my-2 my-sm-0 mr-5" >Uitloggen</a>
                  <script>
                    function refresh() {
                      const date = new Date();
                      $('#Timestamp').html(`<small>Laatste refresh: ${pad(date.getHours())}:${pad(date.getMinutes())}:${pad(date.getSeconds())}</small>`);

                      fetch('.././MARIADB/throwdata.py')
                      .then(response => response.json())
                      .then(json => {
                        //Use data fetched here
                        console.log(json);
                      });
                    }

                    $(document).ready(() => {
                      refresh();
                    });

                    function pad(n){return n<10 ? '0'+n : n}
                  </script>


<script>
function refreshPage(){
    window.location.reload();
} 
</script>
                </div>
              </nav>
              