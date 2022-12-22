class ManiacException(Exception):
	
	def __init__(self, mensaje:str) -> None:
		super().__init__(mensaje)
		self.mensaje = mensaje