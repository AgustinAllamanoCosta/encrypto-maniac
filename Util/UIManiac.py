import tkinter as tk
import threading

class PopUpManiac(threading.Thread):

	def __init__(self):
		threading.Thread.__init__(self)
		self.ventana = tk.Tk()
		self.ventana.geometry("200x80")
		self.mensajeAMostrar = ""
		self.start()
	
	def setMensaje(self, mensaje):
		self.mensajeAMostrar = mensaje

	def callback(self):
		self.ventana.quit()

	def cerrarVentana(self):
		self.ventana.destroy()

	def run(self):
		self.etiqueta = tk.Label(text=self.mensajeAMostrar)
		self.botonCerrar = tk.Button(text="Cerrar",
									width=5,
									height=1,
									bg="white",
									fg="black",
									command= self.cerrarVentana)


		self.botonCerrar.bind('<<botonCerrar1>>',self.cerrarVentana)
		self.etiqueta.pack(pady=5)
		self.botonCerrar.pack(expand=True,pady=5)
		self.ventana.after(4000, lambda: self.ventana.destroy())
		self.ventana.mainloop()
