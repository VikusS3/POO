class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad
        
    def __repr__(self):
        return f'{self.nombre}, Fuerza: {self.fuerza}, Velocidad: {self.velocidad}'
    
    def __add__(self, otro_personaje):
        nuevo_personaje = self.nombre + "-" +otro_personaje.nombre
        nueva_fuerza = round(((self.fuerza + otro_personaje.fuerza)/2)**1.5)
        nueva_velocidad = round(((self.velocidad + otro_personaje.velocidad)/2)**1.2)
        return Personaje(nuevo_personaje, nueva_fuerza, nueva_velocidad)
        
    
Kakarto = Personaje("Kakarto", 100, 50)
Naruto = Personaje("Naruto", 98, 69)
Ichigo = Personaje("Ichigo", 100, 100)

NaruKaka = Kakarto + Naruto
NaruKaka = NaruKaka + Ichigo
print(NaruKaka)