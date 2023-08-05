from abc import ABC, abstractmethod

class Trabajador(ABC):
    
    @abstractmethod
    def trabajar(self):
        pass
    
class Comedor(ABC):
    
    @abstractmethod
    def comer(self):
        pass
    
class Durmiente(ABC):
    
    @abstractmethod
    def dormir(self):
        pass
    
    
class Humano(Trabajador, Comedor, Durmiente):
    def comer(self):
        print("Comiendo")
    
    def trabajar(self):
        print("Trabajando")
    
    def dormir(self):
        print("Durmiendo")
        
        
class Robot(Trabajador):
    
    def trabajar(self):
        print("El Robot puede trabajar")
        

robot = Robot()
robot.trabajar()

humano = Humano()
humano.comer()