'''
5.
Somma di elementi
o
Data una tupla di numeri, calcola la somma di tutti i valori senza usare sum().
o
Stampa il risultato.

'''


numeri = (20,50,30,40,2)


def somma( numeri):

    somma =0 

    for i in range(len(numeri)):
     
        somma = somma +numeri[i]


    return somma


som = somma(numeri)


print(som)