"""
Este módulo contiene una función para cargar un modelo
Random Forest y hacer predicciones sobre nuevos datos.
"""

import os
import logging
import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_percentage_error
from src.data_processing import (
    seleccionar_variables,
)  # Asegúrate de importar la función correcta


def predecir_precio(archivo_entrada, archivo_salida="predicciones.csv"):
    """
    Carga un modelo de Random Forest y realiza predicciones sobre nuevos datos.

    :param archivo_entrada: Ruta del archivo CSV con las variables seleccionadas.
    :param archivo_salida: Ruta donde se guardará el CSV con las predicciones.
    :return: None
    """
    try:
        # Verificar si el modelo existe
        modelo_path = "random_forest_model.pkl"
        if not os.path.exists(modelo_path):
            raise FileNotFoundError(
                "El modelo 'random_forest_model.pkl' no existe.",
                "Entrena el modelo primero.",
            )

        # Cargar el modelo
        model = joblib.load(modelo_path)

        # Cargar los datos de entrada
        data = pd.read_csv(f"./data/{archivo_entrada}")

        # Seleccionar solo las variables relevantes
        data_seleccionado = seleccionar_variables(data)

        # Guardar los datos originales sin la columna SalePrice
        data_original = data_seleccionado.copy()

        # Codificar variables categóricas
        data_codificado = pd.get_dummies(data_seleccionado, drop_first=True)

        # Asegurar que las columnas coincidan con las del modelo entrenado
        model_columns = model.feature_names_in_
        data_codificado = data_codificado.reindex(columns=model_columns, fill_value=0)

        # Hacer predicciones
        data_original["SalePrice_Predicho"] = model.predict(data_codificado)

        # Guardar solo las variables seleccionadas, SalePrice_Predicho y MAPE
        columnas_finales = list(seleccionar_variables(data_original).columns) + [
            "SalePrice_Predicho"
        ]
        data_final = data_original[columnas_finales]

        # Guardar las predicciones en un archivo CSV
        data_final.to_csv(archivo_salida, index=False)
        print(f"Predicciones guardadas en {archivo_salida}")
        logging.info("Predicciones guardadas en %s", archivo_salida)

    except Exception as e:
        logging.error("Error en la predicción: %s", e)
        print(f"Error en la predicción: {e}")
