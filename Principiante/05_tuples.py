# Tuplas

# Una tupla es una caja en la que metemos un conjunto de datos que no se pueden cambiar
my_tuple = tuple()
my_other_tuple = ()  # Se puede definir una tupla de estas dos maneras

my_tuple = (35, 1.77, "Brais", "Moure")
print(my_tuple)
print(type(my_tuple))  # Tipo 'tuple'

my_other_tuple = (60, 30, 35)

print(my_tuple[0])  # Para acceder al primer dato de la tupla
print(my_tuple[-1])  # Para acceder al último dato de la tupla
print(my_tuple[-2])  # Para acceder al penúltimo dato de la tupla


# Funciones

print(my_tuple.count("Brais"))  # Ver cuantas veces se repite un dato en una lista (hay que poner el dato completo)
print(my_tuple.index("Moure"))  # Ver en que posición está la palabra que hayamos puesto entre ""

# my_tuple[1] = 1.80  (No nos deja cambiarlo porque es una tupla y los datos son constantes)
# print(my_tuple)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)
print(my_sum_tuple[3:6])  # Entre el 3 y el 6 sin tener en cuenta el 6

my_tuple = list(my_tuple)  # Así convertimos una tupla a una lista
print(type(my_tuple))

my_tuple[3] = "MoureDev"
my_tuple.insert(1, "Azul")
print(tuple(my_tuple))