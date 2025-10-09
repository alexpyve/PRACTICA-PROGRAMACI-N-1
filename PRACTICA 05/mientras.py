
monto = float (input ("ingresa el monto disponible a invertir"))
saldo=0
print ("saldo disponible es:", saldo)
saldo = float (input ("ingresa la cantidad que deseas invertir en esta compra:"))

terminar = False

while not terminar:
    if monto > saldo and monto > 0:
        print ("compra realizada, saldo restante", saldo)
    elif monto < saldo and monto < 0:
        print ("el monto debe ser mayor que 0")
        terminar = True