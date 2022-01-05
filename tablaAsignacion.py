class Tabla:

	# podemos utilizar este ejercicio para sobrecarga de operaciones sobre listas
	def __init__(self):
		self.position = [number for number in range(0, 24)]
		self.tabla = [ 'T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 
					'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E' ]
		self.result = dict(zip(self.position, self.tabla))

	def get_tabla_len(self):
		return len(self.result)

	def get_letras_tabla(self, position):
		try:
			return self.result[position]
		except:
			return "Fuera de rango"

	def calcularLetra(self, DNI):
		# Obtener el numero del dni del string => dni sano
		# Dividirlo por el número de letras (actualmente 23) y obtener el resto (división módulo)
		# Consultar TablaAsignacion con ese resto = posicion
		position = int(DNI) % self.get_tabla_len()
		return self.get_letras_tabla(position)

	def mostrarTabla(self):
		print(self.result)


if __name__ == "__main__":
	tabla = Tabla()
	tabla.mostrarTabla()


	'''import math
	import random

	tabla = TablaAsignacion()

	print(tabla.getLetra(0))
	print(tabla.getLetra(22))
	letrasNoPermitidas = ['I', 'Ñ', 'O', 'U']
	for letra in letrasNoPermitidas:
		print('Letra %c:' % letra, tabla.letraPermitida(letra)) 

	casosTest = [ #casos OK
				"78484464T","72376173A","01817200Q","95882054E","63587725Q",
				"26861694V","21616083Q","26868974Y","40135330P","89044648X",
		        "80117501Z","34168723S","76857238R","66714505S","66499420A"]

	### Añado casos test FAIL ALEATORIOS ###

	numeroCasos = 15

	for i in range(1, numeroCasos + 1):
		caso = ""
		for j in range(1, 9):
			# random.randrange(start, stop[, step])
			# numeroAleatorio = random.randint(0, 9)
			# ASCII 48-57 = 0-9
			# generamos un numero aleatorio entre 48 y 57 
			caracterAscii = random.randrange(48, 57 + 1, 1)
			# convertimos el numero ASCII a caracter. chr() toma el argumento como codigo ASCII de un caracter
			caso = caso + chr(caracterAscii)
		# en la ultima posicion añado una letra NO PERMITIDA ['I', 'Ñ', 'O', 'U']
		caso = caso + letrasNoPermitidas[ random.randrange(0, 3 + 1, 1) ]
		casosTest = casosTest + [caso]

	print(casosTest)

	tabla = TablaAsignacion()

	for dni in casosTest:
		if tabla.calcularLetra( dni[:-1] ) == dni[-1]:
			print("%s %s" %(dni, Colors.OKGREEN + "OK" + Colors.ENDC) )
		else:
			print("%s %s" %(dni, Colors.FAIL + "FAIL" + Colors.ENDC))'''