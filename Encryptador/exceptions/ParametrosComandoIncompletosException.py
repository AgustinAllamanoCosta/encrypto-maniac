import logging
from Encryptador.exceptions.ManiacException import ManiacException

class ParametrosComandoIncompletosException(ManiacException):
	def __init__(self, mensaje):
		self.mensaje = mensaje
		logging.debug(f'Paramentros incompletos {mensaje}')
		super().__init__(mensaje)