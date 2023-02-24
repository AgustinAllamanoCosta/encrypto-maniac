import logging
from Encryptador.terminal.exceptions.ManiacException import ManiacException

class NoUsuarioRegistradosException(ManiacException):

	def __init__(self) -> None:
		self.mensaje = 'No exiten usuarios registradoss'
		super().__init__(self.mensaje)
		logging.debug(self.mensaje)
			