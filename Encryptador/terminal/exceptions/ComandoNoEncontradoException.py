import logging
from Encryptador.terminal.exceptions.ManiacException import ManiacException
from Util.ConstantesEncryptoManiac import ConstanteConsola

class ComandoNoEncontradoException(ManiacException):
	
	def __init__(self, mensaje: str, sesionActiva = False) -> None:
		super().__init__(mensaje)
		logging.debug('Comando no encontrado ')
		if(sesionActiva):
			self.mensaje = f'{self.mensaje} {ConstanteConsola.mensajeComandosAvanzados}'
		else:
			self.mensaje = f'{self.mensaje} {ConstanteConsola.mensajeComandosSinAutorizacion}'