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
        type_game = input(f"{name},¿Qué tipo de juego prefieres?: ")
