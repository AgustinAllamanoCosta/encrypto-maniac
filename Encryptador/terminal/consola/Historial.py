import logging

class HistorialConsola(object):
	
	def __init__(self):
		logging.info('Iniciando historial')
		self.entradas = []

	def agregarEntrada(self,entrada):
		self.entradas.append(entrada)

	def obtener(self):
		return self.entradas