
from funzioni001 import somma  as som

'''
==>Estrai valori pari
o
Crea una tupla di numeri.
o
Estrai in un’altra tupla solo i numeri pari.
o
Stampa la tupla di numeri pari.
5.
==>Somma di elementi
o
Data una tupla di numeri, calcola la somma di tutti i valori senza usare sum().
o
Stampa il risultato.
'''

numeri = (10,20,30,50,60,70,8,6,2,7,9,10)


pari = []



for ele in numeri:

    if ele %2 == 0:

        pari.append(ele)

print(pari)

numeriPari= (*pari,)
numeriPari= tuple(pari)

print(numeriPari)

somma = 0
for ele in numeriPari:

    somma = som(somma, ele)

print(somma)