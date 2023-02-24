import logging
from Encryptador.terminal.comandos.ComandoSensible import ComandoSensibles
from Encryptador.terminal.consola import EstadoDeSesion
from Encryptador.terminal.exceptions.CuentaEnBaseDuplicadaException import CuentaEnBaseDuplicadaException
from Encryptador.terminal.exceptions.ParametrosComandoIncompletosException import ParametrosComandoIncompletosException
from Util.ConstantesEncryptoManiac import ConstanteConsola

class ComandoAgregar(ComandoSensibles):

	def ejecutar(self,token,parametros) -> EstadoDeSesion:
		logging.info('Se ejecuta comando agregar.')
		if(len(parametros)==0):
			logging.debug('Parametros insuficiente para el comando agregar.')
			raise ParametrosComandoIncompletosException(ConstanteConsola.mensajeAyudaComandoAgregar)
		else:
			self.encriptoManiac.ingresarClave(parametros[0],self.obtenerContraseña(),self.obtenerCredenciales(token))
		self.mensajeComando = "Se agrego la contraseña"