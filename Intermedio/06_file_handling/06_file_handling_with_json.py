# .json file

import json

json_file = open("my_file.json", "w+")  # Crea el fichero si no existe y/o lo sobreescribe

json_test = {
    "name": "Brais",
    "surname": "Moure",
    "age": 35,
    "languages": ["Python", "JavaS cript", "Swift", "Kotlin"],
    "website": "https://moure.dev"
}

json.dump(json_test, json_file, indent=2)  # Sobreescribe el fichero .json con el diccionario de json_test
# indent: lo escribe en diferentes líneas, el nº que pongamos son los espacios de delante


for line in json_file.readlines():
    print(line)

json_file.close()

with open("my_file.json") as my_json_file:
    for line in my_json_file.readlines():  # Accedemos al json y leemos línea a línea
        print(line)

json_dict = json.load(open("my_file.json"))
print(json_dict)
print(type(json_dict))  # tipo 'dict'
print(json_dict["name"])  # accedemos al valor de la clave 'name'


# .csv file

import csv

csv_file = open("csv_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "languages", "website"])
csv_writer.writerow(["Brais", "Moure", 35, "Python", "https://moure.dev"])
csv_writer.writerow(["Amanda", "Benitez", 18, "JavaScript", "https://amanda.dev"])

with open("csv_file.csv") as my_csv_file:
    for line in csv_file.readlines():  # Accedemos al csv y leemos línea a línea
        print(line)

csv_file.close()