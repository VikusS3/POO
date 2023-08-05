class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def imprimir_nombre(self):
        print(f'Mi nombre es {self.nombre}')


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        Persona.__init__(self, nombre, edad)
        self.grado = grado
        
    def imprimir_grado(self):
        print(f'Mi grado es {self.grado} mi nombre es {self.nombre} tengo {self.edad} años')


raul = Estudiante('Raul', 20, 'Universidad')
raul.imprimir_grado()