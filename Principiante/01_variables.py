# Variables

# Las variables se escriben en minúsculas y con _ entre las palabras
my_string_variable = 'My String Variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Cadenas de texto
print(my_string_variable, str(my_int_variable), my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Funciones del sistema
print(len(my_string_variable))  # len: Cuenta los caracteres (contando los espacios)

""""
# input: Nos pide introducir datos en la consola
first_name = input("¿Cuál es tu nombre?: ") 
age = input("¿Cuántos años tienes?: ")
print(first_name)
print(age)
"""

# Variables en una sola línea. ¡No abusar de esta sintaxis!
name, surname, alias, edad = "Brais", "Moure", "MoureDev", 35
print("Me llamo:", name, surname, ". Mi edad es:", edad, ". Y mi alias es:", alias)

# ¿Forzamos el tipo? No
address: str = "Mi dirección"
address = 32
print(type(address))
