# main.py
import random
import asyncio
from fastapi import FastAPI, File, UploadFile, HTTPException

# --- 1. CONFIGURACIÓN DE LA APLICACIÓN ---
app = FastAPI(
    title="API de Detección de Productos (SIMULACIÓN AVANZADA)",
    description="Este mock devuelve respuestas realistas, incluyendo datos para el autollenado del formulario.",
    version="1.0.2-mock-autofill"
)

# --- 2. MAPAS DE DATOS (Simulan la lógica del backend) ---
# Estos mapas son los que usarías en el backend real para derivar los datos.
mapa_categorias = {
    "papa_sabanera": "Tubérculos y Raíces", "cebolla_cabezona": "Hortalizas y Verduras",
    "fresa": "Frutas", "mora": "Frutas", "queso_campesino": "Lácteos y Derivados"
}
mapa_unidades = {
    "papa_sabanera": "Bulto", "cebolla_cabezona": "Atado", "fresa": "Canastilla",
    "mora": "Canastilla", "queso_campesino": "Libra (lb)"
}

# --- 3. DATOS DE SIMULACIÓN AVANZADA ---
# Cada escenario ahora incluye la sección 'autofill_sugerido'.
MOCK_SCENARIOS = {
    "deteccion_unica": {
        "detections": [
            {
                "producto": "fresa",
                "confianza": 0.95,
                "caja_coordenadas": [80, 120, 250, 300],
                "autofill_sugerido": {
                    "nombre_producto": "Fresa",
                    "categoria": "Frutas",
                    "unidad_venta": "Canastilla"
                }
            }
        ]
    },
    "deteccion_multiple": {
        "detections": [
            {
                "producto": "papa_sabanera",
                "confianza": 0.92,
                "caja_coordenadas": [150, 200, 350, 450],
                "autofill_sugerido": {
                    "nombre_producto": "Papa Sabanera",
                    "categoria": "Tubérculos y Raíces",
                    "unidad_venta": "Bulto"
                }
            },
            {
                "producto": "cebolla_cabezona",
                "confianza": 0.85,
                "caja_coordenadas": [400, 300, 500, 400],
                "autofill_sugerido": {
                    "nombre_producto": "Cebolla Cabezona",
                    "categoria": "Hortalizas y Verduras",
                    "unidad_venta": "Atado"
                }
            }
        ]
    },
    "sin_deteccion": {
        "detections": []
    }
}

# --- 4. ENDPOINTS ---
@app.get("/", summary="Endpoint de Bienvenida")
def read_root():
    return {"message": "Bienvenido a la API de simulación con autollenado."}

@app.post("/detect/", summary="Detectar productos y sugerir autollenado (Simulado)")
async def detect_products(file: UploadFile = File(..., description="Imagen a procesar")):
    """
    **Este es un endpoint de simulación avanzada.** Devuelve aleatoriamente uno de los 
    escenarios predefinidos (detección única, múltiple o ninguna).

    La respuesta ahora incluye un objeto `autofill_sugerido` por cada detección,
    listo para ser usado por el frontend para llenar el formulario.
    """
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="El archivo subido no es una imagen.")

    # Elige uno de los escenarios al azar
    lista_escenarios = list(MOCK_SCENARIOS.values())
    respuesta_aleatoria = random.choice(lista_escenarios)
    
    print(f"Simulando respuesta aleatoria. Escenario enviado: {respuesta_aleatoria}")
    
    # Simula un retraso de red
    await asyncio.sleep(random.uniform(0.5, 1.5))
    
    return respuesta_aleatoria
