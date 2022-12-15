
from getpass import getpass
from Encryptador.ComandosManiac import ComandoAgregar, ComandoModificar,ComandoEliminar,ComandoListar,ComandoMostrar,ComandoConfigurar
from Encryptador.EncryptoManiac import EncryptoManiac
from Util.CustomException import CuentaEnBaseDuplicadaException
from Util.UIManiac import PopUpManiac
import unittest

class TestComandosManiac(unittest.TestCase):

	def setUp(self):
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
		
	def dadoQueSeLlamaAlComandoAgregar(self):
		self.comando = ComandoAgregar() 
		return self

	def dadoQueSeLlamaAlComandoModificarClave(self):
		self.comando = ComandoModificar()
		self.comando.obtenerContraseña = self.observadorGetPass
		return self

	def dadoQueSeLlamaAlComandoEliminarClave(self):
		self.comando = ComandoEliminar()
		return self

	def dadoQueSeLlamaAlComandoListar(self):
		self.comando = ComandoListar()

	def dadoQueSeLlamaAlComandoMostrar(self):
		self.comando = ComandoMostrar()
		return self

	def dadoQueSeLlamaAlComandoConfigurar(self):
		self.comando = ComandoConfigurar()
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
		PopUpManiac.run = self.runPopUpMock

	def conParametros(self,parametros):
		self.parametroComando = parametros

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
		self.comando.escribirEnConsolaStrategy(None)

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
		assert self.comando.mensajeComando == '123455'

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

	#UTIL

	def observadorActualizarClave(self,param1,param2):
		self.seEjecutoActualizarClave = True

	def observadorIngresarClave(self,param1,param2):
		self.seEjecutoIngresarClave = True

	def observadorEliminarClave(self,parametro):
		self.seEjecutoEliminarClave = True

	def observadorBuscarClave(self,parametro):
		self.seEjecutoBuscarClave = True

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
	
	def runPopUpMock(self):
		self.seMostroElPopUp = True

	def buscarClaveMock(self,nombreCuenta):
		return '123455'

if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(TestComandosManiac)
	unittest.TextTestRunner(verbosity=2).run(suite)