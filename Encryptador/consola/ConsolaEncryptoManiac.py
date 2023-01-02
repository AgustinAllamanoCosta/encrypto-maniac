from Encryptador.comandos.ComandoMostrar import ComandoMostrar
from Encryptador.comandos.ComandoAyuda import ComandoAyuda
from Encryptador.comandos.ComandoExit import ComandoExit
from Encryptador.comandos.ComandoLogin import ComandoLogin
from Encryptador.comandos.ComandoRegistrar import ComandoRegistrar
from Encryptador.comandos.ComandoSensible import ComandoSensibles
from Encryptador.comandos.ComandoVerMas import ComandoVerMas
from Encryptador.comandos.ComandoEscribirCabeceraDeConsola import ComandoEscribirCabeceraDeConsola
from Encryptador.comandos.ComandoEliminar import ComandoEliminar
from Encryptador.comandos.ComandoModificar import ComandoModificar
from Encryptador.comandos.ComandoAgregar import ComandoAgregar
from Encryptador.comandos.ComandoListar import ComandoListar
from Encryptador.comandos.Comando import Comando
from Encryptador.configuracion.Configuracion import Configuracion
from Encryptador.consola.EstadoDeSesion import EstadoDeSesion
from Encryptador.consola.Historial import HistorialConsola
from Encryptador.exceptions.InterrumpirConsolaException import InterrumpirConsolaException
from Encryptador.exceptions.ComandoNoEncontradoException import ComandoNoEncontradoException
from Encryptador.exceptions.ManiacException import ManiacException
from Encryptador.servicio.ServicioEncrypto import ServicioEncrypto
from Util.ConstantesEncryptoManiac import ConstanteConsola
import logging
import re

class ConsolaEncryptoManiac():

	def __init__(self, historalParam: HistorialConsola, servicioEncripto: ServicioEncrypto):
		logging.info('Iniciando consola')
		self.historial: HistorialConsola = historalParam
		self.sesion: EstadoDeSesion = servicioEncripto.obtenerSesion()
		self.patronConsola = re.compile('\S+')
		self.correrConsola = True
		self.prompt = "EM>>"

		self.comandosEstandar: dict[str,Comando] = {
			'listar': ComandoListar(servicioEncripto),
			'agregar': ComandoAgregar(servicioEncripto),
			'modificar': ComandoModificar(servicioEncripto),
			'eliminar': ComandoEliminar(servicioEncripto),
			'mostrar': ComandoMostrar(servicioEncripto),
			'cabecera': ComandoEscribirCabeceraDeConsola(servicioEncripto),
			'vermas': ComandoVerMas(),
			'ayuda': ComandoAyuda(),
		}

		self.comandosSinSession: dict[str,Comando] = {
			'login': ComandoLogin(servicioEncripto),
			'registrar' : ComandoRegistrar(servicioEncripto),
			'exit': ComandoExit(servicioEncripto),
		}

	def analizarEntrada(self,entrada):
		valoresEntrada: list[str] = self.patronConsola.findall(entrada)
		try:
			self.historial.agregarEntrada(entrada)

			comando: Comando = self.obtenerComando(valoresEntrada[0].lower())
			if(isinstance(comando,ComandoSensibles)):
				self.sesion = comando.ejecutar(valoresEntrada[1:], self.sesion)
			else:
				comando.ejecutar(valoresEntrada[1:])

			if(Configuracion.limpiarTerminal):
				self.comandosEstandar.get('systema').ejecutar([])
			comando.escribirEnConsolaStrategy(self.historial)

		except InterrumpirConsolaException:
			logging.debug('Saliendo de la consola')
			self.correrConsola = False
		except IndexError:
			logging.debug('Index error '+entrada)
			self.escribirError(ConstanteConsola.mensajeAyudaComandoAgregar)
		except ManiacException as expt:
			logging.error(expt)
			self.escribirError(expt.mensaje)

	def obtenerComando(self,entrada):
		if(entrada in self.comandosEstandar.keys() and self.sesion.sesionActiva):
			return self.comandosEstandar.get(entrada)
		elif(entrada in self.comandosSinSession.keys()):
			return self.comandosSinSession.get(entrada)
		else:
			raise ComandoNoEncontradoException(f'Comando no encontra {entrada}')

	def bucleDeConsola(self):
		self.escribirCabeceraDeConsola()
		while self.correrConsola:
			entrada: str = self.ingresarEntradas()
			if(self.sesion is None):
				print('Parece que no estas registrado, vamos a hacerlo antes de continuar.')
				self.analizarEntrada('registrar')
			else:
				self.analizarEntrada(entrada)

	def escribirCabeceraDeConsola(self):
		comando = self.comandosEstandar['cabecera']
		comando.escribirEnConsolaStrategy(self.historial)

	def ingresarEntradas(self):
		return input(self.prompt)

	def escribirError(self,mensaje):
		print(mensaje)
		self.historial.agregarEntrada(mensaje)
 
	def obtenerHistorial(self):
		return self.historial.obtener()

	def obtenerComandos(self):
		return self.comandosEstandar
