
def agregarAlumno():
    """AGREGANDO ALUMNO PUPUPIPU."""

    nuevoAlumno = {
        "Alumno": {
            "nombre": "",
            "ID de alumno": "",
            "edad": 0
        }
    }

    print("\n=== AGREGAR NUEVO ALUMNO ===")
    nuevoAlumno["Alumno"]["nombre"] = input("Dame el nombre del Alumno: ")
    nuevoAlumno["Alumno"]["ID de alumno"] = input("Dame el ID del Alumno: ")
    nuevoAlumno["Alumno"]["edad"] = int(input("Dame la edad del Alumno: "))

    print(f"\nAlumno '{nuevoAlumno['Alumno']['nombre']}' agregado correctamente.\n")
    return nuevoAlumno
