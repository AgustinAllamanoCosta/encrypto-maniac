import logging
from Encryptador.exceptions.ManiacException import ManiacException
from Util.ConstantesEncryptoManiac import ConstanteConsola

class ComandoNoEncontradoException(ManiacException):
	
	def __init__(self, mensaje: str) -> None:
		super().__init__(mensaje)
		logging.debug('Comando no encontrado ')
		self.mensaje = f'{self.mensaje} {ConstanteConsola.mensajeComandosAvanzados}'