# Fichero encargado de gestionar la conexión con la base de datos (MongoDB)
# Instalación de MongoDB: https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/

# pip install pymongo
from pymongo.mongo_client import MongoClient

"""
- Conexión con la base de datos LOCAL:
    - Si no ponemos nada entre paréntesis, se conecta a la base de datos por defecto (localhost:27017)
    - .local: para que no sea necesario ponerlo en cada consulta
--> db_client = MongoClient("mongodb://localhost:27017").local

En el CMD: "C:\Program Files\MongoDB\Server\6.0\bin\mongod.exe" --dbpath="c:\data\db"
"""

# Conexión con la base de datos REMOTA
# Url de conexión: cuando creemos la base de datos en MongoDB Atlas
uri = "mongodb+srv://amandabz:27OaKwNfJYKwm4Ef@firstatlas.iooi7vf.mongodb.net/?retryWrites=true&w=majority"
db_client = MongoClient(uri).firstatlas  # (firstatlas: nombre de la base de datos)
