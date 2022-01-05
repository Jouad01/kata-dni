from string import ascii_uppercase
from random import randint, choice, randrange
from tablaAsignacion import Tabla

class DNI:
    def __init__(self, numero = ""):
        self.dni = numero
        self.numero_valido = False
        self.numero_contrario = False
        self.resultado = Tabla()
    
    def set_dni(self, numero):
        self.dni = numero
    
    def get_dni(self):
        return self.dni
    
    def set_numero_valido(self, estado):
        self.numero_valido = estado
    
    def get_numero_valido(self):
        return self.numero_valido
    
    def set_numero_contrario(self, estado):
        self.numero_contrario = estado
    
    def get_numero_contrario(self):
        return self.numero_contrario
    
    def comprobar_dni(self):
        self.set_numero_valido(self.longitud_dni() and self.ultimo_digito())
        return self.get_numero_valido()

    def longitud_dni(self):
        return len(self.dni) == 9

    def ultimo_digito(self):
        return self.dni[:-1].isdigit()
    
    def comprobar_letra(self):
        if self.get_numero_valido():
            self.set_numero_contrario(
                self.get_letras_dni().isupper()
                and not self.get_letras_dni().isdigit()
                and self.validar_letra_dni())
        
            return self.get_numero_contrario()

        else:
            return False

    def get_letras_dni(self):
        return self.dni[-1]
    
    def get_dni_numerico(self):
        return self.dni[:-1]
    
    def get_letras_tabla(self):
        if self.get_numero_valido():
            return self.resultado.calcularLetra(self.get_dni_numerico())
        else:
            return False

    def validar_letra_dni(self):
        return (self.get_numero_valido() and self.get_letras_dni() == self.get_letras_tabla())
    
    def comprobar_cif(self):
        return self.comprobar_dni and self.comprobar_letra()