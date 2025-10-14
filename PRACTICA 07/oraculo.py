

def calcular_elemento(anio):
    numero_elemento = anio%10
    if numero_elemento == 0 or numero_elemento == 1:
        return "metal ⚙️"
    if numero_elemento == 2 or numero_elemento == 3:
        return "agua 💧"
    if numero_elemento == 4 or numero_elemento == 5:
        return "madera 🪵"
    if numero_elemento == 6 or numero_elemento == 7:
        return "fuego 🔥"
    if numero_elemento == 8 or numero_elemento == 9:
        return "tierra 🌍"

def generar_prediccion (nombre,calcular_elemento,suerte):
    match suerte:
        case 1:
            print (f"{nombre} 🜚, tu conexion con el elemento: ¡{calcular_elemento}! te traera mucha suerte ¡aventurate en un nuevo pasatiempo!木")
        case 2:
            print (f"{nombre} 🜚, eres de ese porcentaje especial con el elemento: ¡{calcular_elemento}! te llovera dinero ¡empieza a disfrutar la vida!木")
        case 3:
            (f"{nombre} 🜚, veo que tienes una conexion con el elemento: ¡{calcular_elemento}! seras golpeado con mucha suerte ¡sal a buscar una aventura!木")
        case 4:
            print (f"{nombre} 🜚, reconozco que tu elemento: ¡{calcular_elemento}! es muy raro, recibiras buenas noticias ¡mantente preparado y abierto al cambio!木")
while True:

    nombre = input("金 ingrese su nombre:")
    print(" 土leyendo tu futuro tururururu",nombre)
    anio = int(input("✦ ingresa tu año de nacimiento:"))
    suerte = int(input("✰elige un numero de la suerte entre 1 y 4:"))

    edad = 2025-anio
    print("✫ tu edad es:", edad)
    elemnto = calcular_elemento (anio)
    print("☆ Tu elemento es:", elemnto)
    generar_prediccion (nombre,elemnto,suerte)

    respuesta= input("¿Desea seguir conociendo su suerte? SI/NO")
    if respuesta == 'NO' or respuesta == 'no' or respuesta == 'No':
        break

#   BRAULIO SARABIA 00000278656, JOSELYN PIVE 00000279281.