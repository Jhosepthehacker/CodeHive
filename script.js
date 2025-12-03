const random = new Random();

const message = () => {
  const welcomeMessage = "Hola Bienvenido(a)";

  alert(welcomeMessage);
  console.log(welcomeMessage);
}

const seeEmoji = () => {
  document.getElementById('emojiHappy').style.display = "block";
}

message();
