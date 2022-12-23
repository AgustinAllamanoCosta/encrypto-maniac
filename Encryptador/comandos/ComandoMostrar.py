from Encryptador.comandos.Comando import Comando
from Util.Portapapeles import PortaPapeles
import logging

class ComandoMostrar(Comando):

	def __init__(self, encryptador):
		super().__init__(encryptador)
		self.portapapelesUtil = PortaPapeles()

	def ejecutar(self,parametros):
		logging.info('Ejecutando el comando mostrar')
		super().validarParametros(parametros)
		contraseniaLimpia = self.encriptoManiac.buscarClave(parametros[0])
		self.portapapelesUtil.copiarPortaPapeles(contraseniaLimpia)
		self.mensajeComando = 'Se copia la calve al portapapeles :D la puedes pegar con ctrl + v'
		return 0
