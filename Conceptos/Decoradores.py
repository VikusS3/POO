def decorador(funcion):
    def funcion_modificada():
        print("Este es el primer mensaje")
        funcion()
        print("Este es el segundo mensaje")
    return funcion_modificada

# def saludo():
#     print("Hola mundo")

# #forma 1 de usar el decorador     
# # decorador(saludo)()

# #forma 2 de usar el decorador
# saludo_modificado = decorador(saludo)
# print(saludo_modificado())
        
#el @ es para indicar que la funcion saludo esta decorada por la funcion decorador
#decorar es agregar funcionalidad a una funcion sin modificarla
@decorador
def saludo():
    print("Hola mundo")

saludo()