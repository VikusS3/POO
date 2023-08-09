#programa del cifrado del cesar

#funcion para cifrar
def cifrar(texto, desplazamiento):
        
        #se crea una variable para almacenar el texto cifrado
        texto_cifrado = ""
        
        #se crea un for para recorrer el texto ingresado
        for i in texto:
            
            #se crea una variable para almacenar el numero de la letra en el codigo ascii
            #ord() es una funcion que devuelve el numero de la letra en el codigo ascii
            numero = ord(i)
            
            #se crea una variable para almacenar el numero de la letra cifrada en el codigo ascii
            numero_cifrado = numero + desplazamiento
            
            #se crea una variable para almacenar la letra cifrada
            #chr() es una funcion que devuelve la letra del codigo ascii
            letra_cifrada = chr(numero_cifrado)
            
            #se agrega la letra cifrada al texto cifrado
            texto_cifrado += letra_cifrada
            
        #se imprime el texto cifrado
        print("El texto cifrado es: {}".format(texto_cifrado))
        

#funcion para descifrar
def descifrar(texto, desplazamiento):
        
        #se crea una variable para almacenar el texto descifrado
        texto_descifrado = ""
        
        #se crea un for para recorrer el texto ingresado
        for i in texto:
            
            #se crea una variable para almacenar el numero de la letra en el codigo ascii
            #ord() es una funcion que devuelve el numero de la letra en el codigo ascii
            numero = ord(i)
            
            #se crea una variable para almacenar el numero de la letra descifrada en el codigo ascii
            numero_descifrado = numero - desplazamiento
            
            #se crea una variable para almacenar la letra descifrada
            #chr() es una funcion que devuelve la letra del codigo ascii
            letra_descifrada = chr(numero_descifrado)
            
            #se agrega la letra descifrada al texto descifrado
            texto_descifrado += letra_descifrada
            
        #se imprime el texto descifrado
        print("El texto descifrado es: {}".format(texto_descifrado))
        
#se crea una variable para almacenar el texto ingresado por el usuario
texto = input("Ingrese el texto a cifrar o descifrar: ")

#se crea una variable para almacenar el desplazamiento ingresado por el usuario

#se crea un while para que el usuario ingrese un numero entre 1 y 25
while True:
    try:
        desplazamiento = int(input("Ingrese el desplazamiento: "))
        if desplazamiento >= 1 and desplazamiento <= 25:
            break
        else:
            print("Ingrese un numero entre 1 y 25")
    except ValueError:
        print("Ingrese un numero entre 1 y 25")
        

#se crea un while para que el usuario ingrese una opcion valida

while True:
    
    #se crea una variable para almacenar la opcion ingresada por el usuario
    opcion = input("Ingrese la opcion que desea realizar: \n1. Cifrar \n2. Descifrar \n")
    
    #se crea un if para verificar si el usuario ingreso una opcion valida
    if opcion == "1" or opcion == "2":
        break
    else:
        print("Ingrese una opcion valida")
        
#se crea un if para verificar si el usuario desea cifrar o descifrar el texto ingresado

if opcion == "1":
    
    #se llama la funcion cifrar
    cifrar(texto, desplazamiento)
    
else:
    
    #se llama la funcion descifrar
    descifrar(texto, desplazamiento)
    
#se imprime un mensaje de despedida
print("Gracias por usar el programa")
