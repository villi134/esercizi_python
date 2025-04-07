'''
9.
Merging di dizionari
o
Crea due dizionari, ciascuno con un set di chiavi e valori.
o
Unisci i due dizionari in uno solo (se ci sono chiavi duplicate, decidi come gestirle).
o
Stampa il dizionario risultante

'''

frutta = {
    'arance': 5,
    'banane': 10,
    'mele':20
}

verdura={
  'insalata': 'verde',
  'cavolfiori': 'bianchi',
  'carote': 'rosse',
   'mele': 'rosse',
}

#frutta.update(verdura)


""" fruttaVerdura = {}


for chiave  in frutta:
     fruttaVerdura[chiave] = frutta[chiave]




for chiave in verdura:   
      if chiave in fruttaVerdura:
            fruttaVerdura[chiave] = [frutta[chiave], verdura[chiave]]
      else:
            fruttaVerdura[chiave] = verdura[chiave]

print(fruttaVerdura) """

fruttaVerdura = {}
chiavi_unite = set()
chiavi_unite.update(frutta.keys())
chiavi_unite.update(verdura.keys())

for chiave in chiavi_unite:

    if chiave in frutta and chiave in verdura:
        fruttaVerdura[chiave] = [frutta[chiave], verdura[chiave]]
    elif chiave in frutta:
        fruttaVerdura[chiave] = frutta[chiave]
    else: # equivale a -> elif chiave in verdura:
        fruttaVerdura[chiave] = verdura[chiave]

print(fruttaVerdura)