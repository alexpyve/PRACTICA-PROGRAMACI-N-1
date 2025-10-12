op=input ("ingrese el texto a analizar:")
op=op.lower()
op1 = input ("ingrese la primera letra a buscar:")
op=op.lower()
op2 = input ("ingrese la segunda letra a buscar:")
op=op.lower()
op3 = input ("ingrese la tercera letra a buscar:")
op=op.lower()

a=op.count(op1)
b=op.count(op2)
c=op.count(op3)

for letra in op:
    if letra==op1:
        a=a+1
    if letra==op2:
        b=b+1
    if letra==op3:
        c=c+1

print ("la letra",op1,"se repite",a,"veces")
print ("la letra",op2,"se repite",b,"veces")
print ("la letra",op3,"se repite",c,"veces")

contador_palabras=0
lista_palabras=op.split()
for palabra in lista_palabras:
    contador_palabras=contador_palabras+1
print ("el texto tiene",contador_palabras,"palabras")

for vuelta in reversed(range(len(op))):
    print (op[vuelta],end="")

if "python" in op.lower():
    print("\n La palabra 'Python' fue encontrada en el texto.")
else:
    print("\n La palabra 'Python' no se encontró en el texto.")

