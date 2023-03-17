# Operadores Aritméticos

print(3 + 4)  # Ha sumado
print(3 - 2)  # Ha restado
print(3 * 4)  # Ha multiplicado
print(type(3 / 4))  # Ha dividido y nos ha dado el tipo de dato (tipo: 'float')

print(10 % 2)  # Establecemos una división y nos da el resto de la división
print(10 // 3)  # Hace una división y aproxima el resultado a un nº entero
print(2 ** 3)  # Calcula 2^3

print("Hola " + "Python " + "¿Qué tal?")  # Ha juntado dos cadenas de texto (Result: 'Hola Python ¿Qué tal?')

print("Hola" + str(5))  # Podemos convertir el 5 en str para mezclar diferentes tipos de datos
print("Hola " * 5)  # Se multiplica el "Hola" x 5

my_float = 2 * 2.5
print("Hola" * int(my_float))


# Operadores Comparativos

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)  # = = (junto) Significa igual (3 es igual que 4)
print(3 != 4)  # ! = (junto) Significa distinto (3 es distinto que 4)

print("A" == "a")  # No es lo mismo

print("Hola" >= "Zola")  # También se puede hacer con datos tipo str comprobando una Ordenación Alfabética
print(len("Hola") >= len("Zola"))  # Contando caracteres


# Operadores Lógicos
# and
# or
# not

print(3 > 4 and "Hola" > "Python")  # False * False = False
print(3 > 4 or "Hola" > "Python")  # False * True = False
print(3 < 4 or "Hola" < "Python")  # True * True = True
print(3 < 4 or ("Hola" > "Python" and 4 == 4))  # Se haría primera la operación que está entre paréntesis

print(not(3 > 4))  # El not es para negar la condición