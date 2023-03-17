# Manejo de Ficheros

import os

# .txt file
txt_file = open("my_file.txt", "w+")  # Leer, escribir y sobreescribir
# (r: modo lectura, w: modo escritura, r+: modo lectura y escritura)

# print(txt_file.read())  # Lee el contenido del fichero
print(txt_file.read(10))  # Solo lee los 10 primeros carácteres

print(txt_file.readline())  # Lectura línea a línea
print(txt_file.readline())  # Siguiente línea

for line in txt_file.readlines():  # Printear línea a línea
    print(line)

txt_file.write("\nAunque tambien me gusta Kotlin")  # Escribir algo en el fichero
print(txt_file.readline())

with open("my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Swift")

# os.remove("my_file.txt")  # Eliminar el fichero

