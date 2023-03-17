# Expresiones regulares

import re  # módulo para trabajar con expresiones regulares

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Lección llamada Manejo de ficheros"


# match: Comprobar si una cadena de texto está en mi variable, comenzando a contar desde el principio
# Nos da la posición

print(re.match("Esta es la lección", my_string))
# Está entre el carácter 0 y el 18

print(re.match("Esta es la lección", my_other_string))

print(re.match("Expresiones Regulares", my_string))
# Printea un None porque empieza a contar desde el principio de la cadena


match = re.match("Esta es la lección", my_string)
print(match)
start, end = match.span()
print(my_string[start:end])  # En caso de que exista, acceder a él


match = re.match("Esta no es la lección", my_other_string)
if not(match == None):  # if match != None:,  if match is not None: Otras formas de comprobar el None
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])


# search: Comprobar si una cadena de texto está en mi variable, comenzando a contar desde cualquier sitio
# Nos da la posición

search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start: end])


# findall: Nos encuentra la cadena de texto y nos la retorna en una lista
# No da la posición

findall = re.findall("lección", my_string, re.I)  # re.I: ignorar mayúsculas y/o minúsculas
print(findall)


# split: busca un patrón (en el caso de abajo :) y divide a partir de ahí

split = re.split(":", my_string)
print(split)


# sub: sustituye dos valores
# solo cambia el primer valor que encuentre

sub = re.sub("Expresiones Regulares", "RegEx", my_string)  # sustituye Expresiones regulares en mayúsculas por RegEx
print(sub)

sub_2 = re.sub("lección|Lección", "LECCIÓN", my_other_string)  # [l|L]ección: Otra forma de hacer que sustituya ambos
print(sub_2)


# Patterns
# Las Expresiones Regulares en Notion

my_test_pattern = r''  # Forma para escribir expresiones regulares en Python

pattern = r'[l|L]ección'
print(re.findall(pattern, my_string))

pattern = r'\d+'
print(re.findall(pattern, my_string))

pattern = r'^[E].*'  # Empezar por E y detrás puede tener cualquier cosa
print(re.findall(pattern, my_string))


# email validation regular expression

def is_valid_email():

    def_pattern = r'[a-zA-Z0-9_.+-]+@(gmail|hotmail)\.[a-zA-Z0-9-.]+$'
    entry = input("¿Cuál es tu correo?: ")

    if re.match(def_pattern, entry):
        print("Es correcto")
    else:
        print("No es correcto")

is_valid_email()


