class Cubo:
	def __init__(self,alto,ancho,profundo):
		self.alto = alto
		self.ancho = ancho
		self.profundo = profundo

	def calcular_volumen(self):
		return self.ancho * self.alto * self.profundo

ancho = int(input('Proporcione el ancho: '))
alto = int(input('Proporcione el alto: '))
profundo = int(input('Proporciona lo profundo: '))

cubo1 = Cubo(ancho,alto,profundo)
print(f'Volumen cubo: {cubo1.calcular_volumen()}')
