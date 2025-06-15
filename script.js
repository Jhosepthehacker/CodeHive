let saludos = "Bienvenidos ";
const saludos2 = "A Mi Página Web";
if (saludos == "Bienvenidos"){
        alert("¡Hola, " + saludos + saludos2 + "!");
        console.log("¡Hola, " + saludos + saludos2 + "!");
}
//Mostrar información
function tipos(){
        document.getElementById('InformacionProgramacion').style.display = 'block';
        document.getElementById('miContenido').style.display = 'block';
}
//Ocultar información
function ocultarTipos(){
        document.getElementById('miContenido').style.display = 'none';
        document.getElementById('InformacionProgramacion').style.display = 'none';
}
