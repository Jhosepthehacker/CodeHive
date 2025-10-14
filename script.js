import { Random } from "random-js";

const random = new Random();

const message = () => {
  const welcomeMessage = "Hola Bienvenido(a)";

  alert(welcomeMessage);
  console.log(welcomeMessage);
}

function emojiRandom(){
  const emojis = [
     "😄", "😁", "😆",
     "😃", "😉", "☺️"
  ];

  const anEmoji = random.pick(emojis);
}

message();
