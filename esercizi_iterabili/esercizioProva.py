

""" i =0

numero = 100

while i < 10  and numero != 0:

 numero = int(input(f'inserisci il {i+1} numero :'))




 print(f'Hai inserito il {numero}')


 i = i+1

 """
""" lato = 6

cubo = lato **2

print(f'il cubo è: {cubo}')
 """


def  calcoloCubo(ciccio,cane):

    ciccio = ciccio+cane

    cubo = ciccio**2
    


    return cubo



numero1 = int(input('Inserisci un primo numero :'))

numero2 = int(input('Inserisci un secondo numero :'))

cubo  = calcoloCubo(numero1 ,numero2)


print(cubo)