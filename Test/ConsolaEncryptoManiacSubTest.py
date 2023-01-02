from os import sys
from Encryptador.consola.ConsolaEncryptoManiac import ConsolaEncryptoManiac
from Encryptador.consola.EstadoDeSesion import EstadoDeSesion
from Encryptador.factory.ManiacFactory import FactoryConsolaEncriptoManiac
from Encryptador.comandos.ComandoAyuda import ComandoAyuda
import unittest

class SubTestConsolaEncriptoManiac(unittest.TestCase):
	
	def setUp(self):
		self.mensajesEsperados = '''Comando listar-> se utiliza para listar todo el contenido de la base, no utiliza parametros para hacerlo :D,
		Comando agregar-> agregar parametro1 parametro2 
		parametro1: es el nombre de la cuenta a agregar
		parametro2: es la contraseña de la cuenta
		LOS DOS PARAMETROS SON OBLIGATORIOS,
		Comando exit-> se utiliza para salir del sistema, todas las contraseñas quedaran guardades en la base de datos, asi que cundo vuelvas todo estara como si nunca te hubieras ido :D,
		Comando mostrar-> mostrar parametro1 \n parametro1: el nombre de la cuenta a mostrar la clave, si no existe la cuenta no se mostrara nada :D,
		Comando verMas-> muestra la lista de comando disponibles :D,
		Comando eliminar-> eliminar parametro1 \n parametro1: nombre de la cuenta a elimnar de la base, la misma despues no se puede recuperar :D,
		Comando modificar-> modificar parametro1 parametro2 \n parametro1: nombre de la cuenta a modificar \n parametro2 nueva calve a ingresar'''
		self.funcionesOriginales = {
			'ComandoAyuda' : ComandoAyuda.ejecutar
		}

	def tearDown(self):
		ComandoAyuda.ejecutar = self.funcionesOriginales['ComandoAyuda']

	def test_ComandoAyudaConsola(self):
		self.dadoQueSeTieneUnContexto()
		for comandoConParametro in ['ayuda listar','ayuda agregar','ayuda vermas','ayuda modificar','ayuda eliminar','ayuda mostrar','ayuda exit']:
			with self.subTest(pattern=comandoConParametro):
				self.dadoQueSeIngresaElComandoAyudaConElNombreDelComdoLisatarComoParametro(comandoConParametro)
				self.cuandoSeLlamaALaFuncionAnalizarEntrada()
				self.seVerificaQueSeMuestraLaAyudaDelComandoListar()

	def dadoQueSeTieneUnContexto(self):
		estadoSesion = EstadoDeSesion('',True)
		self.consola = FactoryConsolaEncriptoManiac().obtenerConsola(sys.platform)
		self.consola.estadoDeSesion = estadoSesion

	def dadoQueSeIngresaElComandoAyudaConElNombreDelComdoLisatarComoParametro(self,comandoConParametro):
		ConsolaEncryptoManiac.ingresarEntradas = lambda x : comandoConParametro

	def cuandoSeLlamaALaFuncionAnalizarEntrada(self):
		self.consola.analizarEntrada(self.consola.ingresarEntradas())

	def seVerificaQueSeMuestraLaAyudaDelComandoListar(self):
		self.assertRegex(self.mensajesEsperados, self.consola.obtenerHistorial()[1]) 

if __name__ == "__main__":
	suite = unittest.TestLoader().loadTestsFromTestCase(SubTestConsolaEncriptoManiac)
	unittest.TextTestRunner(verbosity=2).run(suite)