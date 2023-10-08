import sys
import os
sys.path.insert(0, 'C:/Users/David/Downloads/Prog3_Parcial1-main/')

from Data import Aplicacion




def select_option(option):
    if option == 1:
        print("hay",Aplicacion.get_amount_of_registers(), "registros")
    elif option == 2:
        Aplicacion.show_registers()
        

def _menu():
    option=1
    while 3 != option:
        print("1. Mostrar numero de registros")
        print("2. Mostrar registros")
        print("3. Salir del menu")
        option=int(input("Ingrese la opcion\n"))
        select_option(option)
        if option:
            input("\nPresione enter para continuar")
        os.system('cls')


