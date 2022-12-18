import logging
from Encryptador.comandos.Comando import Comando

class ComandoListar(Comando):

	def ejecutar(self, parametros = []):
		logging.info('Ejecutando el comando listar')
		self.mensajeComando = self.encriptoManiac.listarCuentas()
		return 0