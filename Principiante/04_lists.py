# Listas

# Una lista es una caja en el que almacenamos un conjunto de datos, cada uno en una posición, empezando por el nº 0
my_list = list()
my_other_list = []  # Se puede definir una lista de estas dos maneras

my_list = [35, 24, 62, 52, 30, 30, 17]  # Podemos guardar el mismo valor + de 2 veces en una misma lista
print(my_list)
print(len(my_list))  # Nos da 7 porque tenemos 7 datos dentro de la lista

my_other_list = [35, 1.77, "Brais", "Moure"]
print(my_other_list)
age, height, name, surname = my_other_list
print(name)

print(type(my_other_list))  # Tipo 'list'
print(type(my_list))  # Tipo 'list'

print(my_other_list[0])  # Para acceder al primer dato de la lista
print(my_other_list[-1])  # Para acceder al último dato de la lista
print(my_other_list[-2])  # Para acceder al penúltimo dato de la lista

print(my_other_list + my_other_list)  # Se pueden sumar dos o más listas


# Funciones

print(my_other_list.count("Brais"))  # Ver cuantas veces se repite un dato en una lista (hay que poner el dato completo)
print(my_list.count(30))

my_other_list.append("MoureDev")  # append para añadir elementos
print(my_other_list)

my_other_list.insert(1, "Blue")  # insert para añadir elementos en la posición que queramos (posición 1)
print(my_other_list)

my_other_list[1] = "Red"  # sobreescribir el elemento de esa posición (posición 1)
print(my_other_list)

my_other_list.remove(1.77)  # remove para eliminar elementos que nosotros conocemos que existen
print(my_other_list)

my_list.remove(30)  # solo elimina un 30
print(my_list)

del my_list[2]  # así se eliminan elementos por índice
print(my_list)

my_list.pop()  # pop elimina el último elemento de la lista
print(my_list)

print(my_list.pop(2))  # pop así elimina un elemento de la lista retornándonos ese elemento

my_new_list = my_list.copy()  # copy para copiar la lista
my_list.clear()  # clear para eliminar la lista entera
print(my_list)
print(my_new_list)

my_new_list.reverse()  # reverse para que nos de los elementos de una lista al revés
print(my_new_list)

my_new_list.sort()  # sort para ordenar la lista
print(my_new_list)

print(my_new_list[1:3])  # me da los elementos que estén entre el 1 y el 3 sin contar el 3

