import unittest
from dni import DNI

class test_dni(unittest.TestCase):
    def test_dni_creado(self):
        testing = DNI("123456789")
        self.assertIsInstance(testing, DNI)
    
    def test_comprobar_dni(self):
        value = DNI("123456789")
        self.assertTrue(value.comprobar_dni())
        value2 = DNI("783.d90")
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
        value3 = DNI("4569227N9")
        self.assertFalse(value3.longitud_dni())
            

