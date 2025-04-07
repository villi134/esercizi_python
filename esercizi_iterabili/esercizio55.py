'''

10.
Analisi di testo
o
Chiedi all’utente di inserire un testo più lungo (più frasi).
o
Crea un dizionario che contenga informazioni come:
▪
Numero di frasi (separate da un punto).
▪
Numero di parole totali.
▪
Numero di caratteri (senza spazi).


'''


testo = ' domani andiamo a giocare a calcio tutti insieme.  Ricordatevi di portare via le scarpe....'


diz = {}

diz= testo


k =0

for ele in diz :

    if ele == ' ' in diz:


        k = k + 1

print(k)


cont = 0

for ele in diz:
   
   if ele == '.' in diz :
      
      cont = cont +1 

print(cont)


print(diz.count(" "))
print(diz.count("."))
print(len(diz))