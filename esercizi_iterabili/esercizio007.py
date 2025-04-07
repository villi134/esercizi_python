'''

10. Gioco del Numero Magico
- Imposta un numero segreto (es. 7).
- Chiedi all'utente di indovinarlo con un ciclo `while`.


'''


numero_segreto = 10

while True :

    numero = int(input('inserisci un numero'))

    if  numero == numero_segreto :

        print('hai indovinato')

        break

    else:   
        print(' non hai indovinato')

    
