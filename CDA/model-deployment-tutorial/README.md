
# Despliegue de Modelo con FastAPI y Docker

Este proyecto demuestra cómo desplegar un modelo de machine learning usando FastAPI y Docker.

## Pasos para Configurar y Ejecutar la API

### 1. Crear un Entorno Virtual
Primero, crea un entorno virtual llamado `model_serving`:
```bash
python3 -m venv model_serving
```

Activa el entorno virtual:
- **En MacOS/Linux**:
  ```bash
  source model_serving/bin/activate
  ```
- **En Windows**:
  ```bash
  .\model_serving\Scripts\activate
  ```

### 2. Instalar Requisitos
Instala los paquetes requeridos listados en `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 3. Ejecutar la Aplicación FastAPI
Inicia la aplicación FastAPI con Uvicorn:
```bash
uvicorn main:app --reload
```

La app estará accesible en `http://127.0.0.1:8000`.

Puedes parar la app usando ```ctrl+c```

### 4. Instalar Docker Desktop
Descarga e instala Docker Desktop desde el [sitio oficial de Docker](https://www.docker.com/products/docker-desktop/).

Puedes seguir las instrucciones acá [Windows](https://docs.docker.com/desktop/install/windows-install/), [Mac](https://docs.docker.com/desktop/install/mac-install/), [Linux](https://docs.docker.com/desktop/install/linux/)

Una vez instalado, asegúrate de que Docker Desktop esté en ejecución iniciando la aplicación.

### 5. Crear y Ejecutar el Contenedor Docker
Después de configurar Docker, sigue estos pasos:

1. **Construir la imagen de Docker**:
   ```bash
   docker build -t my-fastapi-app .
   ```

   Si está teniendo problemas con el LinuxEngine en Windows, inicie una consola de PowerShell como administrador y ejecute los siguientes comandos (modifique la dirección de instalación de Docker según sea su caso):
  
    ```bash
     cd "C:\Program Files\Docker\Docker"
  
    ./DockerCli.exe -SwitchLinuxEngine
    ```

3. **Ejecutar el contenedor Docker**:
   ```bash
   docker run -d -p 8000:8000 my-fastapi-app
   ```

4. **Probar la API en Docker**:
   Puedes probar la API enviando una solicitud a `http://localhost:8000` después de iniciar el contenedor.

   A continuación, un script de Python de ejemplo (`test_request.py`) para probar el endpoint `/predict`:
   ```python
   import requests

   url = "http://127.0.0.1:8000/predict"
   sample_data = {
       "customerID": "12345",
       "gender": "Female",
       "SeniorCitizen": 1,
       "Partner": "Yes",
       "Dependents": "No",
       "tenure": 12,
       "PhoneService": "Yes",
       "MultipleLines": "No",
       "InternetService": "Fiber optic",
       "OnlineSecurity": "Yes",
       "OnlineBackup": "No",
       "DeviceProtection": "Yes",
       "TechSupport": "No",
       "StreamingTV": "Yes",
       "StreamingMovies": "No",
       "Contract": "Month-to-month",
       "PaperlessBilling": "Yes",
       "PaymentMethod": "Electronic check",
       "MonthlyCharges": 75.35,
       "TotalCharges": 932.15
   }

   response = requests.post(url, json=sample_data)
   print("Response:", response.json() if response.status_code == 200 else response.text)
   ```

### Notas
- **Ruta del Modelo**: Asegúrate de que el archivo del modelo sea accesible dentro de Docker usando una ruta relativa, como `model/catboost_model.cbm`.


### Apagar Docker
Para detener Docker:
- **Windows/MacOS**: Haz clic derecho en el ícono de Docker Desktop y selecciona **Quit Docker Desktop**.
- **Linux**: Ejecuta `sudo systemctl stop docker` en tu terminal.


