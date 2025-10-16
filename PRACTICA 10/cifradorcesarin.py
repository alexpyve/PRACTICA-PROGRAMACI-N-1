#print(ord("B"))
#isaplha es para saber si es letra o no


while True:
    print("\nCIFRADOR CÉSAR")
    print("1. Cifrar")
    print("2. Descifrar")
    print("3. Salir")
    opcion = input("Elige una opción (1-3): ")

    match opcion:
        case '1':  # Cifrar
            resultado = ""
            texto = input("Introduce el texto a cifrar: ")
            for caracter in texto:
                if caracter.isalpha():
                    valor_ascii = ord(caracter)
                    if caracter.islower():
                        limite = ord("z")
                        base = ord("a")
                    else:
                        limite = ord("Z")
                        base = ord("A")

                    nuevo_ascii = valor_ascii + 3
                    if nuevo_ascii > limite:
                        nuevo_ascii -= 26
                    resultado += chr(nuevo_ascii)
                else:
                    resultado += caracter
            resultado_con_guiones = resultado.replace(" ", "_")
            print("Tu mensaje cifrado es:", resultado_con_guiones)

        case '2':  # Descifrar
            resultado = ""
            texto = input("Introduce el texto a descifrar: ")
            for caracter in texto:
                if caracter.isalpha():
                    valor_ascii = ord(caracter)
                    if caracter.islower():
                        limite = ord("a")
                    else:
                        limite = ord("A")

                    nuevo_ascii = valor_ascii - 3
                    if nuevo_ascii < limite:
                        nuevo_ascii += 26
                    resultado += chr(nuevo_ascii)
                else:
                    resultado += caracter
            resultado_con_guiones = resultado.replace(" ", "_")
            print("Tu mensaje cifrado es:", resultado_con_guiones)

        case '3':  # Salir
            print("Saliendo del programa...")
            break

        case _:  # Opción inválida
            print("Opción no válida. Intenta otra vez.")

#JOSELYN ALEJANDRA PIVE CABANILLAS 00000279281, BRAULIO ANTONIO SARABIA RODRIGUEZ 00000278656
