from strings import *

def ficheromascota():
    with open("mascota.txt", "a") as file:
        mascota = input("Dime el nombre de la mascota")
        while mascota.isalpha() == False:
            print("No es una palabra, introduzcala otra vez")
            mascota = input("Dime el nombre de la mascota")
        cambia_letras(mascota,file)
    file.close()