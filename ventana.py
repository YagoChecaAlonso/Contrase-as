
import os
import tkinter 

from ficheros import ficheromascota

ventana = tkinter.Tk()
ventana.title("Contraseñas")
ventana.geometry("400x600")
ventana.resizable(True,True)
mensaje = tkinter.Label(ventana, text="Introduce el nombre de la mascota")
mensaje.pack(side=tkinter.TOP)

boton1 = tkinter.Button(ventana, text="Aceptar", command = ficheromascota)
boton1.pack()
boton2 = tkinter.Button(ventana, text="Salir", command = ventana.destroy)
boton2.pack(side=tkinter.BOTTOM)

ventana.mainloop()








