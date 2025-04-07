'''
7. Calcolo dell'IMC (Indice di Massa Corporea)
- Chiedi all'utente peso e altezza.
- Calcola l'IMC e classifica il risultato (sottopeso, normopeso, sovrappeso).


'''

peso = int(input('Inserisci il peso :'))

altezza = float(input('Inserisci l\'altezza :'))


imc = (peso/pow(altezza, 2))


print(imc)


if imc  < 19 :

    print('sottopeso')

if imc >= 19 and imc < 25  :

    print('normapeso')


if imc >= 25 and imc < 30 :

    print('sovvrapeso') 

if  imc > 30 :

    print('obesita')       