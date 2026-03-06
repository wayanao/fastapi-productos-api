from fastapi import FastAPI
from app.routes.producto_routes import router as producto_router

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando correctamente"}

app.include_router(producto_router)
