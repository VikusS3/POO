from abc import ABC, abstractmethod
# class Diccionario:
#     def verificar_palabra(self, palabra):
#         #logica para verificar si la palabra existe en el diccionario
#         pass
    
# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()
        
#     def corregir_texto(self, texto):
#         #logica para corregir el texto usando el diccionario
#         pass


class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self, palabra):
        pass
    
    
class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #logica para verificar si la palabra existe en el diccionario
        pass
    
class ServicioWeb(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #logica para verificar si la palabra existe en el servicio web
        pass
    
    
class CorrectorOrtogragico:
    def __init__(self, verificador):
        self.verificador = verificador
        
    def corregir_texto(self, texto):
        #Usamos el verificador para corregir el texto
        pass
    
corrector = CorrectorOrtogragico(ServicioWeb())