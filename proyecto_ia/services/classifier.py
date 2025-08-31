# services/classifier.py
import boto3
from botocore.exceptions import BotoCoreError, ClientError
from data.mappings import MAPA_CLASIFICACION, DICCIONARIO_TRADUCCION_ES

def _clasificar_y_traducir_producto(response_aws: dict):
    """
    Función interna que procesa la respuesta de AWS.
    """
    labels_ordenadas = sorted(response_aws.get('Labels', []), key=lambda x: x.get('Confidence', 0), reverse=True)

    for label in labels_ordenadas:
        nombre_en_ingles = label.get('Name')
        nombre_en_ingles_lower = nombre_en_ingles.lower()

        if nombre_en_ingles_lower in MAPA_CLASIFICACION:
            categoria_asignada = MAPA_CLASIFICACION[nombre_en_ingles_lower]
            nombre_traducido = DICCIONARIO_TRADUCCION_ES.get(nombre_en_ingles, nombre_en_ingles)
            
            sugerencia = {
                "nombre_producto": nombre_traducido,
                "categoria": categoria_asignada,
                "confianza": round(label.get('Confidence', 0) / 100, 2)
            }
            # Devuelve tanto la sugerencia principal como la respuesta completa por si es útil
            return {"sugerencia_principal": sugerencia, "detecciones_completas": response_aws.get('Labels', [])}
            
    return {"sugerencia_principal": None, "detecciones_completas": response_aws.get('Labels', [])}

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