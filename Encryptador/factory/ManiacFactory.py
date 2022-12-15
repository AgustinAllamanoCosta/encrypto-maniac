from Encryptador.repository import BaseRepository, KeyRepository
from Encryptador.consola.ConsolaEncryptoManiac import ConsolaEncryptoManiac
from Encryptador.comandos.ComandosManiac import ComandoWin, ComandoUnix
from Encryptador import EncryptoManiac
import logging

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

		baseRepository = BaseRepository.BaseRepository()
		keyReposiory = KeyRepository.KeyRepository()

		encriptador = EncryptoManiac.EncryptoManiac(baseRepository,keyReposiory)
		return encriptador

class FactoryConsolaEncriptoManiac(object):

	def obtenerConsola(self,plataforma):
		logging.basicConfig(filanme='encrypto.log', encoding='utf-8', level=logging.DEBUG)
		logging.info('Plataforma '+plataforma)

		historial = HistorialConsola()
		encriptador = FactoryEncriptador().obtenerEncripto()

		if('linux' == plataforma.lower()):
			return ConsolaEncryptoManiacLinux(historial,encriptador)
		elif('win32' == plataforma.lower()):
			return ConsolaEncryptoManiacWin(historial,encriptador)