'''

13. Verifica del Triangolo
- Chiedi tre numeri e verifica se possono formare un triangolo.


'''

num1 = int(input('inserisci primo numero'))
num2 = int(input('inserisci primo numero'))
num3 = int(input('inserisci primo numero'))


# la somma degli angoli deve fare 180°

sommaAngoli = (num1+num2+num3)

if  sommaAngoli == 180 :

    print('è un trinagolo')

    """ if  num1  != num2 and num2  != num3 and num1  != num3 :

    print('Triangolo scaleno')


    if (num1 == num2  or num2 == num3 or  num1 == num3) and (num1 != num2 or):

    print('Trinagolo isoscele')


    else:

    print('')  """

    if num1 == num2 and num2 == num3:
      print('Trinagolo equilatero')
    elif num1 == num2 or num2 == num3 or num1 == num3:
      print('Triangolo isoscele')
    else:
      print('Triangolo scaleno')


else:
  print('non è un tringolo')


    




#trinangolo SCALENO (tutti gli angoli sono diversi)
#trinangolo ISOSCELE (2 angoli sono uguali)
#trinangolo EQUILATERO (tutti gli angoli sono uguali)

