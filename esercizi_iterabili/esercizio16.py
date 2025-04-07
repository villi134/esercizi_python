'''

Somma e media
o
Data una lista di numeri, calcola la somma e la media dei suoi elementi senza usare funzioni integrate per la somma.
o
Stampa i risultati.




'''

listaNumeri = [2,3,4,5,6,7,8]

somma = 0

conta = 0
for  ele in listaNumeri:
    conta = conta +1 

    somma = somma + ele

media = somma/conta
print(f'la media è : {media}')

print(f'la somma è :{somma}')

