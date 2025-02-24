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

En base a estas carácterísticas, el modelo predice el precio de un grupo de viviendas y guarda dichas predicciones un archivo `*.csv`.


```{toctree}
:maxdepth: 2
:caption: Contenido:

estructura
info_dockerfile
modules


