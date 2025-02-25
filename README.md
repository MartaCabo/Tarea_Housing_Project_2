# Documentación de Housing Project 🏠

Bienvenido a la documentación del proyecto  **Housing Prices**.

Este proyecto utiliza un conjunto de datos de precios de viviendas en Ames, Iowa, para predecir el precio de un conjunto de viviendas en función de ciertas características.   

## 🚀 Descripción del Proyecto
Este proyecto utiliza un **Random Forest Regressor** para predecir el precio de las viviendas en Ames, Iowa. 

Toma como variables de entrada las siguientes características de la vivienda: 
- `Neigborhood`: Colonia en la que se encuentra
- `MsZoning`: Zona de la ciudad 
    - A: Agrícola
    - C: Comercial
    - FV: Residencial en aldea flotante
    - I: Industrial
    - RH: Residencial de alta densidad
    - RL: Residencial de baja densidad
    - RP: Residencial de baja densidad en parque
    - RM: Residencial de densidad media
- `LotArea`: Área del terreno
- `BldType`: Tipo de vivienda
    - 1Fam: Casa unifamiliar
    - 2FmCon: Casa de dos familias
    - Duplex: Casa dúplex
    - TwnhsE: Casa adosada de dos niveles
    - TwnhsI: Casa adosada de un nivel
- `YearBuilt`: Año de construcción
- `GarageCars`: Capacidad del garaje en número de coches.

En base a estas características, el modelo predice el precio de un grupo de viviendas y guarda dichas predicciones un archivo `*.csv`.

# 📦 Estructura del Proyecto
```bash
.
├── Dockerfile
├── __pycache__
│   └── main.cpython-39.pyc
├── data
│   ├── data_description.txt
│   ├── test.csv
│   └── train.csv
├── docs
│   ├── Makefile
│   ├── build
│   ├── log_file.log
│   ├── make.bat
│   └── source
├── environment.yml
├── log_file.log
├── main.py
├── predicciones.csv
├── predicciones1.csv
├── random_forest_model.pkl
├── src
│   ├── __init__.py
│   ├── __pycache__
│   ├── data_processing.py
│   ├── modelo_RF.py
│   └── predicciones.py
├── test
│   ├── __init__.py
│   ├── __pycache__
│   ├── test_data_processing.py
│   ├── test_modelo_RF.py
│   └── test_predicciones.py
└── tree

10 directories, 23 files

```


# 🐳 Uso del Dockerfile

Este proyecto incluye un `Dockerfile` para facilitar la ejecución del código en un entorno aislado.

Ejecuta el siguiente comando en la terminal desde la raíz del proyecto:

```bash
docker build -t housing_price .
```

Este comando construirá la imagen de Docker con el nombre `housing_price`.

Para ejecutar el contenedor, utiliza el siguiente comando:

```bash
docker run -it --rm -v  $(pwd):/app housing_price train.csv test.csv prediciones.csv
```
Donde `$(pwd)` es el directorio actual en tu máquina local.

Este comando ejecutará el script `main.py` dentro del contenedor de Docker y guardará las predicciones en un archivo `predicciones.csv`, utilizando los archivos `train.csv` y `test.csv` como entrada. 

Asegúrate de tener dichos archivos en tu máquina locales, ya que no vienen en el repositorio.

