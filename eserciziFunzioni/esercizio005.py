'''
5. Funzione di formattazione per la stampa
Definisci una funzione che, data una lista di stringhe, restituisca un’unica stringa formattata come elenco numerato. Ad esempio, data la lista ["mela", "banana", "arancia"], la funzione dovrebbe restituire qualcosa come:

1. mela
2. banana
3. arancia

Punti di attenzione:
•
Come creare un formato di output coerente.
•
Come utilizzare correttamente le concatenazioni di stringhe (o altri metodi di formattazione).




'''
lista = ["mela", "banana", "arancia"]

def funzione(lista):
    stringa = ""

    conta = 1
    for ele in lista:
        stringa += f"{str(conta)}. {ele}\n"
        conta = conta + 1
        

    return stringa
   
   


stringa = funzione(lista)

print(stringa)