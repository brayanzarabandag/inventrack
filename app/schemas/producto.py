from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    cantidad: int
    categoria: str
    codigo_barras: Optional[str] = None
    precio: float
    en_stock: bool = True
    activo: Optional[bool] = True

class ProductUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    cantidad: Optional[int] = None
    categoria: Optional[str] = None
    codigo_barras: Optional[str] = None
    precio: Optional[float] = None
    en_stock: Optional[bool] = None
    activo: Optional[bool] = None
    
class ProductPublic(BaseModel):
    id: int
    nombre: str
    descripcion: Optional[str] = None
    cantidad: int
    categoria: str
    codigo_barras: Optional[str] = None
    precio: float
    en_stock: bool
    activo: bool