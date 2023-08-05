class Animal:
    def comer(self):
        print("Comiendo...")

class Mamifero(Animal):
    def amamantar(self):
        print("Amamantando...")

class Ave(Animal):
    def volar(self):
        print("Volando...")
        
class Murcielago(Mamifero, Ave):
    pass

murcielago = Murcielago()

murcielago.amamantar()
murcielago.volar()
murcielago.comer()

print(Murcielago.__mro__)