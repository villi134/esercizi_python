'''
Unione, Intersezione, Differenza
o
Crea due set di numeri.
o
Calcola e stampa l’unione, l’intersezione e la differenza tra i due set.

'''


num1= set([10,20,30,60,90,40,30])
num2 = set([10,100,300,60,40,30])

print(f'Unione{num1.union(num2)}')
print(f'Intersezione{num1.intersection(num2)}')
print(f'differenza{num1.difference(num2)}')