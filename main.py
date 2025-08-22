# main.py
import io
import random
import asyncio
from fastapi import FastAPI, File, UploadFile, HTTPException
from PIL import Image

# --- 1. CONFIGURACIÓN DE LA APLICACIÓN ---
app = FastAPI(
    title="API de Detección de Productos Agrícolas (VERSIÓN DE SIMULACIÓN ALEATORIA)",
    description="Este es un mock. Devuelve respuestas simuladas y aleatorias para el desarrollo del frontend.",
    version="1.0.1-mock-random"
)

# --- 2. DATOS DE SIMULACIÓN ---
# Creamos respuestas falsas que imitan lo que el modelo real devolvería.
MOCK_RESPONSES = {
    "deteccion_multiple": [
        {
            "producto": "papa_sabanera",
            "confianza": 0.92,
            "caja_coordenadas": [150, 200, 350, 450]
        },
        {
            "producto": "cebolla_cabezona",
            "confianza": 0.85,
            "caja_coordenadas": [400, 300, 500, 400]
        }
    ],
    "deteccion_unica": [
        {
            "producto": "manzana_criolla",
            "confianza": 0.95,
            "caja_coordenadas": [110, 150, 400, 420]
        }
    ],
    "sin_deteccion": [],
    "deteccion_default": [
        {
            "producto": "fresa",
            "confianza": 0.88,
            "caja_coordenadas": [80, 120, 250, 300]
        }
    ]
}

# --- 3. ENDPOINT DE BIENVENIDA ---
@app.get("/", summary="Endpoint de Bienvenida")
def read_root():
    return {"message": "Bienvenido a la API de simulación aleatoria. El endpoint /detect/ devolverá datos de prueba diferentes cada vez."}

# --- 4. ENDPOINT DE DETECCIÓN (SIMULADO Y ALEATORIO) ---
@app.post("/detect/", summary="Detectar productos (Simulado y Aleatorio)")
async def detect_products(file: UploadFile = File(..., description="Imagen a procesar")):
    """
    **Este es un endpoint simulado y aleatorio.** Ignora el contenido y el nombre del archivo. Devuelve una de las 
    respuestas predefinidas al azar para simular el comportamiento real del modelo.
    """
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="El archivo subido no es una imagen.")

    # >>> CAMBIO PRINCIPAL: LÓGICA ALEATORIA <<<
    # 1. Creamos una lista con todos los posibles resultados.
    posibles_respuestas = list(MOCK_RESPONSES.values())
    
    # 2. Elegimos uno de esos resultados al azar.
    respuesta_aleatoria = random.choice(posibles_respuestas)
    
    print(f"Simulando respuesta aleatoria. Respuesta enviada: {respuesta_aleatoria}")
    
    # Simulamos un pequeño retraso para que parezca más realista
    await asyncio.sleep(random.uniform(0.5, 1.5))
    
    return respuesta_aleatoria