'''

8.
Symmetric difference
o
Crea due set di elementi, ad esempio colori preferiti da due persone.
o
Trova la symmetric difference tra i due set (elementi presenti in un set ma non in entrambi).
o
Stampa il risultato.




'''

color1 ={'verde','rosso','giallo'}
color2={'arancione','blu','tortora','rosso'}

differenza = color1.difference(color2)
differenza2 = color2.difference(color1)

print(differenza)
print(differenza2)