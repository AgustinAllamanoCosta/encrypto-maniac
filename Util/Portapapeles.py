import tkinter as tk

class PortaPapeles:

    def __init__(self):
        self.ventana = tk.Tk()

    def copiarPortaPapeles(self, mensajeACopiar):
        self.ventana.withdraw()
        self.ventana.clipboard_clear()
        self.ventana.clipboard_append(mensajeACopiar)
        self.ventana.update()
