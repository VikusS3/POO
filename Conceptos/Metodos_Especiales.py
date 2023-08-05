class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    #__str__ es un metodo especial que se ejecuta cuando se imprime el objeto
    #de la clase Persona en este caso (print(saul)) 
    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}'
    
    #__repr__ es un metodo especial que se ejecuta cuando se imprime el objeto
    #es parecido a __str__ pero se ejecuta cuando se imprime el objeto de la clase
    #Persona pero con la funcion repr() (repr(saul)) es la representacion del objeto pero
    #en codigo python sirve para recrear el objeto
    def __repr__(self):
        return f'Persona("{self.nombre}", "{self.edad}")'
    
    #__add__ sirve para sumar dos objetos de la clase Persona
    #la palabra otro es el otro objeto de la clase Persona que se va a sumar con el objeto actual 
    def __add__(self, otro):
        nuevo_valor = self.edad + otro.edad
        return Persona(self.nombre+otro.nombre, nuevo_valor)
    
saul = Persona("Saul", 25)
pedro = Persona("Pedro", 30)

resultado = saul + pedro
print(resultado)

