import { Random } from "random-js";

const random = new Random();

function colorRandom(){
const colors = [
        "#0000FF", "#FF0000", "#8888FF",
        "#24DA68", "#8888FF", "#42AD86"
];

const color = random.pick(colors);

document.getElementById('mostrarInforme').style.color = color;
document.getElementById('saludando').style.color = `${color_random}`;
}

colorRandom();

let saludos = "Bienvenidos "; // Declarar variable
const saludos2 = "A Mi Página Web"; // Declarar Constante

if (saludos == "Bienvenidos"){  // Comprobando valores y condiciones de la varible saludos
        alert("¡Hola, " + saludos + saludos2 + "!");  // Mostrar alerta en la página web
        console.log("¡Hola, " + saludos + saludos2 + "!"); // Imprimir en la consola
}
// Mostrar información
function tipos(){
        colorRandom();
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
