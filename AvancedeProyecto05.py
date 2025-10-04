from collections import deque


# Función que muestra el menú principal con todas las opciones disponibles
def Mostrarmenu():
    print("===== GESTOR DE NOTAS ACADÉMICAS ====")
    print("1. Registrar nuevo curso y nota")
    print("2. Mostrar todos los cursos y notas")
    print("3. Calcular promedio general")
    print("4. Contar cursos aprobados y reprobados")
    print("5. Buscar curso por nombre (Lineal) ")
    print("6. Actualizar nota de un curso")
    print("7. Eliminar un curso")
    print("8. Ordenar cursos por nota ")
    print("9. Ordenar cursos por nombre ")
    print("10. Buscar curso por nombre (Binaria) ")
    print("11. Simular cola de solicitudes de revisión")
    print("12. Mostrar historial de cambios ")
    print("13. Salir")


# Función para pedir los datos de un nuevo curso
def pedir_curso():
    print("===== REGISTRO DE CURSOS Y NOTAS =====")
    nombre = input("Ingrese el nombre del curso: ")
    nota = float(input("Ingrese la nota: "))
    # Devuelve un diccionario con el nombre y nota del curso
    return {"nombre": nombre, "nota": nota}


# Función que muestra todos los cursos registrados con sus notas
def Mostrar_curso():
    print("Cursos y notas disponibles:")
    if cursos:
        # Recorre la lista de cursos y los enumera desde 1
        for i, c in enumerate(cursos, start=1):
            print(f"{i}. {c['nombre']} - {c['nota']}")
    else:
        print("No hay cursos registrados.")
    print()


# Función que calcula el promedio de todas las notas
def Promedio():
    print(" Calcular promedio general")
    if cursos:
        # Extrae solo las notas de todos los cursos
        notas = [curso['nota'] for curso in cursos]
        # Suma todas las notas y las divide entre la cantidad
        promedio = sum(notas) / len(notas)
        print(f"El promedio general es: {promedio:.2f}")
    else:
        print("No hay cursos registrados para calcular promedio.")


# Función que cuenta cuántos cursos están aprobados y cuántos reprobados
def aprobados_reprobado():
    aprobados = 0
    reprobados = 0

    print("Contar cursos aprobados y reprobados")
    # Recorre cada curso y verifica si aprobó o no (61 es la nota mínima)
    for curso in cursos:
        if curso['nota'] >= 61:
            aprobados += 1
        elif curso['nota'] < 61:
            reprobados += 1
    print(f" La cantidad de cursos aprobados es de: {aprobados:d}")
    print(f"La cantidad de reprobados es de: {reprobados:d}")


# Búsqueda lineal: revisa cada curso uno por uno hasta encontrar el buscado
def busquedacursolineal(cursos, busqueda):
    if not cursos:
        print("No hay cursos registrados")
        return False

    # Revisa cada curso de la lista
    for curso in cursos:
        # Compara el nombre sin importar mayúsculas/minúsculas
        if curso['nombre'].lower() == busqueda.lower():
            print(f"Curso encontrado:")
            print(f"Nombre: {curso['nombre']}")
            print(f"Nota: {curso['nota']}")
            return True

    print("El curso no está en la lista")
    return False


# Función que busca un curso y actualiza su nota
def actualizar_nota_curso(cursos, nombre_cursos, nota_nueva):
    for curso in cursos:
        # Si encuentra el curso, cambia la nota
        if curso['nombre'].lower() == nombre_cursos.lower():
            curso['nota'] = nota_nueva
            return True
    return False


# Muestra los cursos después de una actualización
def Mostrar_actualizacion():
    print("Lista actualizada")
    if cursos:
        for i, c in enumerate(cursos, start=1):
            print(f"{i}. {c['nombre']} - {c['nota']}")
    else:
        print("No hay cursos registrados.")
    print()


# Función que elimina un curso de la lista
def eliminar_curso(cursos, remover):
    if not cursos:
        print("No hay cursos registrados")
        return
    remover = input("Ingrese el nombre del curso que desea eliminar: ")
    for curso in cursos:
        # Si encuentra el curso, lo elimina de la lista
        if curso['nombre'].lower() == remover.lower():
            cursos.remove(curso)
            return True
    else:
        print("Curso no encontrado")
        return False


# Pregunta al usuario si quiere seguir haciendo acciones en la opción actual
def preguntar_continuar():
    while True:
        respuesta = input("¿Desea realizar otra acción dentro de esta opción? (S/N): ").upper()
        if respuesta in ["SI", "S"]:
            return True
        elif respuesta in ["NO", "N"]:
            return False
        else:
            print("Respuesta inválida")


# Ordenamiento por burbuja: compara cursos vecinos y los intercambia si están desordenados
def ordenar_nota(cursos):
    """Ordenamiento por burbuja - ordena por nota de mayor a menor"""
    if not cursos:
        return

    n = len(cursos)
    print("\n--- ORDENAMIENTO POR BURBUJA ---")

    # Recorre toda la lista varias veces
    for i in range(n):
        intercambios = 0
        # Compara cada par de cursos vecinos
        for j in range(0, n - i - 1):
            # Si el curso actual tiene menor nota que el siguiente, los intercambia
            if cursos[j]['nota'] < cursos[j + 1]['nota']:
                cursos[j], cursos[j + 1] = cursos[j + 1], cursos[j]
                intercambios += 1

        # Si no hubo cambios, significa que ya está ordenado
        if intercambios == 0:
            break

    print("Cursos ordenados por nota (mayor a menor):")
    Mostrar_curso()


# Ordenamiento por inserción: toma cada curso y lo coloca en su lugar correcto
def ordenar_curso(cursos):
    """Ordenamiento por inserción - ordena alfabéticamente por nombre"""
    if not cursos:
        print("No hay cursos para ordenar")
        return

    print("\n--- ORDENAMIENTO POR INSERCIÓN ---")

    # Comienza desde el segundo curso
    for i in range(1, len(cursos)):
        curso_actual = cursos[i]
        j = i - 1

        # Mueve los cursos que van después alfabéticamente hacia adelante
        while j >= 0 and cursos[j]['nombre'].lower() > curso_actual['nombre'].lower():
            cursos[j + 1] = cursos[j]
            j -= 1

        # Coloca el curso actual en su posición correcta
        cursos[j + 1] = curso_actual

    print("Cursos ordenados alfabéticamente:")
    Mostrar_curso()


# Verifica si los cursos están ordenados alfabéticamente (necesario para búsqueda binaria)
def verificar_orden_alfabetico(cursos):
    if len(cursos) <= 1:
        return True

    # Revisa que cada curso esté antes que el siguiente alfabéticamente
    for i in range(len(cursos) - 1):
        if cursos[i]['nombre'].lower() > cursos[i + 1]['nombre'].lower():
            return False
    return True


# Búsqueda binaria: divide la lista a la mitad repetidamente para encontrar el curso
# IMPORTANTE: Solo funciona si los cursos están ordenados alfabéticamente
def busqueda_binaria(cursos, busqueda):
    if not cursos:
        print("No hay cursos registrados")
        return False

    # Define los extremos de la búsqueda
    izquierda = 0
    derecha = len(cursos) - 1
    busqueda_lower = busqueda.lower().strip()
    comparaciones = 0

    # Mientras haya elementos por revisar
    while izquierda <= derecha:
        # Encuentra el curso del medio
        medio = (izquierda + derecha) // 2
        curso_medio = cursos[medio]
        nombre_medio = curso_medio['nombre'].lower()
        comparaciones += 1

        print(f"Comparación #{comparaciones}: Posición {medio} - '{curso_medio['nombre']}'")

        # Si el curso del medio es el que buscamos
        if nombre_medio == busqueda_lower:
            estado = "APROBADO" if curso_medio['nota'] >= 61 else "REPROBADO"
            print(f"\n ¡CURSO ENCONTRADO en {comparaciones} comparaciones!")
            print(f"Nombre: {curso_medio['nombre']}")
            print(f"Nota: {curso_medio['nota']} ({estado})")
            print(f"Posición en la lista: {medio + 1}")
            return True
        # Si el curso buscado va después alfabéticamente, busca en la mitad derecha
        elif nombre_medio < busqueda_lower:
            print(f"   → '{curso_medio['nombre']}' < '{busqueda}' → Buscar en mitad derecha")
            izquierda = medio + 1
        # Si el curso buscado va antes alfabéticamente, busca en la mitad izquierda
        else:
            print(f"   → '{curso_medio['nombre']}' > '{busqueda}' → Buscar en mitad izquierda")
            derecha = medio - 1

    print(f"\n Curso '{busqueda}' no encontrado después de {comparaciones} comparaciones")
    return False


# ========== FUNCIONES PARA HISTORIAL DE CAMBIOS (PILA) ==========

# Registra una acción en el historial (agrega al tope de la pila)
def registrar_cambio(historial, tipo_accion, detalles):
    from datetime import datetime

    # Crea un registro con la fecha y hora actual
    cambio = {
        'tipo': tipo_accion,
        'detalles': detalles,
        'fecha': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

    # Agrega el cambio al tope de la pila
    historial.append(cambio)


# Muestra todo el historial de cambios (desde el más reciente al más antiguo)
def mostrar_historial(historial):
    if not historial:
        print("\nNo hay cambios registrados en el historial")
        return

    print("\n===== HISTORIAL DE CAMBIOS =====")
    print(f"Total de acciones: {len(historial)}\n")

    # Recorre la pila desde el final (más reciente) hasta el inicio (más antiguo)
    for i in range(len(historial) - 1, -1, -1):
        cambio = historial[i]
        print(f"{len(historial) - i}. [{cambio['fecha']}] {cambio['tipo']}")
        print(f"   {cambio['detalles']}")
        print("-" * 60)


# Muestra solo los últimos N cambios
def mostrar_ultimos_cambios(historial, cantidad):
    if not historial:
        print("\nNo hay cambios registrados en el historial")
        return

    print(f"\n===== ÚLTIMOS {cantidad} CAMBIOS =====\n")

    # Calcula cuántos cambios mostrar (por si hay menos de los solicitados)
    inicio = max(0, len(historial) - cantidad)

    # Muestra desde el más reciente
    for i in range(len(historial) - 1, inicio - 1, -1):
        cambio = historial[i]
        print(f"[{cambio['fecha']}] {cambio['tipo']}")
        print(f"   {cambio['detalles']}")
        print("-" * 60)


# Deshacer el último cambio (sacar el tope de la pila)
def deshacer_ultimo_cambio(historial):
    if not historial:
        print("\nNo hay cambios para deshacer")
        return None

    # Saca el último cambio de la pila
    ultimo_cambio = historial.pop()
    print(f"\nÚltimo cambio deshecho:")
    print(f"[{ultimo_cambio['fecha']}] {ultimo_cambio['tipo']}")
    print(f"   {ultimo_cambio['detalles']}")

    return ultimo_cambio


# Menú para gestionar el historial
def menu_historial(historial):
    while True:
        print("\n===== HISTORIAL DE CAMBIOS =====")
        print("1. Ver todo el historial")
        print("2. Ver últimos 5 cambios")
        print("3. Ver últimos 10 cambios")
        print("4. Limpiar historial")

        try:
            opcion = int(input("\nSeleccione una opción: "))
        except ValueError:
            print("Opción inválida")
            continue

        if opcion == 1:
            mostrar_historial(historial)
        elif opcion == 2:
            mostrar_ultimos_cambios(historial, 5)
        elif opcion == 3:
            mostrar_ultimos_cambios(historial, 10)
        elif opcion == 4:
            confirmacion = input("¿Está seguro de limpiar todo el historial? (S/N): ").upper()
            if confirmacion in ["SI", "S"]:
                historial.clear()
                print("Historial limpiado correctamente")
            else:
                print("Operación cancelada")
        else:
            print("Opción no válida")

        # Pregunta si quiere seguir en este menú
        if not preguntar_continuar():
            break


# ========== FUNCIONES PARA COLA DE REVISIONES ==========

# Permite a un estudiante solicitar que revisen su nota
def agregar_solicitud_revision(cola_revisiones, cursos):
    if not cursos:
        print("No hay cursos registrados")
        return

    print("\n--- SOLICITAR REVISIÓN DE NOTA ---")
    Mostrar_curso()

    nombre_curso = input("Ingrese el nombre del curso a revisar: ").strip()

    # Busca si el curso existe en la lista
    curso_encontrado = None
    for curso in cursos:
        if curso['nombre'].lower() == nombre_curso.lower():
            curso_encontrado = curso
            break

    if not curso_encontrado:
        print("Curso no encontrado")
        return

    # Pide los datos de la solicitud
    nombre_estudiante = input("Ingrese su nombre (estudiante): ").strip()
    motivo = input("Ingrese el motivo de la revisión: ").strip()

    if not nombre_estudiante or not motivo:
        print("Debe ingresar todos los datos")
        return

    # Crea una nueva solicitud con un número único
    id_solicitud = len(cola_revisiones) + 1
    solicitud = {
        'id': id_solicitud,
        'curso': curso_encontrado['nombre'],
        'nota_actual': curso_encontrado['nota'],
        'estudiante': nombre_estudiante,
        'motivo': motivo,
        'estado': 'Pendiente'
    }

    # Agrega la solicitud al final de la cola
    cola_revisiones.append(solicitud)
    print(f"\nSolicitud #{id_solicitud} agregada a la cola de revisión")
    print(f"  Curso: {curso_encontrado['nombre']}")
    print(f"  Nota actual: {curso_encontrado['nota']}")
    print(f"  Posición en cola: {len(cola_revisiones)}")


# Muestra todas las solicitudes de revisión que están esperando
def ver_cola_revisiones(cola_revisiones):
    if not cola_revisiones:
        print("\nLa cola de revisiones está vacía")
        return

    print("\n===== COLA DE SOLICITUDES DE REVISIÓN =====")
    print(f"Total de solicitudes pendientes: {len(cola_revisiones)}\n")

    # Muestra cada solicitud con todos sus detalles
    for i, sol in enumerate(cola_revisiones, 1):
        print(f"{i}. Solicitud #{sol['id']}")
        print(f"   Curso: {sol['curso']}")
        print(f"   Nota actual: {sol['nota_actual']}")
        print(f"   Estudiante: {sol['estudiante']}")
        print(f"   Motivo: {sol['motivo']}")
        print(f"   Estado: {sol['estado']}")
        print("-" * 50)


# Procesa la primera solicitud de la cola (la más antigua)
def procesar_solicitud_revision(cola_revisiones, cursos):
    if not cola_revisiones:
        print("\nNo hay solicitudes pendientes para procesar")
        return

    # Saca la primera solicitud de la cola (FIFO = First In, First Out)
    solicitud = cola_revisiones.popleft()

    print("\n===== PROCESANDO SOLICITUD DE REVISIÓN =====")
    print(f"Solicitud #{solicitud['id']}")
    print(f"Curso: {solicitud['curso']}")
    print(f"Estudiante: {solicitud['estudiante']}")
    print(f"Nota actual: {solicitud['nota_actual']}")
    print(f"Motivo: {solicitud['motivo']}")
    print("-" * 50)

    # El revisor decide qué hacer con la solicitud
    print("\nOpciones:")
    print("1. Aprobar revisión y cambiar nota")
    print("2. Rechazar revisión (mantener nota)")
    print("3. Regresar a la cola")

    while True:
        try:
            opcion = int(input("\nSeleccione una opción: "))
            if opcion in [1, 2, 3]:
                break
            else:
                print("Opción inválida")
        except ValueError:
            print("Por favor ingrese un número válido")

    # Opción 1: Cambiar la nota
    if opcion == 1:
        while True:
            try:
                nueva_nota = float(input("Ingrese la nueva nota (0-100): "))
                if 0 <= nueva_nota <= 100:
                    break
                else:
                    print("Nota inválida. Debe estar entre 0 y 100")
            except ValueError:
                print("Por favor ingrese un número válido")

        # Busca el curso y actualiza su nota
        for curso in cursos:
            if curso['nombre'].lower() == solicitud['curso'].lower():
                nota_anterior = curso['nota']
                curso['nota'] = nueva_nota
                # Registra el cambio en el historial
                registrar_cambio(historial_cambios, "REVISIÓN APROBADA",
                                 f"Nota del curso '{solicitud['curso']}' cambiada de {nota_anterior} a {nueva_nota} (Estudiante: {solicitud['estudiante']})")
                print(f"\nNota actualizada correctamente")
                print(f"  Nota anterior: {solicitud['nota_actual']}")
                print(f"  Nota nueva: {nueva_nota}")
                break

    # Opción 2: Mantener la nota original
    elif opcion == 2:
        print(f"\nRevisión rechazada. La nota {solicitud['nota_actual']} se mantiene")

    # Opción 3: Devolver la solicitud al final de la cola
    elif opcion == 3:
        cola_revisiones.append(solicitud)
        print(f"\nSolicitud #{solicitud['id']} regresada al final de la cola")


# Menú especial para gestionar todas las solicitudes de revisión
def menu_cola_revisiones(cola_revisiones, cursos):
    while True:
        print("\n===== COLA DE SOLICITUDES DE REVISIÓN =====")
        print("1. Agregar solicitud de revisión")
        print("2. Ver cola de solicitudes")
        print("3. Procesar siguiente solicitud")

        try:
            opcion = int(input("\nSeleccione una opción: "))
        except ValueError:
            print("Opción inválida")
            continue

        if opcion == 1:
            agregar_solicitud_revision(cola_revisiones, cursos)
        elif opcion == 2:
            ver_cola_revisiones(cola_revisiones)
        elif opcion == 3:
            procesar_solicitud_revision(cola_revisiones, cursos)
        else:
            print("Opción no válida")

        # Pregunta si quiere seguir en este menú o volver al principal
        if not preguntar_continuar():
            break


# ========== PROGRAMA PRINCIPAL ==========

# Lista donde se guardan todos los cursos
cursos = []
# Cola donde se guardan las solicitudes de revisión
cola_revisiones = deque()
# Pila donde se guarda el historial de cambios (último cambio arriba)
historial_cambios = []

repetir = True
while repetir:

    Mostrarmenu()
    opcion = int(input("Seleccione una opción: "))

    # OPCIÓN 1: Agregar nuevos cursos
    if opcion == 1:
        while True:
            print("Registrar nuevo curso")
            curso = pedir_curso()
            cursos.append(curso)
            # Registra el cambio en el historial
            registrar_cambio(historial_cambios, "REGISTRO DE CURSO",
                             f"Curso '{curso['nombre']}' registrado con nota {curso['nota']}")
            print("Curso guardado.\n")

            if not preguntar_continuar():
                break

    # OPCIÓN 2: Ver todos los cursos registrados
    elif opcion == 2:
        mostrarcur = print(" Mostrar todos los cursos y notas: ")
        Mostrar_curso()

    # OPCIÓN 3: Calcular el promedio de todas las notas
    elif opcion == 3:
        Promedio()

    # OPCIÓN 4: Contar cuántos aprobaron y cuántos reprobaron
    elif opcion == 4:
        aprobados_reprobado()

    # OPCIÓN 5: Buscar un curso revisando toda la lista (búsqueda lineal)
    elif opcion == 5:
        while True:
            print("Buscar curso por nombre (Lineal)")
            busqueda = input("Ingrese el nombre del curso: ")
            busquedacursolineal(cursos, busqueda)

            if not preguntar_continuar():
                break

    # OPCIÓN 6: Cambiar la nota de un curso
    elif opcion == 6:
        while True:
            print("Actualizar nota de un curso")
            Mostrar_curso()

            if not cursos:
                print("No hay cursos registrados")
                break
            else:
                nombre_curso = input("Ingrese el nombre del curso: ")

                # Verifica que la nota sea válida (entre 0 y 100)
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
                    # Registra el cambio en el historial
                    registrar_cambio(historial_cambios, "ACTUALIZACIÓN DE NOTA",
                                     f"Nota del curso '{nombre_curso}' actualizada a {nueva_nota}")
                    print("Nota actualizada correctamente")
                    Mostrar_actualizacion()
                else:
                    print("Curso no encontrado")

                if not preguntar_continuar():
                    break

    # OPCIÓN 7: Eliminar un curso de la lista
    elif opcion == 7:
        while True:
            print("Eliminar un curso")
            Mostrar_curso()

            if eliminar_curso(cursos, None):
                # Registra el cambio en el historial
                registrar_cambio(historial_cambios, "ELIMINACIÓN DE CURSO",
                                 f"Un curso fue eliminado del sistema")
                print("Curso eliminado correctamente")
                Mostrar_curso()
            else:
                pass

            if not preguntar_continuar():
                break

    # OPCIÓN 8: Ordenar los cursos por nota (de mayor a menor) usando burbuja
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
                # Registra el cambio en el historial
                registrar_cambio(historial_cambios, "ORDENAMIENTO POR NOTA",
                                 f"Cursos ordenados por nota (método burbuja)")
                if not preguntar_continuar():
                    break
            elif orden in ["NO", "N"]:
                break
            else:
                print("Opcion invalida")

    # OPCIÓN 9: Ordenar los cursos alfabéticamente usando inserción
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
                    # Registra el cambio en el historial
                    registrar_cambio(historial_cambios, "ORDENAMIENTO ALFABÉTICO",
                                     f"Cursos ordenados alfabéticamente (método inserción)")
                    print(" Cursos ordenados alfabéticamente")
                    break
                elif orden_cur in ["NO", "N"]:
                    print("Ordenamiento cancelado")
                    break
                else:
                    print("Opción inválida. Por favor ingrese S o N")

            if not preguntar_continuar():
                break

    # OPCIÓN 10: Buscar un curso dividiendo la lista a la mitad (búsqueda binaria)
    # IMPORTANTE: Solo funciona si los cursos están ordenados alfabéticamente
    elif opcion == 10:
        while True:
            print("BÚSQUEDA BINARIA POR NOMBRE ")

            if not cursos:
                print("No hay cursos registrados")
                break

            print("Cursos actuales:")
            Mostrar_curso()

            # Verifica que los cursos estén ordenados antes de buscar
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

    # OPCIÓN 11: Gestionar solicitudes de revisión de notas
    elif opcion == 11:
        menu_cola_revisiones(cola_revisiones, cursos)

    # OPCIÓN 12: Ver el historial de todos los cambios realizados
    elif opcion == 12:
        menu_historial(historial_cambios)

    # OPCIÓN 13: Salir del programa
    elif opcion == 13:
        print("Saliendo del programa...")
        repetir = False
    else:
        print(" Opción no válida, intente de nuevo.")