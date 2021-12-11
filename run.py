#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Encryptador import ConsolaEncryptoManiac as CEM
from Web import EncriptoWeb

def run():
	consola = CEM.FactoryConsolaEncriptoManiac().obtenerConsola(sys.platform)
	consola.bucleDeConsola()

run()
