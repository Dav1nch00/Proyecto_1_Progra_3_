import Data.OrganizarDatos as dt
import pandas as pd

def show_registers():
    number_of_registers=int(input("Ingrese el numero de registros que quiere ver\n"))
    print(dt.df.head(number_of_registers))

def get_amount_of_registers():
    return (len(dt.df.index))

