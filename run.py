from Encryptador import ConsolaEncryptoManiac as CEM
import sys

def run():
	consola = CEM.FactoryConsolaEncriptoManiac().obtenerConsola(sys.platform)
	consola.bucleDeConsola()

run()
