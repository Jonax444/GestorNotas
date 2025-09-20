def Mostrarmenu():
    print("===== GESTOR DE NOTAS ACADÉMICAS ====")
    print("1. Registrar nuevo curso y nota")
    print("2. Mostrar todos los cursos y notas")
    print("3. Calcular promedio general")
    print("4. Contar cursos aprobados y reprobados")
    print("5. Buscar curso por nombre (Lienal) ")
    print("6. Actualizar nota de un curso")
    print("7. Eliminar un curso")
    print("8. Ordenar cursos por nota ")
    print("9. Ordenar cursos por nombre ")
    print("10. Buscar curso por nombre (Binaria) ")
    print("11. Simular cola de solicitudes de revisión")
    print("12. Mostrar historial de cambios ")
    print("13. Salir")

def pedir_curso():
    print("===== REGISTRO DE CURSOS Y NOTAS =====")
    nombre = input("Ingrese el nombre del curso: ")
    nota = float(input("Ingrese la nota: "))
    return {"nombre": nombre, "nota": nota}

def Mostrar_curso():
    print("Cursos y notas disponibles:")
    if cursos:
        for i, c in enumerate(cursos, start=1):
            print(f"{i}. {c['nombre']} - {c['nota']}")
    else:
        print("No hay cursos registrados.")
    print()

def  Promedio():
    print(" Calcular promedio general")
    if cursos:
        notas = [curso['nota'] for curso in cursos]
        promedio = sum(notas) / len(notas)
        print(f"El promedio general es: {promedio:.2f}")
    else:
        print("No hay cursos registrados para calcular promedio.")

def aprobados_reprobado():
    aprobados = 0
    reprobados = 0

    print("Contar cursos aprobados y reprobados")
    for curso in cursos:
        if curso['nota'] >= 61:
            aprobados += 1
        elif curso['nota'] < 61:
            reprobados += 1
    print(f" La cantidadade de cursos aprobadoes es de: {aprobados:d}")
    print(f"la cantidade de reprobados es de: {reprobados:d}")


def busquedacursolineal(cursos, busqueda):
    if not cursos:
        print("No hay cursos registrados")
        return False

    for curso in cursos:
        if curso['nombre'].lower() == busqueda.lower():
            print(f"Curso encontrado:")
            print(f"Nombre: {curso['nombre']}")
            print(f"Nota: {curso['nota']}")
            return True

    print("El curso no está en la lista")
    return False

def actualizar_nota_curso(cursos, nombre_cursos, nota_nueva):
    for curso in cursos:
        if curso['nombre'].lower() == nombre_cursos.lower():
            curso['nota'] = nota_nueva
            return True
    return False

def Mostrar_actualizacion():
    print("Lista actualizada")
    if cursos:
        for i, c in enumerate(cursos, start=1):
            print(f"{i}. {c['nombre']} - {c['nota']}")
    else:
        print("No hay cursos registrados.")
    print()

def eliminar_curso(cursos, remover):
    if not cursos:
        print("No hay cursos registrados")
        return
    remover = input("Ingrese el nombre del curso que desea eliminar: ")
    for curso in cursos:
        if curso['nombre'].lower() == remover.lower():
            cursos.remove(curso)
            return True
    else:
        print("Curso no encontrado")
        return False

def preguntar_continuar():
    while True:
        respuesta = input("¿Desea realizar otra acción dentro de esta opción? (S/N): ").upper()
        if respuesta in ["SI", "S"]:
            return True
        elif respuesta in ["NO", "N"]:
            return False
        else:
            print("Respuesta inválida")

def ordenar_nota(cursos):
    if cursos:
        cursos.sort(key=lambda curso: curso["nota"], reverse=True)
        Mostrar_curso()

def ordenar_curso(cursos):
    if cursos:
        cursos.sort(key=lambda curso: curso["nombre"].lower())
        print("Cursos ordenados alfabéticamente:")
        Mostrar_curso()
    else:
        print("No hay cursos para ordenar")


def verificar_orden_alfabetico(cursos):
    if len(cursos) <= 1:
        return True

    for i in range(len(cursos) - 1):
        if cursos[i]['nombre'].lower() > cursos[i + 1]['nombre'].lower():
            return False
    return True


def busqueda_binaria(cursos, busqueda):
    if not cursos:
        print("No hay cursos registrados")
        return False

    izquierda = 0
    derecha = len(cursos) - 1
    busqueda_lower = busqueda.lower().strip()
    comparaciones = 0

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        curso_medio = cursos[medio]
        nombre_medio = curso_medio['nombre'].lower()
        comparaciones += 1

        print(f"Comparación #{comparaciones}: Posición {medio} - '{curso_medio['nombre']}'")

        if nombre_medio == busqueda_lower:
            estado = "APROBADO" if curso_medio['nota'] >= 61 else "REPROBADO"
            print(f"\n ¡CURSO ENCONTRADO en {comparaciones} comparaciones!")
            print(f"Nombre: {curso_medio['nombre']}")
            print(f"Nota: {curso_medio['nota']} ({estado})")
            print(f"Posición en la lista: {medio + 1}")
            return True
        elif nombre_medio < busqueda_lower:
            print(f"   → '{curso_medio['nombre']}' < '{busqueda}' → Buscar en mitad derecha")
            izquierda = medio + 1
        else:
            print(f"   → '{curso_medio['nombre']}' > '{busqueda}' → Buscar en mitad izquierda")
            derecha = medio - 1

    print(f"\n Curso '{busqueda}' no encontrado después de {comparaciones} comparaciones")
    return False


cursos = []


repetir = True
while repetir:

    Mostrarmenu()
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        while True:
            print("Registrar nuevo curso")
            curso = pedir_curso()
            cursos.append(curso)
            print("Curso guardado.\n")

            if not preguntar_continuar():
                break

    elif opcion == 2:
       mostrarcur = print(" Mostrar todos los cursos y notas: ")
       Mostrar_curso()

    elif opcion == 3:
        Promedio()

    elif opcion == 4:
        aprobados_reprobado()

    elif opcion == 5:
        while True:
            print("Buscar curso por nombre (Lineal)")
            busqueda = input("Ingrese el nombre del curso: ")
            busquedacursolineal(cursos, busqueda)

            if not preguntar_continuar():
                break

    elif opcion == 6:
        while True:
            print("Actualizar nota de un curso")
            Mostrar_curso()

            if not cursos:
                print("No hay cursos registrados")
                break
            else:
                nombre_curso = input("Ingrese el nombre del curso: ")

                while True:
                    try:
                        nueva_nota = float(input("Ingrese la nueva nota (0-100): "))
                        if 0 <= nueva_nota <= 100:
                            break
                        else:
                            print("Nota inválida. Debe estar entre 0 y 100")
                    except ValueError:
                        print("Por favor ingrese un número válido")

                if actualizar_nota_curso(cursos, nombre_curso, nueva_nota):
                    print("Nota actualizada correctamente")
                    Mostrar_actualizacion()
                else:
                    print("Curso no encontrado")

                if not preguntar_continuar():
                    break

    elif opcion == 7:
        while True:
            print("Eliminar un curso")
            Mostrar_curso()

            if eliminar_curso(cursos, None):
                print("Curso eliminado correctamente")
                Mostrar_curso()
            else:
                pass

            if not preguntar_continuar():
                break

    elif opcion == 8:
        print("Ordenar cursos por nota")
        Mostrar_curso()

        while True:
            if not cursos:
                print("No hay cursos registrados")
                break

            orden = input("Desea ordenar las notas de los cursos? (S/N): ").upper()

            if orden in ["SI", "S"]:
                ordenar_nota(cursos)
                if not preguntar_continuar():
                    break
            elif orden in ["NO", "N"]:
                break
            else:
                print("Opcion invalida")

    elif opcion == 9:
        while True:
            print("ORDENAR CURSOS POR NOMBRE")

            if not cursos:
                print("No hay cursos registrados")
                break

            print("Cursos actuales:")
            Mostrar_curso()

            while True:
                orden_cur = input("¿Desea ordenar cursos en orden alfabético? (S/N): ").strip().upper()

                if orden_cur in ["SI", "S"]:
                    ordenar_curso(cursos)
                    print(" Cursos ordenados alfabéticamente")
                    break
                elif orden_cur in ["NO", "N"]:
                    print("Ordenamiento cancelado")
                    break
                else:
                    print("Opción inválida. Por favor ingrese S o N")

            if not preguntar_continuar():
                break

    elif opcion == 10:
        while True:
            print("BÚSQUEDA BINARIA POR NOMBRE ")

            if not cursos:
                print("No hay cursos registrados")
                break

            print("Cursos actuales:")
            Mostrar_curso()

            if not verificar_orden_alfabetico(cursos):
                print("  ADVERTENCIA: Los cursos no están ordenados alfabéticamente")
                print("La búsqueda binaria requiere que la lista esté ordenada por nombre")
                print("Por favor, use la opción 9 primero para ordenar los cursos alfabéticamente")
                print("Búsqueda binaria cancelada")
                break

            print("\n--- BÚSQUEDA BINARIA ---")
            busqueda = input("Ingrese el nombre exacto del curso a buscar: ").strip()

            if busqueda:
                print(f"\nIniciando búsqueda binaria de: '{busqueda}'")
                print("-" * 50)
                busqueda_binaria(cursos, busqueda)
            else:
                print("Nombre de curso no puede estar vacío")

            if not preguntar_continuar():
                break

    elif opcion == 11:
        print("Simular cola de solicitudes de revisión")
    elif opcion == 12:
        print("Mostrar historial de cambios")
    elif opcion == 13:
        print("Saliendo del programa...")
        repetir = False
    else:
        print(" Opción no válida, intente de nuevo.")
