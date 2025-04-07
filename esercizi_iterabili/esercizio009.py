'''

12. Classificazione dell'Età
- Chiedi l'età e classifica in: bambino, adolescente, adulto, anziano.


'''

eta  = int(input('Inserisci eta: '))

if eta < 12 :
    print('bambino')


elif  eta  > 12 and eta < 16 :

    print('adolescente')

elif eta > 16 and  eta <= 18  :

    print('adulto')

elif eta   > 65 and  eta < 90 :

      print('anziano')

else:  

   

     print('Super Anziano')  