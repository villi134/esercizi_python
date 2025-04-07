'''

Ordina un dizionario per chiave
o
Hai un dizionario di città (chiavi) e popolazione (valori).
o
Estrai le chiavi in ordine alfabetico e stampa coppie “città - popolazione” seguendo l’ordine ottenuto.


'''


diz = {

    'parigi': 1000,
    'venezia': 2000,
    'roma': 6000,
     'ancona': 789



}

lista = []

for ele in diz.keys():

  lista.append(ele)

  lista.sort()



for ele in lista:
 print(f'{ele} - {diz[ele]}')





for ele in sorted(diz.keys()):
  print(f'{ele} - {diz[ele]}')
