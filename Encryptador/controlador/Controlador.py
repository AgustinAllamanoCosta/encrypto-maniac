
from Encryptador.servicio.CredencialesManiac import Credenciales
from Encryptador.servicio.ServicioEncrypto import ServicioEncrypto

class ControladorManiac(object):
    
    def __init__(self,servicio) -> None:
        self.servicio: ServicioEncrypto = servicio

    def ingresarClave(self,nombreApp,clave, credenciales: Credenciales):
        self.servicio.ingresarClave(nombreApp,clave,credenciales)

    def buscarClave(self,nombreApp, credenciales: Credenciales):
        self.servicio.buscarClave(nombreApp,credenciales)

    def listarCuentas(self, credenciales: Credenciales):
        self.servicio.listarCuentas(credenciales)

    def eliminarClave(self,parametro,credenciales: Credenciales):
        self.servicio.eliminarClave(parametro,credenciales)

    def actualizarClave(self,nombreApp,claveNueva, credenciales: Credenciales):
        self.servicio.actualizarClave(nombreApp,claveNueva,credenciales)

    def iniciarSesion(self,usuario: str, contrasena: str):
        self.servicio.iniciarSesion(usuario,contrasena)

    def registrarNuevoUsuario(self,usuario: str,contrasena: str,contrasenaDeRecupero: str):
        self.servicio.registrarNuevoUsuario(usuario,contrasena,contrasenaDeRecupero)
