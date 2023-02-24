
class EstadoDeSesion(object):

    def __init__(self, usuarioParam:str = '', sesionActivaParam = False):

        self.usuario = usuarioParam
        self.tokenDelUsuario = None
        self.sesionActiva = sesionActivaParam