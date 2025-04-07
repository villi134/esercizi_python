'''
3. Funzione che verifica l’anagramma
Crea una funzione che, dati due testi, restituisca True se sono anagrammi (contengono esattamente le stesse lettere nello stesso numero di occorrenze), altrimenti restituisca False.
Punti di attenzione:
•
Come normalizzare i testi (maiuscole e minuscole, spazi, punteggiatura).
•
Come confrontare le lettere e il loro conteggio




'''


def funzione(testo1,testo2):
    if  len(testo1) != len(testo2):

          return False  
    lista1= list(testo1)
    lista2= list(testo2)

    diz1={}
    diz2={}

    for i in lista1:
     diz1[i] = lista1.count(i)
    for i in lista2:    
        diz2[i] = lista2.count(i)

    print(diz1)
    print(diz2)

    return diz1 == diz2
    


controllo = funzione('ciao','oaic')

print(controllo)