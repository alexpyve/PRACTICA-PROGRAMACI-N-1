#if else elif

from unittest import case


edad = 25  #int (input ("dime tu edad:"))

if edad >= 10 and edad <18:
    print ("eres un adolescente")
elif edad >= 18:
    print ("eres un adulto")
else:
    print ("todavia eres un niño")



    #match

opcion = int (input("""
1. agregar
2. editar
3. eliminar
4.leer
5.finalizar
"""))

match opcion:
    case 1:
        print ("Se ha agregado correctamente")
    case 2:
        print ("Se ha modificado correctamente")
    case 3:
        print ("Se ha aeliminado correctamente")
    case 4:
        print ("El usuario registrado se llama Jorge")
    case 5:
        print ("Se ha finalizado el programa")

case



