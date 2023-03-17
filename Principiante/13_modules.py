# Módulos

# Importar el módulo entero
import my_module

# hay que poner el nombre del módulo delante
my_module.sumValue(5, 3, 1)
my_module.printValue("Hola Python!")


# Importar un elemento en concreto del módulo
from my_module import sumValue, printValue

# solo hay que poner  el nombre del elemento
sumValue(5, 3, 1)
printValue("Hola Python")


# Módulos del sistema

import math  # Este módulo contiene elementos que nos ayudan a hacer operaciones matemáticas

print(math.pi)  # Valor del número pi

print(math.pow(2, 8))  # pow = Una potencia (2^8)


from math import pi as pi_value  # as para darle el nombre que yo quiera
print(pi_value)



