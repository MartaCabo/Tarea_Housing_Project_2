"""
Módulo para entrenar un modelo de Random Forest para predecir SalePrice.
El módulo contiene una función entrenar_modelo que entrena un modelo 
Random Forest y lo guarda en un archivo.
"""

import logging
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error


# Configuración del log
logging.basicConfig(
    filename="model_training.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def entrenar_modelo(X, y):
    """
    Entrena un modelo de Random Forest para predecir SalePrice.

    :param X: DataFrame con las variables seleccionadas (sin la variable objetivo).
    :param y: Serie o DataFrame con la variable objetivo 'SalePrice'.
    :return: None
    """
    try:
        # Verificar que X y y no estén vacíos
        if X.empty or y.empty:
            raise ValueError("Los datos de entrada (X, y) no pueden estar vacíos.")

        print("Variables seleccionadas antes de codificación: ", X.columns)

        # Codificar variables categóricas
        X = pd.get_dummies(X, drop_first=True)

        # Dividir en entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # Entrenar modelo
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Evaluar modelo
        y_pred = model.predict(X_test)
        error = mean_absolute_percentage_error(y_test, y_pred)
        logging.info('Error Absoluto Medio Porcentual (MAPE):%s', error)
        print(f"Error Absoluto Medio Porcentual (MAPE): {error}")

        # Guardar modelo
        joblib.dump(model, "random_forest_model.pkl")
        logging.info("Modelo guardado como 'random_forest_model.pkl'")
        print("Modelo guardado como 'random_forest_model.pkl'")

    except Exception as e:
        logging.error('Error en el entrenamiento del modelo: %s', e)
        print(f"Error en el entrenamiento: {e}")
