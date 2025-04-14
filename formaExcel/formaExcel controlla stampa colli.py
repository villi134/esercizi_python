
import pandas as pd
from utils import *
import os

COL_BARCODE_CODICI = "codice imballo"

COL_BARCODE_SOSPESI = "BAR1"
COL_STAMPA_SOSPESI = "STAMPA"

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
        file = files_excel[0]
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

def unisci_modifica_file_excel(percorso_in_codici, percorso_in_sospesi, percorso_out_sospesi):

    df_codici_x = pd.read_excel(percorso_in_codici, sheet_name=0, skiprows=0, header=0)
    df_codici_s = pd.read_excel(percorso_in_codici, sheet_name=1, skiprows=0, header=0)

    print(f"tabella codici: {df_codici_x.shape}")
    print(f"tabella codici: {df_codici_s.shape}")

    files = os.listdir(percorso_in_sospesi)
    files_excel = list(filter(lambda x: x.endswith((".xls", ".xlsx")) and not x.startswith((("out_", "~$"))) , files))
    for file in files_excel:
        skiprows = trova_inizio_tabella(percorso_in_sospesi + file)
        df_out = pd.read_excel(percorso_in_sospesi + file, skiprows=skiprows, header=0)

        df_out[COL_STAMPA_SOSPESI] = ""
        #df_out["STAMPA_X"] = ""
        print(df_out)

        df_out.loc[df_out[COL_BARCODE_SOSPESI].isin(df_codici_s[COL_BARCODE_CODICI]), COL_STAMPA_SOSPESI] = "S"
        #df_out.loc[df_out[COL_BARCODE_SOSPESI].isin(df_codici_x[COL_BARCODE_CODICI]), "STAMPA_X"] = "X"
        
        print(df_out)

        df_out.to_excel(percorso_out_sospesi + "out_" + file.split(".")[0] + ".xlsx", index=False)



if __name__ == "__main__":
    percorso_in_codici = "C:\\Users\\user\\Desktop\\EtichetteErrebi\\Nuovi_W18B_W19B\\\Codici\\CUBO AL 14.04.xls"

    percorso_in_sospesi = "C:\\Users\\user\\Desktop\\EtichetteErrebi\\Nuovi_W18B_W19B\\sospesi\\"
    percorso_out_sospesi = "C:\\Users\\user\\Desktop\\EtichetteErrebi\\Nuovi_W18B_W19B\\sospesi\\completati\\"


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

    unisci_modifica_file_excel(percorso_in_codici, percorso_in_sospesi, percorso_out_sospesi)