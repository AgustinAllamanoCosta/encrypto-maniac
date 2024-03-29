import logging
from Encryptador.comandos.ComandoSensible import ComandoSensibles
from Encryptador.consola.EstadoDeSesion import EstadoDeSesion

class ComandoListar(ComandoSensibles):

	def ejecutar(self, parametros: list = []):
		logging.info('Ejecutando el comando listar')
		self.mensajeComando = self.encriptoManiac.listarCuentas(self.obtenerCredenciales())
		return self.encriptoManiac.obtenerSesion()