# services/classifier.py
import boto3
from botocore.exceptions import BotoCoreError, ClientError
from data.mappings import MAPA_CLASIFICACION, DICCIONARIO_TRADUCCION_ES, MAPA_UNIDADES


def _clasificar_y_traducir_producto(response_aws: dict):
    """
    Función interna que procesa la respuesta de AWS.
    --- MODIFICADO ---
    Ahora genera una descripción más natural.
    """
    labels = response_aws.get('Labels', [])
    labels_ordenadas = sorted(labels, key=lambda x: x.get('Confidence', 0), reverse=True)

    for label in labels_ordenadas:
        nombre_en_ingles = label.get('Name')
        nombre_en_ingles_lower = nombre_en_ingles.lower()

        if nombre_en_ingles_lower in MAPA_CLASIFICACION:
            categoria_asignada = MAPA_CLASIFICACION[nombre_en_ingles_lower]
            nombre_traducido = DICCIONARIO_TRADUCCION_ES.get(nombre_en_ingles, nombre_en_ingles)
            
            # Buscamos la unidad de medida sugerida
            unidad_sugerida = MAPA_UNIDADES.get(nombre_en_ingles_lower, 'unidad')

            # --- ¡LÍNEA MODIFICADA! ---
            # En lugar de listar etiquetas, creamos una descripción más útil.
            descripcion_sugerida = f"{nombre_traducido} de alta calidad. Producto clasificado en la categoría de {categoria_asignada}."
            
            sugerencia = {
                "nombre_producto": nombre_traducido,
                "categoria": categoria_asignada,
                "confianza": round(label.get('Confidence', 0) / 100, 2),
                "descripcion_sugerida": descripcion_sugerida, # <-- Campo con la nueva descripción
                "unidad_medida_sugerida": unidad_sugerida
            }
            
            return {"sugerencia_principal": sugerencia, "detecciones_completas": labels}
            
    return {"sugerencia_principal": None, "detecciones_completas": labels}

def analizar_imagen_con_aws(image_bytes: bytes):
    """
    Función principal del servicio: llama a AWS y luego procesa el resultado.
    """
    try:
        rekognition_client = boto3.client('rekognition')
        response_aws = rekognition_client.detect_labels(
            Image={'Bytes': image_bytes}, MaxLabels=10, MinConfidence=75
        )
        return _clasificar_y_traducir_producto(response_aws)
    except (BotoCoreError, ClientError) as e:
        # Re-lanza una excepción personalizada para que el router la maneje
        raise ConnectionError(f"Error de comunicación con AWS: {e}")