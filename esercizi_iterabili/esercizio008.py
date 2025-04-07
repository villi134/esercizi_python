
'''

11. Calcolo del Prezzo Totale
- Chiedi il prezzo e la quantità di un prodotto.
- Applica uno sconto del 10% se il costo totale supera 100 euro.


'''

prezzo = int(input('Inserisci prezzo'))

qty = int(input('inserisci qunatità'))

prezzoTotale = prezzo*qty

if  prezzoTotale > 100 :

   prezzoTotale =  (prezzoTotale*(1-0.1))


   print(f'il prezzo scontato è :{prezzoTotale}') 

else:

 print(f"prezzo normale{prezzoTotale }")