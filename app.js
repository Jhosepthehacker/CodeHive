const sendRequests = () => {
  async function getData() {
    const API_URL = "https://codehive-hkut.onrender.com/welcome";

    try {
      const response = await fetch(API_URL, {
        method: 'GET'
      });
      
      if (!response.ok) {
        throw new Error("Ha ocurrido un error");
      }

      const json = await response.json();
      const message = json.message;
    }
   catch (error) {
     console.log("Ha ocurrido un error: " + error);
    }
  }
  getData();

  async function sendDataOfUsers() {
    const API_URL = "https://codehivedev.netlify.app/endpoint_example";
    const input1 = document.getElementById('userName');
    const input2 = document.getElementById('password');
    
    const userName, password = input1.value, input2.value;

    try {
      const response = await fetch(API_URL, {
        method: 'POST',
        headers: {"Content-Type": "application-json"},
        body: JSON.stringify({
                   userName: userName,
                   password: password
                             })
      });

      if (!response.ok) {
        throw new Error("Ha ocurrido un error");
      }

      const json = await response.json();
      const message = json.message;
    }
    catch (error) {
      console.log("Ha ocurrido un error: " + error);
    }
  }
}

const seeEmoji = () => {
  document.getElementById('emojiHappy').style.display = "block";
}

sendRequests();
message();
