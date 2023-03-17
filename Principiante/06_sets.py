# Sets

# En un set los datos se guardan en una posición aleatoria
# Un set se utiliza cuando no queramos que se repitan datos y nos da igual que se guarden aleatoriamente
my_set = set()
my_other_set = {}  # Se puede definir un set de estas dos maneras

print(type(my_set))  # Tipo 'set'
print(type(my_other_set))  # Inicialmente es un: Tipo 'dict' (diccionario)

my_other_set = {"Brais", "Moure", 35}  # Una vez metemos datos, es un: Tipo 'set'
print(type(my_other_set))

print(len(my_other_set))  # Nos da 3 porque tiene 3 elementos

my_other_set.add("MoureDev")  # add para añadir elementos
print(my_other_set)
my_other_set.add("MoureDev")  # Un set no admite elementos repetidos, por ello no se añade este "MoureDev"
print(my_other_set)

print("Moure" in my_other_set)  # Sintaxis para comprobar si un elemento existe dentro de un set
print("Mouri" in my_other_set)

my_other_set.remove("Moure")  # remove para eliminar elementos
print(my_other_set)

my_other_set.clear()  # clear para eliminar los elementos dentro del set
print(len(my_other_set))  # 0 elementos

del my_other_set  # del para eliminar el set

my_set = {"Brais", "Moure", 35}
my_list = list(my_set)
print(my_list[0])  # Podemos transformar un set a una lista y así tener los elementos ordenados para poder accerder a una posición

my_other_set = {"Kotlin", "Swift", "Python"}
my_new_set = my_set.union(my_other_set)  # Para unir sets (como con +)
print(my_new_set)

print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))  # Prueba

print(my_new_set.difference(my_set))  # difference: para que retorne los elementos diferentes entre los dos sets

print(my_new_set.intersection(my_set))  # intersection: returns a set of items which are in both the sets







