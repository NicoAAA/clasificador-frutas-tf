# API de Clasificación de Productos Agrícolas (Arquitectura Limpia)

Esta API permite clasificar productos agrícolas de Cundinamarca en categorías predefinidas usando un modelo de IA real desplegado en AWS Rekognition. Está diseñada para ser fácilmente consumida desde aplicaciones frontend como React Native, así como por otros clientes.

## Estructura del Proyecto

- `main.py`: Punto de entrada de la API (FastAPI).
- `api/router.py`: Define los endpoints principales.
- `services/classifier.py`: Lógica de clasificación y comunicación con AWS Rekognition.
- `data/mappings.py`: Diccionarios de mapeo y traducción de etiquetas.
- `requirements.txt`: Dependencias del proyecto.

## Instalación y Ejecución

1. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecuta el servidor:
   ```bash
   uvicorn main:app --reload
   ```
   Por defecto, la API estará disponible en `http://127.0.0.1:8000`.

## Endpoints Principales

### 1. Bienvenida
- **GET /**
  - Respuesta: `{ "message": "Bienvenido a la API de Clasificación de Productos" }`

### 2. Clasificación de Producto
- **POST /api/v1/classify/**
  - **Descripción:** Recibe una imagen y devuelve la categoría y nombre del producto detectado.
  - **Body:** FormData con el campo `file` (imagen).
  - **Respuesta exitosa:**
    ```json
    {
      "sugerencia_principal": {
        "nombre_producto": "Papa",
        "categoria": "Verduras",
        "confianza": 0.98,
        "caja_coordenadas": [0.1, 0.2, 0.3, 0.4]
      },
      "sugerencias_alternativas": [
        {
          "nombre_producto": "Zanahoria",
          "confianza": 0.85,
          "caja_coordenadas": [0.5, 0.6, 0.2, 0.3]
        }
      ]
    }
    ```
  - **Errores:**
    - 400: El archivo no es una imagen.
    - 503: Error de comunicación con AWS.
    - 500: Error interno del servidor.

## Integración con React Native

Puedes consumir el endpoint `/api/v1/classify/` desde React Native usando `fetch` o librerías como `axios`. Ejemplo usando `fetch`:

```javascript
const formData = new FormData();
formData.append('file', {
  uri: imageUri, // Ruta local de la imagen
  type: 'image/jpeg',
  name: 'foto.jpg',
});

fetch('http://127.0.0.1:8000/api/v1/classify/', {
  method: 'POST',
  body: formData,
  headers: {
    'Content-Type': 'multipart/form-data',
  },
})
  .then(response => response.json())
  .then(data => {
    // Procesa la respuesta
    console.log(data);
  })
  .catch(error => {
    // Maneja errores
    console.error(error);
  });
```

> **Nota:** Si tu API está en un servidor remoto, reemplaza la URL por la IP pública o dominio.

## Categorías y Traducciones

La API traduce automáticamente los nombres detectados por AWS Rekognition al español y los agrupa en categorías como:
- Verduras
- Frutas
- Granos y Legumbres
- Lácteos y Derivados
- Carnes Frescas
- Huevos y Derivados
- Panadería y Repostería
- Miel y Derivados Apícolas
- Plantas y Flores

Consulta el archivo `data/mappings.py` para ver el mapeo completo.

## Ejemplo de Respuesta

```json
{
  "sugerencia_principal": {
    "nombre_producto": "Fresa",
    "categoria": "Frutas",
    "confianza": 0.97,
    "caja_coordenadas": [0.12, 0.34, 0.22, 0.18]
  },
  "sugerencias_alternativas": [
    {
      "nombre_producto": "Manzana",
      "confianza": 0.80,
      "caja_coordenadas": [0.45, 0.23, 0.15, 0.20]
    }
  ]
}
```

## Extensión y Personalización

- Puedes modificar los diccionarios en `data/mappings.py` para agregar nuevas categorías o traducciones.
- La lógica de clasificación está en `services/classifier.py`.

## Recomendaciones para Producción
- Configura las credenciales de AWS Rekognition correctamente.
- Usa HTTPS en producción.
- Considera desplegar con Docker o en servicios cloud.

## Licencia
Este proyecto es de uso libre para fines educativos y de desarrollo.
