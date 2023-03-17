# Strings

my_string = "Mi string"
my_other_string = 'Mi otro string'  # Se puede poner con comillas dobles (") o comillas simples (')

print(len(my_string))
print(len(my_other_string))  # Len para calcular los carácteres contando los espacios

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un String\ncon salto de línea"  # \n para hacer un salto de línea
print(my_new_line_string)

my_tab_string = "\tEste es un String con tabulación"  # \t para hacer tabulación (esta variable deja un espacio al principio)
print(my_tab_string)

my_scape_string = "\tEste es un String \n espacado"
print(my_scape_string)


# Formateo de strings

name, surname, age = "Brais", "Moure", 35

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))
print("Mi nombre es %s %s y mi edad es %d" %(surname, name, age))  # %s -> string | %d -> nº enteros
                                 # Puedes cambiar el orden de las variables

print("Mi nombre es " + name + " " + surname + "y mi edad es" + " " + str(age))  # Esta manera de hacerlo es la menos óptima

print(f'Mi nombre es {name} {surname} y mi edad es {age}')  # Esta es la MEJOR MANERA de hacerlo


# Desempaquetado de carácteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(e)


# División

# Se empieza a contar las letras desde el nº 0, es decir la 1º letra es el nº 0
language_slice = language[1:3]  # Nos ha cogido de la 1 a la 3 las letras, sin coger la 3
print(language_slice)

language_slice = language[1:]  # Nos ha cogido de la 1 a la última letra
print(language_slice)

language_slice = language[-2]  # Nos ha cogido la 2º empezando por el final
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)


# Reverse

reverse_language = language[::-1]  # Nos imprime la palabra al revés
print(reverse_language)


# Funciones (las más típicas)

print(language.capitalize())  # capitalize pone la primera letra en mayúscula
print(language.upper())  # upper pone todo en mayúscula
print(language.lower())  # lower pone todo en minúsculas
print(language.count("t"))  # count cuenta el nº de letras o palabras que haya de lo que hemos puesto entre ""
print(language.isnumeric())  # isnumeric para comprobar si es un número
print("1".isnumeric())
print(language.lower().isupper())  # isupper para comprobar si está en mayúscula
print(language.startswith("Py"))  # startswith para comprobar por qué letras empieza (key-sensive con mayus. y minus.)

print("Py" == "py")  # No es lo mismo