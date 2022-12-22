import logging
from Encryptador.exceptions.ParametrosComandoIncompletosException import ParametrosComandoIncompletosException
from Encryptador.comandos.ComandoSensible import ComandoSensibles
from Util.ConstantesEncryptoManiac import ConstanteConsola

class ComandoModificar(ComandoSensibles):

	def ejecutar(self,parametros):
		super().validarParametros(parametros)
		logging.info('Ejecutando el comando modificar')
		if(len(parametros)==0):
			raise ParametrosComandoIncompletosException(ConstanteConsola.mensajeAyudaComandoModificar)
		else:
			self.encriptoManiac.actualizarClave(parametros[0],self.obtenerContraseña())
		self.mensajeComando = "Se modifico la contraseña de la cuenta "+parametros[0]
		return 0