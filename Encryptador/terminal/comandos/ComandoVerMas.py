from Encryptador.comandos.Comando import Comando
from Util.ConstantesEncryptoManiac import ConstanteConsola

class ComandoVerMas(Comando):

	def __init__(self):
		pass

	def ejecutar(self,parametros = []) -> int:
		self.mensajeComando = ConstanteConsola.mensajeComandosAvanzados
		return 0