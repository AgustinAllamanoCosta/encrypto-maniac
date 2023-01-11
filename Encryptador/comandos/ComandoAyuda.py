import logging
from Encryptador.comandos.Comando import Comando
from Util.ConstantesEncryptoManiac import ConstanteConsola


class ComandoAyuda(Comando):

	def __init__(self):
		self.mensajeComando = ""
		self.mensajeAyuda = {
		'listar': ConstanteConsola.mensajeAyudaComandoListar,
		'agregar':ConstanteConsola.mensajeAyudaComandoAgregar,
		'exit':ConstanteConsola.mensajeAyudaComandoExit,
		'mostrar':ConstanteConsola.mensajeAyudaComandoMostrar,
		'vermas':ConstanteConsola.mensajeAyudaComandoVerMas,
		'eliminar':ConstanteConsola.mensajeAyudaComandoEliminar,
		'modificar':ConstanteConsola.mensajeAyudaComandoModificar
		}

	def ejecutar(self,parametros) -> int:
		super().validarParametros(parametros)
		logging.info('Ejecutando el comando ayuda')
		self.mensajeComando = self.mensajeAyuda[parametros[0]]
		return 0