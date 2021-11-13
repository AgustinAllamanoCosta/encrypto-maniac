from Encryptador import ConsolaEncryptoManiac as CEM
from Web import aplicacionWeb
import sys

def run(tipo):
	if (tipo[1].lower() == 'consola'):
		consola = CEM.FactoryConsolaEncriptoManiac().obtenerConsola(sys.platform)
		consola.bucleDeConsola()
	else:
		app = aplicacionWeb.aplicacion()
		app.crear().run()

run(sys.argv)
