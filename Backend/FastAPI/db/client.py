# Fichero encargado de gestionar la conexión con la base de datos (MongoDB)

# pip install pymongo
from pymongo import MongoClient


# Conexión con la base de datos
db_client = MongoClient("mongodb://localhost:27017")

# Si no ponemos nada entre paréntesis, se conecta a la base de datos por defecto (localhost:27017)

# En el CMD:
# "C:\Program Files\MongoDB\Server\6.0\bin\mongod.exe" --dbpath="c:\data\db"
