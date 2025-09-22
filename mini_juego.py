import socket
import random as r
import time as t
import sys

class ConnectServer:
    def __init__(self):
        self.HOST = '127.0.0.1' # En desarrollo....
        self.PORT = 8080

        self.connect_server()
    
    def connect_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))

            while True:
                s.sendall("¡Hola, desde el cliente!".encode('utf-8'))

                self.data = s.recv(1024) # Búfer, 1024 bytes
                self.message = self.data.decode() # Mensaje decodificado

                print(f"Mensaje recibido: {self.mensaje}")

def juego():   # Se declara la función juego
    name = input("¡Hola usuario!, ¿Cómo te llamas?: ")  # Entrada de datos "input"
    print("")    # Salto de línea 
    pregunta = input(f"{name}, ¿Quiéres jugar?: ") # Entrada de datos "input" si el usuario quiere jugar o no
    if pregunta.lower() == "si" or pregunta.lower() == "sí" or pregunta.lower() == "si " or pregunta.lower() == "sí ": # Comprobando la respuesta del usuario
        options_game = ["######################################",
                        "#                                     ",
                        "# adivinanzas | adventura, | combate  ",  # Opciones de juego
                        "#                                     ",
                        "######################################",
                       ]
        for i in options_game:  # Iterando la lista "options_game"
            print(i)  # Imprimiendo el valor de la variable "i" que almacenó la iteración de la lista "options_game"
            print("")  # Salto de línea
        type_game = input(f"{name}, ¿Qué tipo de juego prefieres?: ")  # Entrada de datos
        if type_game.lower() == "adivinanzas" or type_game.lower() == "adivinar" or type_game.lower() == "adivinanzas ":
            numero = r.randint(1, 100)
            intentos = 0
            while True:
                try:
                    entrada = int(input("Adivina un número del 1 al 100"))
                except ValueError:
                    print("¡Respuesta Inválida!")
                    intentos += 1
                    print("")
                if entrada > numero:
                    print("Demasiado alto")
                elif entrada < numero:
                    print("Demasiado bajo")
                elif entrada == numero:
                    print(f"Felicidades has encontrado el número {numero} en {intentos} intentos")
                    break
        elif type_game.lower() == "combate" or type_game.lower() == "combate ":
            nombre = input("¿Cómo te llamas?: ")
            print("")
            preguntar = input("¿Quiéres jugar?: ")
            print("")
            if preguntar.lower() == "si" or preguntar.lower() == "sí" or preguntar.lower() == "sí " or preguntar.lower == "si ":
                print("Empezando juego")
                t.sleep(2)
                print("----------------")
                print("  Tu: 200 Live  ")
                print("----------------")
                print("")
                print("---------------------")
                print(" Oponente: 200 Live  ")
                print("---------------------")
    elif pregunta.lower() == "no":
        print("Operación cancelada")
            sys.exit()
    else:
        print("¡Respuesta Inválida!")

# Iniciar el juego llamando la función "juego"

if __name__ == '__main__':
    try:
        app = ConnectServer()
    except OSError:
        print("Hubo un error de conexión")
    juego()
# En desarrollo el programa....
