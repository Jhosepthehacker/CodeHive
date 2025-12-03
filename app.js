const sendRequests = () => {
  async function getData() {
    // Prueba de API en localhost
    const API_URL = "http://127.0.0.1:8080/message";

    const response = await fetch(API_URL, {
      method: 'GET'
    });

    try {
      if (!response.ok) {
        throw new Error(`Ha ocurrido un error: ${response.ok}`);
      }

      const json = await response.json();
      const message = json.message;

      alert("Response Of The Backend: " + message);
      console.log("Response Of The Backend: " + message);
    }
   catch (error) {
     console.log(`Ha ocurrido un error: ${response.ok}`);
    }
  }
}

const message = () => {
  const welcomeMessage = "Hola Bienvenido(a)";

  alert(welcomeMessage);
  console.log(welcomeMessage);
}

const seeEmoji = () => {
  document.getElementById('emojiHappy').style.display = "block";
}

sendRequests();
message();
