
#programa que te pille una palabra y cambie mayusculas minusculas, de todas las maneras posibles, y te lo guarde en un fichero
import os
import tkinter #as tk

def cambia_letras(animal, file):
    file.write(animal)
    file.write("\n")
    animal = animal.lower()
    file.write(animal)
    file.write("\n")
    animal = animal.upper()
    file.write(animal)
    file.write("\n")
    animal = animal.capitalize()     
    file.write(animal)
    file.write("\n")
    animal = animal.title()
    file.write(animal)
    file.write("\n")
    animal = animal.swapcase()
    file.write(animal)
    file.write("\n")
    
def ficheromascota():
    with open("mascota.txt", "a") as file:
        mascota = input("Dime el nombre de la mascota")
        #mascota.strip()
        while mascota.isalpha() == False:
            print("No es una palabra, introduzcala otra vez")
            mascota = input("Dime el nombre de la mascota")
            #mascota = mascota.strip()
        cambia_letras(mascota,file)
    file.close()


ventana = tkinter.Tk()
ventana.title("Contraseñas")
ventana.geometry("400x600")
#ventana.configure(bg='blue')  # Cambia el color de fondo a azul
mensaje = tkinter.Label(ventana, text="Introduce el nombre de la mascota")
mensaje.pack(side=tkinter.TOP)

boton1 = tkinter.Button(ventana, text="Aceptar", command = ficheromascota)
boton1.pack()
boton2 = tkinter.Button(ventana, text="Salir", command = ventana.destroy)
boton2.pack(side=tkinter.BOTTOM)

ventana.mainloop()








