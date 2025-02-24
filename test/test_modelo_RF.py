"""_summary_
Módulo de test para el modelo Random Forest.
Este módulo ejecuta pruebas unitarias para las funciones del módulo de modelo Random Forest.
"""

import unittest
import pandas as pd
import os
import joblib
from src.modelo_RF import entrenar_modelo

class TestModeloRandomForest(unittest.TestCase):
    def setUp(self):
        """_summary_
        Configuración inicial para las pruebas. Crea un DataFrame de prueba y lo guarda en un archivo CSV
        """
        # Crear un DataFrame de prueba con variables seleccionadas y SalePrice
        data = {
            "MSZoning": ["RL", "RM", "C"],
            "LotArea": [8450, 9600, 11250],
            "Neighborhood": ["CollgCr", "Veenker", "Crawfor"],
            "BldgType": ["1Fam", "1Fam", "1Fam"],
            "YearBuilt": [2003, 1976, 2001],
            "GarageCars": [2, 2, 3],
            "SalePrice": [200000, 185000, 250000]
        }
        self.df = pd.DataFrame(data)

    def test_entrenar_modelo(self):
        """_summary_
        Prueba la función de entrenamiento del modelo Random Forest. 
        Verifica que el modelo se ha guardado correctamente
        """
        X = self.df.drop(columns=["SalePrice"])
        y = self.df["SalePrice"]

        entrenar_modelo(X, y)  # Entrenar modelo

        # Verificar que el archivo del modelo se ha guardado
        self.assertTrue(os.path.exists("random_forest_model.pkl"))

        # Verificar que el modelo se puede cargar correctamente
        model = joblib.load("random_forest_model.pkl")
        self.assertIsNotNone(model)
