from Util.ConstantesEncryptoManiac import ConstantesEM

class Configuracion(object):
    rutaALaBaseDeDatos = f'./Encryptador/baseDeDatos/{ConstantesEM.baseEncryptoManiac}'
    rutaAlArchivoDeConfiguracion = f'./Encryptador/key/{ConstantesEM.nombreArchivoKey}'
    limpiarTerminal = False