# API de Clasificación de Frutas con TensorFlow y FastAPI

Esta es una API simple y eficiente diseñada para clasificar imágenes de frutas. Utiliza un modelo de Deep Learning entrenado con **TensorFlow/Keras** y se sirve a través de un backend construido con **FastAPI**.

El modelo actual es capaz de distinguir entre tres tipos de frutas:
* 🍎 Manzana
* 🍌 Banano
* 🍊 Naranja



## 📋 Prerrequisitos

Para poder ejecutar este proyecto, necesitarás tener instalado lo siguiente en tu sistema:

* **Python 3.8** o superior.
* **pip** (el gestor de paquetes de Python).

---

## 🚀 Instalación

Sigue estos sencillos pasos para poner en marcha el proyecto en tu máquina local.

1.  **Clona el repositorio:**
    Abre tu terminal y ejecuta el siguiente comando para descargar el código fuente.
    ```bash
    git clone [https://github.com/NicoAAA/clasificador-frutas-tf.git](https://github.com/NicoAAA/clasificador-frutas-tf.git)
    ```

2.  **Navega al directorio del proyecto:**
    ```bash
    cd clasificador-frutas-tf
    ```

3.  **Instala las dependencias:**
    El proyecto tiene un archivo `requirements.txt` que lista todas las bibliotecas de Python necesarias. Instálalas con pip.
    ```bash
    pip install -r requirements.txt
    ```
---
## ⚡ Uso

Una vez que la instalación esté completa, puedes iniciar el servidor de la API con un solo comando.

* **Ejecuta el servidor:**
    ```bash
    uvicorn main:app --reload
    ```
    El flag `--reload` es muy útil durante el desarrollo, ya que reinicia el servidor automáticamente cada vez que detecta un cambio en el código.

* **Accede a la API:**
    El servidor estará activo y escuchando en `http://127.0.0.1:8000`.

* **Documentación Interactiva (Swagger UI):**
    FastAPI genera automáticamente una documentación interactiva. Puedes acceder a ella visitando `http://12.0.0.1:8000/docs` en tu navegador. Desde allí, podrás probar la API directamente.
    
    

---
## 🤖 Endpoint de la API

La API expone un único endpoint para realizar las clasificaciones.

### `/predict`

* **Método:** `POST`
* **Descripción:** Recibe una imagen y devuelve la clase de fruta predicha junto con el nivel de confianza del modelo.
* **Cuerpo de la Petición (`Request Body`):** Debes enviar los datos en formato `multipart/form-data`, con una clave llamada `file` que contenga el archivo de la imagen (por ejemplo, `.jpg`, `.png`, etc.).

#### ✅ Respuesta Exitosa (Código 200)

Si la imagen se procesa correctamente, la API devolverá un objeto JSON con la predicción y la confianza.

```json
{
  "prediction": "Manzana",
  "confidence": 0.987512469291687
}
