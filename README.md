# Gestor de Notas Académicas

## Redacción del problema

Gestor de Notas Académicas que está diseñado para ayudar a los estudiantes a organizar y manejar sus calificaciones de forma sencilla desde la consola.

La idea principal es que el estudiante pueda registrar todos sus cursos con las notas correspondientes, y también tener la opción de verlas, modificarlas o eliminarlas fácilmente. Además, el sistema permite hacer análisis básicos como calcular el promedio general y saber cuántos cursos ha aprobado o reprobado.

Este programa es útil porque, al estar basado en consola y organizado con un menú interactivo, permite que el estudiante controle su información académica sin complicaciones, usando estructuras de datos y algoritmos simples para facilitar búsquedas, ordenamientos y manejo de la información.


## Requisitos del sistema

### Requisitos funcionales

- Registrar un nuevo curso con su respectiva nota.
- Mostrar todos los cursos y sus notas registradas.
- Calcular el promedio general de las notas ingresadas.
- Contar cuántos cursos han sido aprobados y reprobados.
- Buscar un curso por nombre usando búsqueda lineal.
- Actualizar la nota de un curso existente.
- Eliminar un curso del registro.
- Ordenar los cursos por nota (usando ordenamiento burbuja).
- Ordenar los cursos por nombre (usando ordenamiento por inserción).
- Buscar un curso por nombre usando búsqueda binaria.
- Simular una cola de solicitudes de revisión de notas.
- Mostrar un historial de cambios usando una pila.

### Requisitos no funcionales

- El programa debe ejecutarse en consola usando Python.
- No se deben usar librerías externas, solo las funciones estándar.
- Se debe utilizar al menos una estructura repetitiva para mostrar el menú principal.
- El código debe organizarse en funciones para mantener la modularidad.
- Se deben implementar validaciones básicas, por ejemplo, que las notas estén entre 0 y 100.
- Se deben utilizar estructuras de datos como listas, pilas y colas, y aplicar algoritmos de búsqueda y ordenamiento.

---




## Pseudocodigo

INICIO

  INICIO
    
    repetir = VERDADERO

    MIENTRAS repetir HACER
        IMPRIMIR "====== GESTOR DE NOTAS ACADÉMICAS ======"
        IMPRIMIR "1. Registrar nuevo curso"
        IMPRIMIR "2. Mostrar todos los cursos y notas"
        IMPRIMIR "3. Calcular promedio general"
        IMPRIMIR "4. Contar cursos aprobados y reprobados"
        IMPRIMIR "5. Buscar curso por nombre "
        IMPRIMIR "6. Actualizar nota de un curso"
        IMPRIMIR "7. Eliminar un curso"
        IMPRIMIR "8. Ordenar cursos por nota "
        IMPRIMIR "9. Ordenar cursos por nombre)"
        IMPRIMIR "10. Buscar curso por nombre "
        IMPRIMIR "11. Simular cola de solicitudes de revisión"
        IMPRIMIR "12. Mostrar historial de cambios "
        IMPRIMIR "13. Salir"
        
        IMPRIMIR "Seleccione una opción: "
        LEER opcion

        SI opcion = 1 ENTONCES
            <Registrar nuevo curso>
        SINO SI opcion = 2 ENTONCES
            <Mostrar todos los cursos y notas>
        SINO SI opcion = 3 ENTONCES
            <Calcular promedio general>
        SINO SI opcion = 4 ENTONCES
            <Contar cursos aprobados y reprobados>
        SINO SI opcion = 5 ENTONCES
            <Buscar curso por nombre (búsqueda lineal)>
        SINO SI opcion = 6 ENTONCES
            <Actualizar nota de un curso>
        SINO SI opcion = 7 ENTONCES
            <Eliminar un curso>
        SINO SI opcion = 8 ENTONCES
            <Ordenar cursos por nota (burbuja)>
        SINO SI opcion = 9 ENTONCES
            <Ordenar cursos por nombre (inserción)>
        SINO SI opcion = 10 ENTONCES
            <Buscar curso por nombre (búsqueda binaria)>
        SINO SI opcion = 11 ENTONCES
            <Simular cola de solicitudes de revisión>
        SINO SI opcion = 12 ENTONCES
            <Mostrar historial de cambios (pila)>
        SINO SI opcion = 13 ENTONCES
            repetir = FALSO
        SINO
            IMPRIMIR "Opción inválida, intente nuevamente."
        FIN_SI
    FIN_MIENTRAS

FIN

FIN
