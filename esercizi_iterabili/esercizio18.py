'''
Estrai parole più lunghe di una certa lunghezza
o
Data una lista di parole, chiedi all’utente un numero n.
o
Crea una nuova lista contenente solo le parole con lunghezza superiore a n.
o
Stampa la nuova lista.


'''
lunghezza = int(input('Quante parole vuoi inserire: '))
lista_parole= []
for ele  in range(lunghezza):
   inserisciParole  = input('Inserisci delle parole: ')
   lista_parole.append(inserisciParole)




num = int(input('Inserisci un numero n: '))

listaN = []


for parola in  lista_parole:
   
     if len(parola) > num:
         
         listaN.append(parola)




print(f'Lista parole con lunghezza superiore a n: {listaN}')
         
        
         








""" num= int(input('Inserisci un numero'))


listaNuova = []


for ele in range(num):
    
     listaParole  = input('Inserisci dele parole (una lista)')
   
listaNuova.append(listaParole)
     



     if listaParole > num:
    

      print() """

      