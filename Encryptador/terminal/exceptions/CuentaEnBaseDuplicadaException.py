import logging
from Encryptador.exceptions.ManiacException import ManiacException
from Util.ConstantesEncryptoManiac import ConstanteConsola

class CuentaEnBaseDuplicadaException(ManiacException):
	def __init__(self, nombreCuenta):
		self.mensaje = ConstanteConsola.mensajeErrprComandoDuplicado + nombreCuenta
		super().__init__(self.mensaje)
		logging.debug(f'Cuenta en base duplicada {self.mensaje}')