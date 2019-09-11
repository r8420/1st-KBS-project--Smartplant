<?php
include('inc/header.php');
include('inc/config.php');
$plantNaam = $locatie = $fotoPlaceholder = "";
$message = "";

if (isset($_POST['voeg'])) {
    $plantNaam = $_POST['naam'];
    $locatie = $_POST['locatie'];
    $fotoPlaceholder = $_POST['foto'];
    if (empty($plantNaam && $locatie)) {
        $message = '<div class="alert alert-danger" role="alert">
            Niet alle velden zijn ingevuld!
        </div>';
    } else {
        $sql = "INSERT INTO results (naam, locatie, foto) VALUES ('$plantNaam', '$locatie', '$fotoPlaceholder')";
        $message = '<div class="alert alert-success" role="alert">
           Uw favoriete plant is toegevoegd!
        </div>';
        if (mysqli_query($conn, $sql) == TRUE) { }
    }
}

?>
<div class="container">
    <div class="row mt-4 pt-5 pb-5 bg-white rounded d-flex justify-content-center">
        <div class="card" style="width: 40%;">
            <img id="plantFoto" class="card-img-top" src="https://mdbootstrap.com/img/Photos/Others/images/43.jpg" alt="<?php echo $row['naam']; ?>">
            <div class="card-body">
                <h4 class="card-title"><a>Uw favoriete plant toevoegen</a></h4>
                <?php echo $message; ?>
                <p class="card-text">
                    <form method="post" enctype="multipart/form-data">
                    <input type="hidden" name="foto" value="plant.png">
                        <div class="form-group">
                            <input type="text" name="naam" class="form-control" placeholder="Naam plant">
                        </div>
                        <div class="form-group">
                            <input type="text" name="locatie" class="form-control" placeholder="Locatie plant">
                        </div>
                        <div class="form-group">
                            <label for="plantUploaden">Plant foto uploaden</label>
                            <input name="foto2" type="file" accept="image/*" onchange="loadFile(event);" class="form-control-file" id="plantUploaden">
                        </div>
                        <button name="voeg" type="submit" class="btn btn-primary">Voeg toe</button>
                        <script>
                            var loadFile = function(event) {
                                var output = document.getElementById('plantFoto');
                                output.src = URL.createObjectURL(event.target.files[0]);
                            };
                        </script>
                    </form>
                </p>
            </div>
        </div>
    </div>

</div>






</div>
<?php
include('inc/footer.php');
?>