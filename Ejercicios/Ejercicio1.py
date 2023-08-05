class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print(f'El estudiante {self.nombre} esta estudiando')
        
#brindar los atributos de la clase

nombre = input('Ingrese el nombre del estudiante: ')
edad = input('Ingrese la edad del estudiante: ')
grado = input('Ingrese el grado del estudiante: ')

#crear el objeto
estudiante1= Estudiante(nombre, edad, grado)
estudiante1.estudiar()