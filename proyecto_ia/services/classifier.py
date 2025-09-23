# services/classifier.py
import google.generativeai as genai
import PIL.Image
import io
import os
import json
import requests
import time
from datetime import datetime
from dotenv import load_dotenv
from urllib.parse import quote
from difflib import get_close_matches
from data.sipsa_products import LISTA_PRODUCTOS_SIPSA

# (Configuración de la API key no cambia)
load_dotenv()
try:
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("No se encontró la GOOGLE_API_KEY en el archivo .env")
    genai.configure(api_key=api_key)
except ValueError as e:
    print(f"ERROR DE CONFIGURACIÓN: {e}")


def obtener_precio_sipsa(producto: str, unidad: str):
    # <-- MEJORA: Se añade la fecha del reporte a la respuesta.
    mapa_columnas_precio = {'kg': 'precio_kilogramo', 'unidad': 'precio_unidad', 'l': 'precio_litro'}
    columna_precio = mapa_columnas_precio.get(unidad)
    if not columna_precio: return None, None

    API_URL = "https://www.datos.gov.co/resource/rs5x-q2nz.json"
    producto_codificado = quote(producto)
    query = (f"?mercado=Bogot%C3%A1,%20D.C.,%20Corabastos&producto={producto_codificado}"
             f"&$where={columna_precio}%20IS%20NOT%20NULL&$limit=1&$order=fecha%20DESC")
    url_completa = f"{API_URL}{query}"
    
    try:
        response = requests.get(url_completa, timeout=10)
        response.raise_for_status()
        data = response.json()
        if data and columna_precio in data[0]:
            precio = float(data[0][columna_precio])
            fecha_reporte_str = data[0].get("fecha", "")
            fecha_reporte_dt = datetime.fromisoformat(fecha_reporte_str.replace("T00:00:00.000", ""))
            fecha_formateada = fecha_reporte_dt.strftime("%Y-%m-%d")
            return precio, fecha_formateada
        else:
            return None, None
    except (requests.exceptions.RequestException, ValueError, KeyError) as e:
        print(f"Error al procesar precio para '{producto}' con unidad '{unidad}': {e}")
        return None, None

def encontrar_mejor_coincidencia(nombre_producto: str):
    # (Esta función no cambia)
    coincidencias = get_close_matches(nombre_producto, LISTA_PRODUCTOS_SIPSA, n=1, cutoff=0.7)
    return coincidencias[0] if coincidencias else None

# services/classifier.py

def analizar_imagen_con_gemini(image_bytes: bytes):
    try:
        # 1. Primero, convierte los bytes de la imagen a un objeto de imagen.
        img = PIL.Image.open(io.BytesIO(image_bytes))
        
        # 2. Luego, inicializa el modelo de IA.
        model = genai.GenerativeModel('gemini-2.5-pro')

        # 3. Después, define el prompt que usarás.
        # <-- PROMPT INTELIGENTE -->
        prompt = """
        Tu tarea principal es actuar como un experto en productos de supermercado en Colombia e identificar con la MÁXIMA PRECISIÓN VISUAL el producto y su variedad específica en la imagen. Cubre todas las categorías: frutas, verduras, carnes, lácteos, etc.

        Sigue estas reglas en orden de importancia:
        1.  **Prioridad #1: Precisión Visual.** Identifica el producto exacto. Si la imagen muestra un 'Tomate cherry', tu identificación debe ser 'Tomate cherry'. Si muestra 'Lechuga romana', debe ser 'Lechuga romana'. La evidencia en la imagen es lo más importante.

        2.  **Prioridad #2: Coincidencia con la Base de Datos (SIPSA).** Después de identificar el producto, si el nombre que identificaste es un producto agrícola fresco y coincide o es muy similar a un nombre en la lista de ejemplos oficiales, usa el formato oficial. Esto es para ayudar a una búsqueda de precios posterior.

        **Regla de Oro:** NUNCA fuerces un nombre de la lista de ejemplos si no corresponde con lo que ves en la imagen. Si ves un 'Tomate cherry', NO lo llames 'Tomate chonto' solo porque está en los ejemplos.

        **Ejemplos de formato para la base de datos oficial (SIPSA):**
        - Si identificas una papa parda pastusa, usa 'Papa parda pastusa'.
        - Si identificas una mora de Castilla, usa 'Mora de castilla'.
        - Si identificas una cebolla roja, usa 'Cebolla cabezona roja'.

        Tu única respuesta debe ser un objeto JSON válido en español, sin textos adicionales. La estructura es:
        { "sugerencia_principal": {
            "nombre_producto": "El nombre específico del producto, incluyendo su variedad si es posible.",
            "categoria": "Clasifica el producto en una de estas categorías: 'Verduras', 'Frutas', 'Granos y Legumbres', 'Lácteos y Derivados', 'Carnes Frescas', 'Pescados y Mariscos', 'Huevos y Derivados', 'Panadería y Repostería', 'Miel y Derivados Apícolas', 'Plantas y Flores'",
            "confianza": "Un valor flotante entre 0.0 y 1.0.",
            "descripcion_sugerida": "Una descripción objetiva y útil para un post de venta ecomerce agricola",
            "unidad_medida_sugerida": "Sugiere la unidad de medida más común. Elige entre: 'kg', 'unidad', 'l'."
          }
        }
        """
        
        # 4. Finalmente, llama al modelo con el prompt y la imagen.
        response = model.generate_content([prompt, img])
        
        # El resto de tu código para procesar la respuesta continúa aquí...
        cleaned_response_text = response.text.strip().replace('```json', '').replace('```', '')
        resultado_json = json.loads(cleaned_response_text)
        
        sugerencia = resultado_json.get("sugerencia_principal")
        
        if sugerencia:
            # ... (el resto de tu lógica no necesita cambios)
            sugerencia["precio_mercado"] = None
            nombre_gemini = sugerencia.get("nombre_producto")
            unidad_sugerida = sugerencia.get("unidad_medida_sugerida")

            if nombre_gemini and unidad_sugerida in ['kg', 'unidad', 'l']:
                precio, fecha_reporte = obtener_precio_sipsa(nombre_gemini, unidad_sugerida)
                
                if precio is None:
                    nombre_corregido = encontrar_mejor_coincidencia(nombre_gemini)
                    if nombre_corregido:
                        print(f"Intento 1 falló para '{nombre_gemini}'. Reintentando con coincidencia: '{nombre_corregido}'")
                        precio, fecha_reporte = obtener_precio_sipsa(nombre_corregido, unidad_sugerida)
                        if precio is not None:
                            sugerencia["nombre_producto"] = nombre_corregido
                
                if precio is not None:
                    sugerencia["precio_mercado"] = {
                        "valor": precio,
                        "unidad": unidad_sugerida,
                        "fecha_reporte": fecha_reporte
                    }

        return resultado_json

    except json.JSONDecodeError:
        raise ValueError("La respuesta del modelo no fue un JSON válido.")
    except Exception as e:
        raise ConnectionError(f"Error en el proceso de análisis: {e}")
    
