from Encryptador.comandos.Comando import Comando

class ComandoConfigurar(Comando):

	def ejecutar(self,parametros) -> int:

		for index, param in enumerate(parametros):
			if(param.lower() == '-p'):
				self.encriptoManiac.configurarRutaBBDD(parametros[index + 1 ])
			elif(param.lower() == '-a'):
				self.encriptoManiac.configurarRutaKey(parametros[index + 1])
		return 0