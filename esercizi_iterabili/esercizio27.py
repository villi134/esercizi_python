'''
Estrai valori pari
o
Crea una tupla di numeri.
o
Estrai in un’altra tupla solo i numeri pari.
o
Stampa la tupla di numeri pari.

'''



numeri =(2, 5, 4, 3, 6, 8, 7, 6, )

array = []

for i in  range(len(numeri)):

   if numeri[i] % 2 == 0 :

        array.append(numeri[i])

numeri2 = tuple(array)
print(numeri2) 