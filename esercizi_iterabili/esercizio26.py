'''
Slicing
o
Crea una tupla di numeri da 1 a 10.
o
Ricava una seconda tupla che contenga solo gli elementi dal 3° al 7° (inclusi).
o
Stampa la tupla estratta.

'''

tuplaNumeri = (1,2,3,4,5,6,7,8,9,10)

lista = []

for  i in range(2,7):
    lista.append(tuplaNumeri[i])
tuplaNumeri2 = tuple(lista)
print(tuplaNumeri2)

print(tuplaNumeri[2:7])
print(tuplaNumeri[:3])
print(tuplaNumeri[3:])

print(tuplaNumeri[-1])