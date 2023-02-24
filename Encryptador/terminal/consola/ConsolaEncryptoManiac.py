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
from Encryptador.exceptions.NoUsuariosRegistradosException import NoUsuarioRegistradosException
from Encryptador.servicio.ServicioEncrypto import ServicioEncrypto
from Util.ConstantesEncryptoManiac import ConstanteConsola
import logging
import re

class ConsolaEncryptoManiac():

	def __init__(self, historalParam: HistorialConsola, servicioEncripto: ServicioEncrypto):
		logging.info('Iniciando consola')
		self.historial: HistorialConsola = historalParam
		self.sesion: EstadoDeSesion = EstadoDeSesion()
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
			'exit': ComandoExit(servicioEncripto),
		}

		self.comandosSinSesion: dict[str,Comando] = {
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
				if(isinstance(comando,ComandoRegistrar) or isinstance(comando,ComandoLogin)):
					self.sesion = comando.ejecutar(self.sesion,valoresEntrada[1:])
				else:
					comando.ejecutar(self.sesion,valoresEntrada[1:])
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
		except NoUsuarioRegistradosException as expt:
			logging.error(expt)
			self.escribirError('Parece que tu usuario no esta registrado... puedes registrarlo escribiendo registrar')
		except ManiacException as expt:
			logging.error(expt)
			self.escribirError(expt.mensaje)

	def obtenerComando(self,entrada):
		if(self.sesion.tokenDelUsuario is not None):
			if(entrada in self.comandosEstandar.keys()):
				return self.comandosEstandar.get(entrada)
			else:
				raise ComandoNoEncontradoException(f'Comando no encontra {entrada}', True)
		else:
			self.escribirError('Parece que no estas logeado o registrado, podes hacer lo escribiendo login o registrar')
			if(entrada in self.comandosSinSesion.keys()):
				return self.comandosSinSesion.get(entrada)
			else:
				raise ComandoNoEncontradoException(f'Comando no encontra {entrada}')

	def bucleDeConsola(self):
		self.escribirCabeceraDeConsola()
		while self.correrConsola:
			entrada: str = self.ingresarEntradas()
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
