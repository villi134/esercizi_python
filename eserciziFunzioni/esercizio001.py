'''

1. Funzione che calcola la media
Definisci una funzione che riceva in ingresso una lista di numeri e restituisca la media aritmetica di tali numeri. La funzione dovrebbe gestire correttamente il caso in cui la lista sia vuota.
Punti di attenzione:
•
Come verificare se la lista è vuota.
•
Come calcolare la media.
•
Come restituire un valore di default (es. 0 o un messaggio) se la lista è vuota.



'''
numeri =[10,20,40,50,2,8,4,9,3]
#numeri =[]

def calcolaLaMedia(num: list )-> float:


    if  len(num) == 0 or num == list():
        return 0
    

  
    somma= 0

    for ele in numeri:
    
        somma = somma+ele

    media = somma/len(numeri)


    return media 

   









media = calcolaLaMedia(numeri)


print(round(media, 2))