'''
Ordina una lista (bubble sort semplificato)
o
Implementa un algoritmo di ordinamento semplice (es: bubble sort) per ordinare una lista di numeri dal più piccolo al più grande.
o
Stampa la lista ordinata.

'''


listaNumeri =[1,10,20,2,3,6,7,50,40]


temp = 0


while True:
    conta = 0
    for  i in range(len(listaNumeri)-1): ####

       

        if listaNumeri[i] > listaNumeri[i+1]:

            temp = listaNumeri[i]
            listaNumeri[i] = listaNumeri[i+1]

            listaNumeri[i+1] =  temp
            conta = conta +1

    if    conta == 0:
        break

print(listaNumeri)


""" listaNumeri.sort()
print(listaNumeri) """

""" sorted(listaNumeri)
print(listaNumeri)
new_listaNumeri = sorted(listaNumeri)
print(sorted(listaNumeri)) """

""" 
persone = [
    {"nome":"Mario2", "eta": 20},
    {"nome": "Luigi", "eta": 30}
]

print(sorted(persone, key=lambda x: x["nome"].upper(), reverse=False)) """