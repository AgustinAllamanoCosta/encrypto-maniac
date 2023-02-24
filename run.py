from Encryptador.terminal.terminal.factory.ManiacFactory import FactoryConsolaEncriptoManiac
import sys

def run():
	consola = FactoryConsolaEncriptoManiac().obtenerConsola(sys.platform)
	consola.bucleDeConsola()

run()
