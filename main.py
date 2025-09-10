# main.py
from fastapi import FastAPI
from api.router import router as api_router
from mangum import Mangum 

app = FastAPI(
    title="API de Clasificación de Productos - Arquitectura Limpia",
    description="Clasifica productos agrícolas de Cundinamarca en categorías predefinidas.",
    version="5.0.0-clean-architecture"
)

# Incluimos las rutas definidas en el router de la API bajo el prefijo /api/v1
# Ahora tu endpoint será: http://127.0.0.1:8000/api/v1/classify/
app.include_router(api_router, prefix="/api/v1")

@app.get("/", summary="Endpoint de Bienvenida")
def read_root():
    return {"message": "Bienvenido a la API de Clasificación de Productos"}

handler = Mangum(app)