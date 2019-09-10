<?php
include'config.php';

$sql = "SELECT id, plantNaam, locatie, temperatuur, vocht FROM plant WHERE 1";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
    while($row = mysqli_fetch_assoc($result)){
        echo "PLant naam: " . $row['plantNaam'] . "Locatie: " . $row['locatie'] . "temperatuur: " . $row['temperatuur'] . "vocht: " . $row['vocht'];

    } 
} else {
    echo "null";
}

mysqli_close($conn);


?>