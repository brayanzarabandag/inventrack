from fastapi import APIRouter
from app.schemas.producto import ProductCreate, ProductPublic, ProductUpdate

router = APIRouter()

@router.get("/", response_model=list[ProductPublic])
def listar_productos():
    return [
        {
            "id": 1,
            "nombre": "Mouse Gamer",
            "descripcion": "RGB",
            "cantidad": 50,
            "categoria": "Periféricos",
            "ubicacion_fisica": "A1",
            "codigo_barras": "123456",
            "stock_minimo": 5,
            "activo": True
        }
    ]

@router.post("/", response_model=ProductPublic)
def crear_producto(data: ProductCreate):
    return {
        "id": 10,
        **data.dict()
    }

@router.put("/{producto_id}", response_model=ProductPublic)
def actualizar_producto(producto_id: int, data: ProductUpdate):
    return {
        "id": producto_id,
        **{
            k: v if v is not None else getattr(data, k)
            for k, v in {
                "nombre": data.nombre,
                "descripcion": data.descripcion,
                "cantidad": data.cantidad,
                "categoria": data.categoria,
                "ubicacion_fisica": data.ubicacion_fisica,
                "codigo_barras": data.codigo_barras,
                "stock_minimo": data.stock_minimo,
                "activo": data.activo,
            }.items()
        }
    }

@router.delete("/{producto_id}")
def eliminar_producto(producto_id: int):
    return {"message": f"Producto {producto_id} eliminado correctamente"}