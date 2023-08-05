class Persona:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
    
    #el decorador @property permite que el metodo sea llamado como una propiedad y no como un metodo
    #por ejemplo: persona.get_nombre() se convierte en persona.nombre
    @property
    def nombre(self):
        return self.__nombre
    
    #el decorador @nombre es para que el metodo sea llamado como una propiedad y no como un metodo
    #es decir, persona.set_nombre("Saul") se convierte en persona.nombre = "Saul"
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
        
    #el decorador @nombre es para que el metodo sea llamado como una propiedad y no como un metodo
    #usamos deleter para eliminar la propiedad
    @nombre.deleter
    def nombre(self):
        del self.__nombre

saul = Persona("Saul", "Canelo", 30)
nombre = saul.nombre

print(nombre)

saul.nombre = "Saul Alvarez"
print(saul.nombre)

#usamos esto para eliminar la propiedad
# del saul.nombre