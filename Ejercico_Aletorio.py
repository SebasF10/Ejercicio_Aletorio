from random import*
from time import*

colores = ['rojo', 'azul', 'verde',]

print("vamos a pintar un pared tenemos los siguientes colores :")
print("---------------------------------------------------------")
print("Colores disponibles:", colores)
print("---------------------------------------------------------")
print("de los colores que hay , vamos a sacar uno aletorio para pintar un pared")
print("---------------------------------------------------------")

opcion = input("¿Quieres agregar un color a la lista dada? (si/no): ")

if opcion == "si":
    print("---------------------------------------------------------")
    nuevo_color = input("Introduce el nuevo color: ")
    colores.append(nuevo_color)
elif opcion == "no":
    print("la eleccion se dara con los colores ya establecidos anteriormente")
    print("---------------------------------------------------------")

color_seleccionado = choice(colores)
print("El color seleccionado es:", color_seleccionado)