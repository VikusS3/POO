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
        self.grado = grado

Saul = Empleado('Saul', 20, 'Mexicano', 'Programador', 1000)

Saul.saludar()