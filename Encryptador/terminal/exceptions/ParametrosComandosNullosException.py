import logging
from Encryptador.terminal.exceptions.ManiacException import ManiacException
from Util.ConstantesEncryptoManiac import ConstanteConsola

class ParametrosComandosNullosException(ManiacException):

	def __init__(self, mensaje: str) -> None:
		super().__init__(ConstanteConsola.mensajeErrorComandoParametros)
		logging.debug(f'Error en los parametros del comando {mensaje}')