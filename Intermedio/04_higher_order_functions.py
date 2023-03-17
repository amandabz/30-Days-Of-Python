# Funciones de Orden Superior

def sum_one(value):
    return value + 1  # sum_one le suma 1 a sum_two_values_and_add_one


def sum_five(value):
    return value + 5  # sum_five le suma 5 a sum_two_values_and_add_one


def sum_two_values_and_add_value(first_value, second_value, f_sum):  # el f_sum se lo estamos pasando como una función
    return f_sum(first_value + second_value)  # Le llegan los valores, los suma y llama a sum_one

print(sum_two_values_and_add_value(5, 2, sum_one))
print(sum_two_values_and_add_value(5, 2, sum_five))


# Closures

def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(1)
print(add_closure(5))

print((sum_ten(5))(1))  # Es lo mismo que lo de arriba


# Funciones de Orden Superior (que ya existen en el propio lenguaje)

numbers = [2, 5, 30, 10, 21, 3]


    # Map
# map: con un listado iterable genera otro listado iterable en función de la función que le hemos pasado
def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))  # map ha iterado cada uno de los valores y ha ejecutado la función

print(list(map(lambda number: number * 2, numbers)))  # usando una lambda


    # Filter
# filter: recorre todos los valores y ejecuta una función que retorna True o False para saber como filtrar los valores del iterado
def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False  # Lo mismo que poner un else:

print(list(filter(filter_greater_than_ten, numbers)))  # lo hace con la función
print(list(filter(lambda number: number > 10, numbers)))  # lo hace sin la función


    # Reduce
# reduce: opera entre los valores que va recorriendo y va operando con los valores que va teniendo a medida que avanza
from functools import reduce  # hay que importarlo

def sum_two_values(first_value, second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value

# reduce opera con un valor más el acumulado
print(reduce(sum_two_values, numbers))


