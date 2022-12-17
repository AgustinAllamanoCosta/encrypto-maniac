
class EstadoDeSesion(object):

    def __init__(self, usuarioParam:str):

        self.usuario = usuarioParam
        self.sesionActiva = False