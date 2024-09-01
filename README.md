# portalinmobiliario
Extracción de propiedades en portal inmobiliario

# portalinmobiliario
Extracción de propiedades en portal inmobiliario

# Proyecto de Extracción y Análisis de Datos del Portal Inmobiliario

Este proyecto está diseñado para extraer, procesar y analizar datos de propiedades disponibles para arriendo en Concepción, Biobío, utilizando Python.

## Estructura del Proyecto

- **`data/`**: Contiene los datos crudos, procesados y otros.
- **`notebo**oks/`: Contiene los notebooks de Jupyter para exploración y análisis.
- **`src/`:** Contiene el código fuente del proyecto.
- **`tests/**`: Contiene pruebas unitarias.
- **`logs/`**: Archivos de logs generados durante la ejecución del proyecto.
- **`report**s/`: Reportes generados del análisis de datos.

## Plano de Proyecto

```
PortalInmobiliario/
│
├── data/
│   ├── raw/                # Datos crudos directamente extraídos del sitio web
│   ├── processed/          # Datos procesados o limpios listos para el análisis
│   ├── interim/            # Datos intermedios, transformaciones que aún no están listas para análisis
│   └── external/           # Datos de fuentes externas, si aplica
│
├── notebooks/              # Notebooks de Jupyter para análisis, EDA (Exploratory Data Analysis), etc.
│   ├── scraping.ipynb      # Notebook para probar y desarrollar el código de scraping
│   ├── cleaning.ipynb      # Notebook para el procesamiento y limpieza de los datos
│   └── analysis.ipynb      # Notebook para el análisis de los datos
│
├── src/                    # Código fuente del proyecto
│   ├── __init__.py         # Archivo para hacer el módulo importable
│   ├── scraping/           # Código relacionado con la extracción de datos
│   │   ├── __init__.py
│   │   └── scraper.py      # Script principal para realizar el scraping
│   ├── data_preparation/   # Código para la limpieza y transformación de datos
│   │   ├── __init__.py
│   │   └── cleaning.py     # Script para limpiar los datos extraídos
│   └── analysis/           # Código para el análisis de los datos
│       ├── __init__.py
│       └── analyze.py      # Script para realizar análisis y generar reportes
│
├── tests/                  # Pruebas unitarias para el código
│   ├── test_scraper.py     # Pruebas para el script de scraping
│   ├── test_cleaning.py    # Pruebas para el script de limpieza de datos
│   └── test_analyze.py     # Pruebas para el script de análisis
│
├── logs/                   # Archivos de log para registrar las actividades y errores
│   └── scraping.log        # Log para registrar los eventos durante el scraping
│
├── reports/                # Reportes generados a partir del análisis de datos
│   └── figures/            # Figuras y gráficos generados durante el análisis
│
├── requirements.txt        # Archivo para listar las dependencias del proyecto
├── README.md               # Documentación básica del proyecto
└── .gitignore              # Archivos y carpetas a ignorar por git
```



## Configuración

1. Clona el repositorio.
2. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
3. Ejecuta los notebooks o scripts según sea necesario.

## Uso

- Ejecuta el script de scraping para extraer datos.
- Limpia y transforma los datos.
- Realiza análisis y genera reportes.
