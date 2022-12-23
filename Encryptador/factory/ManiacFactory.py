import logging
from Encryptador.repository.BaseRepository import BaseRepository
from Encryptador.repository.KeyRepository import KeyRepository
from Encryptador.consola.ConsolaEncryptoManiac import ConsolaEncryptoManiac
from Encryptador.comandos.ComandoWin import ComandoWin
from Encryptador.comandos.ComandoUnix import ComandoUnix
from Encryptador.EncryptoManiac import EncryptoManiac
from Encryptador.consola.Historial import HistorialConsola

class ConsolaEncryptoManiacWin(ConsolaEncryptoManiac):

	def __init__(self,historalParam: HistorialConsola, encryptadorParam: EncryptoManiac):
		super().__init__(historalParam, encryptadorParam)
		self.comandosEstandar['systema'] = ComandoWin()

class ConsolaEncryptoManiacLinux(ConsolaEncryptoManiac):

	def __init__(self,historalParam: HistorialConsola, encryptadorParam: EncryptoManiac):
		super().__init__(historalParam, encryptadorParam)
		self.comandosEstandar['systema'] = ComandoUnix()

class FactoryEncriptador(object):

	def obtenerEncripto(self):
		encriptador = EncryptoManiac(BaseRepository(),KeyRepository())
		encriptador.iniciarBaseDeClaves()
		encriptador.cargarSesionSiExiste()
		return encriptador

class FactoryConsolaEncriptoManiac(object):

	def __init__(self):
		logging.basicConfig(filename='./Encryptador/logs/encrypto.log', level=logging.DEBUG)

	def obtenerConsola(self, plataforma):
		encriptador = FactoryEncriptador().obtenerEncripto()
		if('linux' == plataforma.lower()):
			return ConsolaEncryptoManiacLinux(HistorialConsola(),encriptador)
		elif('win32' == plataforma.lower()):
			return ConsolaEncryptoManiacWin(HistorialConsola(),encriptador)
