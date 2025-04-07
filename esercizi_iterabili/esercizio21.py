'''

Rotazione a destra
o
Dato un numero k e una lista di elementi, ruota gli elementi della lista verso destra di k posizioni (gli ultimi vanno in testa).
o
Stampa la lista ruotata.


'''


k = 3

listaNumeri = [ 10,20,50,2,8,20,90,45,80,100]


temp=0

for _ in range(k):
    for ele in range(len(listaNumeri)):
        temp = listaNumeri[ele]
        listaNumeri[ele] = listaNumeri[len(listaNumeri)-1]
        listaNumeri[len(listaNumeri)-1] = temp

print(listaNumeri)


for _ in range(k):
    ultimo = listaNumeri.pop()
    listaNumeri.insert(0, ultimo)
print(listaNumeri)


