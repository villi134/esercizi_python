

from utils import *
import pandas as pd
import os

# Colonne da confrontare
COL_BARCODE_CODICI = "pn cliente"   # nel file "codici"
COL_BARCODE_SOSPESI = "DEST2"       # nel file "sospesi"
COL_STAMPA_SOSPESI = "STAMPA"       # colonna di output

# Trova da dove parte la tabella (salta eventuali righe iniziali vuote)
def trova_inizio_tabella(percorso_file):
    df = pd.read_excel(percorso_file, header=None)
    for i, riga in df.iterrows():
        if riga.notna().any():
            return i
    return None

# Legge tutti i file Excel da una cartella
def leggi_file_da_cartella(percorso):
    files = os.listdir(percorso)
    files_excel = [f for f in files if f.endswith((".xls", ".xlsx")) and not f.startswith(("~$"))]

    if not files_excel:
        print("NESSUN FILE EXCEL TROVATO")
        return pd.DataFrame()

    dataframes = []
    for file in files_excel:
        print(f"Leggo file: {file}")
        full_path = os.path.join(percorso, file)
        skiprows = trova_inizio_tabella(full_path)
        df = pd.read_excel(full_path, skiprows=skiprows, header=0)
        dataframes.append(df)

    # Unisce tutti i file in un unico DataFrame
    df = pd.concat(dataframes, ignore_index=True)
    return df.dropna(how="all")

# Funzione principale
def unisci_modifica_file_excel(percorso_in_codici, percorso_in_sospesi, percorso_out_sospesi):
    df_codici = leggi_file_da_cartella(percorso_in_codici)
    df_sospesi = leggi_file_da_cartella(percorso_in_sospesi)

    # Codici unici per confronto
    codici_validi = set(df_codici[COL_BARCODE_CODICI].dropna().astype(str))

    print(f"Totale codici validi: {len(codici_validi)}")

    files = os.listdir(percorso_in_sospesi)
    files_excel = [f for f in files if f.endswith((".xls", ".xlsx")) and not f.startswith(("out_", "~$"))]

    for file in files_excel:
        full_path = os.path.join(percorso_in_sospesi, file)
        skiprows = trova_inizio_tabella(full_path)
        df_out = pd.read_excel(full_path, skiprows=skiprows, header=0)

        # Inizializza la colonna "STAMPA"
        df_out[COL_STAMPA_SOSPESI] = ""

        # Confronta i codici
        df_out[COL_BARCODE_SOSPESI] = df_out[COL_BARCODE_SOSPESI].astype(str)
        df_out.loc[df_out[COL_BARCODE_SOSPESI].isin(codici_validi), COL_STAMPA_SOSPESI] = "S"

        print(f"{file}: {df_out[COL_STAMPA_SOSPESI].value_counts().to_dict()}")

        output_file = os.path.join(percorso_out_sospesi, f"out_{os.path.splitext(file)[0]}.xlsx")
        df_out.to_excel(output_file, index=False)
        print(f"Salvato file: {output_file}")

# Percorsi
if __name__ == "__main__":
    percorso_in_codici = r"C:\Users\user\Desktop\EtichetteErrebi\Nuovi_W18B_W19B\Codici\\"
    percorso_in_sospesi = r"C:\Users\user\Desktop\EtichetteErrebi\Nuovi_W18B_W19B\sospesi\\"
    percorso_out_sospesi = r"C:\Users\user\Desktop\EtichetteErrebi\Nuovi_W18B_W19B\sospesi\completati\\"

    unisci_modifica_file_excel(percorso_in_codici, percorso_in_sospesi, percorso_out_sospesi)
