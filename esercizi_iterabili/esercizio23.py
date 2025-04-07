'''
Intersezione di due liste
o
Hai due liste di elementi, che possono avere duplicati.
o
Crea una terza lista che contenga l’intersezione delle due liste, mantenendo il numero di occorrenze minime comuni.
o
Stampa la lista risultante.




'''

lista1 = [10,20,3,4,5,6,7,8,10,8]
lista2 =[1,2,3,4,20,5,8,30,50]

lista3 = []

""" for ele in lista1:
   if ele in lista2 and ele not in lista3:
      
      card_min = min(lista1.count(ele), lista2.count(ele))

      for i in range(card_min):
         lista3.append(ele)

lista3 = [ele for ele in lista1 if ele in lista2 and ele not in lista3 for i in range(min(lista1.count(ele), lista2.count(ele)))] """

for ele1 in lista1 :
   
   for ele2  in lista2:
      
      if ele1==ele2 :
         
        if ele1  in lista3 :
            
            count_1 = 0
            for ele1_1 in lista1:
               if ele1_1 == ele1:
                  count_1 += 1
            count_2 = 0
            for ele2_2 in lista2:
               if ele2_2 == ele2:
                  count_2 += 1

           
            if lista3.count(ele1) < min(lista1.count(ele1), lista2.count(ele1)):
                lista3.append(ele1)
            
        else:
            lista3.append(ele1)



print(lista3)         