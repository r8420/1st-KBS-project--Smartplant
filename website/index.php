<?php
include('inc/header.php');
include('inc/config.php');

$alert = "";

$sql = "SELECT id, plantNaam, locatie, temperatuur, vocht, licht, foto FROM plant WHERE 1";
$result = mysqli_query($conn, $sql);


?>
    <div class="container">
        <div class="row mt-4">
        <?php if (mysqli_num_rows($result) > 0) {
    while($row = mysqli_fetch_assoc($result)){
?>
            <div class="col-3">
              <div class="card mb-2 bg-white-transparent d-flex align-items-center">
                <img class="card-img-top p-3 text-center" src="img/<?php echo $row['foto']; ?>" alt="Card image cap" style="width: 80%; height: 80%;">
                <div class="card-body">
                  <h4 class="card-title"><a><?php echo $row['plantNaam'] ?></a></h4>
                  <p class="card-text"><b>Locatie: </b><?php echo $row['locatie']; ?></p>
                  <ul class="list-group list-group-flush ">
                    <li class="list-group-item bg-white-transparent-0"><b>Temperatuur: </b> <?php echo $row['temperatuur']; ?>&#x2103;</li>
                    <li class="list-group-item bg-white-transparent-0"><b>Vocht: 
                      <span class="
                      <?php if ($row['vocht'] === "Voldoende"){
                        echo "text-success";
                      } else {
                        echo "text-danger";
                      } ?>">
                        <?php echo $row['vocht']; ?></span></b></li>
                    <li class="list-group-item bg-white-transparent-0"><b>Licht: 
                      <span class="
                      <?php if ($row['licht'] === "Voldoende"){
                        echo "text-success";
                      } else {
                        echo "text-danger";
                      } ?>
                      "><?php echo $row['licht']; ?></span></b></li>
                  </ul>
                </div>
              </div>
            </div>

            <?php  } 
}
?> 
    </div>
</div>
<?php
include('inc/footer.php');
?>