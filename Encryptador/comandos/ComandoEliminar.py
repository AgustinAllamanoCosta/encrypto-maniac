import logging
from Encryptador.comandos.Comando import Comando

class ComandoEliminar(Comando):
	
	def ejecutar(self,parametros):
		super().validarParametros(parametros)
		logging.info('Ejecutando el comando eliminar')
		self.encriptoManiac.eliminarClave(parametros[0])
		return 0