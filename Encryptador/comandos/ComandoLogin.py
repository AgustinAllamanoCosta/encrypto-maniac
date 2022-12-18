import getpass
from Encryptador.comandos.Comando import Comando
from Encryptador import EncryptoManiac as EM
from Encryptador.consola.EstadoDeSesion import EstadoDeSesion

class ComandoLogin(Comando):

	def __init__(self, encryptador: EM.EncryptoManiac, sesionUsuarioParam: EstadoDeSesion ):
		self.encriptoManiac: EM.EncryptoManiac = encryptador
		self.sesionUsuario: EstadoDeSesion = sesionUsuarioParam
		self.mensajeComando = ""

	def ejecutar(self,parametros):
		usuario = self.obtenerUsuario()
		self.sesionUsuario.sesionActiva = self.encriptoManiac.iniciarSesion(usuario,self.obtenerContrasenia())
		self.sesionUsuario.usuario = usuario

	def obtenerUsuario(self):
		return input('Usuario: ')

	def obtenerContrasenia(self):
		return getpass('Contrasenia: ')