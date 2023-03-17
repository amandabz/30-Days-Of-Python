from fastapi import APIRouter, HTTPException, status

from Backend.FastAPI.db.models.user import User  # importar el modelo de usuario
from Backend.FastAPI.db.client import db_client  # importar el cliente de la base de datos
from Backend.FastAPI.db.schemas.user import user_schema  # importar el esquema de usuario

router = APIRouter(
    tags=["userdb"], responses={404: {"message": "No encontrado"}}, prefix="/userdb"
)


"""
@router.get("/")
async def users():
    return users_list
"""

"""
# Path
@router.get("/{uuid}")
async def user(uuid: str):
    return search_user(uuid)


# Query
@router.get("/")
async def user(uuid: str):
    return search_user(uuid)
"""


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user_data: User):
    """
    Buscar un usuario por su email y si no existe,  se inserta en la base de datos
    :param user_data: datos del usuario
    :return: el usuario insertado
    """
    # Comprobar si el usuario ya existe
    if search_user_by_mail(user_data.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario ya existe",
        )

    # Convertir el objeto User en un diccionario/json
    user_dict = dict(user_data)

    # Eliminar el id del diccionario, porque MongoDB lo genera automáticamente
    del user_dict["uuid"]

    # Insertar un usuario (insert_one) en la base de datos
    # local: nombre de la base de datos
    # users: nombre de la colección (localhost/local/users)
    uuid = db_client.local.users.insert_one(user_dict).inserted_id

    # Obtener el usuario que se ha insertado
    inserted_user = user_schema(db_client.local.users.find_one({"_id": uuid}))

    return User(**inserted_user)

"""
@router.put("/")
async def user(user_data: User):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.uuid == user_data.uuid:
            users_list[index] = user_data
            found = True
            break

    if not found:
        return {"error": "No se ha actualizado el usuario"}

    return user
"""

"""
@router.delete("/{uuid}")
async def user(uuid: int):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == uuid:
            del users_list[index]
            found = True

    if not found:
        return {"error": "No se ha eliminado el usuario"}
"""


def search_user_by_mail(email: str) -> bool:
    try:
        # Obtener el usuario que se ha buscado por su email
        user = db_client.local.users.find_one({"email": email})
        return user is not None
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se ha encontrado el usuario",
        )
