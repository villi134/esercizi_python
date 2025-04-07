'''
1.
Crea una lista da input
o
Chiedi all’utente di inserire una serie di numeri separati da virgola.
o
Trasforma la stringa di input in una lista di numeri (ricordati di convertire i dati correttamente).


'''

"""  VERSIONE 1
lunghezza = int(input('Ineserisci quanti numeri vuoi inserire: '))

numeri = []

for _ in range(lunghezza):
    inserisciNumeri = int(input('Ineserisci un numero: '))
    numeri.append(inserisciNumeri)

print(numeri)
 """


stringa = "10, 20, 30"
print(stringa)
stringa_divisa = stringa.split(",")
print(stringa_divisa)

numeri = []

for ele in stringa_divisa:

    numeri.append(int(ele))

    print(numeri)


numeri = [int(ele) for ele in stringa.split(",")]

""" 
stringa = input('inserisci stringa') # "10, 20, 30"
 #[10, 20, 30]


numeri = []

for ele in range(stringa.split(',')) :

    numeri.append(stringa)

    print(numeri)

 """
