"""
Módulo de test para el módulo de procesamiento de datos.
Este módulo ejecuta pruebas unitarias para las funciones del módulo de procesamiento de datos.
"""
import unittest
import pandas as pd
import os
from src.data_processing import cargar_datos, seleccionar_variables

class TestProcesamientoDatos(unittest.TestCase):
    def setUp(self):
        """
        Configuración inicial para las pruebas. Crea un DataFrame de prueba y lo guarda en un archivo CSV
        """
        # Crear un DataFrame de prueba
        data = {
            "MSZoning": ["RL", "RM", "C"],
            "LotArea": [8450, 9600, 11250],
            "Neighborhood": ["CollgCr", "Veenker", "Crawfor"],
            "BldgType": ["1Fam", "1Fam", "1Fam"],
            "YearBuilt": [2003, 1976, 2001],
            "GarageCars": [2, 2, 3]
        }
        #Convierte data en un DataFrame de pandas
        self.df = pd.DataFrame(data)
        # Crea un archivo CSV de prueba
        self.test_file = "test/test_data.csv"
        # Guarda el DataFrame en el archivo CSV
        self.df.to_csv(self.test_file, index=False)

    def tearDown(self):
        """
        Limpieza después de las pruebas. Elimina el archivo CSV de prueba
        """
        # Eliminar archivos generados durante el test
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists("test/test_file.csv"):
            os.remove("test/test_file.csv")
    
    def test_cargar_datos(self):
        """
        Prueba la función cargar_datos del módulo de procesamiento de datos
        """
        data = cargar_datos(self.test_file)
        self.assertIsNotNone(data)
        self.assertEqual(len(data), 3)
        self.assertEqual(list(data.columns), list(self.df.columns))
    
    def test_seleccionar_variables(self):
        """
        Prueba la función seleccionar_variables del módulo de procesamiento de datos
        """
        data = cargar_datos(self.test_file)
        data_seleccionado = seleccionar_variables(data)
        self.assertIsNotNone(data_seleccionado)
        self.assertEqual(list(data_seleccionado.columns), ["MSZoning", "LotArea", "Neighborhood", "BldgType", "YearBuilt", "GarageCars"])

