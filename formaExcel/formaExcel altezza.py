
import pandas as pd
from utils import *
import os

def trova_inizio_tabella(percorso_file):
    df = pd.read_excel(percorso_file, header=None)

    for i, riga in df.iterrows():
        if riga.notna().any():
            return i

    return None

def unisci_modifica_file_excel(percorso_in, percorso_out):

    files = os.listdir(percorso_in)
    print(files)


    files_excel = list(filter(lambda x: x.endswith((".xls", ".xlsx")) and not x.startswith(("out_", "~$")) , files))

    print(files_excel)

    if len(files_excel) == 0:
        print("NON CI SONO FILE EXCEL NELLA CARTELLA")
        return
    elif len(files_excel) == 1:
        skiprows = trova_inizio_tabella(percorso_in + file)
        df = pd.read_excel(percorso_in + files_excel[0], skiprows=skiprows, header=0)
        week = df["orcamp04"][0]
        nome_file_output = f"out_settimana_{week}"

    else:
        dataframes = []
        for file in files_excel:
            print(f"Leggo file: {file}")
            skiprows = trova_inizio_tabella(percorso_in + file)
            print(skiprows)
            df = pd.read_excel(percorso_in + file, skiprows=skiprows, header=0)
            dataframes.append(pd.read_excel(percorso_in + file))
            print(f"\tè una tabella: {df.shape}")
        
        # dataframes = [pd.read_excel(percorso_in + file) for file in files_excel]

        df = pd.concat(dataframes, ignore_index=True)
        df = df.dropna(how="all")
        
        weeks = "_".join(sorted(list(set(df["orcamp04"]))))
        nome_file_output = f"out_settimane_{weeks}"

    altezze = set(df[df["altezz"] != 0]["altezz"])

    for altezza in altezze:
        df_altezza_singola = df[df["altezz"] == altezza]

        print(f"Stampo sul file: {nome_file_output}_{altezza}.xlsx: {df_altezza_singola.shape}")
        df_altezza_singola.to_excel(f"{percorso_out}{nome_file_output}_{altezza}.xlsx", index=False)


if __name__ == "__main__":
    percorso_in = "C:\\Users\\user\\Desktop\\EtichetteErrebi\\Nuovi_W18B_W19B\\"
    percorso_out = "C:\\Users\\user\\Desktop\\EtichetteErrebi\\Nuovi_W18B_W19B\\altezze\\"

    unisci_modifica_file_excel(percorso_in, percorso_out)