class Rectangulo:
	def __init__(self, base, altura):
		self.base = base
		self.altura = altura

	def calcular_area(self):
		return self.base * self.altura

base = int(input('Proporciona la base del rect: '))
altura = int(input('Proporciona la altura del rect: '))

rectangulo1 = Rectangulo(base,altura)
print(f'Área rectangulo: {rectangulo1.calcular_area()}')

base = int(input('Proporciona la base del rect: '))
altura = int(input('Proporciona la altura del rect: '))

rectangulo2 = Rectangulo(base,altura)
print(f'Área rectangulo: {rectangulo2.calcular_area()}')

