
from getpass import getpass
from Encryptador.comandos.ComandoAgregar import ComandoAgregar
from Encryptador.comandos.ComandoLogin import ComandoLogin
from Encryptador.comandos.ComandoModificar import ComandoModificar
from Encryptador.comandos.ComandoEliminar import ComandoEliminar
from Encryptador.comandos.ComandoListar import ComandoListar
from Encryptador.comandos.ComandoMostrar import ComandoMostrar
from Encryptador.comandos.ComandoConfigurar import ComandoConfigurar
from Encryptador.consola.EstadoDeSesion import EstadoDeSesion
from Encryptador.consola.Historial import HistorialConsola
from Encryptador.factory.ManiacFactory import FactoryEncriptador
from Encryptador.EncryptoManiac import EncryptoManiac
from Encryptador.exceptions.CuentaEnBaseDuplicadaException import CuentaEnBaseDuplicadaException
import unittest

class TestComandosManiac(unittest.TestCase):

	def setUp(self):
		self.encriptoManiac = FactoryEncriptador().obtenerEncripto()
		estadoSesion = EstadoDeSesion('',True)
		self.encriptoManiac.estadoSesion = estadoSesion
		self.funcionesOriginales = {
			'ingresarClave': EncryptoManiac.ingresarClave,
			'actualizarClave': EncryptoManiac.actualizarClave,
			'eliminarClave': EncryptoManiac.eliminarClave,
			'buscarClave': EncryptoManiac.buscarClave,
			'listarCuentas': EncryptoManiac.listarCuentas,
			'existeCuentaEnBase': EncryptoManiac.existeCuentaEnBase,
			'configurarBBDD' : EncryptoManiac.configurarRutaBBDD,
			'configurarKey' : EncryptoManiac.configurarRutaKey,
			'getpass' : getpass,
			'iniciarSesion': EncryptoManiac.iniciarSesion,
		}

	def tearDown(self):
		EncryptoManiac.ingresarClave = self.funcionesOriginales['ingresarClave']
		EncryptoManiac.actualizarClave = self.funcionesOriginales['actualizarClave']
		EncryptoManiac.eliminarClave = self.funcionesOriginales['eliminarClave']
		EncryptoManiac.buscarClave = self.funcionesOriginales['buscarClave']
		EncryptoManiac.listarCuentas = self.funcionesOriginales['listarCuentas']
		EncryptoManiac.existeCuentaEnBase = self.funcionesOriginales['existeCuentaEnBase']
		EncryptoManiac.configurarRutaBBDD = self.funcionesOriginales['configurarBBDD']
		EncryptoManiac.configurarRutaKey = self.funcionesOriginales['configurarKey']
		EncryptoManiac.iniciarSesion = self.funcionesOriginales['iniciarSesion']
		getpass = self.funcionesOriginales['getpass']

	def test_dadoQueSeLlamaAlComandoModificarConParametrosNombreDeCuentaYContraseñaSeVerifiacaQueSeLlamaALaFuncionActualizarClave(self):
		self.dadoQueSeLlamaAlComandoModificarClave().conParametros(['slack','456'])
		self.cuandoSeLlamanALaFuncionEjecutarDelComandoModificarClave()
		self.seVerificaQueSeLlamaALaFuncionModificarClave()

	def test_dadoQueSeLlamaAlComandoEliminarConParametrosNombreDeCuentaSeVerifiacaQueSeLlamaALaFuncionEliminarClave(self):
		self.dadoQueSeLlamaAlComandoEliminarClave().conParametros(['slack'])
		self.cuandoSeLlamanALaFuncionEjecutarDelComandoEliminarClave()
		self.seVerificaQueSeLlamaALaFuncionEliminarClave()

	def test_dadoQueSeLlamaComandoMostrarConParametroNombreDeCuentaSeVerifiacaQueSeLlamanALaFuncionBuscarClave(self):
		self.dadoQueSeLlamaAlComandoMostrar().conParametros(['slack'])
		self.cuandoSeLlamanALaFuncionEjecutarDelComandoMostrar()
		self.seVerificaQueSeLlamaALaFuncionMostrar()

	def test_dadoQueSeLlamaComandoListarSeVerifiacaQueSeLlamanALaFuncionListarCuentas(self):
		self.dadoQueSeLlamaAlComandoListar()
		self.cuandoSeLlamanALaFuncionEjecutarDelComandoListar()
		self.seVerificaQueSeLlamaALaFuncionListarCuentas()

	def test_dadoQueSeLlamaAlComandoAgregarConParametrosDeNombreDeCuentaYContraseniaSeVerificaQueSeLlamaALaFuncionIngresarClave(self):
		self.dadoQueSeLlamaAlComandoAgregar().conParametros(['slack'])
		self.dadoQueNoExisteLaCuentaEnLaBase()
		self.cuandoSeLlamanALaFuncionEjecutarDelComandoAgregar()
		self.seVerificaQueSeLlamaALaFuncionIngresarClave()

	def test_dadoQueExisteUnaCuentaLaBaseCuandoSeVaAIngresarUnaCuentaConElMismoNombreSeVerificaQueSeLanzaUnaExcepcion(self):
		self.dadoQueSeLlamaAlComandoAgregar().conParametros(['slack'])
		self.dadoQueExisteUnaCuentaEnLaBase()
		with self.assertRaises(CuentaEnBaseDuplicadaException):
			self.cuandoSeLlamanALaFuncionEjecutarDelComandoAgregar()
		self.seVerificaQueSeLanzaLaExcepcionDeCuentaDuplicada()

	def test_dadoQueSeLlamaAlComandoAgregarConParametrosDeNombreDeCuentaYContraseniaSeVerificaSeDesactivaElEchoDeLaConsola(self):
		self.dadoQueSeLlamaAlComandoAgregar().conParametros(['slack'])
		self.dadoQueNoExisteLaCuentaEnLaBase()
		self.cuandoSeLlamanALaFuncionEjecutarDelComandoAgregar()
		self.seVerificaSeDesactivaElEchoDeLaConsola()

	def test_dadoQueSeEjecutaElComandoMostrarDadoQueSeMuestraSeVerficaQueSeMuestraUnPopUpConLaMisma(self):
		self.dadoQueSeLlamaAlComandoMostrar().conParametros(['slack'])
		self.dadoQueSeMuestraLaContraseña()
		self.cuandoSeLlamaALaFuncionEscribirDelComando()
		self.seVerficaQueSeMuestraUnPopUpConLaMisma()

	def test_dadoQueSeLlamaAlComandoModificarConParametrosDeNombreDeCuentaYContraseniaSeVerificaSeDesactivaElEchoDeLaConsola(self):
		self.dadoQueSeLlamaAlComandoModificarClave().conParametros(['slack'])
		self.cuandoSeLlamanALaFuncionEjecutarDelComandoModificarClave()
		self.seVerificaSeDesactivaElEchoDeLaConsola()

	def test_dadoQueSeLlamaAlComandoConfigurarConParametrosMenosBYUnaNuevaRutaParaLaBBDDSeVerificaQueSeActualizaYSeCargaLaNuevaBBDD(self):
		self.dadoQueSeLlamaAlComandoConfigurar().conParametros(['-p','c:\\'])
		self.cuandoSeLlamaALaFuncionEjecutarDelComandoConfigurar()
		self.seVerificaQueSeActualizaYSeCargaLaNuevaBBDD()

	def test_dadoQueSeLlamaAlComandoConfigurarConParametrosMenosAYUnaNuevaRutaParaElArchivoDeKeySeVerificaQueSeActualizaYSeCargaLaNuevaBBDD(self):
		self.dadoQueSeLlamaAlComandoConfigurar().conParametros(['-a','c:\\'])
		self.cuandoSeLlamaALaFuncionEjecutarDelComandoConfigurar()
		self.seVerificaQueSeActualizaYSeCargaLaNuevaKey()

	def test_dadoQueSeLlamaAlComandoConfigurarConLosDosParametrosSeguidosConValoresValidosSeVerificaQueSeLlamaALasDosFuncionesDelEncryptoManiac(self):
		self.dadoQueSeLlamaAlComandoConfigurar().conParametros(['-a','c:\\','-p','c:\\'])
		self.cuandoSeLlamaALaFuncionEjecutarDelComandoConfigurar()
		self.seVerificaQueSeLlamaALasFuncionesDelEncryptoManiacCorrespondiente()

	def test_dadoQueSeLlamaAlComandoLoginConUnUsusarioYContraseniaValidosSeEsperaQueRetorneTrue(self):
		self.dadoQueSeLlamaAlComandoLogin()
		self.conUsuarioYContraseniaValidos()
		self.cuandoSeLlamaAlComandoLogin()
		self.seVerificaQueRetornaTrue()

	def dadoQueSeLlamaAlComandoLogin(self):
		self.comando = ComandoLogin(self.encriptoManiac)
		self.comando.obtenerContrasenia = lambda : 'contrasenia'
		self.comando.obtenerUsuario = lambda : 'usuario'
		return self

	def dadoQueSeLlamaAlComandoAgregar(self):
		self.comando = ComandoAgregar(self.encriptoManiac)
		return self

	def dadoQueSeLlamaAlComandoModificarClave(self):
		self.comando = ComandoModificar(self.encriptoManiac)
		self.comando.obtenerContraseña = self.observadorGetPass
		return self

	def dadoQueSeLlamaAlComandoEliminarClave(self):
		self.comando = ComandoEliminar(self.encriptoManiac)
		return self

	def dadoQueSeLlamaAlComandoListar(self):
		self.comando = ComandoListar(self.encriptoManiac)

	def dadoQueSeLlamaAlComandoMostrar(self):
		self.comando = ComandoMostrar(self.encriptoManiac)
		return self

	def dadoQueSeLlamaAlComandoConfigurar(self):
		self.comando = ComandoConfigurar(self.encriptoManiac)
		return self

	def dadoQueExisteUnaCuentaEnLaBase(self):
		self.seEjecutoExisteCuentaEnBase = False
		EncryptoManiac.existeCuentaEnBase = self.observadorExisteCuentaEnBase

	def dadoQueNoExisteLaCuentaEnLaBase(self):
		self.seEjecutoExisteCuentaEnBase = False
		EncryptoManiac.existeCuentaEnBase = self.observadorNoExisteCuentaEnBase

	def dadoQueSeMuestraLaContraseña(self):
		self.seMostroElPopUp = False
		EncryptoManiac.buscarClave = self.buscarClaveMock

	def conParametros(self,parametros):
		self.parametroComando = parametros

	def conUsuarioYContraseniaValidos(self):
		EncryptoManiac.iniciarSesion = self.iniciarSessionMock

	def cuandoSeLlamaAlComandoLogin(self):
		self.restpuestaComando = self.comando.ejecutar([])

	def cuandoSeLlamanALaFuncionEjecutarDelComandoAgregar(self):
		self.seEjecutoIngresarClave = False
		self.seDesactivaElEcho = False
		EncryptoManiac.ingresarClave = self.observadorIngresarClave
		self.comando.obtenerContraseña = self.observadorGetPass
		self.comando.ejecutar(self.parametroComando)

	def cuandoSeLlamanALaFuncionEjecutarDelComandoModificarClave(self):
		self.seEjecutoActualizarClave = False
		EncryptoManiac.actualizarClave = self.observadorActualizarClave
		self.comando.ejecutar(self.parametroComando)

	def cuandoSeLlamanALaFuncionEjecutarDelComandoEliminarClave(self):
		self.seEjecutoEliminarClave = False
		EncryptoManiac.eliminarClave = self.observadorEliminarClave
		self.comando.ejecutar(self.parametroComando)

	def cuandoSeLlamanALaFuncionEjecutarDelComandoMostrar(self):
		self.seEjecutoBuscarClave = False
		EncryptoManiac.buscarClave = self.observadorBuscarClave
		self.comando.ejecutar(self.parametroComando)

	def cuandoSeLlamanALaFuncionEjecutarDelComandoListar(self):
		self.seEjecutoListarCuentas = False
		EncryptoManiac.listarCuentas = self.observadorListarCuentas
		self.comando.ejecutar()

	def cuandoSeLlamaALaFuncionEscribirDelComando(self):
		self.comando.ejecutar(self.parametroComando)
		self.comando.escribirEnConsolaStrategy(HistorialConsola())

	def cuandoSeLlamaALaFuncionEjecutarDelComandoConfigurar(self):
		self.seEjecutoConfigurarKey = False
		self.seEjecutoConfigurarBBDD = False
		EncryptoManiac.configurarRutaBBDD = self.observadorComandoConfigurarBBDD
		EncryptoManiac.configurarRutaKey  = self.observadorComandoConfigurarKey
		self.comando.ejecutar(self.parametroComando)

	def seVerificaQueSeLlamaALaFuncionIngresarClave(self):
		assert self.seEjecutoIngresarClave == True
		assert self.seEjecutoExisteCuentaEnBase == True

	def seVerificaQueSeLlamaALaFuncionModificarClave(self):
		assert self.seEjecutoActualizarClave == True

	def seVerificaQueSeLlamaALaFuncionEliminarClave(self):
		assert self.seEjecutoEliminarClave == True

	def seVerificaQueSeLlamaALaFuncionMostrar(self):
		assert self.seEjecutoBuscarClave == True

	def seVerificaQueSeLlamaALaFuncionListarCuentas(self):
		assert self.seEjecutoListarCuentas == True

	def seVerificaQueSeLanzaLaExcepcionDeCuentaDuplicada(self):
		assert self.seEjecutoExisteCuentaEnBase == True
		assert self.seEjecutoIngresarClave == False

	def seVerficaQueSeMuestraUnPopUpConLaMisma(self):
		assert self.comando.mensajeComando == 'Se copia la calve al portapapeles :D la puedes pegar con ctrl + v'

	def seVerificaSeDesactivaElEchoDeLaConsola(self):
		assert self.seDesactivaElEcho == True

	def seVerificaQueSeActualizaYSeCargaLaNuevaBBDD(self):
		assert self.seEjecutoConfigurarBBDD == True
		assert self.seEjecutoConfigurarKey == False
		
	def seVerificaQueSeActualizaYSeCargaLaNuevaKey(self):
		assert self.seEjecutoConfigurarKey == True
		assert self.seEjecutoConfigurarBBDD == False
		
	def seVerificaQueSeLlamaALasFuncionesDelEncryptoManiacCorrespondiente(self):
		assert self.seEjecutoConfigurarKey == True
		assert self.seEjecutoConfigurarBBDD == True

	def seVerificaQueRetornaTrue(self):
		assert self.comando.mensajeComando == 'Login correcto :)'

	#UTIL

	def observadorActualizarClave(self,param1,param2):
		self.seEjecutoActualizarClave = True

	def observadorIngresarClave(self,param1,param2):
		self.seEjecutoIngresarClave = True

	def observadorEliminarClave(self,parametro):
		self.seEjecutoEliminarClave = True

	def observadorBuscarClave(self,parametro):
		self.seEjecutoBuscarClave = True
		return 'contrasena'

	def observadorListarCuentas(self):
		self.seEjecutoListarCuentas = True

	def observadorExisteCuentaEnBase(self, nombreCuenta):
		self.seEjecutoExisteCuentaEnBase = True
		return True

	def observadorNoExisteCuentaEnBase(self,nombreCuenta):
		self.seEjecutoExisteCuentaEnBase = True
		return False
	
	def observadorGetPass(self):
		self.seDesactivaElEcho = True
		return '1234'

	def observadorComandoSystema(self):
		self.seEejecutoElComandoDelSystema = True
	
	def observadorComandoConfigurarBBDD(self,rutaAConfigurar):
		self.seEjecutoConfigurarBBDD = True
	
	def observadorComandoConfigurarKey(self,rutaAConfigurar):
		self.seEjecutoConfigurarKey = True
	
	def runPopUpMock(self,mensaje):
		self.seMostroElPopUp = True

	def buscarClaveMock(self,nombreCuenta):
		return '123455'

	def iniciarSessionMock(self,usuario,contrasenia):
		return True

if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(TestComandosManiac)
	unittest.TextTestRunner(verbosity=2).run(suite)