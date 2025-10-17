from collections import deque


# ========== MENÚ PRINCIPAL ==========
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


# ========== FUNCIONES DE REGISTRO Y VISUALIZACIÓN ==========
# Función para pedir los datos de un nuevo curso
def pedir_curso():
    print("\n" + "=" * 50)
    print("REGISTRO DE CURSO Y NOTA")
    print("=" * 50)
    nombre = input("\nIngrese el nombre del curso: ").strip()

    # Pide la nota con validación de rango 0-100
    while True:
        try:
            print("Ingrese la nota del curso (rango: 0 a 100)")
            nota = float(input("Nota: "))
            if 0 <= nota <= 100:
                break
            else:
                print("ERROR: La nota debe estar entre 0 y 100. Intente de nuevo.")
        except ValueError:
            print("ERROR: Ingrese un número válido (ejemplo: 85.5)")

    print()
    # Devuelve un diccionario con el nombre y nota del curso
    return {"nombre": nombre, "nota": nota}


# Función que muestra todos los cursos registrados con sus notas
def Mostrar_curso():
    print("\n" + "=" * 50)
    print("CURSOS Y NOTAS REGISTRADOS")
    print("=" * 50)
    if cursos:
        # Recorre la lista de cursos y los enumera desde 1
        print(f"\n{'#':<3} {'Curso':<30} {'Nota':<10} {'Estado':<12}\n")
        print("-" * 50)
        for i, c in enumerate(cursos, start=1):
            estado = "APROBADO" if c['nota'] >= 61 else "REPROBADO"
            print(f"{i:<3} {c['nombre']:<30} {c['nota']:<10.2f} {estado}")
        print("-" * 50)
    else:
        print("\n⚠ No hay cursos registrados.\n")
    print()


# ========== FUNCIONES DE CÁLCULOS ==========
# Función que calcula el promedio de todas las notas
def Promedio():
    print("\n" + "=" * 50)
    print("CÁLCULO DE PROMEDIO GENERAL")
    print("=" * 50)

    if cursos:
        # Extrae solo las notas de todos los cursos
        notas = [curso['nota'] for curso in cursos]
        # Suma todas las notas y las divide entre la cantidad
        promedio = sum(notas) / len(notas)

        # Determina si el promedio es aprobado
        estado = "APROBADO" if promedio >= 61 else "REPROBADO"
        print(f"\nPromedio general: {promedio:.2f}")
        print(f"Estado: {estado}")
        print(f"Cantidad de cursos: {len(cursos)}\n")
    else:
        print("\n⚠ No hay cursos registrados para calcular promedio.\n")


# Función que cuenta cuántos cursos están aprobados y cuántos reprobados
def aprobados_reprobado():
    print("\n" + "=" * 50)
    print("ESTADÍSTICAS DE APROBACIÓN")
    print("=" * 50)

    aprobados = 0
    reprobados = 0

    # Recorre cada curso y verifica si aprobó o no (61 es la nota mínima)
    for curso in cursos:
        if curso['nota'] >= 61:
            aprobados += 1
        elif curso['nota'] < 61:
            reprobados += 1

    print(f"\nNota mínima para aprobar: 61")
    print(f"\nCursos APROBADOS:  {aprobados}")
    print(f"Cursos REPROBADOS: {reprobados}")
    print(f"Total de cursos:   {len(cursos)}\n")


# ========== FUNCIONES DE BÚSQUEDA ==========
# Búsqueda lineal: revisa cada curso uno por uno hasta encontrar el buscado
# Complejidad: O(n) - revisa todos los elementos si es necesario
def busquedacursolineal(cursos, busqueda):
    if not cursos:
        print("\n⚠ No hay cursos registrados\n")
        return False

    # Revisa cada curso de la lista
    for curso in cursos:
        # Compara el nombre sin importar mayúsculas/minúsculas
        if curso['nombre'].lower() == busqueda.lower():
            print(f"\n✓ CURSO ENCONTRADO:")
            print(f"  Nombre: {curso['nombre']}")
            print(f"  Nota: {curso['nota']:.2f}")
            estado = "APROBADO" if curso['nota'] >= 61 else "REPROBADO"
            print(f"  Estado: {estado}\n")
            return True

    print(f"\n✗ El curso '{busqueda}' no está registrado.\n")
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
    print("\n" + "=" * 50)
    print("LISTA ACTUALIZADA DE CURSOS")
    print("=" * 50)
    if cursos:
        print(f"\n{'#':<3} {'Curso':<30} {'Nota':<10} {'Estado':<12}\n")
        print("-" * 50)
        for i, c in enumerate(cursos, start=1):
            estado = "APROBADO" if c['nota'] >= 61 else "REPROBADO"
            print(f"{i:<3} {c['nombre']:<30} {c['nota']:<10.2f} {estado}")
        print("-" * 50)
    else:
        print("\n⚠ No hay cursos registrados.")
    print()


# Función que elimina un curso de la lista
def eliminar_curso(cursos, remover):
    if not cursos:
        print("\n⚠ No hay cursos registrados\n")
        return False

    remover = input("Ingrese el nombre del curso a ELIMINAR: ").strip()

    for curso in cursos:
        # Si encuentra el curso, lo elimina de la lista
        if curso['nombre'].lower() == remover.lower():
            cursos.remove(curso)
            print(f"\n✓ Curso '{curso['nombre']}' eliminado correctamente.\n")
            return True
    else:
        print(f"\n✗ El curso '{remover}' no fue encontrado.\n")
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


# ========== FUNCIONES DE ORDENAMIENTO ==========
# Ordenamiento por burbuja: compara cursos vecinos y los intercambia si están desordenados
# Complejidad: O(n²) en el peor caso
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
# Complejidad: O(n²) en el peor caso
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
# Complejidad: O(log n) - mucho más rápida que búsqueda lineal
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
# El historial usa una estructura PILA (LIFO - Last In, First Out)

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
# La cola usa estructura FIFO (First In, First Out - primero en entrar, primero en salir)

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

    # Agrega la solicitud al final de la cola (FIFO)
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
# Cola donde se guardan las solicitudes de revisión (estructura FIFO)
cola_revisiones = deque()
# Pila donde se guarda el historial de cambios (estructura LIFO - último cambio arriba)
historial_cambios = []

repetir = True
while repetir:

    Mostrarmenu()
    opcion = int(input("Seleccione una opción: "))

    # OPCIÓN 1: Agregar nuevos cursos
    if opcion == 1:
        while True:
            curso = pedir_curso()
            cursos.append(curso)
            # Registra el cambio en el historial
            registrar_cambio(historial_cambios, "REGISTRO DE CURSO",
                             f"Curso '{curso['nombre']}' registrado con nota {curso['nota']:.2f}")
            print("✓ Curso guardado exitosamente.\n")

            if not preguntar_continuar():
                break

    # OPCIÓN 2: Ver todos los cursos registrados
    elif opcion == 2:
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
            print("\n" + "=" * 50)
            print("BÚSQUEDA LINEAL DE CURSO")
            print("=" * 50)
            busqueda = input("\nIngrese el nombre del curso a buscar: ").strip()

            if busqueda:
                busquedacursolineal(cursos, busqueda)
            else:
                print("⚠ Ingrese un nombre válido.\n")

            if not preguntar_continuar():
                break

    # OPCIÓN 6: Cambiar la nota de un curso
    elif opcion == 6:
        while True:
            print("\n" + "=" * 50)
            print("ACTUALIZAR NOTA DE UN CURSO")
            print("=" * 50)
            Mostrar_curso()

            if not cursos:
                break
            else:
                nombre_curso = input("Ingrese el nombre del curso: ").strip()

                # Verifica que la nota sea válida (entre 0 y 100)
                print("Ingrese la nueva nota (rango: 0 a 100)")
                while True:
                    try:
                        nueva_nota = float(input("Nota: "))
                        if 0 <= nueva_nota <= 100:
                            break
                        else:
                            print("ERROR: La nota debe estar entre 0 y 100. Intente de nuevo.")
                    except ValueError:
                        print("ERROR: Ingrese un número válido (ejemplo: 85.5)")

                if actualizar_nota_curso(cursos, nombre_curso, nueva_nota):
                    # Registra el cambio en el historial
                    registrar_cambio(historial_cambios, "ACTUALIZACIÓN DE NOTA",
                                     f"Nota del curso '{nombre_curso}' actualizada a {nueva_nota:.2f}")
                    print("\n✓ Nota actualizada correctamente")
                    Mostrar_actualizacion()
                else:
                    print(f"\n✗ El curso '{nombre_curso}' no fue encontrado.\n")

                if not preguntar_continuar():
                    break

    # OPCIÓN 7: Eliminar un curso de la lista
    elif opcion == 7:
        while True:
            print("\n" + "=" * 50)
            print("ELIMINAR UN CURSO")
            print("=" * 50)
            Mostrar_curso()

            if eliminar_curso(cursos, None):
                # Registra el cambio en el historial
                registrar_cambio(historial_cambios, "ELIMINACIÓN DE CURSO",
                                 "Un curso fue eliminado del sistema")
                Mostrar_curso()

            if not preguntar_continuar():
                break

    # OPCIÓN 8: Ordenar los cursos por nota (de mayor a menor) usando burbuja
    elif opcion == 8:
        print("\n" + "=" * 50)
        print("ORDENAR CURSOS POR NOTA (Mayor a Menor)")
        print("=" * 50)
        Mostrar_curso()

        while True:
            if not cursos:
                break

            orden = input("¿Desea ordenar los cursos por nota? (S/N): ").upper().strip()

            if orden in ["SI", "S"]:
                ordenar_nota(cursos)
                # Registra el cambio en el historial
                registrar_cambio(historial_cambios, "ORDENAMIENTO POR NOTA",
                                 "Cursos ordenados por nota (método burbuja)")
                if not preguntar_continuar():
                    break
            elif orden in ["NO", "N"]:
                break
            else:
                print("⚠ Opción inválida. Ingrese S o N")

    # OPCIÓN 9: Ordenar los cursos alfabéticamente usando inserción
    elif opcion == 9:
        while True:
            print("\n" + "=" * 50)
            print("ORDENAR CURSOS POR NOMBRE (Alfabético)")
            print("=" * 50)

            if not cursos:
                print("\n⚠ No hay cursos registrados\n")
                break

            print("\nCursos actuales:")
            Mostrar_curso()

            while True:
                orden_cur = input("¿Desea ordenar los cursos alfabéticamente? (S/N): ").strip().upper()

                if orden_cur in ["SI", "S"]:
                    ordenar_curso(cursos)
                    # Registra el cambio en el historial
                    registrar_cambio(historial_cambios, "ORDENAMIENTO ALFABÉTICO",
                                     "Cursos ordenados alfabéticamente (método inserción)")
                    break
                elif orden_cur in ["NO", "N"]:
                    print("✗ Ordenamiento cancelado\n")
                    break
                else:
                    print("⚠ Opción inválida. Ingrese S o N")

            if not preguntar_continuar():
                break

    # OPCIÓN 10: Buscar un curso dividiendo la lista a la mitad (búsqueda binaria)
    # IMPORTANTE: Solo funciona si los cursos están ordenados alfabéticamente
    elif opcion == 10:
        while True:
            print("\n" + "=" * 50)
            print("BÚSQUEDA BINARIA DE CURSO")
            print("=" * 50)

            if not cursos:
                print("\n⚠ No hay cursos registrados\n")
                break

            # Verifica que los cursos estén ordenados antes de buscar
            if not verificar_orden_alfabetico(cursos):
                print("\n⚠ ADVERTENCIA: Los cursos NO están ordenados alfabéticamente")
                print("   La búsqueda binaria requiere que la lista esté ordenada.")
                print("   Use la opción 9 primero para ordenar los cursos.")
                print("   Búsqueda binaria cancelada.\n")
                break

            busqueda = input("\nIngrese el nombre exacto del curso a buscar: ").strip()

            if busqueda:
                print(f"\nBuscando: '{busqueda}'...")
                print("-" * 50)
                busqueda_binaria(cursos, busqueda)
            else:
                print("⚠ Ingrese un nombre válido.\n")

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
        print("\n" + "=" * 50)
        print("SALIENDO DEL PROGRAMA")
        print("=" * 50)
        print("\n✓ ¡Hasta luego! Gracias por usar el Gestor de Notas.\n")
        repetir = False

    else:
        print("\n✗ Opción no válida. Por favor, ingrese un número del 1 al 13.\n")