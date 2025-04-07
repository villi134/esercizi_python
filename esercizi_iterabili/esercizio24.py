'''
1.
Crea una tupla da input
o
Chiedi all’utente di inserire una serie di valori separati da virgola.
o
Trasforma la stringa di input in una tupla (senza usare liste intermedie se possibile).

'''

stringa = '20,30,40,50,90'

variabile =  (*stringa.split(','), )
print(variabile)

variabile =  tuple(stringa.split(','))
print(variabile)

 
