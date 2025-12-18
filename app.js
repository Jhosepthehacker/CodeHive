const sendRequests = () => {
  async function getData() {
    const API_URL = "https://codehive-hkut.onrender.com/welcome";

    try {
      const response = await fetch(API_URL, {
        method: 'GET'
      });
      
      if (!response.ok) {
        throw new Error(`Ha ocurrido un error`);
      }

      const json = await response.json();
      const message = json.message;

      // alert("Response Of The Backend: " + message);
      console.log("Response Of The Backend: " + message);
    }
   catch (error) {
     console.log(`Ha ocurrido un error`);
    }
  }
  getData();
}

const seeEmoji = () => {
  document.getElementById('emojiHappy').style.display = "block";
}

sendRequests();
message();
