# Tipos de Errores


# SyntaxError
# print "Hola Mundo!"  # Error (descomentar para Error)
print("¡Hola Mundo!")  # Solucionado

# NameError
language = "Spanish"  # comentar para Error
print(language)  # Error (language no está definido)

# IndexError
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
# print(my_list[9])  # IndexError: no hay un elemento en la posición 9 en esta lista

# ModuleNotFoundError
# import maths  # Error: No existe este módulo (es math, no maths)
import math

# AttributeError
# print(math.PI)  # Error: no existe el atributo "PI" en este módulo (es pi, no PI)
print(math.pi)

# KeyError
my_dict = {"Nombre": "Brais", "Apellido": "Moure", "Edad": 35}
# print(my_dict["Apelido"])  # Error: no existe esta clave en el dict (es Apellido, no Apelido)

# TypeError
# print(my_list["Nombre"])  # Error: en la lista no puedes buscar un elemento con un tipo str

# ImportError
# from math import PI  # Error

# ValueError
# my_int = int("10 años")  # transformarlo a int
# Error: my_int es int y tiene "años" que es un str. No se pueden juntar

# ZeroDivisionError
# print(4/0)  # Error: no se puede dividir entre 0




