#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Encryptador.configuracion.Configuracion import Configuracion
import logging
import sqlite3

class BaseRepository(object):

    def __init__(self):
        self.rutaBBDD = Configuracion.rutaAlArchivoLaBaseDeDatos

    def _ejcutarConsultaBase(self,conexion: sqlite3.Connection, query: str,params: tuple):
        try:
            cursor = conexion.execute(query,params)
            conexion.commit()
            return cursor
        except Exception as e:
            logging.error(f'Error {e}')
            raise e

    def obtenerUnElemento(self,query,params):
        baseDeDatos = sqlite3.connect(self.rutaBBDD)
        cursor = self._ejcutarConsultaBase(baseDeDatos,query,params)
        respuesta = cursor.fetchone()
        baseDeDatos.close()
        return respuesta

    def obtenerUnGrupoDeElementos(self,query,params):
        baseDeDatos = sqlite3.connect(self.rutaBBDD)
        cursor = self._ejcutarConsultaBase(baseDeDatos,query,params)
        respuesta = cursor.fetchall()
        baseDeDatos.close()
        return respuesta

    def ejecutarConsultaConParametros(self,query,params):
        baseDeDatos = sqlite3.connect(self.rutaBBDD)
        self._ejcutarConsultaBase(baseDeDatos,query,params)
        baseDeDatos.close()

    def ejecutarConsulta(self,query):
        self.ejecutarConsultaConParametros(query,())
    
    def obtenerTodos(self,query):
        return self.obtenerUnGrupoDeElementos(query,())
