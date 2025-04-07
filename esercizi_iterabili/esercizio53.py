'''
8.
Dizionario di liste
o
Crea un dizionario che abbia come chiave il genere di un film (ad esempio “azione”, “commedia”) e come valore una lista di titoli di quel genere.
o
Aggiungi un nuovo titolo a uno dei generi e stampa la struttura finale.



'''

film_per_genere = {
    "Azione": ["Die Hard", "Mad Max: Fury Road", "The Dark Knight"],
    "Commedia": ["La vita è bella", "Fantozzi", "The Hangover"],
    "Drammatico": ["Shawshank Redemption", "Forrest Gump", "Requiem for a Dream"],
    "Horror": ["The Shining", "It", "A Nightmare on Elm Street"],
    "Fantascienza": ["Star Wars", "Blade Runner", "Inception"],
    "Romantico": ["Titanic", "La La Land", "Notting Hill"],
}

while True:
    titolo = input('inserisci un titolo (0 per uscire):')
    if titolo == "0":
        break

    categoria = input('inserisci la categoria :')

    """ for chiave,valore in film_per_genere.items():
        if categoria == chiave:
            film_per_genere[chiave].append(titolo) """


    if categoria in film_per_genere.keys():
        film_per_genere[categoria].append(titolo)
    else:
        film_per_genere[categoria] = [titolo]

    #print(film_per_genere)

    print()
    for chiave, valore in film_per_genere.items():
        print(f"{chiave}: {valore}")
    print()




