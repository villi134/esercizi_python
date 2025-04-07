'''

Controllo del Flusso (while loop)
- Chiedi all'utente un numero intero positivo.
- Usa un ciclo `while` per calcolare la somma di tutti i numeri da 1 fino al numero inserito.


'''

""" 
numero_intero  = int(input('inserisci un numero intero'))

somma = 0
numero_attuale = 1
while  True:

    print(f"somma: {somma}")
    somma = somma + numero_attuale

    print(f"numero_attuale: {numero_attuale}")
    print(f"somma: {somma}")
    print()

    if  numero_attuale == numero_intero :
        break 
    numero_attuale = numero_attuale + 1

 """

""" for num in range(1, numero_intero+1) :

    somma = somma + num 


print(f"somma :{somma}") """





""" 

chiedi all'utente un numero compreso tra 0 e 100
se il numero inserito è sbagliato glielo richiediamo

"""
# caso 1
while True:
    numero_intero = int(input(" un numero compreso tra 0 e 100"))

    if numero_intero > 0 and numero_intero < 100 :
        break
    else:
        print("Il numero è sbagliato")

# caso 2
numero_intero = int(input(" un numero compreso tra 0 e 100"))
while numero_intero <= 0 or numero_intero >= 100:
    print("Il numero è sbagliato")
    numero_intero = int(input(" un numero compreso tra 0 e 100"))

# caso 3
numero_intero = -100
while numero_intero <= 0 or numero_intero >= 100:
    numero_intero = int(input(" un numero compreso tra 0 e 100"))

    if numero_intero <= 0 or numero_intero >= 100 :
        print("Il numero è sbagliato")