from Encryptador.comandos.Comando import Comando
from Util.ConstantesEncryptoManiac import ConstanteConsola

class ComandoEscribirCabeceraDeConsola(Comando):

	def escribirEnConsolaStrategy(self,historial):
		print(ConstanteConsola.mensajeBienvenida)
		print(ConstanteConsola.mensajeComandosBasicos)
		historial.agregarEntrada(ConstanteConsola.mensajeBienvenida)
		historial.agregarEntrada(ConstanteConsola.mensajeComandosBasicos)