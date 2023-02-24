from getpass import getpass
from Encryptador.comandos.ComandoSensible import ComandoSensibles
from Encryptador.consola.EstadoDeSesion import EstadoDeSesion
from Encryptador.servicio.ServicioEncrypto import ServicioEncrypto

class ComandoRegistrar(ComandoSensibles):

	def __init__(self, encryptador: ServicioEncrypto):
		super().__init__(encryptador)
		self.caracteresEspeciales = ['!','@','#','$','%','^','&','*','(',')','<','>','?','-','_','+','=','[',']','{','}','~']

	def ejecutar(self,sesion:EstadoDeSesion,parametros: list = []) -> EstadoDeSesion:
		usuario = self.obtenerUsuario()
		credenciales = self.obtenerCredenciales()
		self.encriptoManiac.registrarNuevoUsuario(usuario,credenciales[0],credenciales[1])
		self.mensajeComando = 'Usuario Registrado con exito'

		estadoDeSession = EstadoDeSesion()
		estadoDeSession.usuario = usuario
		estadoDeSession.sesionActiva = False
		estadoDeSession.tokenDelUsuario = self.encriptoManiac.obtenerToken(usuario)
		return estadoDeSession

	def obtenerUsuario(self):
		return input('Usuario: ')

	def obtenerCredenciales(self):
		contrasenia = self.obtenerContrasenias()
		contraseniaRecupero = self.obtenerContraseniaDeRecupero(contrasenia)
		return (contrasenia,contraseniaRecupero)

	def obtenerContrasenias(self):
		contraseniaUno = getpass('Contrasenia: ')
		contraseniaDos = getpass('La misma contrasenia para verificar: ')
		if(self.validarContrasenias(contraseniaUno,contraseniaDos)):
			return contraseniaUno
		else:
			return self.obtenerContrasenias()

	def obtenerContraseniaDeRecupero(self,contraseniaEnterior):
		print('Bien ahora vamos a generar la contrasenia de recupero, anotala y no la pierdas, la vas a necesitar para recuperar esta cuenta en caso de que te olvides de la anterior ;)')
		print('y tiene que ser distinte a la contrasenia original')
		contraseniaRecupero = getpass('contrasenia de recupero:')
		if(self.validadorDeFormatoContrasenias(contraseniaRecupero) and contraseniaEnterior != contraseniaRecupero):
			return contraseniaRecupero
		else:
			return self.obtenerContraseniaDeRecupero()

	def validarContrasenias(self,contraseniaUno: str,contraseniaDos: str) -> bool:
		if(not contraseniaUno == contraseniaDos):
			print('Las contrasenias no coinciden')
			return False
		return self.validadorDeFormatoContrasenias(contraseniaUno)

	def validadorDeFormatoContrasenias(self,contrasenia: str):
		contieneEspeciales = False
		for caracter in self.caracteresEspeciales:
			if(caracter in contrasenia):
				contieneEspeciales = True
		if(contieneEspeciales and len(contrasenia)>8):
			return True
		else:
			print('No cumple con los requisitons de un caracter especial o 8 caracteres de largo')
			return False