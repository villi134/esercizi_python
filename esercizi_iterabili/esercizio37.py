'''
Conta elementi unici
o
Chiedi all’utente di inserire una frase.
o
Trasforma la frase in un set di parole per scoprire quante parole distinte ci sono.
o
Stampa il numero di parole uniche

'''

#frase = input('Inserisci frase')

frase = "ciao io sono mario ciao sono"

parole = frase.split(" ")

fraseSet = set(parole)

print(len(parole))

print(len(fraseSet))


