from Encryptador.terminal.exceptions.ManiacException import ManiacException
from Util.ConstantesEncryptoManiac import ConstanteConsola

class NoExisteUsuarioEnLaBaseException(ManiacException):
	def __init__(self):
		self.mensaje = ConstanteConsola.mensajeUsuarioInexsistente
		super().__init__(self.mensaje)