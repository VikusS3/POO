class Persona:
    def __init__ (self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
        
    def saludar(self):
        print(f'Hola mi nombre es {self.nombre}')
        
#esta clase hereda de la clase Persona
class Empleado(Persona):
    #con el metodo init se inicializan los atributos de la clase
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
        #con super se heredan los atributos de la clase padre
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, escuela, grado):
        super().__init__(nombre, edad, nacionalidad)
        self.escuela = escuela

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
        
    def mostrar_habilidad(self):
        print(f'La habilidad del artista es: {self.habilidad}')

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, salario, habilidad, empresa):
        #con super se heredan los atributos de la clase padre
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
        
    def presentarse(self):
        return f'{super().mostrar_habilidad()}'
    

pablo= EmpleadoArtista('Pablo', 20, 'Mexicano', 1000, 'Pintar', 'Google')

# pablo.presentarse()
        
        
#saber si una clase es hija de otra
#la funcion issubclass recibe dos parametros, la clase hija y la clase padre
herencia = issubclass(EmpleadoArtista, Persona)

#saber si un objeto es instancia de una clase
#la funcion isinstance recibe dos parametros, el objeto y la clase
instancia = isinstance(pablo, Persona)
print(instancia)
