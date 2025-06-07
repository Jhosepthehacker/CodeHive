import random as r
import time as t
import sys

def juego():   # Se declara la función juego
    name = input("¡Hola usuario!, ¿Cómo te llamas?: ")  # Entrada de datos "input"
    print("")    # Salto de línea 
    pregunta = input(f"{name}, ¿Quiéres jugar?: ") # Entrada de datos "input" si el usuario quiere jugar o no
    if pregunta.lower() == "si" or pregunta.lower() == "sí": # Comprobando la respuesta del usuario
        options_game = ["######################################",
                        "#                                     ",
                        "# adivinanzas | adventura, | combate  ",  # Opciones de juego
                        "#                                     ",
                        "######################################",
                       ]
        for i in options_game:  # Iterando la lista "options_game"
            print(i)  # Imprimiendo el valor de la variable "i" que almacenó la iteración de la lista "options_game"
            print("")  # Salto de línea
        type_game = input(f"{name}, ¿Qué tipo de juego prefieres?: ")
        if type_game.lower() == "adivinanzas" or type_game.lower() == "adivinar":
            numero = r.randint(1, 100)
            intentos = 0
            while True:
                try:
                    entrada = int(input("Adivina un número del 1 al 100"))
                except ValueError:
                    print("¡Respuesta Inválida!")
                if entrada > numero:
                    print("Demasiado alto")
                elif entrada < numero:
                    print("Demasiado bajo")
                elif entrada == numero:
                    print(f"Felicidades has encontrado el número {numero} en {intentos} intentos")
                    break
        elif pregunta.lower() == "no":
            print("Operación cancelada")
            sys.exit()

# Iniciar el juego llamando la función "juego"

if __name__ == '__main__':
    juego()
