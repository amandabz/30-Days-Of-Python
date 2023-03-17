# Loops (Bucles/Ciclos)

# Un bucle nos sirve para pasar por el mismo código varias veces

# While

my_condition = 0

while my_condition < 10:  # Imprime my_condition infinitas veces
    print(my_condition)
    my_condition += 2  # Incrementa 2 cada vez que imprima my_condition hasta que el while no se cumpla
else:  # Es opcional
    print("Mi condición es mayor o igual que 10")  # Cuando deja de cumplirse el while se ejecuta el else


while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condición es 15")
        print("Se detiene la ejecución")
        break  # break para detener la ejecución (cuando llegue a 15 en este caso)
    print(my_condition)

print("La ejecución continúa")


# For
# Un for se utiliza para estructuras que pueden almacenar más de un valor
# Un for sirve para iterar un listado de elementos

my_list = [35, 24, 62, 52, 30, 30, 17]

for ages in my_list:  # Se va a ejecutar tantas veces como elementos tenga
    print(ages)

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
for element in my_tuple:
    print(element)

my_set = {"Brais", "Moure", 35}
for element in my_set:
    print(element)

my_dict = {
    "Nombre": "Brais",
    "Apellido": "Moure",
    "Edad": 35,
    1: "Python"
}
for element in my_dict:  # Imprime las claves
    print(element)

for element in list(my_dict.values()):  # Para imprimir los valores
    print(element)


for element in my_dict:
    print(element)
    if element == "Edad":
        break  # Cuando lleguemos a una clave "Edad" se detiene el For
    print("Se ejecuta")  # "Se ejecuta hasta que llega a "Edad"
else:  # Cuando hacemos un break este else ya no se ejecuta
    print("El bucle for para dict ha finalizado")  # Cuando acaba el For se imprime el print

print("La ejecución continúa")


for element in my_dict:
    print(element)
    if element == "Edad":
        continue  # No es algo muy aconsejado
    print("Se ejecuta")  # "Se ejecuta menos en "Edad"
else:
    print("El bucle for para dict ha finalizado")


