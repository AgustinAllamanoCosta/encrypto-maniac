import logging
from Encryptador.exceptions.InterrumpirConsolaException import InterrumpirConsolaException
from Encryptador.comandos.Comando import Comando


class ComandoExit(Comando):

	def ejecutar(self, parametros = []):
		logging.info('Ejecutando el comando exit')
		raise InterrumpirConsolaException('Saliendo del al terminal')