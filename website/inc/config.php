<?php
$servername = "localhost";
$dbname = "plant";
$username = "mo";
$password = "mootje";


$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>