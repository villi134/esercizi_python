'''
6.
Rimuovi un elemento se esiste
o
Dato un set di numeri, chiedi all’utente di fornire un numero da rimuovere.
o
Se esiste nel set, eliminalo. Altrimenti, stampa un messaggio di errore.
o
Stampa il set finale.

'''


numDarimuovere= int(input('inserisci un numero da rimuovere: '))


setNumeri = {10,20,5,78,90,60,50,70,100}



for ele in setNumeri:

   if numDarimuovere == ele :

     setNumeri.remove(ele)
     break

print(setNumeri)

# OPPURE

trovato = False
for i in range(len(setNumeri)):

   if numDarimuovere == ele :
     trovato = True

if trovato:
    setNumeri.remove(numDarimuovere)
print(setNumeri)

# OPPURE

setNumeri.discard(numDarimuovere)

