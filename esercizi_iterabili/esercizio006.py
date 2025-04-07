'''
8. Calcolatrice Avanzata
- Chiedi due numeri e l'operazione desiderata (+, -, *, /).
- Usa if-else per eseguire l'operazione e stampa il risultato.



'''

num1 = float(input('Inserisci un numero'))
num2 = float(input('Inserisci un secondo numero'))

operatore = input('inserisci un simbolo + , - , / ,*')

risultato = 0

if  operatore == '+' :

    risultato = num1+num2

    print(f'La somma è : {risultato}')


elif   operatore == '-' : 

    risultato = num1-num2

    

    print(f'La differenza è : {risultato}')



elif  operatore =='/'  :

    if num2 > 0 :

      risultato = num1/num2

    else:
        print('Non si puo fare l \'operazione')


    print(f'La divisione è : {risultato}')


elif  operatore == '*' :

     risultato = num1*num2
     print(f'La moltiplicazione è : {risultato}')

     