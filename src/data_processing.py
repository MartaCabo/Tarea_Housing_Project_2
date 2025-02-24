"""
    Módulo que lee los datos de entrenamiento, 
    y selecciona las variables de interés para el modelo de machine learning. 
    El módulo contiene dos funciones: cargar_datos y seleccionar_variables.
"""

import logging
import pandas as pd

# Configuración del log
logging.basicConfig(
    filename="log_file.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def cargar_datos(archivo):
    """
    Carga un archivo CSV en un DataFrame de pandas.
    :param archivo: Ruta del archivo CSV.
    :return: DataFrame con los datos cargados.
    """
    try:
        data = pd.read_csv(f"./data/{archivo}")
        logging.info("Datos cargados correctamente desde %s", archivo)
        print("Datos cargados correctamente.")
        return data
    except Exception as e:
        logging.error("Error al cargar el archivo: %s", e)
        print(f"Error al cargar el archivo: {e}")
        return None


def seleccionar_variables(data):
    """
    Selecciona variables específicas del DataFrame.
    :param data: DataFrame original.
    :return: Nuevo DataFrame con las variables seleccionadas.
    """
    columnas = [
        "MSZoning",
        "LotArea",
        "Neighborhood",
        "BldgType",
        "YearBuilt",
        "GarageCars",
    ]
    try:
        data_seleccionado = data[columnas].copy()
        logging.info("Variables seleccionadas correctamente.")
        print("Variables seleccionadas correctamente.")
        return data_seleccionado
    except KeyError as e:
        logging.error("Error: Alguna columna no se encuentra en los datos - %s", e)
        print(f"Error: Alguna columna no se encuentra en los datos - {e}")
        return None
