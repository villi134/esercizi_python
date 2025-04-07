'''
Dizionari

1.
Crea un dizionario da input
o
Chiedi all’utente di inserire coppie di chiave e valore (per esempio, “nome, età”).
o
Costruisci un dizionario fino a quando l’utente non decide di interrompere.
o
Stampa il dizionario.



'''


#coppieCv = input('inserisci chiave,valore')

diz = {

'nome': 'luca',
'eta': 10



}

#chiave_valore = input("Inseirsci chiave:valore ")
#[chiave, valore] = chiave_valore.split(":")

chiave = input("Inserisci la chiave: ")
valore = input("Inserisci il valore: ")

   

diz[chiave] = valore

print(diz)