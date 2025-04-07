'''
Somma dei Numeri Pari
- Chiedi un numero positivo e calcola la somma dei numeri pari da 0 fino a quel numero.


'''

numeroPos = int(input('Inserisci un numero')) # = 5
11

somma = 0


for ele in range(numeroPos+1):

    if ele > 0  and ele % 2 == 0 :


        somma = somma + ele

        print(f' il numero è positivo e pari: {ele}')

print(f' La somma dei numeri positivi e pari è : {somma}')

   

   


