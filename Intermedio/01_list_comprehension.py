# List Comprehension
# Crear listas de forma "comprimida"
# De forma rápida o en base de listas que ya tenemos


my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_range = range(8)
print(list(my_range))  # Crear una lista con un rango

my_list = [i + 1 for i in range(21)]  # el i significa que pasa por cada uno de los elementos y le suma 1
print(my_list)

my_list = [i * 2 for i in range(21)]  # pasa por cada uno de los elementos y le suma el doble
print(my_list)

my_list = [i * i for i in range(21)]  # pasa por cada uno de los elementos y se multiplica por sí mismo
print(my_list)


def sum_five(number):
    return number + 5


my_list = [sum_five(i) for i in range(8)]
print(my_list)
