'''
6.
Inverti chiavi e valori
o
Hai un dizionario con chiavi e valori (entrambi univoci).
o
Crea un nuovo dizionario che inverta il ruolo di chiavi e valori.
o
Stampa il nuovo dizionario.



'''
"""  persona2 = {}
persona3 = {} """

persona4={}

persona = {

  'nome': 'luca',
  'cognome':'santin',
   'eta': 28,
   'indirizzo':' via  4 strade'


} 



for chiave in persona:
    valore =  persona[chiave]


    temp = chiave
    chiave = valore
    valore = temp
    persona4[chiave]=valore

   # print(f'stampa il valore{persona4}')
   # print(temp)  

print(persona4)