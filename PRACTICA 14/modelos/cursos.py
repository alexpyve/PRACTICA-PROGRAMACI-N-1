# modelos/cursos.py

def agregarCursos():

    curso = {
        "instructor": {
            "nombre": "",
            "titulo": "",
            "edad": 0
        },
        "aula": 0,
        "Alumnos": {}
    }

    print("\n=== AGREGAR NUEVO CURSO ===")
    curso["instructor"]["nombre"] = input("Dame el nombre del instructor: ")
    curso["instructor"]["titulo"] = input("Dame el título del instructor (Ej: Lic., Ing., Mtro., etc.): ")
    curso["instructor"]["edad"] = int(input("Dame la edad del instructor: "))
    curso["aula"] = int(input("Número de aula: "))

    print(f"\nCurso creado con instructor: {curso['instructor']['nombre']}.\n")
    return curso


def ModificarCurso(curso):
    """Permite modificar los datos de un curso existente."""
    print("\n=== MODIFICAR CURSO ===")
    print(f"Instructor actual: {curso['instructor']['nombre']}")
    print(f"Título actual: {curso['instructor']['titulo']}")
    print(f"Edad actual: {curso['instructor']['edad']}")
    print(f"Aula actual: {curso['aula']}\n")

    nuevo_nombre = input("Nuevo nombre del instructor: ")
    nuevo_titulo = input("Nuevo título del instructor: ")
    nueva_edad = input("Nueva edad del instructor: ")
    nuevo_aula = input("Nuevo número de aula: ")

    if nuevo_nombre != "":
        curso["instructor"]["nombre"] = nuevo_nombre
    if nuevo_titulo != "":
        curso["instructor"]["titulo"] = nuevo_titulo
    if nueva_edad != "":
        curso["instructor"]["edad"] = int(nueva_edad)
    if nuevo_aula != "":
        curso["aula"] = int(nuevo_aula)

    print("\nCurso actualizado correctamente.\n")
    return curso
