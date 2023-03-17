from datetime import datetime, timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

# python -m pip install "python-jose[cryptography]"
from jose import JWTError, jwt

# python -m pip install "passlib[bcrypt]"
from passlib.context import CryptContext  # Criterio de encriptación
from pydantic import BaseModel

# openssl rand -hex 32 (Git Bash)
# Clave secreta para encriptar el token
SECRET_KEY = "a1a0be6192cfe06497f13aa1ceffb795f2266fe2c396160e43d03f95435ab2f7"

# Algoritmo utilizado para encriptar el token
ALGORITHM = "HS256"

# Duración del token en minutos (30 minutos)
ACCESS_TOKEN_DURATION = 30


router = APIRouter(tags=["JWT Auth"])

# Inicia el server: python -m uvicorn jwt_auth_users:app --reload


# Criterio de autenticación
oauth2 = OAuth2PasswordBearer(
    tokenUrl="login"
)  # tokenUrl: url que se va a encargar de la autenticación

# Criterio de encriptación
crypt = CryptContext(schemes=["bcrypt"])  # Para encriptar la contraseña


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_db = {
    "mouredev": {
        "username": "mouredev",
        "full_name": "Brais Moure",
        "email": "brais@gmail.com",
        "disabled": False,
        "password": "$2a$12$54yU3kDBqToFs1BnE838BeQJQ.bZ4Zlys1RpLoNYRXYI9/OArfLNS"
        # https://bcrypt-generator.com/ (contraseña sin encriptar: 123456)
    },
    "amandab": {
        "username": "amandab",
        "full_name": "Amanda Benitez",
        "email": "amanda@gmail.com",
        "disabled": True,
        "password": "$2a$12$nf4/SCURsFXYgGnB7N4ad.i6FqgFk5hOtKHDT5I0jwNjuJfBMzTDC"
        # https://bcrypt-generator.com/ (contraseña sin encriptar: 654321)
    },
}


def search_user_db(username: str) -> UserDB | None:
    """
    Busca un usuario en la base de datos
    :param username:
    :return: UserDB
    """
    if username in users_db:
        # **: significa que puede haber varios parámetros
        return UserDB(**users_db[username])


def search_user(username: str) -> User | None:
    """
    Busca un usuario en la base de datos
    :param username: str
    :return: User
    """
    if username in users_db:
        return User(**users_db[username])


async def auth_user(token: str = Depends(oauth2)):
    http_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticación inválidas",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        username = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise http_exception

    except JWTError:
        raise http_exception

    return search_user(username)


async def current_user(user: User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario deshabilitado"
        )

    return user


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()) -> dict | None:
    """
    Autenticación de usuarios
    :param form: OAuth2PasswordRequestForm
    :return: dict | None
    """
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="El usuario no es correcto",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = search_user_db(form.username)

    crypt_password = crypt.verify(form.password, user.password)
    # Comprueba si la contraseña encriptada es correcta
    # form.password = contraseña sin encriptar
    # user.password = contraseña encriptada

    if not crypt_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La contraseña no es correcta",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario deshabilitado",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Duración del token
    access_token_expiration = timedelta(minutes=ACCESS_TOKEN_DURATION)

    # Fecha de expiración del token
    expire = datetime.utcnow() + access_token_expiration

    # Genera el token
    access_token = jwt.encode(
        {"sub": user.username, "exp": expire}, SECRET_KEY, algorithm=ALGORITHM
    )

    # Devuelve el token
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me")  # /users/me?token=...
async def me(user: User = Depends(current_user)) -> User | None:
    """
    Devuelve el usuario
    :param user: User
    :return: user | None
    """
    return user


# https://jwt.io/ (para decodificar el token)
