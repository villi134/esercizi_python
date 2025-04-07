'''

Trova minimo e massimo
o
Data una lista di numeri, trova il valore minimo e il valore massimo senza usare funzioni integrate come min() e max().
o
Stampa i due valori.

'''


numerodiInserimenti = int(input('numero di volte'))

numeri = []

for ele in range(numerodiInserimenti):
        
    inserisciNumero = int(input('inserisci numeri'))
    numeri.append(inserisciNumero)


""" min_value = numeri[0]
max_value = numeri[0]

for i in range(len(numeri)):
     

  
    if  numeri[i] < min_value :
        min_value = numeri[i]
      
    elif numeri[i] > max_value:
        max_value = numeri[i] 

print(f'il minimo è :{min_value}')
print(f'il massimo è :{max_value}') """

min_value = min(numeri)
max_value = max(numeri)

print(f'il minimo è :{min_value}')
print(f'il massimo è :{max_value}')










""" numeri = []

lista = [1,2,20,30,50,4,90]


min = lista[0]
max = lista[0]


for  i  in range(len(lista)):

    if  lista[i] < min :
        min = lista[i]
      
    elif lista[i] > max:
        max= lista[i] 

print(f'il minimo è :{min}')
print(f'il massimo è :{max}') """


