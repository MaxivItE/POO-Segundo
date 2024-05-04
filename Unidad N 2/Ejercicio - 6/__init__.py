'''Ejercicio 6 
La empresa “PagoTusCuentas”, lo contrata como desarrollador, con el objetivo de desarrollar una 
aplicación para su billetera virtual. 
Los clientes solicitan crear Cuenta, para lo que la aplicación les solicita: Apellido, nombre, DNI, 
teléfono, saldo, CVU, porcentaje anual por rendimiento (es el mismo para todas las cuentas). 
Las Transacciones tienen: CVU, numero de transacción, importe, tipo de transacción ('D'-Débito, 
'C'-Crédito) 
Para desarrollar la aplicación usted debe tener en cuenta los requerimientos que proporcionan desde 
el área de desarrollo de la empresa. 
Requerimientos: 
1. Crear una clase Cuenta, con los atributos identificados y los métodos necesarios para 
resolver la problemática planteada. 
2. Crear una clase Transacción, con los atributos identificados y los métodos necesarios para 
resolver la problemática planteada. 
3. Crear una clase GestorCuentas, basado en un arreglo Numpy, que permita almacenar los 
datos de las cuentas, leyendo los datos de las mismas desde un archivo .csv. Esta clase será 
un gestor de las cuentas de los clientes de la empresa. El archivo se denomina 
“cuentasBilletera.csv”. 
4. Crear una clase GestorTransacciones, basado en una lista Python, que permita almacenar los 
datos de las Transacciones, leyendo los datos de las mismas desde un archivo .csv. Esta 
clase será un gestor de transacciones que han sido recibidas a través de la app telefónica. El 
archivo se denomina “transaccionesBilletera.csv”. 
5. Crear un menú de opciones que permita: 
a. Leer por teclado el DNI de un cliente e informar los datos del cliente: apellido, nombre, 
CVU y saldo (actualizado por las transacciones). 
b. Leer por teclado el nuevo porcentaje anual del rendimiento, modificarlo para la clase 
Cuenta (variable de Clase). 
c. Actualizar el saldo, incrementándolo para todos los clientes, en función del porcentaje 
anual de rendimiento, teniendo en cuenta que el rendimiento, se actualiza en el 
porcentaje diario (ver Reglas de Negocio). 
d. Leer por teclado un número de CVU, informar el saldo inicial, procesar todas las 
transacciones, y obtener el nuevo saldo actualizado, que modifica el saldo para la cuenta 
que es identificada por el CVU. 
e. Almacenar los datos actualizados de las Cuentas en un archivo .csv. 
Reglas de negocio: 
El porcentaje de anual de rendimiento, se aplica diariamente, por lo que debe dividirse en 365, que 
es la cantidad de día que tiene el año, inicialmente se fija en un 68% anual, por lo que el porcentaje
diario es del 0.18%. 
Proveer donde crea conveniente, los destructores que permitan liberar memoria.'''