from Encryptador.comandos.Comando import Comando
from Util.UIManiac import PopUpManiac
import logging

class ComandoMostrar(Comando):
	
	def __init__(self,encripto):
		super().__init__(encripto)
		self.popUp = PopUpManiac(True,4000)

	def ejecutar(self,parametros):
		logging.info('Ejecutando el comando mostrar')
		super().validarParametros(parametros)
		self.mensajeComando = self.encriptoManiac.buscarClave(parametros[0])
		self.popUp.setMensaje(self.mensajeComando)
		return 0

	def escribirEnConsolaStrategy(self,historial):
		try:
			self.popUp.mostrarPopUp()
		except:
			pass