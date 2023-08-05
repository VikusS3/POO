from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    @abstractmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        return print(f'Hola, mi nombre es {self.nombre} y tengo {self.edad} años')
    
    
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacer_actividad(self):
        print(f'Hola, soy {self.nombre} y estoy estudiando {self.actividad}')
        
        
class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
        
    def hacer_actividad(self):
        print(f'Hola, soy {self.nombre} y estoy trabajando en {self.actividad}')
    

saul = Estudiante('Saul', 25, 'M', 'Estudiar')
lucas = Trabajador('Lucas', 30, 'M', 'Programador')

saul.presentarse()
saul.hacer_actividad()
lucas.presentarse()
lucas.hacer_actividad()