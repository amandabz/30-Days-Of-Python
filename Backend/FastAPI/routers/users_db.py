from fastapi import APIRouter, HTTPException, status

from Backend.FastAPI.db.models.user import User  # importar el modelo de usuario
from Backend.FastAPI.db.client import db_client  # importar el cliente de la base de datos
from Backend.FastAPI.db.schemas.user import user_schema, users_schema  # importar el esquema de usuario
from bson import ObjectId  # ObjectId: para poder buscar por el ID de MongoDB

router = APIRouter(
    tags=["userdb"], prefix="/userdb"
)


@router.get("/", response_model=list[User])
# response_model: para que la respuesta sea una lista de User
async def get_users():
    users = users_schema(db_client.users.find())
    return users


# Path
@router.get("/{uuid}")
async def get_user(uuid: str):
    user = search_user("_id", ObjectId(uuid))

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El usuario no existe",
        )

    return user


# Crear usuario
@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user_data: User):
    """
    Buscar un usuario por su email y si no existe, lo inserta en la base de datos
    :param user_data: datos del usuario
    :return: el usuario insertado
    """
    # Comprobar si el usuario ya existe
    existing_user = search_user("email", user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario ya existe",
        )

    # Convertir el objeto User en un diccionario/json para:
    # - poder insertarlo en la base de datos
    # - poder eliminar el ID del diccionario, porque MongoDB lo genera automáticamente
    user_dict = dict(user_data)

    # Eliminar el ID del diccionario
    del user_dict["uuid"]

    # Insertar un usuario (insert_one) en la base de datos
    # local: nombre de la base de datos
    # users: nombre de la colección (localhost/local/users)
    inserted_id = db_client.users.insert_one(user_dict).inserted_id

    # Obtener el usuario que se ha insertado
    get_inserted_user = user_schema(db_client.users.find_one({"_id": inserted_id}))
    return User(**get_inserted_user)


# Eliminar usuario
@router.delete("/{uuid}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(uuid: str) -> None:
    """
    Elimina un usuario por su id
    :param uuid: id del usuario
    """
    found = db_client.users.find_one_and_delete({"_id": ObjectId(uuid)})

    if not found:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El usuario no ha podido ser eliminado",
        )


# Actualizar usuario
@router.put("/{uuid}", response_model=User, status_code=status.HTTP_202_ACCEPTED)
async def update_user(user: User):
    try:
        # Convertimos el objeto User en un diccionario/json para poder actualizarlo
        user_dict = dict(user)

        # Eliminar el ID para que no se actualice porque el id es algo que NO debe cambiar
        del user_dict["uuid"]

        # Actualizar el usuario
        # replace: actualiza el documento entero
        # update: actualiza solo los campos que le pasemos
        db_client.users.find_one_and_replace({"_id": ObjectId(user.uuid)}, user_dict)

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El usuario no se ha podido actualizar",
        )

    # Devolver el usuario actualizado
    return search_user("_id", ObjectId(user.uuid))


# Buscar usuario
def search_user(field: str, key) -> User | None:
    # key: clave (puede ser de cualquier tipo)
    # field: campo por el que se va a buscar
    # key: valor del campo por el que se va a buscar

    # Obtener el usuario por el campo que le digamos
    find_user = db_client.users.find_one({field: key})
    if find_user:
        return User(**user_schema(find_user))
