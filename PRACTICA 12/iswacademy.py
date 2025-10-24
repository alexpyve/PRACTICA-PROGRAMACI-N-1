#agregar cursooo
def agregar_curso(cursos):
    nombre = input("Nombre del curso: ")
    instructor = input("Nombre del instructor: ")
    aula = input("Aula: ")
    cursos.append([nombre, instructor, aula, []])
    print("\n Curso agregado correctamente.\n")

#eliminar cursooo

def eliminar_curso(cursos):
    mostrar_cursos(cursos)
    if len(cursos) == 0:
        print("No hay cursos para eliminar.\n")
        return
    
    indice = int(input("Número del curso a eliminar: ")) - 1
    if indice >= 0 and indice < len(cursos):
        eliminado = cursos.pop(indice)
        print(f"\n Curso '{eliminado[0]}' eliminado correctamente.\n")
    else:
        print("Número inválido.\n")

#modificarloooo

def modificar_curso(cursos):
    mostrar_cursos(cursos)
    if len(cursos) == 0:
        print("No hay cursos para modificar.\n")
        return
    
    indice = int(input("Número del curso a modificar: ")) - 1
    if indice >= 0 and indice < len(cursos):
        curso = cursos[indice]
        print(f"\nEditando curso: {curso[0]}")
        nuevo_nombre = input("Nuevo nombre (Enter para dejar igual): ")
        nuevo_instructor = input("Nuevo instructor (Enter para dejar igual): ")
        nueva_aula = input("Nueva aula (Enter para dejar igual): ")

        if nuevo_nombre != "":
            curso[0] = nuevo_nombre
        if nuevo_instructor != "":
            curso[1] = nuevo_instructor
        if nueva_aula != "":
            curso[2] = nueva_aula

        print("\n Curso actualizado correctamente.\n")
    else:
        print("Número inválido.\n")

#mostrarloooo
def mostrar_cursos(cursos):
    if len(cursos) == 0:
        print("\n No hay cursos registrados.\n")
    else:
        print("\n LISTA DE CURSOS:")
        for i in range(len(cursos)):
            curso = cursos[i]
            print(f"{i+1}. {curso[0]} - Instructor: {curso[1]} - Aula: {curso[2]} -   Alumnos: {len(curso[3])}")
        print()

#agregar alumnooo
def agregar_alumno(curso):
    alumno = input("Nombre del alumno: ")
    curso[3].append(alumno)
    print(f" Alumno '{alumno}' agregado al curso '{curso[0]}'.\n")

#bajaaa
def dar_baja_alumno(curso):
    mostrar_alumnos(curso)
    if len(curso[3]) == 0:
        print("No hay alumnos para dar de baja.\n")
        return
    
    indice = int(input("Número del alumno a dar de baja: ")) - 1
    if indice >= 0 and indice < len(curso[3]):
        eliminado = curso[3].pop(indice)
        print(f" Alumno '{eliminado}' dado de baja correctamente.\n")
    else:
        print("Número inválido.\n")

#mostraaaaaar
def mostrar_alumnos(curso):
    print(f"\n ALUMNOS DEL CURSO '{curso[0]}':")
    if len(curso[3]) == 0:
        print("No hay alumnos inscritos.\n")
    else:
        for i in range(len(curso[3])):
            print(f"{i+1}. {curso[3][i]}")
        print()


def menu():
    cursos = []

    while True:
        print("""

*********ACADEMIA DE INGENIERÍA EN SOFTWARE *********
1. Agregar curso
2. Eliminar curso
3. Modificar curso
4. Mostrar cursos
5. opciones de alumnos
6. Salir
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_curso(cursos)

        elif opcion == "2":
            eliminar_curso(cursos)

        elif opcion == "3":
            modificar_curso(cursos)

        elif opcion == "4":
            mostrar_cursos(cursos)

        elif opcion == "5":
            if len(cursos) == 0:
                print("\n No hay cursos registrados.\n")
            else:
                mostrar_cursos(cursos)
                id_curso = int(input("Seleccione el número del curso: ")) - 1

                if id_curso >= 0 and id_curso < len(cursos):
                    curso = cursos[id_curso]

                    while True:
                        print(f"""
 ALUMNOS OPCIONES - {curso[0]} 
1. Agregar alumno
2. Dar de baja alumno
3. Mostrar alumnos
4. Volver al menú principal
""")
                        subop = input("Seleccione una opción: ")

                        if subop == "1":
                            agregar_alumno(curso)
                        elif subop == "2":
                            dar_baja_alumno(curso)
                        elif subop == "3":
                            mostrar_alumnos(curso)
                        elif subop == "4":
                            break
                        else:
                            print("Opción no válida.\n")
                else:
                    print("Número inválido de curso.\n")

        elif opcion == "6":
            print("\n Ha salido del programa baibai \n")
            break

        else:
            print("\n Opción no válida. Intente de nuevo.\n")


menu()
