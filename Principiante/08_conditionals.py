# Condicionales

my_condition = False

if my_condition:  # Es lo mismo que if my_condition == True:
    print("Se ejecuta la condición del if")  # No se ejecuta porque my_condition es falsa


my_condition = 5 * 2

if my_condition == 11:
    print("Se ejecuta la condición del segundo if")  # No se ejecuta porque my_condition = 5 * 2 == 11 es False


if my_condition >= 10:
    print("Se ejecuta la condición del tercer if")  # Se ejecuta porque my_condition = 5 * 2 >= 10


if my_condition > 10:
    print("Es mayor que 10")
else:
    print("Es menor o igual que 10")  # Si no se cumple el if, ejecuta el else


if my_condition == 10 and my_condition < 20:  # Se pueden meter operadores lógicos
    print("Es igual a 10 y menor que 20")  # Se tienen que cumplir estas dos condiciones para que se imprima
else:
    print("Es menor o igual que 10")


my_condition = 5 * 5

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:  # Comprobación extra
    print("Es igual a 25")
else:
    print("Es menor o igual que 10, mayor o igual que 20 o distinto de 25")


my_string = ""

if not my_string:
    print("Mi cadena de texto es vacía")

