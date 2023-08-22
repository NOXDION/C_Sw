<h1>Codigo HTML</h1>

<?php

# Esto va a imprimir
echo '<h1>Codigo PHP</h1>';
print('Otra funcion para imprimir en pantalla');

// Este comentario no se interpreta

// Variables
$nombre = 'Esteban';
$texto = "Repaso de PHP con $nombre";
$altura = 1.72;

echo '<h2>'.$texto.'</h2>';

$textoFinal = "<h4>Tu nombre es ". $nombre ." y tu altura es ".$altura.".</h4>";

echo $textoFinal;

$textoFinal .= "<h4>Has sido trolleado</h4>";

echo $textoFinal;


// Get
echo $_GET["altura"];

// Condiciones

if(!$altura){
    $altura = 180;
}

if($altura >= 180){
    echo "<h4>Eres una persona alta.</h4>";
} else {
    echo "<h4>Eres una persona baja.</h4>";
}




?>