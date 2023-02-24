from Encryptador.terminal.repository.BaseRepository import BaseRepository
from Encryptador.terminal.repository.KeyRepository import KeyRepository
from Encryptador.terminal.consola.ConsolaEncryptoManiac import ConsolaEncryptoManiac
from Encryptador.terminal.comandos.ComandoWin import ComandoWin
from Encryptador.terminal.comandos.ComandoUnix import ComandoUnix
from Encryptador.terminal.servicio.EncryptoManiac import EncryptoManiac
from Encryptador.terminal.servicio.Autorisador import Autorisador
from Encryptador.terminal.servicio.ServicioEncrypto import ServicioEncrypto
from Encryptador.terminal.consola.Historial import HistorialConsola
import logging

class ConsolaEncryptoManiacWin(ConsolaEncryptoManiac):

	def __init__(self,historalParam: HistorialConsola, servicioEncryptadorParam: ServicioEncrypto):
		super().__init__(historalParam, servicioEncryptadorParam)
		self.comandosEstandar['systema'] = ComandoWin()

class ConsolaEncryptoManiacLinux(ConsolaEncryptoManiac):

	def __init__(self,historalParam: HistorialConsola, servicioEncryptadorParam: ServicioEncrypto):
		super().__init__(historalParam, servicioEncryptadorParam)
		self.comandosEstandar['systema'] = ComandoUnix()

class FactoryServicio(object):

	def obtenerServicio(self):
		baseRepo: BaseRepository = BaseRepository()
		keyRepo: KeyRepository = KeyRepository()
		encriptador = EncryptoManiac(baseRepo,keyRepo)
		encriptador.iniciarBaseDeClaves()
		autorizador: Autorisador = Autorisador(baseRepo,keyRepo)
		servicio: ServicioEncrypto = ServicioEncrypto(autorizador,encriptador)
		return servicio

class FactoryConsolaEncriptoManiac(object):

	def __init__(self):
		logging.basicConfig(filename='./Encryptador/logs/encrypto.log', level=logging.DEBUG)

	def obtenerConsola(self, plataforma: str):
		servicio: ServicioEncrypto = FactoryServicio().obtenerServicio()
		if('linux' == plataforma.lower()):
			return ConsolaEncryptoManiacLinux(HistorialConsola(),servicio)
		elif('win32' == plataforma.lower()):
			return ConsolaEncryptoManiacWin(HistorialConsola(),servicio)
