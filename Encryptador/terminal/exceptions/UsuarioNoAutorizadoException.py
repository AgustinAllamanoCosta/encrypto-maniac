import logging
from Encryptador.terminal.exceptions.ManiacException import ManiacException

class UsuarioNoAutorizadoException(ManiacException):
	
	def __init__(self, mensaje: str) -> None:
		super().__init__(mensaje)
		self.mensaje = 'Usuario no Autorisado para hacer esta accion, porfavor registrese o ingrese antes de continuar'
		logging.debug('Usuario no Autorisado para hacer esta accion')
			