# Functions

def my_function():
    print("Esto es una función")


my_function()  # Con esto llamaré a mi función


# Una función puede recibir y devolver código
# Recibir parámetros

def sum_two_values(first_value, second_value):  # Valores que necesito darle para hacer algo dentro la función
    print(first_value + second_value)


sum_two_values(5, 7)  # first_number = 5, second_number = 7
sum_two_values(6, 3)  # first_number = 6, second_number = 3
sum_two_values(456, 129)  # first_number = 456, second_number = 129


# Devolver parámetros

def sum_two_values_with_return(first_value, second_value):
    return first_value + second_value  # return


my_result = sum_two_values_with_return(10, 5)  # El resultado de la función lo tienes que asignar a una variable
print(my_result)


def print_name(name, surname):
    print(f"{name} {surname}")


print_name(surname="Moure", name="Brais")  # Si quitamos un parámetro nos da error


def print_name_with_default(name, surname, alias="Sin alias"):  # para asignarle un valor por defecto a alias
    print(f"{name} {surname} {alias}")


print_name_with_default("Amanda", "Benítez", "Abenhid")
print_name_with_default("Brais", "Moure")


def print_texts(*text):  # * para indicarle que puedo pasarle la cantidad de valores que quiera
    print(text)


print_texts("Hola", "Python", "MoureDev")


def print_texts(*texts):
    for text in texts:  # Imprime en una línea "Hola", en otra "Python" y en otra "MoureDev"
        print(text.upper())  # upper para convertir los carácteres en mayúsculas


print_texts("Hola", "Python", "MoureDev")


# Ejemplo de GitHub 1

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age


print("Age:", calculate_age(2023, 2004))


# Ejemplo de GitHub 2

def sum(a, b):
    return (a + b)

a = int(input("Primer valor:"))
b = int(input(("Segundo valor:")))

try:
    print(f"La suma de {a} más {b} es: {sum(a, b)}")
    print("Funciona la suma")
except TypeError as e:
    print("No funciona la suma")