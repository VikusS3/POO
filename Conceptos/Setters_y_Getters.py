class Persona:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
    
    #los setters y getters son metodos publicos
    #el metodo get es para obtener el valor de un atributo
    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_edad(self):
        return self.__edad
    
    #metodo set es para modificar el valor de un atributo
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def set_apellido(self, apellido):
        self.__apellido = apellido
    
    def set_edad(self, edad):
        self.__edad = edad
    
saul = Persona("Saul", "Canelo", 30)

saul.set_nombre("Saul el Canelo Alvarez")

print(saul.get_nombre())
