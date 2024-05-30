
"""Programación Orientada a Objetos Año 2024
Tema 1 - Recuperatorio Práctico Unidad 2
Resuelva la siguiente situación problemática, utilizando el lenguaje de programación Python.
El sanatorio “El cerezo” lo contrata para desarrollar un sistema que permita administrar la
información de los nacimientos que se atendieron los últimos 30 días.
Para ello cuenta con los datos de:
Cada Mamá: DNI, edad, apellido y nombre.
Cada Nacimiento: DNI de la mamá, tipo de parto ('N'- normal o ‘C’ - cesárea), Fecha y hora del
nacimiento, peso (en kg) y altura del bebé (en cm).
Los datos de las mamás están en el archivo “Mamas.csv”. Los datos de los bebés están registrados
en el archivo “Nacimientos.csv”. Ambos archivos tienen como separador el carácter “;”.
El equipo de desarrollo ha acordado que cada clase debe estar en un módulo, y usted debe
implementar en Python:
1. Las clases Mamá y Bebe, con los atributos y métodos necesarios.
2. Una clase GestorMamas que almacene instancias de la clase Mama. Cada una de estas
instancias se creará con los datos registrados en el archivo “Mamas.csv”. Este gestor debe
basarse en un arreglo Numpy.
3. Una clase Gestor Nacimientos que almacene instancias de la clase Nacimiento. Cada una de
estas instancias se crearán con los datos registrados en el archivo “Nacimientos.csv”. Este
gestor debe basarse en una lista Python.
4. La carga de cada gestor con los datos respectivos.
5. Utilizando exclusivamente los Gestores cargados con los datos de los archivos, implemente
un menú de opciones que permita:
a. Ingresar por teclado el DNI de una mamá, mostrar la siguiente información:
Apellido y Nombre: xxxxxxxx, xxxxxxxx
Edad: xx
Tipo de parto: xxxxxxxx
Bebé/s
Peso Altura
xxxx xx
xxxx xx
b. Mostrar los datos de la/s mamá/s que han tenido parto múltiple (mellizos, gemelos, trillizos,
etc). Es decir, para una misma mamá en una misma fecha se registró más de un nacimiento.
Reglas:
 Para esta funcionalidad debe definir la sobrecarga del operador __eq__ en la clase
Nacimiento considerando el DNI de la madre y la fecha del nacimiento.
 Resolver la funcionalidad usando la sobrecarga definida.
Reglas de negocio generales:
 Todas las funcionalidades deben resolverse con los Gestores definidos. Tiene prohibido sacar
sublistas o subarreglos para procesar por fuera de los métodos definidos en los Gestores.
 El manejo del dato fecha y el dato hora debe hacerse como un string. 
"""