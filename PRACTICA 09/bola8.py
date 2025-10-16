nombre = input ("ingresa tu nombre: ")
print ("hola", nombre, "bienvenido a la bola 8")
pregunta_bienvenida= input ("¿quieres hacer una pregunta? (si/no): ")
pregunta= input ("¿cual es tu pregunta? ")
import random
while True:
    opcion= input ("¿quieres que te responda? (si/no): ").lower()
    if opcion == "no":
        break
    respuestas = ["Es cierto", "Es decididamente así", "Sin lugar a dudas", "Sí, definitivamente", " Puedes confiar en ello", "Como yo lo veo, sí", "Lo más probable", "Perspectiva buena", "Sí",  "Las señales apuntan a que sí", " Respuesta confusa, vuelve a intentarlo.", "Vuelve a preguntar más tarde", "Mejor no decirte ahora", "No se puede predecir ahora", "Concéntrate y vuelve a preguntar", "No cuentes con ello", "Mi respuesta es no", "Mis fuentes dicen que no", "Las perspectivas no son muy buenas", "Muy dudoso"]
    print (random.choice(respuestas))
print ("gracias por jugar, hasta luego", nombre)