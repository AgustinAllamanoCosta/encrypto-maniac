import logging
from Encryptador.comandos.ComandoSensible import ComandoSensibles
from Encryptador.exceptions.CuentaEnBaseDuplicadaException import CuentaEnBaseDuplicadaException
from Encryptador.exceptions.ParametrosComandoIncompletosException import ParametrosComandoIncompletosException
from Util.ConstantesEncryptoManiac import ConstanteConsola

class ComandoAgregar(ComandoSensibles):

	def ejecutar(self,parametros):
		logging.info('Se ejecuta comando agregar.')
		if(len(parametros)==0):
			logging.debug('Parametros insuficiente para el comando agregar.')
			raise ParametrosComandoIncompletosException(ConstanteConsola.mensajeAyudaComandoAgregar)
		else:
			if(self.encriptoManiac.existeCuentaEnBase(parametros[0]) != True):
				self.encriptoManiac.ingresarClave(parametros[0],self.obtenerContraseña())
			else:
				logging.debug('La cuenta esta duplicada')
				raise CuentaEnBaseDuplicadaException(parametros[0])
		self.mensajeComando = "Se agrego la contraseña"
		return 0