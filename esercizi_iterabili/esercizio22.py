'''

9.
Rimuovi elementi multipli di un valore
o
Data una lista di numeri, chiedi all’utente un numero m.
o
Elimina dalla lista tutti gli elementi che sono multipli di m.
o
Stampa la lista filtrata.

'''


m = int(input('Inserisci un numero  :'))

lista = [4, 10,20,30,5,80,45,50]

""" for ele in lista :

    if ele % m  == 0 : 
     
     lista.remove(ele)2


     print( ele) """

i = 0
while True:
    if   i  >= len(lista):
        break

    ele = lista[i]
    if ele % m  == 0 :
        lista.remove(ele) 
        i -= 1 
     
        print(ele)

    i+=1

      
print(lista)
         