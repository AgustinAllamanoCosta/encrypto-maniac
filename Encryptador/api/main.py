import datetime
from fastapi import FastAPI
from Encryptador.controlador.Controlador import ControladorManiac
from Encryptador.servicio.ServicioEncrypto import ServicioEncrypto

app = FastAPI()
servicio = ServicioEncrypto()
controlador = ControladorManiac(servicio)

@app.get("/healthCheck")
def read_root(self):
    return {"Time": datetime.datetime.now(), "Greeting": "Hello There"}

@app.get("/ingresar")
def ingresarClave(self,nombreApp,clave):
    controlador.ingresarClave(nombreApp,clave)

@app.get("/buscar")
def buscarClave(self,nombreApp):
    controlador.buscarClave()

@app.get("/listar")
def listarCuentas(self):
    controlador.listarCuentas()

@app.get("/eliminar")
def eliminarClave(self,parametro):
    controlador.eliminarClave()

@app.get("/actulizar")
def actualizarClave(self,nombreApp,claveNueva):
    controlador.actualizarClave()

@app.get("/login")
def iniciarSesion(self,usuario: str, contrasena: str):
    controlador.iniciarSesion()

@app.get("/sigin")
def registrarNuevoUsuario(self,usuario: str,contrasena: str,contrasenaDeRecupero: str):
    controlador.registrarNuevoUsuario()