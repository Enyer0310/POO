class Persona:
	def __init__(self, nombre, apellido, edad,*valores,**terminos):
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad
		self.valores = valores
		self.terminos = terminos

	def mostrar_detalle(self):
		print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')

persona1 = Persona('Enyer','perez', 22, '954818809',2,3,4,p='platano')
persona1.mostrar_detalle()

persona2 = Persona('Karina', 'Aburto', 40)
persona2.mostrar_detalle()
