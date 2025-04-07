'''
Aggiorna un valore
o
Dato un dizionario di nomi e punteggi, chiedi all’utente un nome e un nuovo punteggio.
o
Se il nome esiste, aggiorna il suo punteggio; altrimenti aggiungilo come nuova chiave.
o
Stampa il dizionario aggiornato.




'''
 
nomePunteggi ={}

num = 5


for i in range(num):
    nome= input('Inserisci un nome :')
    punteggio= int(input('Inserisci un punteggio:'))

    if nome in nomePunteggi.keys():
        nomePunteggi[nome] = nomePunteggi[nome] + punteggio

    else:
        nomePunteggi[nome] = punteggio




    print(nomePunteggi)
