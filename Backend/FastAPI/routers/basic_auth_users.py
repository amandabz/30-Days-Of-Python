from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

router = APIRouter()

# Criterio de autenticación
oauth2 = OAuth2PasswordBearer(
    tokenUrl="login"
)  # tokenUrl: url que se va a encargar de la autenticación


# Inicia el server: python -m uvicorn basic_auth_users:app --reload


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
        "password": "123456",
    },
    "amandab": {
        "username": "amandab",
        "full_name": "Amanda Benitez",
        "email": "amanda@gmail.com",
        "disabled": True,
        "password": "654321",
    },
}


def search_user_db(username: str) -> UserDB | None:
    if username in users_db:
        return UserDB(
            **users_db[username]
        )  # **: significa que puede haber varios parámetros


def search_user(username: str) -> User:
    if username in users_db:
        return User(**users_db[username])


async def current_user(
    token: str = Depends(oauth2),
):  # outh2: criterio de autenticación (arriba)
    user = search_user(token)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales de autenticación inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario deshabilitado"
        )

    return user


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto"
        )

    user = search_user_db(form.username)

    if not form.password == user.password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La contraseña no es correcta",
        )

    return {"access_token": user.username, "token_type": "bearer"}


@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
