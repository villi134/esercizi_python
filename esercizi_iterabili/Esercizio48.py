'''
3.
Ricerca di un valore
o
Hai un dizionario che associa prodotti a prezzi.
o
Chiedi all’utente di inserire un prezzo e trova tutti i prodotti che hanno quel prezzo.
o
Stampa i prodotti o un messaggio se non ve ne sono.


'''


prezzoDainserire =  float(input('Inserisci prezzo : '))

prodotti = { 

        'dentifricio': 5.30,
        'matita':1.20,
        'calcolatrice': 7.60,
        'penna': 2.75

}


bandiera = False

for p in prodotti.keys():

    if prezzoDainserire == prodotti[p]:
           bandiera = True
           print(p)



if bandiera == False:
    print('Non c e nessun prodotto')


# OPPURE


bandiera = False

for chiave, valore in prodotti.items():

    if prezzoDainserire == valore:
           bandiera = True
           print(chiave)



if bandiera == False:
    print('Non c e nessun prodotto')


