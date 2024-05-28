'''
Ejercicio Nº4: 
Herencia y métodos con ligadura dinámica 
Descripción del Sistema 
Una compañía editorial produce publicaciones para la venta, estas pueden ser, libros impresos 
y audio-libros en discos compactos. 
De todas las publicaciones se conoce: su título, categoría (comedia, drama, autoayuda etc.), 
y su precio base.
De un libro impreso se conoce, además: nombre del autor, fecha de edición, y cantidad de 
páginas. 
De un CD se conoce, además: el tiempo de reproducción en minutos, y el nombre del narrador. 
El importe de venta de cada publicación se calcula en función del precio base y de sus 
características. Para ello se deben considerar las siguientes reglas de negocio: 
Importe de venta de un libro impreso es el precio base, menos el 1% por cada año de 
antigüedad (año actual - año de edición), este porcentaje se calcula sobre el precio base. 
Importe de venta de un audio-libro es el precio base, más 10% por gastos de regalía, 
porcentaje se calculan sobre el precio base. 
El analista de la editorial le solicita a usted que desarrolle una aplicación con las siguientes 
restricciones: 
a- Definir la jerarquía de clases con los métodos correspondientes a cada clase de la 
narrativa dada. 
b- Almacenar en una colección tipo Lista definida por el programador, las publicaciones 
de la editorial. 
c- Implementar un programa principal con un menú de opciones que permita testear las 
siguientes acciones: 
1. Agregar publicaciones a la colección 
2. Dada una posición de la lista: Mostrar por pantalla qué tipo de publicación se 
encuentra almacenada en dicha posición (usar la función isinstance()). 
3. Mostrar la cantidad de publicaciones de cada tipo. 
4. Recorrer la colección y mostrar para todas las publicaciones Titulo, categoría e 
importe de venta. 
'''