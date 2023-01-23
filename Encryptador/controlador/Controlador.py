
from Encryptador.servicio.CredencialesManiac import Credenciales
from Encryptador.servicio.ServicioEncrypto import ServicioEncrypto

class ControladorManiac(object):
    
    def __init__(self,servicio) -> None:
        self.servicio: ServicioEncrypto = servicio

    def ingresarClave(self,nombreApp,clave, token: str):
        credenciales: Credenciales = Credenciales()
        credenciales.token = token
        self.servicio.ingresarClave(nombreApp,clave,credenciales)

    def buscarClave(self,nombreApp, credenciales: Credenciales):
        pass

    def listarCuentas(self, credenciales: Credenciales):
        pass

    def eliminarClave(self,parametro,credenciales: Credenciales):
        pass

    def actualizarClave(self,nombreApp,claveNueva, credenciales: Credenciales):
        pass

    def iniciarSesion(self,usuario: str, contrasena: str):
        pass

    def registrarNuevoUsuario(self,usuario: str,contrasena: str,contrasenaDeRecupero: str):
        pass
