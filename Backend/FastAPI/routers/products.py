from fastapi import APIRouter

router = APIRouter(
    prefix="/products", tags=["products"], responses={404: {"message": "No encontrado"}}
)
# prefix: para añadir una ruta por defecto a todos los endpoints
# responses: para añadir un mensaje por defecto a todos los endpoints cuando haya un error
# tags: para agrupar products.py en la documentación de nuestra API con ese tag

# Inicia el server: python -m uvicorn products:app --reload


products_list = ["Producto 1", "Producto 2", "Producto 3", "Producto 4", "Producto 5"]


@router.get("/")
async def products():
    return products_list


@router.get("/{id}")  # Path
async def products(id: int):
    return products_list[id]
