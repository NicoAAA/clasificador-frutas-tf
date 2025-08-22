API de Detección de Productos Agrícolas 🥕

Este documento proporciona la información necesaria para que el equipo de Frontend pueda entender, ejecutar y consumir la API para la detección de productos agrícolas.

⚠️ Estado Actual: Modo de Simulación (Mock)

Es muy importante entender que la API se encuentra actualmente en modo de simulación. Esto significa que NO está utilizando un modelo de Inteligencia Artificial real.

    Comportamiento: La API ignora la imagen que se sube y devuelve una respuesta aleatoria predefinida.

    Propósito: El objetivo de esta versión es desbloquear al equipo de Frontend, permitiéndoles construir y probar la interfaz de usuario para todos los escenarios posibles (detección única, múltiple o fallida) sin tener que esperar a que el modelo real esté entrenado.

🚀 Cómo Empezar (Running Locally)

Para ejecutar la API en tu entorno de desarrollo local, sigue estos pasos:

1. Prerrequisitos

    Python 3.8 o superior

    pip y venv

2. Instalación

    Clona este repositorio en tu máquina local.

    Abre una terminal en la raíz del proyecto y crea un entorno virtual:
    Bash

python -m venv venv

Activa el entorno virtual:

    En macOS/Linux: source venv/bin/activate

    En Windows: venv\Scripts\activate

Instala todas las dependencias con un solo comando usando el archivo requirements.txt:
Bash

    pip install -r requirements.txt

3. Ejecutar el Servidor

Una vez instaladas las dependencias, inicia el servidor de desarrollo con el siguiente comando:
Bash

uvicorn main:app --reload

La API estará disponible en http://127.0.0.1:8000.

Endpoints de la API

La API cuenta con una interfaz de documentación interactiva generada automáticamente por FastAPI. Puedes acceder a ella para probar los endpoints de forma visual.

URL de la Documentación: http://127.0.0.1:8000/docs

POST /detect/

Este es el endpoint principal. Se encarga de recibir una imagen y devolver los productos detectados en ella.

    Método: POST

    Descripción: Recibe un archivo de imagen y devuelve una lista de objetos, donde cada objeto es un producto detectado.

    Cuerpo de la Petición (Request Body): multipart/form-data

        key: file

        value: El archivo de imagen (ej. imagen_del_producto.jpg).

Posibles Respuestas del Servidor (Simuladas)

Cada vez que llames a este endpoint, recibirás aleatoriamente una de las siguientes tres estructuras de respuesta. Esto te permite probar todos los flujos de la aplicación.

✅ Escenario 1: Detección Múltiple

El modelo encuentra varios productos en la imagen. La API devuelve una lista con dos o más objetos.

    Código de Respuesta: 200 OK

    Cuerpo de la Respuesta:
    JSON

    [
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
    ]

✅ Escenario 2: Detección Única

El caso ideal donde se encuentra un solo producto. La API devuelve una lista con un solo objeto.

    Código de Respuesta: 200 OK

    Cuerpo de la Respuesta:
    JSON

    [
      {
        "producto": "manzana_criolla",
        "confianza": 0.95,
        "caja_coordenadas": [110, 150, 400, 420]
      }
    ]

✅ Escenario 3: Sin Detección

El modelo no pudo identificar ningún producto conocido. La API devuelve una lista vacía.

    Código de Respuesta: 200 OK

    Cuerpo de la Respuesta:
    JSON

    []

🔮 Próximos Pasos

Una vez que el modelo de IA esté entrenado, el motor interno de este endpoint será reemplazado. Sin embargo, el contrato de la API (la forma en que se envía la petición y la estructura de la respuesta JSON) permanecerá idéntico. La transición será transparente para la aplicación frontend.
