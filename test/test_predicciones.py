"""
    Módulo de test para las predicciones.
    Este módulo ejecuta pruebas unitarias para las funciones del módulo de predicciones.
"""
import unittest
import pandas as pd
import os
from src.predicciones import predecir_precio
import joblib

class TestPredicciones(unittest.TestCase):

    def setUp(self):
        """Configura los datos de prueba antes de cada test"""
        # Crear un DataFrame de prueba con las variables necesarias
        self.test_data = pd.DataFrame({
            "MSZoning": ["RL", "RM"],
            "LotArea": [8500, 9600],
            "Neighborhood": ["CollgCr", "Veenker"],
            "BldgType": ["1Fam", "1Fam"],
            "YearBuilt": [2003, 1976],
            "GarageCars": [2, 2]
        })

        self.test_input_file = "test/test_nuevos_datos.csv"
        self.test_output_file = "test/test_predicciones.csv"

        # Guardar el archivo CSV de prueba
        self.test_data.to_csv(self.test_input_file, index=False)

        # Crear un modelo de prueba si no existe
        if not os.path.exists("random_forest_model.pkl"):
            dummy_model = joblib.dump(
                joblib.load("random_forest_model.pkl"), "random_forest_model.pkl"
            )

    def tearDown(self):
        """Limpia los archivos generados después de cada test"""
        if os.path.exists(self.test_input_file):
            os.remove(self.test_input_file)
        if os.path.exists(self.test_output_file):
            os.remove(self.test_output_file)

    def test_predecir_precio(self):
        """Prueba que el archivo de predicciones se genera correctamente"""
        predecir_precio(self.test_input_file, self.test_output_file)
        
        # Verificar que el archivo de salida existe
        self.assertTrue(os.path.exists(self.test_output_file))

        # Cargar los resultados y verificar estructura
        resultados = pd.read_csv(self.test_output_file)
        self.assertIn("SalePrice_Predicho", resultados.columns)
        self.assertEqual(len(resultados), len(self.test_data))  # Debe coincidir el número de filas

