'''

2. Funzione per contare le vocali
Scrivi una funzione che prenda in input una stringa e restituisca il numero di vocali (a, e, i, o, u) presenti al suo interno, senza distinzione tra maiuscole e minuscole.
Punti di attenzione:
•
Come trattare la stringa in maiuscolo e minuscolo.
•
Come verificare se un carattere è una vocale.
•
Come incrementare correttamente il contatore.


'''

stringa = input('Inserisci una stringa :')





def contaVocali(stri: str) -> int:
    vocali = 'aiuoe'
    k = 0
    for ele in stri:

        if ele.lower() in vocali:
            k= k+1




    return k















vocali = contaVocali(stringa)


print(vocali)