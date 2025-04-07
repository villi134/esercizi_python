'''
1.Definisci una funzione che riceva in ingresso una lista di numeri e restituisca la media aritmetica di tali numeri. La funzione dovrebbe gestire correttamente il caso in cui la lista sia vuota.
Punti di attenzione:
•
Come verificare se la lista è vuota.
•
Come calcolare la media.
•
Come restituire un valore di default (es. 0 o un messaggio) se la list



'''
lista =[10,20,50,60,30]


def funzione(lista) :
   somma =0
   for ele in lista:  
         somma = somma + ele

   media = somma/len(lista)

   return media

media = funzione(lista)

print(media)