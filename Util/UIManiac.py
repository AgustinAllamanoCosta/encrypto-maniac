import tkinter as tk
import threading

class PopUpManiac:

	def __init__(self):
		self.mensajeAMostrar = ""
	
	def setMensaje(self, mensaje):
		self.mensajeAMostrar = mensaje

	def mostrarPopUp(self):
		ventana = tk.Tk()
		ventana.geometry("200x80")
		self.etiqueta = tk.Label(text=self.mensajeAMostrar)
		self.botonCerrar = tk.Button(text="Cerrar",
									width=5,
									height=1,
									bg="white",
									fg="black",
									command= lambda: ventana.destroy())

		self.etiqueta.pack(pady=5)
		self.botonCerrar.pack(expand=True,pady=5)
		ventana.after(4000, lambda: ventana.destroy())
		ventana.mainloop()


