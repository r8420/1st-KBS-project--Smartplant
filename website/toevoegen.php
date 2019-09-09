<?php
include('inc/header.php');
?>
    <div class="container">
        <div class="row mt-4 pt-5 pb-5 bg-white rounded d-flex justify-content-center">
            <div class="card" style="width: 40%;">
                <img class="card-img-top" src="https://mdbootstrap.com/img/Photos/Others/images/43.jpg"
                    alt="Card image cap">
                <div class="card-body">
                    <h4 class="card-title"><a>Uw favoriete plant toevoegen</a></h4>
                    <p class="card-text">
                        <form>
                            <div class="form-group">
                                <input type="text" class="form-control" placeholder="Naam plant">
                            </div>
                            <div class="form-group">
                                <input type="text" class="form-control" placeholder="Locatie plant">
                            </div>
                            <div class="form-group">
                                <label for="plantUploaden">Plant foto uploaden</label>
                                <input type="file" class="form-control-file" id="plantUploaden">
                            </div>
                            <button type="submit" class="btn btn-primary">Voeg toe</button>
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