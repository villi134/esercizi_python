'''
4.
Verifica sottoinsieme
o
Dati due set, verifica se il primo è un sottoinsieme del secondo.
o
Stampa un messaggio appropriato.



'''

A = set([1, 2])
B = set([2])

unione = A.union(B)

print(f'unione : {unione}')

if unione == A:
    print("B è un sottoinsieme")
else:
    print("B non è un sottoinsieme")



A = set([1, 2])
B = set([3])

unione = A.union(B)

print(f'unione : {unione}')

if unione == A:
    print("B è un sottoinsieme")
else:
    print("B non è un sottoinsieme")




A = set([1, 2])
B = set([3])

differenza = A.difference(B)

print(f'unione : {unione}')

if differenza == A:
    print("B non è un sottoinsieme")
else:
    print("B è un sottoinsieme")




A = set([1, 2])
B = set([3])

intersezione = A.intersection(B)

print(f'unione : {unione}')

if intersezione == B:
    print("B è un sottoinsieme")
else:
    print("B non è un sottoinsieme")