from pydantic import BaseModel, Field

class Producto(BaseModel):
    nombre: str = Field(min_length=3)
    precio: float = Field(gt=0)
