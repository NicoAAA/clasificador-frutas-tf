# api/router.py
from fastapi import APIRouter, File, UploadFile, HTTPException
# Importamos la nueva función de nuestro servicio clasificador
from services.classifier import analizar_imagen_con_gemini

router = APIRouter()

@router.post("/classify/", summary="Clasifica un producto usando IA Generativa (Gemini)")
async def classify_product(file: UploadFile = File(..., description="Imagen a procesar")):
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="El archivo subido no es una imagen.")
    
    try:
        image_bytes = await file.read()
        # ¡Aquí está el cambio! Llamamos a la nueva función.
        resultado = analizar_imagen_con_gemini(image_bytes)
        return resultado
    except (ConnectionError, ValueError) as e:
        # Capturamos los errores que nuestra función de servicio puede lanzar
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        # Captura cualquier otro error inesperado
        print(f"Ocurrió un error inesperado: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor.")