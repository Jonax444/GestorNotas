# GestorNotas
Gestor de Notas Académicas — aplicación consola en Python para registrar y analizar calificaciones.


## Redacción del problema
Es un sistema diseñado para ayudar a registrar, consultar, modificar y analizar calificaciones de una manera sencilla. A través de un menú interactivo por medio de consola, el usuario puede gsetionar la informacion
de todos los cursos.

## Requisitos del sistema

### Funcionales
1. Registrar un nuevo curso y su nota (validando que la nota esté entre 0 y 100).  
2. Mostrar todos los cursos y sus notas.  
3. Calcular y mostrar el promedio general de las notas registradas.  
4. Contar cuántos cursos han sido aprobados y cuántos reprobados.


### No funcionales
- El sistema se ejecuta exclusivamente en la consola, utilizando **Python** sin librerías externas.  
- El código debe emplear **bucles** y **condicionales** expresados en pseudocódigo en la etapa de diseño.  
- Debe usar **listas**, **pilas**, **colas** y algoritmos básicos de **búsqueda** y **ordenamiento**.  
- La interacción con el usuario debe ser clara y con mensajes legibles.  



INICIO
    MIENTRAS VERDADERO HACER
        IMPRIMIR "====== GESTOR DE NOTAS ACADÉMICAS ======"
        IMPRIMIR "1. Registrar nuevo curso"
        IMPRIMIR "2. Mostrar todos los cursos y notas"
        IMPRIMIR "3. Calcular promedio general"
        IMPRIMIR "4. Contar cursos aprobados y reprobados"
        IMPRIMIR "5. Salir"
        IMPRIMIR "Seleccione una opción: "
        LEER opcion

        SI opcion = 1 ENTONCES
            <registrar nuevo curso>
        SINO SI opcion = 2 ENTONCES
            <mostrar todos los cursos y notas>
        SINO SI opcion = 3 ENTONCES
            <calcular promedio general>
        SINO SI opcion = 4 ENTONCES
            <contar cursos aprobados y reprobados>
        SINO SI opcion = 5 ENTONCES
            IMPRIMIR "Gracias por usar el sistema. ¡Hasta pronto!"
            SALIR DEL BUCLE
        SINO
            IMPRIMIR "Opción no válida. Intente de nuevo."
        FIN_SI
    FIN_MIENTRAS
FIN
