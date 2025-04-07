'''

8.
Trova indice di un valore
o
Crea una tupla di stringhe.
o
Chiedi all’utente di inserire una stringa e trova il suo indice nella tupla (senza usare index()).
o
Stampa l’indice o un messaggio se non è presente.


'''

stri = input('Inserisci stringa  :')
stringa =('a','ciao','paolo','b')
trovato = False

for i in  range(len(stringa)):

    if stri == stringa[i]:
       print(i)
       trovato = True
       break
else:
    print('non è presente')


if not trovato:
    print('non è presente')



