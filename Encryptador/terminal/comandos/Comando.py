from Encryptador.terminal.servicio.ServicioEncrypto import ServicioEncrypto
from Encryptador.terminal.consola.Historial import HistorialConsola
from Encryptador.terminal.exceptions.ParametrosComandosNullosException import ParametrosComandosNullosException

class Comando(object):

	def __init__(self, servicioEncripto: ServicioEncrypto):
		self.encriptoManiac: ServicioEncrypto = servicioEncripto
		self.mensajeComando: str = ""

	def ejecutar(self,parametros: list = []) -> int:
		return 0

	def validarParametros(self,parametros: list):
		if(parametros == []):
			raise ParametrosComandosNullosException('Parametros Nullos')

	def escribirEnConsolaStrategy(self,historial: HistorialConsola):
		if(self.mensajeComando != None):
			print(self.mensajeComando)
			historial.agregarEntrada(self.mensajeComando)
