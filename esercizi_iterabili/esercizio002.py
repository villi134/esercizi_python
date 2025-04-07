'''
4. Controllo del Flusso (for loop)
- Chiedi all'utente un numero intero positivo.
- Usa un ciclo `for` per stampare i numeri da 1 fino al numero inserito


'''

""" for i in range(2, 10, 2):
    print(i)
 """

""" numero_intero = int(input('Inserisci un numero intero'))

for numero in range(1,numero_intero+1) :
    print(numero) """


""" numero_intero = [1,2,4,10,'ciao',8,156,789] """


""" for i in range(len(numero_intero)) :

    print(numero_intero[i])
 """

""" for numero in numero_intero :
    print(numero) """

""" for i , ele in enumerate(numero_intero):

    print(i,ele) """

frase = 'domani Ginevra,Anna e Andrea vanno ad una festa'

print(len(frase))

""" 
for i in   range(len(frase)) :

    print(frase[i]) """

""" for  ele in frase :

    print(ele) """


""" for i, ele in enumerate(frase) :

 if i ==7:
   print(i,ele) """

for i in  range(len(frase)):
   
   if frase[i].isupper() :
 
     print(frase[i],i)

     if not frase[i-1].isalnum() :
      
        print('La Maiuscola non è preceduta da una lettera e ne da un numero')

        if frase[i+1].isalpha() and frase[i+1].islower():
           print('La maiuoscola è seguita da una lettera minusccola')


           testo = 'ciao'

           print(testo.isalpha())

           testo = 'ciao123'
        print(testo.isalpha())