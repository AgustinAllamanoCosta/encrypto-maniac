import logging
from Util.CustomException import InterrumpirConsola
from Encryptador.comandos.Comando import Comando


class ComandoExit(Comando):

	def ejecutar(self, parametros = []):
		logging.info('Ejecutando el comando exit')
		raise InterrumpirConsola()