# Fichero encargado de gestionar la conexión con la base de datos (MongoDB)
# Instalación de MongoDB: https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/
# En el CMD: "C:\Program Files\MongoDB\Server\6.0\bin\mongod.exe" --dbpath="c:\data\db"

# pip install pymongo
from pymongo import MongoClient

"""
- Conexión con la base de datos LOCAL:
    - Si no ponemos nada entre paréntesis, se conecta a la base de datos por defecto (localhost:27017)
    - .local: para que no sea necesario ponerlo en cada consulta
--> db_client = MongoClient("mongodb://localhost:27017").local
"""

# Conexión con la base de datos REMOTA
# Url de conexión: cuando creemos la base de datos en MongoDB Atlas
uri = "mongodb+srv://amandabz:27OaKwNfJYKwm4Ef@firstatlas.iooi7vf.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri).amandabz

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)






