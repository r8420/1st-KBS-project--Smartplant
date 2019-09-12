<?php
include('inc/header.php');
include('inc/config.php');
$plantNaam = $locatie = $fotoPlaceholder = $idkoppeling = $message = "";

if (isset($_POST['voeg']) && isset($_FILES['foto'])) {
    // foto upload
    $errors= array();
    $file_name = $_FILES['foto']['name'];
    $file_size =$_FILES['foto']['size'];
    $file_tmp =$_FILES['foto']['tmp_name'];
    $file_type=$_FILES['foto']['type'];
    $file_ext=strtolower(end(explode('.',$_FILES['foto']['name'])));
    
    $extensions= array("jpeg","jpg","png");

    if(in_array($file_ext,$extensions)=== false){
        $errors[]="extension not allowed, please choose a JPEG or PNG file.";
     }
     
     if($file_size > 2097152){
        $errors[]='File size must be excately 2 MB';
     }
     
     if(empty($errors)==true){
        move_uploaded_file($file_tmp,"img/uploads/".$file_name);
     }else{
        print_r($errors);
     }

    // gegevens upload
    $plantNaam = $_POST['naam'];
    $locatie = $_POST['locatie'];
    $fotoPlaceholder = $_POST['foto'];
    $idkoppeling = $_POST['idkoppeling'];
    if (empty($plantNaam && $locatie && $idkoppeling)) {
        $message = '<div class="alert alert-danger" role="alert">
            Niet alle velden zijn ingevuld!
        </div>';
    } else {
        $sql = "INSERT INTO results (naam, locatie, foto, idkoppeling) VALUES ('$plantNaam', '$locatie', '$file_name', '$idkoppeling')";
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
                    <form method="post" action="" enctype="multipart/form-data">
                        <div class="form-group">
                            <input type="text" name="naam" class="form-control" placeholder="Naam plant">
                        </div>
                        <div class="form-group">
                            <input type="text" name="locatie" class="form-control" placeholder="Locatie plant">
                        </div>
                        <div class="form-group">
                                <select class="form-control" name="idkoppeling">
                                    <option >Plant koppelen</option>
                                    <option value="1" name="idkoppeling" >Raspberry 1</option>
                                    <option value="2" name="idkoppeling" >Raspberry 2</option>
                                    <option value="3" name="idkoppeling" >Raspberry 3</option>
                                    <option value="4" name="idkoppeling" >Raspberry 4</option>
                                    <option value="5" name="idkoppeling" >Raspberry 5</option>
                                </select>
                        </div>
                        <div class="form-group">
                            <label for="plantUploaden">Plant foto uploaden</label>
                            <input name="foto" type="file" accept="image/*" onchange="loadFile(event);" class="form-control-file" id="plantUploaden">
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