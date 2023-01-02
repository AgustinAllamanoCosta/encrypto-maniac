from Encryptador.servicio.EncryptoManiac import EncryptoManiac
from Encryptador.comandos.ComandoUnix import ComandoUnix
from Encryptador.comandos.ComandoWin import ComandoWin
from Encryptador.comandos.ComandoAgregar import ComandoAgregar
from Encryptador.comandos.ComandoVerMas import ComandoVerMas
from Encryptador.comandos.ComandoModificar import ComandoModificar
from Encryptador.comandos.ComandoEliminar import ComandoEliminar
from Encryptador.comandos.ComandoListar import ComandoListar
from Encryptador.comandos.ComandoMostrar import ComandoMostrar
from Encryptador.comandos.ComandoExit import ComandoExit
from Encryptador.comandos.ComandoAyuda import ComandoAyuda
from Encryptador.consola.ConsolaEncryptoManiac import ConsolaEncryptoManiac
from Encryptador.consola.EstadoDeSesion import EstadoDeSesion
from Encryptador.factory.ManiacFactory import FactoryConsolaEncriptoManiac
from Util.ConstantesEncryptoManiac import ConstanteConsola
import threading as t
import sys
import unittest

class TestConsolaManiac(unittest.TestCase):

	def setUp(self):
		self.funcionesOriginales = {
			'ComandoModificar': ComandoModificar.ejecutar,
			'ComandoAgregar': ComandoAgregar.ejecutar,
			'ComandoListar': ComandoListar.ejecutar,
			'ComandoVerMas': ComandoVerMas.ejecutar,
			'ComandoExit' : ComandoExit.ejecutar,
			'ComandoEliminar' : ComandoEliminar.ejecutar,
			'ComandoMostrar' : ComandoMostrar.ejecutar,
			'ComandoAyuda' : ComandoAyuda.ejecutar,
			'existeCuentaEnBase' :EncryptoManiac.existeCuentaEnBase
		}

	def tearDown(self):
		ComandoModificar.ejecutar = self.funcionesOriginales['ComandoModificar']
		ComandoAgregar.ejecutar = self.funcionesOriginales['ComandoAgregar']
		ComandoListar.ejecutar = self.funcionesOriginales['ComandoListar']
		ComandoVerMas.ejecutar = self.funcionesOriginales['ComandoVerMas']
		ComandoExit.ejecutar = self.funcionesOriginales['ComandoExit']
		ComandoEliminar.ejecutar = self.funcionesOriginales['ComandoEliminar']
		ComandoMostrar.ejecutar = self.funcionesOriginales['ComandoMostrar']
		ComandoAyuda.ejecutar = self.funcionesOriginales['ComandoAyuda']
		EncryptoManiac.existeCuentaEnBase = self.funcionesOriginales['existeCuentaEnBase']

	def test_dadoQueTengoUnaConsolaDeLaConsolaSeVerificaQueSeMuestraElMensajeDeBienvenida(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeSaleDelContextoAlIniciar()
		self.cuandoSeInicia()
		self.seVerificaQueSeMuestraElMensajeDeBienvenida()

	def test_dadoQueTengoUnaConsolaCuadnoSeIniciaLaConsolaSeVerificaQueSeMuestrasLaListaDeComandosbasicos(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeSaleDelContextoAlIniciar()
		self.cuandoSeInicia()
		self.seVerificaQueSeMuestrasLaListaDeComandosbasicos()

	def test_dadoQueTengoUnaConsolaCundoSeIngresaElComandoAgregarSeVerificaQueSeEjecutaLaFuncionAgregarCuenta(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeEjecutaElComandoAgregar()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada() 
		self.seVerificaQueSeLlamaALaFuncionAgregar()

	def test_dadoQueTengoUnaConsolaCuandoSeIngresaElComandoAgregarSinParametroSeVerificaMuestraElMensajeDeAyudaDelComando(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeEjecutaElComandoAgregarSinParametros()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaMuestraElMensajeDeAyudaDelComando()

	def test_dadoQueTengoUnaConsolaConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoListarSeVerificaQueSeLlamaALaFuncionListar(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeEjecutaElComandoListar()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaQueSeLlamaALaFuncionListar()

	def test_dadoQueTengoUnaConsolaConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoVerMasSeListanElRestoDeLosComandos(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeEjecutaElComandoVerMas()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaQueSeMuestraLaAyudaDeLosComandos()
	
	def test_dadoQueTengoUnaConsolaConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoModificarSeVerificaQueSeLlamaALaFuncionComandoModificar(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeEjecutarElComandoModificar()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerifiacaQueSeLlamaALaFuncionComandoModificar()

	def test_dadoQueTengoUnaConsolaConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoModificarSinElParametroSeVerificaQueSeMuestraElMensajeDeError(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeEjecutarElComandoModificarSinElParametro()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaQueSeMuestraElMensajeDeError()

	def test_dadoQueTengoUnaConsolaConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoEliminarSeVerirficaQueSeLlamaALaFuncion(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeEjecutarElComandoEliminar()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerifiacaQueSeLlamaALaFuncionComandoEliminar()

	def test_dadoQueTengoUnaConsolaCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoEliminarSinParametrosSeVerirficaQueSeMuestraElMensajeDeError(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeEjecutarElComandoEliminarSinParametros()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaQueSeMuestraElMensajeDeError()

	def test_dadoQueTengoUnaConsolaConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoMostrarrSeVerirficaQueSeLlamaALaFuncion(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeEjecutaElComandoMostrar()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerficaQueSeLlamaALaFuncionMostrar()

	def test_dadoQueTengoUnaConsolaConCuentasAgregadasEnLaBaseCuandoSeIngresaElComandoMostrarrSinParametrosSeVerirficaQueSeMuestraElMensajeDeError(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeEjecutaElComandoMostrarSinParametro()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaQueSeMuestraElMensajeDeError()

	def test_dadoQueTengoUnaConsolaConCuentasAgregadasEnLaBaseCuandoSeIngresaUnComandoQueNoExisteSeVerificaQueSeMuestraElMensajeDeComandosAvanzados(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueIngresaUnComandoQueNoExiste()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaQueSeListanElRestoDeLosComandos()

	def test_dadoQueTengoUnaConsolaCuandoSeEnviaUnComandoEnMayusculaLoEjecutoIgual(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeEnviaUnComandoEnMayuscula()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada()
		self.seVerificaQueSeEjecutaIgual()	

	def test_dadoQueEstoyTrabajandoEnSistemaUnixCuandoSeInstanciaUnaConsolaDesdeElFactorySeVerificaQueSeCarganLosComandosDeUnixDeSystema(self):
		self.dadoQueEstoyTrabajandoiEnSistemasUnix()
		self.dadoQueSeInstanciaUnaConsolaDesdeElFactoryDeConsolas()
		self.seVerificaQueSeCarganLosComandosDeSystemaUnix()

	def test_dadoQueEstoyTrabajandoEnSistemaWinCuandoSeInstanciaUnaConsolaDesdeElFactorySeVerificaQueSeCarganLosComandosDeWin32DeSystema(self):
		self.dadoQueEstoyTrabajandoiEnSistemasWin()
		self.dadoQueSeInstanciaUnaConsolaDesdeElFactoryDeConsolas()
		self.seVerificaQueSeCarganLosComandosDeSystemaWin()

	def test_dadoQueTengoUnaConsolaCuandoSeIngresaElComandoAgregarYLaCuentaExisteEnLaBaseSeVerificaQueSeVerificaLanzaUnErrorYSeMuestraElMensajeEnLaConsola(self):
		self.dadoQueTengoUnaConsola()
		self.dadoQueSeEjecutaElComandoAgregarConUnaCuentaQueExisteEnLaBase()
		self.cuandoSeLlamaALaFuncionAnalizarEntrada() 
		self.seVerificaLanzaUnErrorYSeMuestraElMensajeEnLaConsola()
		
	def dadoQueTengoUnaConsola(self):
		estadoSesion = EstadoDeSesion('',True)
		self.consola = FactoryConsolaEncriptoManiac().obtenerConsola(sys.platform)
		self.consola.encriptador.estadoSesion = estadoSesion
		self.consola.estadoDeSesion = estadoSesion

	def dadoQueSeSaleDelContextoAlIniciar(self):
		self.comando = 'exit'
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : self.comando
		self.consolaEnParalelo =  HiloQueSePuedeDetener(target=self.consola.bucleDeConsola,daemon=True)		

	def dadoQueSeEjecutaElComandoAgregarSinParametros(self):
		self.comando = 'agregar'
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : self.comando

	def dadoQueSeEjecutaElComandoAgregar(self):
		self.comando = 'agregar slack'
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : self.comando
		ComandoAgregar.ejecutar = self.observadorFuncionAgregar

	def dadoQueSeEjecutaElComandoAgregarConUnaCuentaQueExisteEnLaBase(self):
		self.comando = 'agregar slack'
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : self.comando
		EncryptoManiac.existeCuentaEnBase = self.existeCuentaEnBaseMock

	def dadoQueSeEjecutaElComandoListar(self):
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : 'listar'
		ComandoListar.ejecutar = self.observadorFuncionListar

	def dadoQueSeEjecutaElComandoVerMas(self):
		self.comando = 'vermas'
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : self.comando

	def dadoQueSeEjecutarElComandoModificar(self):
		self.comando = 'modificar slack'
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : self.comando
		ComandoModificar.ejecutar = self.observadorFuncionModificar

	def dadoQueSeEjecutarElComandoModificarSinElParametro(self):		
		self.comando = 'modificar'
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : self.comando

	def dadoQueSeEjecutarElComandoEliminar(self):		
		self.comando = 'eliminar slack'
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : self.comando
		ComandoEliminar.ejecutar = self.observadorFuncionEliminar
	
	def dadoQueSeEjecutarElComandoEliminarSinParametros(self):		
		self.comando = 'eliminar'
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : self.comando

	def dadoQueSeEjecutaElComandoMostrar(self):		
		self.comando = 'mostrar slack'
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : self.comando
		ComandoMostrar.ejecutar = self.observadorFuncionMostrar

	def dadoQueSeEjecutaElComandoMostrarSinParametro(self):
		self.comando = 'mostrar'
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : self.comando

	def dadoQueIngresaUnComandoQueNoExiste(self):
		self.comando = 'asdasdasdsa'
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : self.comando

	def dadoQueSeEnviaUnComandoEnMayuscula(self):
		ConsolaEncryptoManiac.ingresarEntradas = lambda x :'MOSTRAR'
		ComandoMostrar.ejecutar = self.observadorFuncionMostrar

	def dadoQueEstoyTrabajandoiEnSistemasUnix(self):
		self.plataform = 'Linux'

	def dadoQueEstoyTrabajandoiEnSistemasWin(self):
		self.plataform = 'Win32'

	def dadoQueSeInstanciaUnaConsolaDesdeElFactoryDeConsolas(self):
		self.consola = FactoryConsolaEncriptoManiac().obtenerConsola(self.plataform)

	def cuandoSeInicia(self):
		self.consolaEnParalelo.start()

	def cuandoSeLlamaALaFuncionAnalizarEntrada(self):
		self.consola.analizarEntrada(self.consola.ingresarEntradas())

	def seVerificaQueSeMuestraElMensajeDeBienvenida(self):
		self.consolaEnParalelo.stop()
		self.consolaEnParalelo.join()
		assert self.consola.obtenerHistorial()[0] == ConstanteConsola.mensajeBienvenida

	def seVerificaQueSeMuestrasLaListaDeComandosbasicos(self):
		self.consolaEnParalelo.stop()
		self.consolaEnParalelo.join()
		assert self.consola.obtenerHistorial()[1] == ConstanteConsola.mensajeComandosBasicos

	def seVerificaQueSeLlamaALaFuncionListar(self):
		assert self.seEjecutoListar == True 

	def seVerificaQueSeListanElRestoDeLosComandos(self):
		assert self.consola.obtenerHistorial()[1] == f'Comando no encontra {self.comando} {ConstanteConsola.mensajeComandosAvanzados}'
	
	def seVerificaQueSeMuestraLaAyudaDeLosComandos(self):
		assert self.consola.obtenerHistorial()[1] == ConstanteConsola.mensajeComandosAvanzados

	def seVerifiacaQueSeLlamaALaFuncionComandoModificar(self):
		assert self.seEjecutoModificar == True

	def seVerificaQueSeLlamaALaFuncionAgregar(self):
		assert self.seEjecutoAgregar == True

	def seVerificaQueSeMuestraElMensajeDeError(self):
		assert self.consola.obtenerHistorial()[1] == ConstanteConsola.mensajeErrorComandoParametros

	def seVerificaMuestraElMensajeDeAyudaDelComando(self):
		assert self.consola.obtenerHistorial()[1] == ConstanteConsola.mensajeAyudaComandoAgregar		

	def seVerifiacaQueSeLlamaALaFuncionComandoEliminar(self):
		assert self.seEjecutoEliminar == True

	def seVerficaQueSeLlamaALaFuncionMostrar(self):
		assert self.seEjecutoMostrar == True

	def seVerificaQueSeEjecutaIgual(self):
		assert self.seEjecutoMostrar == True

	def seVerificaQueSeCarganLosComandosDeSystemaUnix(self):
		assert isinstance(self.consola.obtenerComandos()['systema'],ComandoUnix)

	def seVerificaQueSeCarganLosComandosDeSystemaWin(self):
		assert isinstance(self.consola.obtenerComandos()['systema'],ComandoWin)

	def seVerificaLanzaUnErrorYSeMuestraElMensajeEnLaConsola(self):
		assert self.consola.obtenerHistorial()[1] == ConstanteConsola.mensajeErrprComandoDuplicado + 'slack'
#Utilidades 
	def observadorFuncionListar(self,arg):
		self.seEjecutoListar = True

	def observadorFuncionEliminar(self,arg):
		self.seEjecutoEliminar = True

	def observadorFuncionMostrar(self,arg):
		self.seEjecutoMostrar = True

	def observadorFuncionModificar(self,arg):
		self.seEjecutoModificar = True

	def observadorFuncionAgregar(self,arg):
		self.seEjecutoAgregar = True

	def existeCuentaEnBaseMock(self,arg):
		return True

class HiloQueSePuedeDetener(t.Thread):

	def __init__(self,  *args, **kwargs):
		super(HiloQueSePuedeDetener, self).__init__(*args, **kwargs)
		self.frenarHilo = t.Event()

	def stop(self):
		self.frenarHilo.set()

	def stopped(self):
		return self.frenarHilo.is_set()

if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(TestConsolaManiac)
	unittest.TextTestRunner(verbosity=2).run(suite)