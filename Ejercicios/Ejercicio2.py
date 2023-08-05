class Personaje:
    def __init__(self, nombre, tipo, vida, ataque, defensa):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        
    def guardar_datos_txt(self):
        with open('Ejercicios\\personaje.txt', 'w', encoding='utf8') as archivo:
            #con el metodo write se escribe en el archivo de texto pero se puede escribir mas de una linea
            archivo.writelines([f"Nombre: {self.nombre}\n",f"Tipo: {self.tipo}\n",f"Vida: {self.vida}\n",f"Ataque: {self.ataque}\n",f"Defensa: {self.defensa}\n"])
            
            
nombre = input('Ingrese el nombre del personaje: ')
tipo = input('Ingrese el tipo del personaje: ')
vida = input('Ingrese la vida del personaje: ')
ataque = input('Ingrese el ataque del personaje: ')
defensa = input('Ingrese la defensa del personaje: ')

personaje = Personaje(nombre, tipo, vida, ataque, defensa)

#llamar al metodo
personaje.guardar_datos_txt()