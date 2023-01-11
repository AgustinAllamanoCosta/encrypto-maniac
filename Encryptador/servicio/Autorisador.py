from Encryptador.servicio.CredencialesManiac import Credenciales
from Encryptador.configuracion.Configuracion import Configuracion
from Encryptador.consola.EstadoDeSesion import EstadoDeSesion
from Encryptador.exceptions.LoginErrorException import LoginErrorException
from Encryptador.repository.BaseRepository import BaseRepository
from Encryptador.repository.KeyRepository import KeyRepository
from Encryptador.exceptions.UsuarioNoAutorizadoException import UsuarioNoAutorizadoException
from Util import ConstantesEncryptoManiac as CEM

class Autorisador(object):

	def __init__(self,baseRepositoryParam: BaseRepository, keyReposioryParam: KeyRepository):
		self.baseRepository: BaseRepository = baseRepositoryParam
		self.keyRepository: KeyRepository = keyReposioryParam
		self.estadoSesion: EstadoDeSesion = None

	def iniciarSesion(self,usuario,contrasenia):

		if(self.existeUnUsuarioRegistrado()):
			archivoDelUsuario = self.baseRepository.obtenerUnElemento(CEM.ConsultaDB.buscarArchivo,(usuario,))[0]
			self.keyRepository._cargarClave(archivoDelUsuario)
			self.estadoSesion.sesionActiva = self.confirmarContrasena(usuario,contrasenia)
			self.estadoSesion.tokenDelUsuario = f'someUUID.{usuario}'
		else:
			self.estadoSesion.sesionActiva = False
			raise LoginErrorException('Usuario o contrasena incorrectos')

	def registrarUsuario(self,usuario: str,contrasenia: str, contraseniaRecupero: str):

		nombreArchivosDeCrendenciales = Configuracion.rutaAlArchivoDeCredenciales + usuario + CEM.ConstantesEM.nombreArchivoKey

		self.keyRepository._generarClave(nombreArchivosDeCrendenciales)
		self.keyRepository._cargarClave(nombreArchivosDeCrendenciales)
		
		contraseniaEncriptada = self.keyRepository.encriptarASE(contrasenia)
		contraseniaRecuperoEncriptada = self.keyRepository.encriptarASE(contraseniaRecupero)

		datosARegistrar = (usuario,contraseniaEncriptada,contraseniaRecuperoEncriptada, nombreArchivosDeCrendenciales)

		self.baseRepository.ejecutarConsultaConParametros(CEM.ConsultaDB.ingresarUsuario,datosARegistrar)
		self.estadoSesion = EstadoDeSesion(usuario)

	def existeUnUsuarioRegistrado(self):
		respuestaBase = self.baseRepository.obtenerUnGrupoDeElementos(CEM.ConsultaDB.listarUsuarios,())
		return len(respuestaBase)>0 and respuestaBase[0] is not None

	def obtenerUsuarioRegistrado(self):
		respuestaBase = self.baseRepository.obtenerUnGrupoDeElementos(CEM.ConsultaDB.listarUsuarios,())
		return respuestaBase[0]

	def estaAutorizadoElUsuario(self):
		return self.estadoSesion is not None and self.estadoSesion.sesionActiva

	def cargarSesionSiExiste(self):
		if(self.existeUnUsuarioRegistrado()):
			self.estadoSesion = EstadoDeSesion(self.obtenerUsuarioRegistrado()[0])
		else:
			self.estadoSesion = None

	def confirmarContrasena(self,usuario,contrasenia) -> bool:
		contraseniaEnBase = self.baseRepository.obtenerUnElemento(CEM.ConsultaDB.buscarUsuario,(usuario,))[0]
		if(contraseniaEnBase is not None or contraseniaEnBase is not ''):
			contraseniaLimpia = self.keyRepository.desencriptarASE(contraseniaEnBase)
			return contraseniaLimpia == contrasenia
		else:
			raise LoginErrorException('Usuario o contrasena incorrectos')

	def validarUsuario(self, credencialesDeLaAccion: Credenciales):
		contraseniaValida = self.confirmarContrasena(credencialesDeLaAccion.usuario,credencialesDeLaAccion.contrasena)
		tokenValido = credencialesDeLaAccion.token == self.estadoSesion.tokenDelUsuario
		usuarioValido = self.estaAutorizadoElUsuario() and tokenValido and contraseniaValida
		if(not usuarioValido ):
			raise UsuarioNoAutorizadoException()
