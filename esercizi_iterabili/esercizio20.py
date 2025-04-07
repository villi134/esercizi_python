'''
Lista di liste
o
Crea una lista di liste (ad esempio, la matrice dei voti di più studenti).
o
Calcola la somma di tutti i voti e la media complessiva.
o
Stampa i risultati.


'''


studenti = [[10,20,30,],[5,6,7],[100,200,150]]
somma = 0

""" for  i in range(len(studenti)):

    for j in studenti[i]:

        somma = somma +  j


print(somma)
 """


for  voti in studenti:

    for voto in voti:

        somma = somma +  voto


print(somma)



