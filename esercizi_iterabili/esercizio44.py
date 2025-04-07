'''
Aggiorna un set
o
Hai un set di parole. Chiedi all’utente di inserire un elenco di nuove parole (separate da virgola).
o
Aggiorna il set con queste parole.
o
Stampa il set aggiornato.



'''



setParole ={ 'ciao','cinema','cielo'}

num = 3
conta = num
i =0


while i < num:

    #parole = input(f'inserisci parole fino a {num - i} :' )
    parole = input(f'inserisci parole fino a {conta} :' )

    setParole.add(parole)

    i = i +1
    conta = conta - 1

print( setParole)