import msvcrt
import funciones as fn
import os
import numpy as np

os.system("cls")

cine = np.zeros((12,6), int)

lista_rut = []
lista_correos = []
lista_telefonos = []
lista_filas = []
lista_columnas = []

while True:
    opcion = fn.menu()

    if opcion==1:
        fn.ver_sala(cine)
    elif opcion==2:
        pass
    elif opcion==3:
        pass
    elif opcion==4:
        pass
    else:
        print("GRACIAS, ADIOS!")
        break