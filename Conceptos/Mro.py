class A:
    def hablar(self):
        print("Hola soy A")
        
class F(A):
    def hablar(self):
        print("Hola soy F")
        
class B(A):
    def hablar(self):
        print("Hola soy B")
    
class C(F):
    def hablar(self):
        print("Hola soy C")

class D(B, C):
    pass
        
        
d= D()

#la funcion mro() nos muestra el orden de ejecucion de las clases
# print(D.mro())

#llamamos a la clase a su metodo hablar con el objeto d
F.hablar(d)