
import tkinter as tk
from interfaz import AplicacionClientes


def iniciar_aplicacion():

    ventana = tk.Tk()

    app = AplicacionClientes(ventana)

    ventana.mainloop()


if __name__ == "__main__":
    iniciar_aplicacion()
