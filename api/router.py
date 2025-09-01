# api/router.py
from fastapi import APIRouter, File, UploadFile, HTTPException
from services.classifier import analizar_imagen_con_aws

router = APIRouter()

@router.post("/classify/", summary="Clasifica un producto en categorías predefinidas")
async def classify_product(file: UploadFile = File(..., description="Imagen a procesar")):
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="El archivo subido no es una imagen.")
    
    try:
        image_bytes = await file.read()
        resultado = analizar_imagen_con_aws(image_bytes)
        return resultado
    except ConnectionError as e:
        # Captura el error específico del servicio y devuelve un error 503
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        # Captura cualquier otro error inesperado
        print(f"Ocurrió un error inesperado: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor.")