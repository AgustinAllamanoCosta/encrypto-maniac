import encriptoManiac as em
from os import system
class AdministradorConsolaEncriptoManiac():

	def __init__(self):
		self.encriptoManiac = em.EncriptoManiac()
		self.cabeceraConsola = """
ENCRIPTO_MANIAC
Press 1 para ingresar una nueva clave
Press 2 para ver la clave de una cuenta ya ingresada
Press 3 para listar todas las cuentas ingresadas
Press 4 para modificar la clave de una cuenta ya ingresada
Press 5 para salir :D
"""
		self.cursorConsola = '>->->->'
		self.correrLoopPrincipal = True
		self.consolLoop()


	def consolLoop(self):
		print(self.cabeceraConsola)
		while self.correrLoopPrincipal:
			resultado = '';
			operancion = self.inputConsolaManiac('')
			if operancion == '1':
				resultado += self.ingresarClavePorConsola()
			elif operancion == '2':
				resultado += self.verClavaDeCuenta()
			elif operancion == '3':
				resultado += self.listarCuentasPorConsola()
			elif operancion == '4':
				resultado += self.modificarClavePorConsola()
			elif operancion == '5':
				self.salirPorConsola()
			else:
				resultado += 'Operacion no encontrada'
			system('clear')
			print(self.cabeceraConsola)
			print(resultado)

	def ingresarClavePorConsola(self):
		
		nombreApp = self.inputConsolaManiac('Nombre de app a ingresar ')
		calveAEncryptar = self.inputConsolaManiac('Clave a encryptar ')

		self.encriptoManiac.ingresarClave(nombreApp,calveAEncryptar)
		
		return 'se encrypto la clave exitosamente'

	def verClavaDeCuenta(self):
		nombreCuentaABuscar = self.inputConsolaManiac('Nombre de cuenta a buscar ')
		clave = self.encriptoManiac.buscarClave(nombreCuentaABuscar)
		if clave == None:
			return ''
		else:
			return clave

	def listarCuentasPorConsola(self):
		return self.encriptoManiac.listarCuentas()

	def modificarClavePorConsola(self):
		nombreApp = self.inputConsolaManiac('Nombre de cuenta a modificar ')
		nuevaClave = self.inputConsolaManiac('Nueva clave de la cuenta ')

		if self.encriptoManiac.buscarClave(nombreApp) == None:
			return 'La cuenta no existe en la bbdd '
		else:
			self.encriptoManiac.actualizarClave(nombreApp,nuevaClave)
			return 'Se actualizo la calve correctamente '

	def salirPorConsola(self):
		self.correrLoopPrincipal = False

	def inputConsolaManiac(self,mensjaeOpciona):
		return input(self.cursorConsola + mensjaeOpciona)

def main():
	adminConsol = AdministradorConsolaEncriptoManiac()

if __name__ == "__main__":
	main()