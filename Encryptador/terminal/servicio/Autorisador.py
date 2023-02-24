from Encryptador.servicio.CredencialesManiac import Credenciales
from Encryptador.configuracion.Configuracion import Configuracion
from Encryptador.consola.EstadoDeSesion import EstadoDeSesion
from Encryptador.exceptions.LoginErrorException import LoginErrorException
from Encryptador.exceptions.NoUsuariosRegistradosException import NoUsuarioRegistradosException
from Encryptador.repository.BaseRepository import BaseRepository
from Encryptador.repository.KeyRepository import KeyRepository
from Encryptador.exceptions.UsuarioNoAutorizadoException import UsuarioNoAutorizadoException
from Util import ConstantesEncryptoManiac as CEM
import secrets

class Autorisador(object):

	def __init__(self,baseRepositoryParam: BaseRepository, keyReposioryParam: KeyRepository):
		self.baseRepository: BaseRepository = baseRepositoryParam
		self.keyRepository: KeyRepository = keyReposioryParam
		self.tokensDeSesion: dict = {}

	def iniciarSesion(self,usuario,contrasenia):

		if(self.existeUnUsuarioRegistrado()):
			archivoDelUsuario = self.baseRepository.obtenerUnElemento(CEM.ConsultaDB.buscarArchivo,(usuario,))[0]
			if(archivoDelUsuario == None):
				raise NoUsuarioRegistradosException()	
			self.keyRepository._cargarClave(archivoDelUsuario)
			self.confirmarContrasena(usuario,contrasenia)
			self.tokensDeSesion[usuario] = secrets.token_urlsafe()
		else:
			raise NoUsuarioRegistradosException()

	def registrarUsuario(self,usuario: str,contrasenia: str, contraseniaRecupero: str):

		nombreArchivosDeCrendenciales = Configuracion.rutaAlArchivoDeCredenciales + usuario + CEM.ConstantesEM.nombreArchivoKey

		self.keyRepository._generarClave(nombreArchivosDeCrendenciales)
		self.keyRepository._cargarClave(nombreArchivosDeCrendenciales)
		
		contraseniaEncriptada = self.keyRepository.encriptarASE(contrasenia)
		contraseniaRecuperoEncriptada = self.keyRepository.encriptarASE(contraseniaRecupero)

		datosARegistrar = (usuario,contraseniaEncriptada,contraseniaRecuperoEncriptada, nombreArchivosDeCrendenciales)

		self.baseRepository.ejecutarConsultaConParametros(CEM.ConsultaDB.ingresarUsuario,datosARegistrar)
		self.tokensDeSesion[usuario] = ''

	def existeUnUsuarioRegistrado(self):
		respuestaBase = self.baseRepository.obtenerUnGrupoDeElementos(CEM.ConsultaDB.listarUsuarios,())
		return len(respuestaBase)>0 and respuestaBase[0] is not None

	def obtenerUsuarioRegistrado(self):
		respuestaBase = self.baseRepository.obtenerUnGrupoDeElementos(CEM.ConsultaDB.listarUsuarios,())
		return respuestaBase[0]

	def obtenerSesionToken(self,nombreUsuario:str):
		return self.tokensDeSesion[nombreUsuario]

	def estaAutorizadoElUsuario(self):
		return self.tokensDeSesion is not None

	def confirmarContrasena(self,usuario,contrasenia) -> bool:
		contraseniaEnBase = self.baseRepository.obtenerUnElemento(CEM.ConsultaDB.buscarUsuario,(usuario,))[0]
		if(contraseniaEnBase is not None or contraseniaEnBase is not ''):
			contraseniaLimpia = self.keyRepository.desencriptarASE(contraseniaEnBase)
			return contraseniaLimpia == contrasenia
		else:
			raise LoginErrorException('Usuario o contrasena incorrectos')

	def validarUsuario(self, credencialesDeLaAccion: Credenciales):
		contraseniaValida = self.confirmarContrasena(credencialesDeLaAccion.usuario,credencialesDeLaAccion.contrasena)
		tokenValido = credencialesDeLaAccion.token == self.tokensDeSesion[credencialesDeLaAccion.usuario]
		usuarioValido = self.estaAutorizadoElUsuario() and tokenValido and contraseniaValida
		if(not usuarioValido ):
			raise UsuarioNoAutorizadoException()
