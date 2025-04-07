'''

5.
Conta occorrenze di parole
o
Chiedi all’utente di inserire una frase.
o
Dividi la frase in parole e conta quante volte compare ciascuna parola.
o
Stampa il dizionario risultato (parola -> numero di occorrenze).


'''

frase = "Lorem ipsum dolor sit amet consectetur adipisicing elit Corporis ea provident lorem ipsam accusamus iusto inventore officiis distinctio Lorem iure tempora totam quasi quam consequatur voluptatibus voluptatem ducimus omnis temporibus minima Quas"

parole = frase.split(' ')

print(parole)

conta = {}

for ele in parole:
    print(ele)

    ele = ele.lower()

    if ele in conta:
        conta[ele] += 1
    else:
        conta[ele] = 1

print(conta)


 