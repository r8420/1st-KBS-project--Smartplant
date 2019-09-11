<?php
include('inc/header.php');
include('inc/config.php');

$alert = "";
$id = "";

$sql = "SELECT id, naam, locatie, temp, vocht, licht, foto, tempC FROM results WHERE 1";
$result = mysqli_query($conn, $sql);





?>
    <div class="container">
        <div class="row mt-4">
        <?php if (mysqli_num_rows($result) > 0) {
    while($row = mysqli_fetch_assoc($result)){
      $id = $row['id'];
?>
            <div class="col-sm-3">
              <div class="card mb-2 bg-white-transparent d-flex align-items-center">
                <img class="card-img-top p-3 text-center" src="img/<?php echo $row['foto']; ?>" alt="<?php echo $row['naam']; ?>" style="width: 80%; height: 80%;">
                <div class="card-body">
                  <h4 class="card-title"><a><?php echo $row['naam'] ?></a></h4>
                  <p class="card-text"><b>Locatie: </b><?php echo $row['locatie']; ?></p>
                  <ul class="list-group list-group-flush ">
                    <li class="list-group-item bg-white-transparent-0"><b>Temperatuur: </b> <?php echo $row['temp']; ?>&#x2103;</li>
                    <li class="list-group-item bg-white-transparent-0"><b>Vocht: 
                      <?php if ($row['vocht'] === '0') {
                        echo '<span class="text-success">Voldoende</span>';
                      }else{
                        echo '<span class="text-danger">Onvoldoende</span>';
                      }?>
                    </b></li>
                    <li class="list-group-item bg-white-transparent-0"><b>Licht: 
                    <?php if ($row['licht'] === '1') {
                        echo '<span class="text-success">Voldoende</span>';
                      }else{
                        echo '<span class="text-danger">Onvoldoende</span>';
                      }?>
                    </b></li>
                    <li class="list-group-item bg-white-transparent-0">
                      <form method="post" action="">
                      <button class="btn btn-outline-danger btn-sm" type="submit" value="<?php echo $row['id']; ?>" name="verwijderen" onClick="refreshPage()">Plant verwijderen</button>
                    </form>
                    </li>
                  </ul>
                </div>
              </div>
            </div>

            <?php  } 
}
if (isset($_POST['verwijderen'])) {
  $delete = "DELETE FROM results WHERE id=".$_POST['verwijderen'];
  if(mysqli_query($conn, $delete)){
    
} else{
    echo "ERROR: Could not able to execute $sql. " . mysqli_error($delete);
}
}
?> 
    </div>
</div>
<?php
include('inc/footer.php');
?>