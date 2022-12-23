import logging
from Encryptador.exceptions.ManiacException import ManiacException

class LoginErrorException(ManiacException):

	def __init__(self, mensaje: str) -> None:
		super().__init__(mensaje)
		self.mensaje = 'Usuario o contrasena incorrectos'
		logging.debug('Usuario o contrasena incorrectos')
			