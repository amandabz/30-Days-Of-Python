from fastapi import APIRouter, HTTPException
from pydantic import BaseModel  # El BaseModel nos da la capacidad de crear una entidad

router = APIRouter(tags=["users"], responses={404: {"message": "No encontrado"}})

# Inicia el server: python -m uvicorn users:app --reload


# Creamos una clase para crear un modelo de usuario


class User(BaseModel):  # El BaseModel nos da la capacidad de crear una entidad
    id: int
    name: str  # ponemos el str para ayudar al IDE, pero no es obligatorio
    surname: str
    url: str
    age: int


users_list = [
    User(id=1, name="Brais", surname="Moure", url="https://moure.dev", age=35),
    User(id=2, name="Amanda", surname="Benitez", url="https://amanda.dev", age=24),
    User(id=3, name="Alex", surname="Gutierrez", url="https://alex.dev", age=19),
]


# Get: obtener información de la lista de usuarios.
@router.get("/users")
async def user_list():
    return users_list


# Path (se utiliza cuando un parámetro es fijo). Ejemplo: /user/1
# Get usuario según su ID:


@router.get("/user/{id}")
async def get_user(id: int):
    for user in users_list:
        if user.id == id:
            return user

    raise HTTPException(status_code=404, detail="El usuario no existe")


# Url local: http://127.0.0.1:8000/user/1 (Get)

"""
Otra forma de hacerlo:

@app.get("/user/{id}")  # Para devolvernos el user según su ID
async def get_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    return list(users)

"""


# Query (se utiliza cuando un parámetro es variable). Ejemplo: /user/?id=1


@router.get("/user/")
async def get_user(id: int) -> User | dict:
    return search_user(id)


def search_user(id: int) -> User | dict:
    for user in users_list:
        if user.id == id:
            return user

    raise HTTPException(status_code=404, detail="El usuario no existe")


# Url local: http://127.0.0.1:8000/user/?id=1 (1 se cambia por las diferentes IDs) (Get)


# Post
# Añadir un nuevo usuario.
@router.post("/user/", response_model=User, status_code=201)
# status_code=201: para que nos devuelva el código 201 (Created) en vez del 200
# response model: para que en nuestra documentación aparezca lo que nos tiene que devolver
async def new_user(user: User) -> dict | User:  # Class User
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
        # el detail lo devuelve cuando hay un código de error, con un 204 no te lo devolvería

    users_list.append(user)
    return user


# Url local: http://127.0.0.1:8000/user/ (Post)
# Meter en Postman para añadir un nuevo usuario:
# {"id": 4, "name": "CarLa", "surname": "Benavente", "url": "https://carla.dev", "age": 23}


# Patch: actualizar una parte concreta de usuario (no está en el curso)
# Put: actualizar usuario completo


@router.put("/user/")
async def put_user(user: User) -> dict | User:
    """
    Actualiza un usuario.
    :param user: Usuario a actualizar.
    :return: Usuario actualizado o un diccionario con el error.
    """
    found_user = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found_user = True

    if not found_user:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    return user


users_dict = {
    1: User(id=1, name="Brais", surname="Moure", url="https://moure.dev", age=35),
    2: User(id=2, name="Amanda", surname="Benitez", url="https://amanda.dev", age=24),
    3: User(id=3, name="Alex", surname="Gutierrez", url="https://alex.dev", age=19),
}


@router.put("/user/")
async def put_user_eff(user: User) -> dict | User:
    if user.id in users_dict:
        users_dict[user.id] = user
        return user
    return {"Error": "No se ha actualizado el usuario"}


# Url local: http://127.0.0.1:8000/user/ (Put)
# Meter en Postman para actualizar un usuario:
# {"id": 4, "name": "CarLa", "surname": "Benavente", "url": "https://carla.dev", "age": 23}


# Delete: eliminar usuario.


@router.delete("/user/{id}")
async def delete_user(id: int):  # -> None | dict:
    """
    Elimina un usuario.
    :param id: id del usuario.
    :return: None o un diccionario con el error.
    """

    found_user = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]  # eliminar el usuario
            found_user = True

    if not found_user:
        raise HTTPException(status_code=404, detail="El usuario no existe")


# Url local: http://127.0.0.1:8000/user/4 (el 4 se cambia por el ID del usuario que queremos eliminar)
