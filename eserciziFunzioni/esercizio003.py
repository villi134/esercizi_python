'''
3. Funzione che verifica l’anagramma
Crea una funzione che, dati due testi, restituisca True se sono anagrammi (contengono esattamente le stesse lettere nello stesso numero di occorrenze), altrimenti restituisca False.
Punti di attenzione:
•
Come normalizzare i testi (maiuscole e minuscole, spazi, punteggiatura).
•
Come confrontare le lettere e il loro conteggio.



'''

testo1 = ' ca sa asadsadaasadaadadsadasdadads'
testo2 = ' sa ac asadsadaasadaadadsadasdadads'



def verifica(t1, t2):
    t1 = t1.replace(" ", "")
    t1 = t1.lower()
    t2 = t2.replace(" ", "")
    t2 = t2.lower()

    bandiera = True
    k = 0
    
    if len(t1) != len(t2):
        return False
     

    for ele in set([*t1]):
        if t1.count(ele) != t2.count(ele):
            bandiera = False
            break

    return bandiera

oggetto = verifica(testo1, testo2) 
print(f"é palindroma? {oggetto}")