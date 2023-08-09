class MedioDeTransporte:
    def __init__(self, combustible, velocidad_maxima, pasajeros_maximos):
        self.combustible = combustible
        self.velocidad_maxima = velocidad_maxima
        self.pasajeros_maximos = pasajeros_maximos
        
    def imprimir_detalles(self):
        print("Combustible:", self.combustible)
        print("Velocidad máxima:", self.velocidad_maxima)
        print("Pasajeros máximos:", self.pasajeros_maximos)
        
        
class Coche(MedioDeTransporte):
    def __init__(self, combustible, velocidad_maxima, pasajeros_maximos, numero_puertas, marca, modelo):
        super().__init__(combustible, velocidad_maxima, pasajeros_maximos)
        self.numero_puertas = numero_puertas
        self.marca = marca
        self.modelo = modelo
        
    def imprimir_detalles(self):
        super().imprimir_detalles()
        print("Número de puertas:", self.numero_puertas)
        
        
class Avion(MedioDeTransporte):
    def __init__(self, combustible, velocidad_maxima, pasajeros_maximos, numero_motores, numero_ruedas):
        super().__init__(combustible, velocidad_maxima, pasajeros_maximos)
        self.numero_motores = numero_motores
        self.numero_ruedas = numero_ruedas
        
    def imprimir_detalles(self):
        super().imprimir_detalles()
        print("Número de motores:", self.numero_motores)
        print("Número de ruedas:", self.numero_ruedas)
        
class Moto(MedioDeTransporte):
    def __init__(self, combustible, velocidad_maxima, pasajeros_maximos, cilindrada, tipo):
        super().__init__(combustible, velocidad_maxima, pasajeros_maximos)
        self.cilindrada = cilindrada
        self.tipo = tipo
        
    def imprimir_detalles(self):
        super().imprimir_detalles()
        print("Cilindrada:", self.cilindrada)
        print("Tipo:", self.tipo)
        
print("Coche")
coche1 = Coche("Gasolina", 200, 5, 5, "Ford", "Focus")
coche1.imprimir_detalles()
print()
print("Avión")
avion1 = Avion("Queroseno", 800, 200, 4, 6)
avion1.imprimir_detalles()
print()
print("Moto")
moto1 = Moto("Gasolina", 180, 2, 1000, "Deportiva")
moto1.imprimir_detalles()
print()
print("Fin del programa")