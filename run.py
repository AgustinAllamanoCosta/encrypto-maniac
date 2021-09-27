from consolaEncriptoManiac import *
import sys

def run():
	consola = FactoryConsolaEncriptoManiac().obtenerConsola(sys.platform)
	consola.bucleDeConsola()

run()
