'''

2.
Ricerca di una chiave
o
Hai un dizionario che associa nomi di studenti a un voto.
o
Chiedi all’utente di inserire il nome di uno studente e verifica se è presente nel dizionario come chiave.
o
Stampa il voto se esiste o un messaggio se non esist




'''

class persona:
    def __init__(self):
      self.eta = 10
      self.nazionalita = "italiana"
    
    def __str__(self):
      return f"eta: {self.eta}, nazionalita: {self.nazionalita}"


persone = {
    "mario": {
        "eta": 10,
        "nazionalita": "italia",
        "voti": [1, 2, 3, 4, 5, 6]
    },
    "luca": {
        "eta": 20,
        "nazionalita": "italia",
         "voti": [1, 2, 3, 4, 5, 6]
    }
}

print(persone["luca"]["voti"][2])


persone = {
  "luca": persona(),
  "mario": persona(),
}

print(persone["luca"])






diz ={



"luca": 10,
"dario": 15,
'gianni':20

}

nome= input('inserisci nome: ')

if nome in diz.keys():

 print(diz[nome])
else:
 print("il nome non esiste")

   

   
