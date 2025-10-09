dia = (input("ingrese por favor el día de hoy"))
if (dia == "sabado" or dia == "domingo"):
    clima = (input("ingrese el clima"))
    match clima:
        case "soleado":
            print ("ve a la playa")
        case "nublado":
            print ("ve a caminar")
        case "lluvioso":
            print ("quedate en casa") 


dia = (input("ingrese por favor el día de hoy"))
if (dia == "lunes" or dia == "martes" or dia == "miercoles" or dia == "jueves" or dia == "viernes"):
    clima = (input("ingrese el clima"))
    match clima:
        case "soleado":
            print ("ve a visitar a un familiar y vayan a comer")
        case "nublado":
            print ("adelanta el trabajo de la oficina")
        case "lluvioso":
            print ("tomar cafe y dibujar") 
