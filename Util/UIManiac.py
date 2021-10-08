import tkinter as tk
import threading

class PopUpManiac:

	def __init__(self):
		self.mensajeAMostrar = ""
		self.tiempoVidaVentana = 4000

	def setMensaje(self, mensaje):
		self.mensajeAMostrar = mensaje

	def copiarPortaPapeles(self):
		self.ventana.withdraw()
		self.ventana.clipboard_clear()
		self.ventana.clipboard_append(self.mensajeAMostrar)
		self.ventana.update()

	def centrarVentana(self):
		ancho_ventana = 200
		alto_ventana = 80

		x_ventana = self.ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
		y_ventana = self.ventana.winfo_screenheight() // 2 - alto_ventana // 2

		posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
		self.ventana.geometry(posicion)

	def configurarWidget(self):
		self.etiqueta = tk.Label(text=self.mensajeAMostrar)
		self.botonCerrar = tk.Button(text="Cerrar",
									width=5,
									height=1,
									bg="white",
									fg="black",
									command= lambda: self.ventana.destroy())

		self.botonCopiarContrasenia = tk.Button(text="Copiar",
									width=5,
									height=1,
									bg="white",
									fg="black",
									command= lambda: self.copiarPortaPapeles())

		self.etiqueta.pack(pady=5)
		self.botonCerrar.pack(expand=True,side="left",pady=5)
		self.botonCopiarContrasenia.pack(expand=True,side="right",pady=5)

	def mostrarPopUp(self):
		self.ventana = tk.Tk()
		self.ventana.title("Encrypto Maniac")

		self.centrarVentana()

		self.configurarWidget()		


		self.ventana.after(self.tiempoVidaVentana, lambda: self.ventana.destroy())
		self.ventana.mainloop()

r = PopUpManiac()
r.setMensaje("asdasdasdasdasd")
r.mostrarPopUp()
