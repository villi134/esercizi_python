#open(nomeFile  estensione , operazione)  x = create, r read , w = write, a = append
f = open('C:\\Users\\user\\desktop\\Cartella\\testo.txt' , 'x')
#f = open('C:\\Users\\user\\desktop\\Cartella\\testo.txt' , 'w')
f = open('C:\\Users\\user\\Desktop\\AnticaProvatesto.txt' , 'w')

#print(f.read())

f.write('Finalmente')



f.close()
