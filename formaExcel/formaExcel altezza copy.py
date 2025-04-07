
import pandas as pd
from utils import *
import os

COL_BARCODE_CODICI = "codart"
COL_BARCODE_COLORI = "codart"

def trova_inizio_tabella(percorso_file):
    df = pd.read_excel(percorso_file, header=None)

    for i, riga in df.iterrows():
        if riga.notna().any():
            return i

    return None

def leggi_file_da_cartella(percorso):
    files = os.listdir(percorso)
    files_excel = list(filter(lambda x: x.endswith((".xls", ".xlsx")) and not x.startswith(("~$")) , files))
    if len(files_excel) == 0:
        print("NON CI SONO FILE EXCEL NELLA CARTELLA")
        return
    elif len(files_excel) == 1:
        file = files[0]
        skiprows = trova_inizio_tabella(percorso + file)
        df = pd.read_excel(percorso + files_excel[0], skiprows=skiprows, header=0)
    else:
        dataframes = []
        for file in files_excel:
            print(f"Leggo file: {file}")
            skiprows = trova_inizio_tabella(percorso + file)
            df = pd.read_excel(percorso + file, skiprows=skiprows, header=0)
            dataframes.append(pd.read_excel(percorso + file))
            print(f"\tè una tabella: {df.shape}")

        df = pd.concat(dataframes, ignore_index=True)
        df = df.dropna(how="all")
            
    return df

def unisci_modifica_file_excel(percorso_in_codici, percorso_in_colori, percorso_out):

    df_codici = leggi_file_da_cartella(percorso_in_codici)
    df_colori = leggi_file_da_cartella(percorso_in_colori)

    df_colori = df_colori.drop_duplicates()

    print(f"tabella codici: {df_codici.shape}")
    print(f"tabella colori: {df_colori.shape}")

    righe_disponibili = list(df_codici[COL_BARCODE_CODICI].copy())
    merged_rows = []
    for _, riga2 in df_colori.iterrows():
        trovato = False

        i = 0
        while i < len(righe_disponibili):
            riga1 = righe_disponibili[i]
            if riga2[COL_BARCODE_COLORI] == riga1:
                merged_rows.append([riga2[COL_BARCODE_COLORI], "S"])
                trovato = True
                righe_disponibili.pop(i)
                break
            i += 1

        """ for i, riga1 in df_codici.iterrows():
            if riga2[COL_BARCODE_COLORI] == riga1[COL_BARCODE_CODICI] and i not in righe_usate:
                merged_rows.append([riga2[COL_BARCODE_COLORI], "S"])
                trovato = True
                righe_usate.append(i)
                break """
        
        if trovato == False:
            merged_rows.append([riga2[COL_BARCODE_COLORI], ""])
        


    df_merge = pd.DataFrame(merged_rows, columns=[COL_BARCODE_COLORI, "Stampa"])


    print(df_merge)
    print(df_merge.shape)

    df_merge.to_excel(f"{percorso_out}stampati.xlsx", index=False)

        



if __name__ == "__main__":
    percorso_in_codici = "C:\\Users\\user\\Desktop\\EtichetteErrebi\\Nuovi_W18B_W19B\\Codici\\"
    percorso_in_colori = "C:\\Users\\user\\Desktop\\EtichetteErrebi\\Nuovi_W18B_W19B\\colori\\"

    percorso_out = "C:\\Users\\user\\Desktop\\EtichetteErrebi\\Nuovi_W18B_W19B\\"


    """ df1 = pd.DataFrame([
        [1, "A"],
        [1, "B"],
        [1, "C"],
        [2, "A"],
        [3, "A"],
        [3, "B"]
        ], columns=["A1", "B1"])
    df2 = pd.DataFrame([
        [4, 4],
        [2, 2],
        [2, 2],
        [5, 5],
        [1, "AA"],
        [1, "BB"]
        ], columns=["A2", "B2"])

    print(df1)
    print(df2)

    #df_merge = pd.merge(left=df1, left_on="A1", right=df2, right_on="A2", how="outer", indicator=True)
    righe_usate = []
    merged_rows = []
    for _, riga2 in df2.iterrows():
        trovato = False
        for i, riga1 in df1.iterrows():
            if riga2["A2"] == riga1["A1"] and i not in righe_usate:
                merged_rows.append([riga2["A2"], "S"])
                trovato = True
                righe_usate.append(i)
                break
        
        if trovato == False:
            merged_rows.append([riga2["A2"], ""])
        


    df_merge = pd.DataFrame(merged_rows, columns=["A2", "Stampa"])
    print(df_merge) """

    unisci_modifica_file_excel(percorso_in_codici, percorso_in_colori, percorso_out)