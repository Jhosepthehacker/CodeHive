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
