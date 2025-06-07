import random as r
import time as t

def juego():
    name = input("¡Hola usuario!, ¿Cómo te llamas?: ")
    print("")
    pregunta = input(f"{name}, ¿Quiéres jugar?: ")
    if pregunta.lower() == "si" or pregunta.lower() == "sí":
        options_game = ["######################################",
                        "#                                     ",
                        "# adivinanzas | adventura, | combate  ",
                        "#                                     ",
                        "######################################",
                       ]
        for i in options_game:
            print(i)
            print("")
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
