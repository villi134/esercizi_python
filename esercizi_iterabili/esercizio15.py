'''
o
Hai una lista di nomi.
o
Chiedi all’utente un nome da cercare e conta quante volte compare nella lista.
o
Stampa il numero di occorrenze.


'''

nomeDaCercare = input('Inserisci un nome: ')

nomi = ['giovanni','luca','dario','michele','giovanni','lisa','giuseppe']


""" nomi.append("mario")
nomi.extend(["Mario", "Luigi"])

for i, nome in enumerate(nomi):
    print(i, nome)

for i in nomi:
    nome = nomi[i]
    print(i, nome) """

""" conta = 0


for  ele in nomi :
  

  if  nomeDaCercare == ele:

    conta = conta +1

print(f'Nome trovato :{nomeDaCercare} numero di volte {conta}') """

print(f'Nome trovato :{nomeDaCercare} numero di volte {nomi.count(nomeDaCercare)}')

  