import unittest
from app import calcular_promedio, evaluar_estudiante

class TestSistemaAcademico(unittest.TestCase):
    def test_calcular_promedio(self):
        self.assertEqual(calcular_promedio(10, 10, 10), 10)
    
    def test_evaluar_estudiante(self):
        self.assertEqual(evaluar_estudiante(15), "Aprobado")
        self.assertEqual(evaluar_estudiante(10), "Desaprobado")

        self.assertEqual(evaluar_estudiante(12), "Aprobado")

if __name__ == '__main__':
    unittest.main()