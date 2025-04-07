import PyPDF2
import re
import pandas as pd
import os

percorso = "C:\\Users\\user\\Desktop\\EtichetteErrebi\\PianiVerniciatura\\"
files = os.listdir(percorso)
files = filter(lambda x: x.endswith(".pdf"), files)

for nome_file_input in files:
    nome_file_output = nome_file_input.replace(".pdf", ".xlsx")

    file = open(percorso + nome_file_input, mode="rb")
    reader = PyPDF2.PdfReader(file)

    testo = reader.pages[-1].extract_text()

    testo = testo.split("\n")[:-1]


    dati_excel = []

    for riga in testo:
        riga = re.sub(r"\s+", " ", riga)
        ele_riga = riga.split(" ")

        bancale = ele_riga[2]
        totale_mq = ele_riga[5]
        descrizione = " ".join(ele_riga[6:]).split("-")[1]

        dati_excel.append([bancale, totale_mq, descrizione])

        
    df = pd.DataFrame(dati_excel, columns=["Bancale", "Totale MQ", "Descrizione"])
    df.to_excel(percorso + nome_file_output, index=False)

    file.close()
