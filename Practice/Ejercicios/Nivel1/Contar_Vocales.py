#contar las vocales ingresadas por el usuario

#se crea una variable para almacenar el texto ingresado por el usuario

texto_ingresado= input("Ingrese una palabra o frase: ")

#se crea una variable para almacenar el numero de vocales que se encuentren en el texto ingresado

vocales = 0

#se crea un for para recorrer el texto ingresado

for i in texto_ingresado:
        
        #se crea un if para verificar si el caracter es una vocal
        
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            
            #se incrementa la variable vocales en 1
            
            vocales += 1
            
#se imprime el numero de vocales que se encontraron en el texto ingresado

print("El numero de vocales en el texto ingresado es: {}".format(vocales))
