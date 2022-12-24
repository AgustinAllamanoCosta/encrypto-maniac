from Encryptador.comandos.Comando import Comando
import logging, pyperclip

class ComandoMostrar(Comando):

	def ejecutar(self,parametros):
		logging.info('Ejecutando el comando mostrar')
		super().validarParametros(parametros)
		contraseniaLimpia = self.encriptoManiac.buscarClave(parametros[0])
		pyperclip.copy(contraseniaLimpia)
		self.mensajeComando = 'Se copia la calve al portapapeles :D la puedes pegar con ctrl + v'
		return 0
