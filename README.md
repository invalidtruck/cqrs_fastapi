Proyecto FastAPI con CQRS y DevSecOps
Este repositorio contiene una aplicación web construida con FastAPI implementando el patrón CQRS (Command Query Responsibility Segregation), junto con un robusto pipeline DevSecOps automatizado usando GitHub Actions. El objetivo es demostrar cómo integrar la seguridad desde las primeras etapas del desarrollo (Shift Left Security) en un flujo de entrega continua.

🚀 Características Principales
Aplicación FastAPI: Una API moderna y de alto rendimiento construida con el framework web FastAPI para Python.

Patrón CQRS: Separación de las operaciones de lectura (Queries) y escritura (Commands) para mejorar la escalabilidad, el rendimiento y la mantenibilidad de la aplicación.

Contenedorización con Docker: La aplicación está empaquetada en una imagen Docker para asegurar un entorno consistente y portable.

Pipeline CI/CD con GitHub Actions: Automatización de los procesos de integración y entrega continua directamente desde GitHub.

Análisis de Seguridad de Imágenes Docker (Trivy): Escaneo automatizado de la imagen Docker en busca de vulnerabilidades conocidas en el sistema operativo y las librerías. El pipeline fallará si se encuentran vulnerabilidades críticas o altas.

Análisis de Seguridad Estático (SAST) con Bandit: Escaneo del código fuente de Python en busca de problemas de seguridad comunes y malas prácticas. Los resultados se suben como un artefacto.

Subida a Docker Hub: Una vez que la imagen pasa los controles de seguridad, se sube automáticamente a Docker Hub.

📂 Estructura del Proyecto
tu-repositorio/
├── .github/
│   └── workflows/
│       └── main.yml        # Definición del pipeline DevSecOps
├── app/
│   ├── __init__.py
│   └── main.py             # Archivo principal de la aplicación FastAPI
│   └── ...                 # Otros módulos de tu implementación CQRS (commands, queries, handlers, etc.)
├── Dockerfile              # Instrucciones para construir la imagen Docker
├── requirements.txt        # Dependencias de Python
├── README.md               # Este archivo
└── ...                     # Otros archivos del proyecto

🛠️ Requisitos Previos
Antes de empezar, asegúrate de tener instalado lo siguiente:

Python 3.9+

Docker Desktop: Para construir y ejecutar imágenes Docker localmente.

Cuenta de GitHub: Para alojar el repositorio y usar GitHub Actions.

Cuenta de Docker Hub: Para almacenar y gestionar tus imágenes Docker.

Configuración de GitHub Secrets
Para que el pipeline de GitHub Actions pueda iniciar sesión en Docker Hub y subir imágenes, necesitas configurar dos secretos en tu repositorio de GitHub:

Ve a tu repositorio en GitHub.

Haz clic en Settings (Configuración).

En el menú lateral, selecciona Secrets and variables > Actions.

Haz clic en New repository secret y crea los siguientes:

DOCKER_USERNAME: Tu nombre de usuario de Docker Hub.

DOCKER_PASSWORD: Un Personal Access Token (PAT) de Docker Hub. Genera uno en tu configuración de Docker Hub (Account Settings > Security). No uses tu contraseña principal.

🚀 Configuración y Ejecución Local
Para levantar la aplicación FastAPI localmente (sin Docker), sigue estos pasos:

Clona el repositorio:

git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio

Crea un entorno virtual (recomendado):

python -m venv venv
source venv/bin/activate  # En Linux/macOS
# venv\Scripts\activate   # En Windows

Instala las dependencias:

pip install -r requirements.txt

Ejecuta la aplicación FastAPI:

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

La aplicación estará disponible en http://127.0.0.1:8000. Puedes acceder a la documentación interactiva de la API en http://127.0.0.1:8000/docs.

Construir y Ejecutar la Imagen Docker Localmente
Para construir y ejecutar la aplicación usando Docker:

Construye la imagen Docker:

docker build -t invalidtruck/cqrs_fastapi:latest .

Ejecuta el contenedor Docker:

docker run -p 8000:8000 invalidtruck/cqrs_fastapi:latest

La aplicación estará accesible en http://localhost:8000.

⚙️ Pipeline DevSecOps (GitHub Actions)
El archivo .github/workflows/main.yml define el pipeline de CI/CD y DevSecOps. Se activa automáticamente en cada push a la rama main y en cada pull_request dirigido a main.

El pipeline consta de los siguientes pasos clave:

Checkout del código: Clona el repositorio en el entorno del runner de GitHub Actions.

Configurar variables de Docker: Define el nombre y la etiqueta de la imagen Docker (invalidtruck/cqrs_fastapi con una etiqueta basada en el SHA del commit).

Iniciar sesión en Docker Hub: Autentica el runner con Docker Hub usando los secretos configurados.

Construir la imagen Docker: Construye la imagen Docker de la aplicación. Esta imagen se carga localmente en el runner para el escaneo, pero no se sube a Docker Hub todavía.

Escanear la imagen Docker con Trivy: Ejecuta Trivy para escanear la imagen construida en busca de vulnerabilidades. Si se encuentran vulnerabilidades de severidad CRITICAL, HIGH o MEDIUM, el paso fallará, deteniendo el pipeline.

Subir la imagen Docker a Docker Hub: Si el escaneo de Trivy es exitoso (no se encuentran vulnerabilidades de alta severidad), la imagen se sube a Docker Hub.

Configurar Python: Configura el entorno de Python para los pasos de escaneo de código.

Instalar Bandit y dependencias de la aplicación: Instala la herramienta Bandit y las dependencias de tu aplicación para permitir el análisis estático.

Ejecutar escaneo SAST con Bandit: Ejecuta Bandit en el código fuente de tu aplicación (app/). Los resultados se guardan en bandit-report.json. El paso está configurado para no fallar inmediatamente (|| true), permitiendo que el pipeline continúe mientras se genera el reporte.

Subir reporte de Bandit (artifact): El reporte de Bandit se sube como un artefacto de GitHub Actions, el cual puedes descargar desde la interfaz de GitHub para su revisión.

Puedes ver el estado de tus pipelines y los logs detallados en la pestaña "Actions" de tu repositorio de GitHub.

🤝 Contribución
Si deseas contribuir a este proyecto, por favor, sigue estos pasos:

Haz un "fork" de este repositorio.

Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).

Realiza tus cambios y asegúrate de que pasen los tests y los escaneos de seguridad.

Haz "commit" de tus cambios (git commit -m 'feat: Añade nueva funcionalidad').

Sube tu rama (git push origin feature/nueva-funcionalidad).

Abre un "Pull Request" a la rama main.

📄 Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
