import logging
from Encryptador.terminal.exceptions.InterrumpirConsolaException import InterrumpirConsolaException
from Encryptador.terminal.comandos.Comando import Comando


class ComandoExit(Comando):

	def ejecutar(self, parametros = []):
		logging.info('Ejecutando el comando exit')
		raise InterrumpirConsolaException('Saliendo del al terminal')