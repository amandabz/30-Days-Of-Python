# Clases

# Una clase nos sirve para especificar que todo lo que esté dentro de esa clase tiene que responder a una cierta lógica
# Las clases van con la 1º letra de cada palabra en mayúscula y todo juntos

class MyEmptyPerson:  # class <nombre_clase>: para definir una clase.
    pass  # pass es para un clase vacía


print(MyEmptyPerson)
print(MyEmptyPerson())


class Person:
    def __init__(self, name, surname):  # __init__(self) Es obligatorio siempre
        self.name = name  # Estas son las propiedades que creamos
        self.surname = surname


my_person = Person("Brais", "Moure")
print(my_person.name)
print(f"{my_person.name} {my_person.surname}")


class MyOtherPerson:
    def __init__(self, name, surname):
        self.full_name = f"{name} {surname}"  # Junta el name y el surname y los mete en una propiedad llamada full_name

    def walk(self):  # Podemos meter funciones dentro de clases
        print(f"{self.full_name} está caminando")


my_other_person = MyOtherPerson("Brais", "Moure")
print(my_other_person.full_name)

my_other_person.walk()


class MyOtherPerson:
    def __init__(self, name, surname, alias="(Sin alias"):  # Podemos ponerle también valores por defecto
        self.full_name = f"{name} {surname} ({alias})"

    def walk(self):
        print(f"{self.full_name} está caminando")


my_other_person = MyOtherPerson("Brais", "Moure", "MoureDev")
print(my_other_person.full_name)

my_other_person.walk()
my_other_person.full_name = "Amanda Benítez (La loca de los perros)"  # Brais Moure pasa a llamarse Amanda Benítez etc.
print(my_other_person.full_name)

