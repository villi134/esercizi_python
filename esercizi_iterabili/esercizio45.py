'''

10.
Set comprehension
o
Utilizzando un elenco di numeri da 1 a 20, crea un set che contenga solo i numeri pari (senza usare cicli espliciti, ma con una comprensione di set).
o
Stampa il set risultante.


'''

eleNumeri = set()

for ele in range(1, 21):

    if ele %2 == 0:

      eleNumeri.add(ele)

print(eleNumeri)

# oppure


eleNumeri = {ele for ele in range(1, 21) if ele % 2 == 0}

print(eleNumeri)
