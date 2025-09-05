# services/classifier.py
import boto3
from botocore.exceptions import BotoCoreError, ClientError
from data.mappings import MAPA_CLASIFICACION, DICCIONARIO_TRADUCCION_ES, ETIQUETAS_GENERICAS_A_IGNORAR

def clasificar_y_traducir_producto(response_aws: dict):
    """
    Versión final que incluye coordenadas en TODAS las sugerencias cuando estén disponibles.
    """
    labels_ordenadas = sorted(response_aws.get('Labels', []), key=lambda x: x.get('Confidence', 0), reverse=True)

    sugerencia_principal = None
    sugerencias_alternativas = []
    nombre_principal_encontrado = None

    # --- PRIMERA PASADA: Buscar la sugerencia principal ---
    for label in labels_ordenadas:
        nombre_en_ingles = label.get('Name')
        nombre_en_ingles_lower = nombre_en_ingles.lower()

        if nombre_en_ingles_lower in ETIQUETAS_GENERICAS_A_IGNORAR:
            continue

        if nombre_en_ingles_lower in MAPA_CLASIFICACION:
            categoria_asignada = MAPA_CLASIFICACION[nombre_en_ingles_lower]
            nombre_traducido = DICCIONARIO_TRADUCCION_ES.get(nombre_en_ingles, nombre_en_ingles)
            
            # Lógica para extraer coordenadas (si existen)
            coordenadas = [] 
            if label.get('Instances'):
                box = label['Instances'][0]['BoundingBox']
                coordenadas = [box['Left'], box['Top'], box['Width'], box['Height']]

            sugerencia_principal = {
                "nombre_producto": nombre_traducido,
                "categoria": categoria_asignada,
                "confianza": round(label.get('Confidence', 0) / 100, 2),
                "caja_coordenadas": coordenadas  # <-- Campo añadido
            }
            nombre_principal_encontrado = nombre_en_ingles
            break

    # --- SEGUNDA PASADA: Construir la lista de alternativas ---
    for label in labels_ordenadas:
        nombre_en_ingles = label.get('Name')

        if nombre_en_ingles == nombre_principal_encontrado or nombre_en_ingles.lower() in ETIQUETAS_GENERICAS_A_IGNORAR:
            continue

        # Lógica para extraer coordenadas para las alternativas también
        coordenadas_alt = []
        if label.get('Instances'):
            box = label['Instances'][0]['BoundingBox']
            coordenadas_alt = [box['Left'], box['Top'], box['Width'], box['Height']]

        sugerencias_alternativas.append({
            "nombre_producto": DICCIONARIO_TRADUCCION_ES.get(nombre_en_ingles, nombre_en_ingles),
            "confianza": round(label.get('Confidence', 0) / 100, 2),
            "caja_coordenadas": coordenadas_alt # <-- Campo añadido
        })

    return {
        "sugerencia_principal": sugerencia_principal, 
        "sugerencias_alternativas": sugerencias_alternativas
    }

def analizar_imagen_con_aws(image_bytes: bytes):
    try:
        rekognition_client = boto3.client('rekognition')
        response_aws = rekognition_client.detect_labels(
            Image={'Bytes': image_bytes}, MaxLabels=10, MinConfidence=75
        )
        return clasificar_y_traducir_producto(response_aws)
    except (BotoCoreError, ClientError) as e:
        raise ConnectionError(f"Error de comunicación con AWS: {e}")