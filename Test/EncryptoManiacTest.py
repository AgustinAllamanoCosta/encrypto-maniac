from Encryptador.terminal.terminal.configuracion.Configuracion import Configuracion
from Encryptador.terminal.terminal.repository import BaseRepository, KeyRepository
from Encryptador.terminal.terminal.servicio.EncryptoManiac import EncryptoManiac
import os 
import sqlite3
import unittest

class TestEncryptoManiac(unittest.TestCase):

	def test_CunadoSeEjecutaElMetodoGenerarClaveSeGeneraUnArchivoPunotKey(self):
		self.dadoQueInicioCryptoManiacSinInciarLasClaves()
		self.caundoGeneraLaClave()
		self.seVerificaQueSeCrearElArchivoPuntoKey()

	def test_CuandoInicioElEncriptadorSeCargaUnaClave(self):
		self.dadoQueInicioCryptoManiac()
		self.seVerificaQueSeCargaUnaClave()

	def test_DadoQueIngresoUnaPalabraALaFuncionEncriptarASEMeLaRetornaEncriptada(self):
		self.dadoQueInicioCryptoManiac()
		self.cuandoSeEncryptaLaPalabra("holaMundoCripto123")
		self.seVerificaQueSeEncryptoExitosamente()

# Test de integracion con base de datos mejorar 
	def test_DadoQueSeEjecutaLaFuncionIngresarClaveSeEncriptaYSeInsertaEnLaBaseDeDatos(self):
		self.limpiarBase()
		self.dadoQueInicioCryptoManiac()
		self.cuandoSeIngresaLaCuenta('slack').conlaClave('1234Allamano')
		self.seVerificaQueSeInsertoCorrectamenteEnLaBase()
		self.limpiarBase()

	def test_DadoQueSeEjecutaLaFuncionBuscarClaveSeEsperaQueRetorneLaClaveDesencryptada(self):
		self.limpiarBase()
		self.dadoQueInicioCryptoManiac()
		self.dadoQueExisteUnaCuentaEnLaBase()
		self.cuandoBuscoPorSuNombre()
		self.seVerificaQueSeObtieneLaCalveIngresada()
		self.limpiarBase()

	def test_DadoQueSeEjecutaLaFuncionBuscarClaveConUnNombreDeAppQueNoExisteEnLaBaseSeEsperaQueRetorneNone(self):
		self.limpiarBase()
		self.dadoQueInicioCryptoManiac()
		self.cuandoEjecutoElMetodoBuscarConUnNombreQueCuentaQueNoEstaEnLaBase()
		self.seVerificaQueLaRespuestaEsNone()
		self.limpiarBase()

	def test_DadoQueSeEjecutaLaFuncionListarCuentasYQueExistenCuentasEnLaBBDDSeVerificaQueLaFuncionRetornasLasCuentas(self):
		self.limpiarBase()
		self.dadoQueInicioCryptoManiac()
		self.dadoQueExisteUnaCuentaEnLaBase()
		self.cuandoSeEjecutaListarCuentas()
		self.seVerificaQueSeListenLasCuentas()
		self.limpiarBase()	

	def test_DadoQueSeEjecutaLaFuncionActualizarClaveYQueExisteUnRegistroEnLaBBDDSeVerificaQueLaClaveDeEseRegistroSeActualiza(self):
		self.limpiarBase()
		self.dadoQueInicioCryptoManiac()
		self.dadoQueExisteUnaCuentaEnLaBase()
		self.cuandoSeActualizaLaClave('4444')
		self.seVerificaQueSeActualizo()
		self.limpiarBase()		

	def test_DadoQueSeEjecutaLaFuncionEliminarYQueExisteUnRegistroEnLaBBDDQueCoincideConElValorAEliminarSeVerificaQueSeEliminaDeLaBase(self):
		self.limpiarBase()
		self.dadoQueInicioCryptoManiac()
		self.cuandoSeIngresaLaCuenta('slack').conlaClave('1234Admin')
		self.cuandoQueSeEjecutaLaFuncionEliminar()
		self.seVerficaQueSeEliminoLaCuentaSlack()
		self.limpiarBase()

	def test_DadoQueSeEjecutaLaFuncionExisteCuentaEnBaseYQueNoExisteLaCuentaBuscadaEnLaBaseSeVerificaQueLaFuncionRetornaFalse(self):
		self.limpiarBase()
		self.dadoQueInicioCryptoManiac()
		self.dadoQueExisteLaCuenta('slack').conlaClave('1234Admin')
		self.cuandoQueSeEjecutaLaFuncionExisteCuentaEnLaBase('slack')
		self.seVerficaQueLaFuncionRetornaTrue()
		self.limpiarBase()

	def test_DadoQueSeEjecutaLaFuncionExisteCuentaEnBaseYQueExisteLaCuentaBuscadaEnLaBaseSeVerificaQueLaFuncionRetornaFalse(self):
		self.limpiarBase()
		self.dadoQueInicioCryptoManiac()
		self.cuandoQueSeEjecutaLaFuncionExisteCuentaEnLaBase('slack')
		self.seVerficaQueLaFuncionRetornaFalse()
		self.limpiarBase()

	def test_DadoQueSeTieneConfiguradoElDirectorioDeLaBBDDPorDefectocuandoSeEjecutaLaFuncionConfigurarBBDDBBDDSeVerificaQueCambiaElOrigenDeLaBBDD(self):
		self.limpiarBase()
		self.dadoQueInicioCryptoManiac()
		self.cuandoSeEjecutaLaFuncionConfigurarBBDD('c:\\ArchivoBBDD\\')
		self.seVerificaQueCambiaElOrigenDeLaBBDD()
		self.seVerificarQueSeRecargaLaConfiguracionDeLaBBD()
		self.limpiarBase()

	def test_DadoQueSeTieneConfiguradoElDirectorioDelArchivoDeClavesPorDefectocuandoSeEjecutaLaFuncionConfigurarBBDDKeySeVerificaQueCambiaElOrigenDelArchivoDeClaves(self):
		self.limpiarBase()
		self.dadoQueInicioCryptoManiac()
		self.cuandoSeEjecutaLaFuncionConfigurarKey('c:\\ArchivoKey\\')
		self.seVerificaQueCambiaElOrigenDelArchivoDeClaves()
		self.seVerificarQueSeRecargaLaConfiguracionDeLasKey()
		self.limpiarBase()

#Utilidades

	def dadoQueInicioCryptoManiacSinInciarLasClaves(self):
		self.encryptoManiac = EncryptoManiac(BaseRepository.BaseRepository(),KeyRepository.KeyRepository())
		self.encryptoManiac.iniciarBaseDeClaves()

	def dadoQueInicioCryptoManiac(self):
		keyRepo = KeyRepository.KeyRepository()
		keyRepo.generarOCargarArchivoDeCalvesExistente(Configuracion.rutaAlArchivoDeCredenciales + 'test.key')
		self.encryptoManiac = EncryptoManiac(BaseRepository.BaseRepository(),keyRepo)
		self.encryptoManiac.iniciarBaseDeClaves()
	
	def dadoQueExisteUnaCuentaEnLaBase(self):
		self.nombreAPP = 'slack'
		self.claveAIngresar = 'aaaa'
		self.encryptoManiac.ingresarClave(self.nombreAPP,self.claveAIngresar)

	def dadoQueExisteLaCuenta(self,nombre):
		self.nombreAPP = nombre
		return self

	def dadoQueTengoUnUsuarioConCredencialesValidasEnLaBase(self):
		self.contraseniaUsuario = '1234'
		self.nombreUsuario = 'usuarioUno'
		keyRepo = KeyRepository.KeyRepository()
		keyRepo.generarOCargarArchivoDeCalvesExistente()
		baseDeDatos = sqlite3.connect(Configuracion.rutaAlArchivoLaBaseDeDatos)
		baseDeDatos.execute('INSERT INTO usuarios(usuario,contrasenia,contraseniaRecupero,rutaArchivoKey) VALUES (?,?,?,?)',(self.nombreUsuario,keyRepo.encriptarASE(self.contraseniaUsuario),keyRepo.encriptarASE(self.contraseniaUsuario),Configuracion.rutaAlArchivoDeCredenciales))
		baseDeDatos.commit()

	def caundoGeneraLaClave(self):
		self.encryptoManiac.keyRepository.generarOCargarArchivoDeCalvesExistente(Configuracion.rutaAlArchivoDeCredenciales + 'test.key')

	def cuandoSeEncryptaLaPalabra(self,palabra):
		self.palabraAEncryptar = palabra
		self.palabraEncryptada = self.encryptoManiac.keyRepository.encriptarASE(self.palabraAEncryptar)

	def cuandoSeIngresaLaCuenta(self,nombre):
		self.nombreAPP = nombre
		return self
	
	def cuandoBuscoPorSuNombre(self):
		self.claveIngresada = self.encryptoManiac.buscarClave(self.nombreAPP)

	def cuandoEjecutoElMetodoBuscarConUnNombreQueCuentaQueNoEstaEnLaBase(self):
		self.claveIngresada = self.encryptoManiac.buscarClave('adadsasdadasdasds')

	def cuandoSeEjecutaListarCuentas(self):
		self.cuentaListadas = self.encryptoManiac.listarCuentas()

	def cuandoSeActualizaLaClave(self,clave):
		self.nuevaClave = clave
		self.encryptoManiac.actualizarClave(self.nombreAPP,self.nuevaClave)

	def conlaClave(self,clave):
		self.claveAIngresar = clave
		self.encryptoManiac.ingresarClave(self.nombreAPP,self.claveAIngresar)

	def cuandoQueSeEjecutaLaFuncionEliminar(self):
		self.encryptoManiac.eliminarClave('slack')

	def cuandoQueSeEjecutaLaFuncionExisteCuentaEnLaBase(self,nombreCuenta):
		self.existeCuenta = self.encryptoManiac.existeCuentaEnBase(nombreCuenta)

	def cuandoSeEjecutaLaFuncionConfigurarBBDD(self,parametros):
		self.baseIniciada = False
		self.encryptoManiac.iniciarBaseDeClaves = self.mockIniciarBase
		self.encryptoManiac.configurarRutaBBDD(parametros)

	def cuandoSeEjecutaLaFuncionConfigurarKey(self,parametros):
		self.archvioIniciado = False 
		self.encryptoManiac.keyRepository.generarOCargarArchivoDeCalvesExistente = self.mockArchivoKey
		self.encryptoManiac.configurarRutaKey(parametros)

	def seVerificaQueSeCrearElArchivoPuntoKey(self):
		self.assertTrue(os.path.exists(Configuracion.rutaAlArchivoDeCredenciales))

	def seVerificaQueSeCargaUnaClave(self):
		self.assertNotEqual(self.encryptoManiac.keyRepository.fernet, None)

	def seVerificaQueSeEncryptoExitosamente(self):
		self.assertNotEqual(self.palabraEncryptada,self.palabraAEncryptar)

	def seVerificaQueSeInsertoCorrectamenteEnLaBase(self):
		baseDeDatos = sqlite3.connect(Configuracion.rutaAlArchivoLaBaseDeDatos)
		cursor = baseDeDatos.execute('SELECT * FROM clavesYAplicaciones WHERE nombreApp == ?',(self.nombreAPP,))
		self.assertNotEqual(len(cursor.fetchall()),0)
		baseDeDatos.close()

	def seVerificaQueSeObtieneLaCalveIngresada(self):
		self.assertEqual(self.claveIngresada,self.claveAIngresar)

	def seVerificaQueLaRespuestaEsNone(self):
		self.assertEqual(self.claveIngresada,None)

	def seVerificaQueSeListenLasCuentas(self):
		respuestaEsperada = ' '+self.nombreAPP+',\n'
		self.assertEqual(self.cuentaListadas,respuestaEsperada)	

	def seVerificaQueSeActualizo(self):
		self.assertEqual(self.encryptoManiac.buscarClave(self.nombreAPP),self.nuevaClave)

	def seVerficaQueSeEliminoLaCuentaSlack(self):
		baseDeDatos = sqlite3.connect(Configuracion.rutaAlArchivoLaBaseDeDatos)
		cursor = baseDeDatos.execute('SELECT * FROM clavesYAplicaciones WHERE nombreApp == ?',('slack',))
		self.assertEqual(len(cursor.fetchall()),0)
		baseDeDatos.close()

	def seVerficaQueLaFuncionRetornaTrue(self):
		assert self.existeCuenta == True

	def seVerficaQueLaFuncionRetornaFalse(self):
		assert self.existeCuenta == False

	def seVerificaQueCambiaElOrigenDeLaBBDD(self):
		assert self.encryptoManiac.rutaBBDD != ""

	def seVerificarQueSeRecargaLaConfiguracionDeLaBBD(self):
		assert self.baseIniciada == True
		
	def seVerificarQueSeRecargaLaConfiguracionDeLasKey(self):
		assert self.archvioIniciado == True

	def seVerificaQueCambiaElOrigenDelArchivoDeClaves(self):
		assert self.encryptoManiac.rutaKey != Configuracion.rutaAlArchivoDeCredenciales

	def seVerificaQueRetornaTrue(self):
		assert self.respuestaLogin == True

	def mockIniciarBase(self):
		self.baseIniciada = True

	def mockArchivoKey(self,ruta):
		self.archvioIniciado = True

	def limpiarBase(self):
		try:
			baseDeDatos = sqlite3.connect(Configuracion.rutaAlArchivoLaBaseDeDatos)
			baseDeDatos.execute('DELETE FROM clavesYAplicaciones')
			baseDeDatos.execute('DELETE FROM usuarios')
			baseDeDatos.commit()
			baseDeDatos.close()
		except sqlite3.OperationalError as exp:
			pass

if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(TestEncryptoManiac)
	unittest.TextTestRunner(verbosity=2).run(suite)