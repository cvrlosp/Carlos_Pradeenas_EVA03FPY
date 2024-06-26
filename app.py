'''
Este algoritmo gestiona el inventario de la tienda Pinturas Acrílicas Mandarina
'''
from modules.construccion import construir_menu, sol_ans
from modules.data import menup, ruta_c, ruta_j
from modules.buscar import slt_vals, buscar
from modules.eliminar import slt_code, eliminar
from modules.exportar import exportar
from modules.agregar import agregar
import os

while True:
    construir_menu(menup)
    ans = sol_ans()
    if ans == '1':
        print(ruta_j)
    elif ans == '2':
        buscar(slt_vals(), ruta_j)
    elif ans == '3':
        agregar(ruta_j)
    elif ans == '4':
        eliminar(slt_code(), ruta_j)
    elif ans == '5':
        exportar(ruta_c, ruta_j)
    elif ans == '6':
        os.system('cls')
        exit('Hasta pronto\n')
    else:
        os.system('cls')
        print('Opcion incorrecta\n')