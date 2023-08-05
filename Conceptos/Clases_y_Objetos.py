class Celular:
    #def __init__ es el metodo constructor una clase
    #self es una referencia a la instancia de la clase
    #self es el primer parametro de cada metodo de instancia
    def __init__(self, marca, modelo, camara):
        #estos son atributos de la clase
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
        
    #medotos de una clase
    #self es una referencia a la instancia de la clase
    def llamar(self):
        print('Llamando... ' + self.marca + ' '  + self.modelo)
        
    def cortar(self):
        print('Cortando... ' + self.marca + ' '  + self.modelo)
        
#creacion de objetos de la clase        
celular1 = Celular("Samsung", "Galaxy", "12MP")
celular2 = Celular("Apple", "Iphone", "76MP")
# print(celular1.marca)

celular2.llamar()
