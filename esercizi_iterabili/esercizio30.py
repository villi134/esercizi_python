'''
Conteggio di un valore
o
Data una tupla di nomi, chiedi all’utente di inserirne uno.
o
Conta quante volte compare nella tupla (senza usare count()).
o
Stampa il numero di occorrenze.


'''


tuplaNomi = ('luca','paolo','denis','romeo','luca','gianluca')

conta = 0

nome = input('Inserisci un nome')


for ele in tuplaNomi:
 
    if ele == nome:

        conta = conta +1


print(conta)

