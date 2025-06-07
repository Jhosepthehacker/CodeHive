#!/bin/bash
echo "Hola Usuario ¿Cómo te llamas?"
echo ""
read -p "Tu Nombre: " name
printf ""
echo -e "Hola \e[33m$name\e[0m ¿Cómo estás?"
printf ""
read -p "¿Cómo Estás?: " respuesta
echo ""
if [[ "$respuesta" == "bien" ]]; then
    echo "¡Que bueno que estás bien! :)"
elif [[ "$respuesta" == "bien y tu" ]]; then
    echo "¡Que bueno que estás bien! :)"
elif [[ "$respuesta" == "bien y tú" ]]; then
    echo "¡Que bueno que estás bien! :)"
elif [[ "$respuesta" == "mal" ]]; then
    echo "Lo siento entiendo que te puedas sentir mal :("
else
     echo "No es una respuesta válida"
fi
echo ""
echo -e "Contáctame ^_^\e[32m josemanuelramirezrengifo9@gmail.com"
echo ""
echo -e "\e[34m Visita mi página web: https://jhosepthehacker.github.io/CodeHive"
