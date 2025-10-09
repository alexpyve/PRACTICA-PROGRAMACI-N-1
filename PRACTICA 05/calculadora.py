while True:
    print ("\n CALCULADORA BASICA")
    print ("1. Suma")
    print ("2. Resta")
    print ("3. Multiplicacion")
    print ("4. Division")
    print ("5. Salir")
    opcion = input ("Elige una opcion (1-5): ")
    if opcion == '1':
        num1 = int(input("Ingresa el primer numero: "))
        num2 = int(input("Ingresa el segundo numero: "))
        print("El resultado de la suma es:", num1 + num2)

    elif opcion == '2':
        num1 = int(input("Ingresa el primer numero: "))
        num2 = int(input("Ingresa el segundo numero: "))
        print("El resultado de la resta es:", num1 - num2)

    elif opcion == '3':
        num1 = int(input("Ingresa el primer numero: "))
        num2 = int(input("Ingresa el segundo numero: "))
        print("El resultado de la multiplicacion es:", num1 * num2)

    elif opcion == '4':
        num1 = int(input("Ingresa el primer numero: "))
        num2 = int(input("Ingresa el segundo numero: "))

        if num2 != 0:
            print("El resultado de la division es:", num1 / num2)
        else:
            print("Error: No se puede dividir entre cero.")
            
    elif opcion == '5':
        print("Saliendo de la calculadora. ¡Hasta luego!")
        break
    else:
        print("Opcion no valida. Por favor, elige una opcion del 1 al 5.")
# Calculadora basica en Python