
class Animale:
    def __init__(self, nome, colore):
        self.nome = nome
        self.colore = colore

    def verso(self):
        raise NotImplemented
    
    def __str__(self):
        return f"nome: {self.nome}, colore: {self.colore}"

class Gatto(Animale):
    def __init__(self, nome, colore):
        super().__init__(nome, colore)

    def verso(self):
        print("miao")
    

class Cane(Animale):
    def __init__(self, nome, colore, razza):
        super().__init__(nome, colore)
        self.razza = razza

    def verso(self):
        print("bau")
    
    def __str__(self):
        return f"{super().__str__()}, razza: {self.razza}"

cane = Cane("nome", "colore", "razza")
print(cane)
gatto = Gatto("nome", "colore")
print(gatto)

gatto("a", "b", nome="mario", eta=4)