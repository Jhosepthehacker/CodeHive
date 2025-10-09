import {Random} from "random-js";

const random = new Random();

while (true){
const colors = [
        "#0000FF", "#FF0000", "#8888FF",
        "#24DA68", "#8888FF", "#42AD86"
];

const colorRandom = Random.choice(colors);

document.getElementById('mostrarInforme').style.color = `${color_random}`;
}

let saludos = "Bienvenidos "; // Declarar variable
const saludos2 = "A Mi Página Web"; // Declarar Constante

if (saludos == "Bienvenidos"){  // Comprobando valores y condiciones de la varible saludos
        alert("¡Hola, " + saludos + saludos2 + "!");  // Mostrar alerta en la página web
        console.log("¡Hola, " + saludos + saludos2 + "!"); // Imprimir en la consola
}
// Mostrar información
function tipos(){
        document.getElementById('informacionProgramacion').style.display = 'block';
        document.getElementById('report').style.margin = '60px';
        document.getElementById('contacto').style.margin = '20px';
}
// Ocultar información
function ocultarTipos(){
        document.getElementById('informacionProgramacion').style.display = 'none';
        document.getElementById('contacto').style.margin = '0';
}

// En desarrollo....
