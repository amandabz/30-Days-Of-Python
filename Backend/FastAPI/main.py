from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from Backend.FastAPI.routers import products, users, users_db,  basic_auth_users, jwt_auth_users

app = FastAPI()

# Routers: importar mis otras API's
app.include_router(products.router)
app.include_router(users.router)
app.include_router(users_db.router)

app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)

# Recursos estáticos
app.mount("/static", StaticFiles(directory="Backend/FastAPI/static"), name="static")
# mount: Para poder acceder a la carpeta static y ver la imágen (url: http://127.0.0.1:8000/static/images/image.jpg)

# pip install uvicorn
# Inicia el server: python -m uvicorn Backend.FastAPI.main:app --reload

"""
Documentación de nuestra API (2 alternativas):
    - Con Swagger: http://127.0.0.1:8000/docs
    - Con Redocly: http://127.0.0.1:8000/redoc
"""

"""
En la terminal: (para levantar un servidor local)
    - python -m uvicorn main:app --reload
          (main es el nombre del fichero)
          (app es el nombre de la variable)
    - CTRL + C: detener el servidor
"""


@app.get("/")  # .get: pedir una petición a una página web
async def root():  # async: para que esta función funcione en cuanto pueda
    return "¡Hola FastAPI!"


# Url local: http://127.0.0.1:8000
# Mirar en Postman


@app.get("/url")
async def url():
    return {"url": "https://mouredev.com/python"}  # json


# Url local: http://127.0.0.1:8000/url
# Mirar en Postman
