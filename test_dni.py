import unittest
from dni import DNI

class test_dni(unittest.TestCase):
    def test_dni_creado(self):
        testing = DNI("123456789")
        self.assertIsInstance(testing, DNI)
    
    def test_comprobar_dni(self):
        value = DNI("123456789")
        self.assertTrue(value.comprobar_dni())
        value2 = DNI("783,d90")
        self.assertFalse(value2.comprobar_dni())
        value3 = DNI("45692272N")
        self.assertTrue(value3.comprobar_dni())
        value4 = DNI("345")
        self.assertFalse(value4.comprobar_dni())
    
    def test_longitud_dni(self):
        value = DNI("18219212912")
        self.assertFalse(value.longitud_dni())
        value2 = DNI("123456789")
        self.assertTrue(value2.longitud_dni())
    
    def test_ultimo_digito(self):
        value = DNI("45692272N")
        self.assertTrue(value.ultimo_digito())
        value2 = DNI("45692272NN")
        self.assertFalse(value2.ultimo_digito())
        value3 = DNI("4569,e2N9")
        self.assertFalse(value3.ultimo_digito())

    def test_get_dni_numerico(self):
        value = DNI("45692272N")
        self.assertEqual(value.get_dni_numerico(), "45692272")
        value2 = DNI("45692272N")
        self.assertNotEqual(value2.get_dni_numerico(), "45692272N")
    
    def test_get_letras_dni(self):
        value = DNI("45692272N")
        self.assertEqual(value.get_letras_dni(), "N")
    
    def test_calcular_dni(self):
        value = DNI("45692272N")
        value.set_numero_valido(True)
        self.assertTrue(value.get_letras_tabla())
        self.assertEqual(value.get_letras_tabla(), "N")
        self.assertNotEqual(value.get_letras_tabla(), "U")
        value2 = DNI("45692272D")
        value2.set_numero_valido(True)
        self.assertTrue(value2.get_letras_tabla())
        self.assertEqual(value2.get_letras_tabla(), "N")

    def test_validar_letra_dni(self):
        value = DNI("45692272N")
        value2 = DNI("456922722")
        value.set_numero_valido(True)
        self.assertTrue(value.validar_letra_dni())
        self.assertFalse(value2.validar_letra_dni())

    def test_comprobar_letra(self):
        value = DNI("45692272N")
        value.set_numero_valido(True)
        self.assertTrue(value.comprobar_letra())
    
    def test_comprobar_cif(self):
        value = DNI("45692272N")
        value.set_numero_valido(True)
        value.set_numero_contrario(False)
        self.assertTrue(value.comprobar_cif())
    
if __name__ == "__main__":
    unittest.main()
