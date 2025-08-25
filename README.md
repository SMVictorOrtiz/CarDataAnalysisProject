# CarDataAnalysisProject

Aplicación web interactiva para el análisis de datos de anuncios de venta de automóviles en EE.UU.  
El proyecto permite explorar, visualizar y comprender las características principales de un dataset de vehículos usados mediante gráficos dinámicos y estadísticas descriptivas.

**Demo en línea:** [Car_Data_Analysis en Render](https://sprint6-dwqy.onrender.com)

---

## Características

- Visualización de datos en una tabla interactiva.  
- Construcción de histogramas personalizados (ejemplo: distribución del odómetro).  
- Gráfico de dispersión **Precio vs Odómetro**, segmentado por tipo de combustible.  
- Estadísticas básicas del dataset (media, desviación estándar, etc.).  
- Interfaz sencilla e intuitiva construida con **Streamlit** y **Plotly**.  

---

## Tecnologías utilizadas

- [Python 3](https://www.python.org/)  
- [Streamlit](https://streamlit.io/) – creación de la interfaz web interactiva  
- [Pandas](https://pandas.pydata.org/) – manejo y análisis de datos  
- [Plotly Express](https://plotly.com/python/plotly-express/) – gráficos interactivos  

---

## Datos

El dataset utilizado corresponde a anuncios de venta de automóviles en EE.UU., almacenado en el archivo: vehicles_us.csv

Incluye información como precio, kilometraje, modelo, año, condición, tipo de transmisión y combustible

---

## Instalación y ejecución

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

1) Clonar el repositorio y entrar a la carpeta:
   git clone https://github.com/SMVictorOrtiz/CarDataAnalysisProject.git
   cd CarDataAnalysisProject

2) (Opcional) Crear y activar un entorno virtual:
   # macOS / Linux
   python3 -m venv .venv
   source .venv/bin/activate

   # Windows (PowerShell)
   python -m venv .venv
   .venv\Scripts\Activate.ps1

3) Instalar dependencias:
   pip install -r requirements.txt

4) Ejecutar la aplicación:
   streamlit run app.py

5) Abrir en el navegador:
   http://localhost:8501/
