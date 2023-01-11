from Encryptador.comandos.ComandoSensible import ComandoSensibles
import logging, pyperclip

from Encryptador.consola import EstadoDeSesion

class ComandoMostrar(ComandoSensibles):

	def ejecutar(self,parametros: list = []) -> EstadoDeSesion:
		logging.info('Ejecutando el comando mostrar')
		super().validarParametros(parametros)
		contraseniaLimpia = self.encriptoManiac.buscarClave(parametros[0],self.obtenerCredenciales())
		pyperclip.copy(contraseniaLimpia)
		self.mensajeComando = 'Se copia la calve al portapapeles :D la puedes pegar con ctrl + v'
		return self.encriptoManiac.obtenerSesion()
