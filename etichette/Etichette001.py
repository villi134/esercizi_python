
import pandas as pd
from utils import *

def modifica_file_excel(percorso, nome_file_input):
    nome_no_ext = nome_file_input.split(".")[0]

    max_val = trova_valore_max_modifica_file(percorso, nome_no_ext)
    incremento = max_val + 1

    incremento = da_int_a_formato_numero_str(incremento)

    nome_file_output = f"{nome_no_ext}_modifica_{incremento}.xlsx"



    df = pd.read_excel(percorso + nome_file_input)


    print(df.head())

    #df = pd.read_excel(percorso, usecols=[""codart", "codric"])
    df = df[ ["codart", "codric","c_alt",	"c_largh","c_prof"	] ]

    print(f"Stampo sul file: {nome_file_output}")
    df.to_excel(percorso + nome_file_output, index=False, sheet_name="etichetta 01")

if __name__ == "__main__":
    percorso = "C:\\Users\\user\\Desktop\\EtichetteErrebi\\"
    #nome_file_input = "etic 25037262.xls"
    nome_file_input = "w18b.xls"
    modifica_file_excel(percorso, nome_file_input)