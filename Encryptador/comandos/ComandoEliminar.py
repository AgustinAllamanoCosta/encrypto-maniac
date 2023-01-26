import logging
from Encryptador.comandos.ComandoSensible import ComandoSensibles
from Encryptador.consola import EstadoDeSesion

class ComandoEliminar(ComandoSensibles):
	
	def ejecutar(self,sesion: EstadoDeSesion,parametros: list = []) -> EstadoDeSesion:
		super().validarParametros(parametros)
		logging.info('Ejecutando el comando eliminar')
		self.encriptoManiac.eliminarClave(parametros[0],self.obtenerCredenciales(sesion))