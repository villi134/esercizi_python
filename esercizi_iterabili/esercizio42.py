'''
7.
Verifica la presenza di un elemento
o
Hai un set di stringhe (ad esempio, nomi di frutta).
o
Chiedi all’utente di inserire il nome di un frutto e verifica se è presente nel set.
o
Stampa il risultato.



'''

frutto = input('inserisci un nome di un frutto :')


stringa = {'banana','mela','ciliegia','pera'}


trovato = False


for ele in   stringa:

    if frutto == ele:

        trovato= True

    if trovato:

        print(f'il frutto {ele} è presente') 

        break   

else:   
             print('non è presente')
