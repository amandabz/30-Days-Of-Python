# Exception Handling

# Errores que si no arreglamos nuestro programa se muere

numberOne = 5
numberTwo = "1"

# try except
# si hay un try tiene que haber un except
try:
    print(numberOne + numberTwo)  # Si esto falla salta el except
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

numberOne = 5
numberTwo = 1

try:
    print(numberOne + numberTwo)  # Como no falla, salta el try
    print("No se ha producido un error")
except:
    print("Se ha producido un error")

# try except else

numberOne = 5
numberTwo = 1

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")

# try except else finally

numberOne = 5
numberTwo = "1"

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:  # Opcional
    # Se ejecuta si no se produce una excepción
    print("La ejecución continúa correctamente")  # Como se ha producido un error, no se ejecuta el else
finally:  # Opcional
    # Se ejecuta siempre, haya error o no
    print("La ejecución continúa")

numberOne = 5
numberTwo = "1"

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    print("La ejecución continúa correctamente")
finally:
    print("La ejecución continúa")


# Excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except ValueError:  # este except solo se ejecuta si se produce un ValueError
    print("Se ha producido un ValueError")
except TypeError:  # este except solo se ejecuta si se produce un TypeError
    print("Se ha producido un TypeError")


# Captura de la información de la excepción

numberOne = 5
numberTwo = "1"

try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError as error:  # Nos va a dar más información sobre que es lo que ha producido el error
    print(error)


try:
    print(numberOne + numberTwo)
    print("No se ha producido un error")
except TypeError as error:
    print(error)
except Exception as exception_error:  # Exception para sea cual sea el error
    print(exception_error)

