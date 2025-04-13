#python 3.12

# No les voy a mentir este archivo solamente de python está copiado por la IA hasta que lo aprenda yo misml

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola, mundo!"

if __name__ == "__main__":
    app.run(debug=True)

    print ("Hola Mundo")
