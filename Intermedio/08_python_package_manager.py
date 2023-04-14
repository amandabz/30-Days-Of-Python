# Manejo de Paquetes
# PIP: https://pypi.org

# Comandos en la terminal de Python
# pip list: (lista de las librerías que tenemos intaladas)
# pip uninstall <libreria que queramos desinstalar>
# pip show <libreria> (ver información sobre una libreria)
# pip --version

# pip install numpy
import numpy  # pip install numpy
print(numpy.version.version)  # ver versión de numpy


numpy_array = numpy.array([7, 5, 2, 35])  # crea un array = lista
print(numpy_array * 2)
print(type(numpy_array))


# pip install pandas
import pandas   # pip install pandas

panda_array = pandas.array([4, 5, 6])
print(panda_array)
print(type(panda_array))


# pip install requests
import requests  # para pedir peticiones a una APIs

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.json())  # me trae el json
print(response.status_code)


# Package Arithmetics (in mypackage)

from mypackage import arithmetics  # hay que hacerlo con from

print(arithmetics.sum_two_values(1, 4))
