class Gato():
    def sonido(self):
        return "Miau"
    
class Perro():
    def sonido(self):
        return "Guau"

class Vaca():
    def sonido(self):
        return "Muu"
    
#creando una funcion fuera de las clases
def hacer_sonido(animal):
    print(animal.sonido())
    
gato = Gato()
perro = Perro()
vaca = Vaca()

hacer_sonido(gato)