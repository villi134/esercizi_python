
class Persona:
    nome=''
    cognome=''
    
    def __init__(self, nome="", cognome=""):
        self.nome = nome
        self.cognome = cognome
    
    def stampa_informazioni(self):
        print(f"nome: {self.nome}, cosnome: {self.cognome}")
    
    def __str__(self):
        return f"nome: {self.nome}, cosnome: {self.cognome}" 
   




persona = Persona()
persona.nome = "Mario"
persona.cognome = "Rossi"

persona1 = Persona("Luigi", "Verdi")



print(persona.nome)
print(persona1.nome)

print(persona)

persona.stampa_informazioni()

