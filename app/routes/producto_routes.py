from fastapi import APIRouter
from app.models.producto_model import Producto
from app.controllers.producto_controller import *



router = APIRouter()

@router.get("/productos/{id}")
def get_productos(id: int):
    return obtener_productos(id)


@router.post("/productos")
def post_producto(producto: Producto):
    return crear_producto(producto)


@router.put("/productos/{id}")
def put_producto(id: int, producto: Producto):
    return actualizar_producto(id, producto)


@router.delete("/productos/{id}")
def delete_producto(id: int):
    return eliminar_producto(id)
