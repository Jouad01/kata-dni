import unittest
from tablaAsignacion import Tabla


class TestingTabla(unittest.TestCase):

    def test_tabla_asignacion(self):
        resultado = Tabla()
        self.assertIsInstance(resultado, Tabla)

    def test_get_resultado(self):
        resultado = Tabla()
        self.assertEqual(resultado.get_tabla_len(), 23)

    def test_get_letras_tabla(self):
        resultado = Tabla()
        self.assertTrue(resultado.get_letras_tabla(0), "N")
        self.assertTrue(resultado.get_letras_tabla(1), "J")
        self.assertTrue(resultado.get_letras_tabla(2), "E")

    def test_calcular_dni(self):
        resultado = Tabla()
        self.assertTrue(resultado.calcularLetra(123456789), "F")
        self.assertTrue(resultado.calcularLetra(987654321), "N")
        self.assertTrue(resultado.calcularLetra(45692272), "T")

if __name__ == "__main__":
    unittest.mani()