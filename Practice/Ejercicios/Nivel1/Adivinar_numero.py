#ejercicio de adivinar un numero aleatorio

import random

numero_aleatorio = random.randint(1, 20)

print("Estoy pensando en un numero entre 1 y 20")

#se crea un for para que el usuario tenga 6 intentos de adivinar el numero
for intentos in range(1, 7):
    print("Adivina")
    numero = int(input())
    
    #pistas que le damos al usuario
    
    #si el numero ingresado es menor al numero aleatorio
    if numero < numero_aleatorio:
        print("Tu numero es muy bajo")
        
    #si el numero ingresado es mayor al numero aleatorio
    elif numero > numero_aleatorio:
        print("Tu numero es muy alto")
    else:
        break

#comparamos el numero ingresado con el numero aleatorio

if numero == numero_aleatorio:
    print("Correcto, adivinaste en {} intentos".format(intentos))
else:
    print("No, el numero que estaba pensando era {}".format(numero_aleatorio))
    
    
