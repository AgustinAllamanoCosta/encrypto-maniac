from Encryptador.consola.EstadoDeSesion import EstadoDeSesion
from Encryptador.repository import BaseRepository, KeyRepository
from Encryptador.consola.ConsolaEncryptoManiac import ConsolaEncryptoManiac
from Encryptador.comandos.ComandoWin import ComandoWin
from Encryptador.comandos.ComandoUnix import ComandoUnix
from Encryptador import EncryptoManiac
import logging

from Encryptador.consola.Historial import HistorialConsola

class ConsolaEncryptoManiacWin(ConsolaEncryptoManiac):

	def __init__(self,historalParam: HistorialConsola, encryptadorParam: EncryptoManiac, estadoDeSesionParam: EstadoDeSesion):
		super().__init__(historalParam, encryptadorParam, estadoDeSesionParam)
		self.comandosEstandar['systema'] = ComandoWin()

class ConsolaEncryptoManiacLinux(ConsolaEncryptoManiac):

	def __init__(self,historalParam: HistorialConsola, encryptadorParam: EncryptoManiac, estadoDeSesionParam: EstadoDeSesion):
		super().__init__(historalParam, encryptadorParam, estadoDeSesionParam)
		self.comandosEstandar['systema'] = ComandoUnix()

class FactoryEncriptador(object):

	def obtenerEncripto(self):

		baseRepository = BaseRepository.BaseRepository()
		keyReposiory = KeyRepository.KeyRepository()

		encriptador = EncryptoManiac.EncryptoManiac(baseRepository,keyReposiory)
		encriptador.iniciarBaseDeClaves()
		return encriptador

class FactoryConsolaEncriptoManiac(object):

	def obtenerConsola(self, plataforma):

		logging.basicConfig(filename='encrypto.log', level=logging.DEBUG)
		logging.info('Plataforma '+plataforma)

		historial = HistorialConsola()
		encriptador = FactoryEncriptador().obtenerEncripto()
		sesionUsuario = EstadoDeSesion('')

		if('linux' == plataforma.lower()):
			return ConsolaEncryptoManiacLinux(historial,encriptador,sesionUsuario)
		elif('win32' == plataforma.lower()):
			return ConsolaEncryptoManiacWin(historial,encriptador,sesionUsuario)