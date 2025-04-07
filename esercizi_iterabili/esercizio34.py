'''
7.
Conteggio di un valore
o
Data una tupla di nomi, chiedi all’utente di inserirne uno.
o
Conta quante volte compare nella tupla (senza usare count()).
o
Stampa il numero di occorrenze.



'''

conta = 0


nome = input('Inserisci un nome')

nomi = ('Alessandro', 'Maria', 'Maria', 'Francesca', 'Luca', 'Sofia', 'Matteo', 'Elena', 'Marco', 'Giulia', 'Antonio', 'Beatrice', 'Stefano', 'Maria', 'Davide')
 

for ele in nomi:

    if  nome in ele :

        conta = conta+1

print(conta)        
