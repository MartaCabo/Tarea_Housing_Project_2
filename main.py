"""
Este script orquesta todo el flujo del proceso:
1.- Carga los datos
2.- Selecciona variables relevantes
3.- Entrena modelo
4.- Genera predicciones y guarda resultados
"""

import logging
import argparse
from src.data_processing import cargar_datos, seleccionar_variables
from src.modelo_RF import entrenar_modelo
from src.predicciones import predecir_precio

# Configuración de logs
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def main(archivo_train, archivo_test, archivo_salida):
    """
    Orquesta todo el flujo del proceso:
    1. Carga los datos de entrenamiento.
    2. Selecciona variables relevantes.
    3. Separar características y variable objetivo
    4. Entrena modelo.
    5. Carga datos de prueba y genera predicciones.
    6. Guarda las predicciones con las variables seleccionadas.

    :param archivo_train: Ruta del archivo CSV con los datos de entrenamiento.
    :param archivo_test: Ruta del archivo CSV con los datos para predecir.
    :param archivo_salida: Ruta del archivo CSV donde se guardarán las predicciones.
    """
    try:
        # Paso 1: Cargar datos de entrenamiento
        logging.info("Cargando datos de entrenamiento...")
        datos_train = cargar_datos(archivo_train)
        # Verificar si se cargaron datos correctamente
        if datos_train is None or datos_train.empty:
            raise ValueError(
                "El archivo de entrenamiento no se cargó correctamente o está vacío."
            )

        # Paso 2: Seleccionar variables
        logging.info("Seleccionando variables...")
        datos_seleccionados = seleccionar_variables(datos_train)
        # Verificar que seleccionar_variables devolvió datos
        if datos_seleccionados is None or datos_seleccionados.empty:
            raise ValueError(
                "La selección de variables falló.",
                "Verifique que las variables sean correctas.",
            )

        # Paso 3: Separar características y variable objetivo
        if "SalePrice" not in datos_train.columns:
            raise ValueError(
                "El dataset de entrenamiento debe contener la variable objetivo 'SalePrice'."
            )

        y = datos_train["SalePrice"]  # Tomamos SalePrice antes de filtrar variables
        X = datos_seleccionados  # datos_seleccionados ya contiene las variables correctas

        # Paso 4: Entrenar modelo
        logging.info("Entrenando modelo de Random Forest...")
        entrenar_modelo(X, y)

        # Paso 5: Cargar datos de prueba y hacer predicciones
        logging.info("Cargando datos de prueba y generando predicciones...")
        predecir_precio(archivo_test, archivo_salida)

        logging.info('Proceso completado. Predicciones guardadas en %s',archivo_salida)

    except Exception as e:
        logging.error('Error en la ejecución del script: %s',e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Pipeline de predicción de precios de casas con Random Forest."
    )
    parser.add_argument("archivo_train", help="Ruta del archivo CSV de entrenamiento.")
    parser.add_argument(
        "archivo_test", help="Ruta del archivo CSV con los datos a predecir."
    )
    parser.add_argument(
        "archivo_salida",
        help="Ruta del archivo CSV donde se guardarán las predicciones.",
    )

    args = parser.parse_args()
    main(args.archivo_train, args.archivo_test, args.archivo_salida)
