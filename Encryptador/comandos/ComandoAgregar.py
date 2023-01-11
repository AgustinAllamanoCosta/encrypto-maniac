import logging
from Encryptador.comandos.ComandoSensible import ComandoSensibles
from Encryptador.consola import EstadoDeSesion
from Encryptador.exceptions.CuentaEnBaseDuplicadaException import CuentaEnBaseDuplicadaException
from Encryptador.exceptions.ParametrosComandoIncompletosException import ParametrosComandoIncompletosException
from Util.ConstantesEncryptoManiac import ConstanteConsola

class ComandoAgregar(ComandoSensibles):

	def ejecutar(self,parametros) -> EstadoDeSesion:
		logging.info('Se ejecuta comando agregar.')
		if(len(parametros)==0):
			logging.debug('Parametros insuficiente para el comando agregar.')
			raise ParametrosComandoIncompletosException(ConstanteConsola.mensajeAyudaComandoAgregar)
		else:
			self.encriptoManiac.ingresarClave(parametros[0],self.obtenerContraseña(),self.obtenerCredenciales())
		self.mensajeComando = "Se agrego la contraseña"
		return self.encriptoManiac.obtenerSesion()