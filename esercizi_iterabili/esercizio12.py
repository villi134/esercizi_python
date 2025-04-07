'''
16. Contare le Vocali
- Chiedi una stringa e conta quante vocali contiene.


'''
vocali = 'aiuoe'
stringa = input("Inserisci una stringa")

# 1) devo scorrere la stringa, lettera per lettera
# 2) dobbiamo vere un contatore per contare le vocali

conta = 0

for ele in stringa:
    if ele in vocali:
      #  print(ele)
        conta = conta+1
    



print(conta)
