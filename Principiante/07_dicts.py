# Diccionarios

# Los diccionarios son una estructura que sirve para almacenar datos clave-valor
my_dict = dict()
my_other_dict = {}  # Un dict se puede definir de estas dos maneras

print(type(my_dict))  # Tipo 'dict'
print(type(my_other_dict))  # Tipo 'dict'

my_other_dict = {  # Defininimos una clave y le asociamos un valor
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35
}
print(my_other_dict)
print(type(my_other_dict))

my_dict = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.77
}
print(my_dict)

print(len(my_other_dict))  # 3 elementos
print(len(my_dict))  # 5 elementos (el set que hay dentro no cuenta)

print(my_dict["Nombre"])  # Nos retorna el valor asociado a la clave "Nombre"

my_dict["Nombre"] = "Pedro"  # Actualizamos el valor de la clave
print(my_dict["Nombre"])

my_dict["Calle"] = "Calle Alozaina"  # Añadimos una nueva clave ya que esta no existe
print(my_dict)


# Funciones

del my_dict["Calle"]  # usamos el del para acceder y eliminar uno de los elementos
print(my_dict)

print("Apellido" in my_dict)  # Buscar por clave si algo está en un diccionario (no por valor)
print(my_dict["Apellido"])  # Buscar el valor de una clave

print(my_dict.items())  # Imprime las claves con sus valores
print(my_dict.keys())  # Imprime las claves
print(my_dict.values())  # Imprime los valores de las claves

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))  # fromkeys crea un diccionario con claves pero sin valores
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict)  # se ha quedado únicamente con las claves de my_dict
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, "Brais")  # le hemos metido "Brais" a todas las claves
print(my_new_dict)



