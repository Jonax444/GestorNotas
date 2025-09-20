# Mi Gestor de Notas Académicas - Explicación Personal 

## Explicación Personal

Hola, quiero explicarles mi programa de gestión de notas académicas que
he estado desarrollando. He implementado las funcionalidades desde la
opción 1 hasta la 10, mientras que las opciones 11 y 12 aún no las he
completado.

### Opción 1: Registrar nuevo curso y nota

He creado esta función para poder agregar cursos a mi sistema.
Básicamente, creo un diccionario que contiene el nombre del curso y la
nota correspondiente, luego lo añado a mi lista principal. Incluí una
función que me pregunta si quiero continuar agregando más cursos para
hacer el proceso más eficiente.

### Opción 2: Mostrar todos los cursos y notas

Esta es bastante directa - simplemente recorro mi lista de cursos y los
muestro enumerados con sus respectivas notas. Si no tengo cursos
registrados, el programa me informa que la lista está vacía.

### Opción 3: Calcular promedio general

Aquí extraigo todas las notas de los cursos que tengo registrados, las
sumo y las divido entre el total de cursos. Muestro el resultado con dos
decimales para mayor precisión en el cálculo.

### Opción 4: Contar cursos aprobados y reprobados

Implementé contadores que revisan cada curso individualmente. Si la nota
es 61 o mayor, lo cuento como aprobado; si es menor, como reprobado.
Luego muestro ambas cantidades.

### Opción 5: Buscar curso por nombre (Lineal)

Desarrollé una búsqueda secuencial que va curso por curso hasta
encontrar una coincidencia exacta, sin importar si está en mayúsculas o
minúsculas. Si encuentra el curso, muestra su información; si no, me
dice que no está en la lista.

### Opción 6: Actualizar nota de un curso

Esta función me permite modificar la nota de cualquier curso existente.
Primero muestro todos los cursos disponibles, luego solicito el nombre
del curso a actualizar y la nueva nota. Incluí validación para
asegurarme de que la nota esté entre 0 y 100.

### Opción 7: Eliminar un curso

Con esta opción puedo remover cursos de mi lista. Solicito el nombre del
curso a eliminar, busco coincidencias y si lo encuentro, lo elimino
usando la función remove() de Python.

### Opción 8: Ordenar cursos por nota

Implementé un sistema de ordenamiento que usa la función sort() con
lambda para ordenar los cursos por nota de mayor a menor. Después del
ordenamiento, muestro la lista actualizada para que pueda ver los
cambios.

### Opción 9: Ordenar cursos por nombre

Similar a la opción anterior, pero esta vez ordeno alfabéticamente por
nombre. Uso lower() para ignorar las diferencias entre mayúsculas y
minúsculas, manteniendo un orden consistente de A a Z.

### Opción 10: Buscar curso por nombre (Binaria)

Esta ha sido la más compleja de implementar. Primero verifico que mi
lista esté ordenada alfabéticamente, ya que es un requisito para la
búsqueda binaria. Si no está ordenada, aviso que deben usar primero la
opción 9. La búsqueda divide la lista por la mitad repetidamente y
muestra cada paso del proceso, incluyendo cuántas comparaciones se
realizaron.

### Funcionalidades adicionales que implementé:

-   **preguntar_continuar()**: Me permite quedarme en una opción y
    realizar múltiples operaciones sin volver al menú principal.\
-   **verificar_orden_alfabetico()**: Verifica que los cursos estén
    ordenados para poder usar búsqueda binaria.\
-   Validaciones de entrada y manejo básico de errores.

### Estado actual del proyecto:

-   Opciones 1-10: Completamente implementadas y funcionando.\
-   Opción 11 (Cola de solicitudes): Aún no la he implementado.\
-   Opción 12 (Historial de cambios): Aún no la he implementado.\
-   Opción 13 (Salir): Implementada - termina el programa.

El programa funciona con un bucle principal que se mantiene activo hasta
que selecciono la opción 13 para salir. Cada opción tiene su propia
lógica y validaciones para asegurar una buena experiencia de usuario.

------------------------------------------------------------------------

