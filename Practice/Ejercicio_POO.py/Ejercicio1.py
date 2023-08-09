class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def imprimir_detalles(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        
    #calcular años restantes a una edad objetivo
    def calcular_años_restantes(self, edad_objetivo):
        años_restantes = edad_objetivo - self.edad
        print("Años restantes:", años_restantes)
        
        
persona1 = Persona("Juan", 20)
persona1.imprimir_detalles()
persona1.calcular_años_restantes(70)