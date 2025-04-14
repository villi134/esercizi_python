

import os
import pandas as pd
import csv

percorso = "C:\\Users\\user\\Desktop\\Csv"

df_lista =[]


for  file in  os.listdir(percorso):

   if file.endswith('.csv'):
        # Crea il percorso completo del file
        percorso_file = os.path.join(percorso, file)

        print(f'{percorso_file}')
        
        # Leggi il CSV
        df = pd.read_csv(percorso_file, delimiter=';', index_col=0)
        
        # Aggiungi il DataFrame alla lista
        df_lista.append(df)


 #Combina tutti i DataFrame in uno solo
df_completo = pd.concat(df_lista, ignore_index=True)


for i, riga in df_completo.iterrows():
   if pd.isna(riga["IDRiga"]) or riga['TRiga'] != 1:
      continue
 
   

   #print(list(riga))
   descrizione = str(riga["Descrizione"])

   [desc, nome, misura_colore] = descrizione.split(",")
   df_completo.loc[i, "Descrizione"] = desc
   df_completo.loc[i, "Modello"] = nome

   [misura, colore] = misura_colore.strip().split(" ", maxsplit=1)
   df_completo.loc[i, "Finitura"] = colore

   [altezza, lunghezza, spessore] = misura.split("X")
   df_completo.loc[i, "Alt"] = altezza
   df_completo.loc[i, "Larg"] = lunghezza
   df_completo.loc[i, "Spes"] = spessore

   df_completo.loc[i, "Prezzo"] = f"{float(df_completo.loc[i, "Prezzo"].replace(",", ".")):.3f}".replace(".", ",")
   df_completo.loc[i, "Qta"] = str(int(float(df_completo.loc[i, "Qta"].replace(",", "."))))


  # TDoc	DataDoc	NumDoc	DataOrd	NumOrd	TRiga	IDRiga	CodArt	Descrizione	Qta	Prezzo	Alt	Larg	Spes	Modello	Finitura

     #TDoc	DataDoc	NumDoc	DataOrd	NumOrd	TRiga	IDRiga	CodArt  Descrizione	Modello  Finitura Alt	Larg	Spes Prezzo 	Qta


df_completo = df_completo[["TDoc", "DataDoc", "NumDoc", "DataOrd", "NumOrd", "TRiga", "IDRiga", "CodArt", "Descrizione", "Modello", "Finitura", "Alt", "Spes", "Prezzo", "Qta"]]

# Scrivi il DataFrame combinato in un file Excel
df_completo.to_excel("C:\\Users\\user\\Desktop\\Csv\\amen.xlsx", index=False)

print("File Excel creato con successo.")

# Stampa il DataFrame finale (opzionale)
print(df_completo)



print("File Excel creato con successo.")





