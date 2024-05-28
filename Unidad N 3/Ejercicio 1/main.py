from GestorEdificios import GestorEdificios
from Edificio import Edificio
from os import system

def ingresarOpcion() -> str:
    print("\n 1. Mostrar propietarios de departamentos de un Edificio")
    print(" 2. Mostrar Superficie total cubierta de un edificio")
    print(" 3. Mostrar Total y Porcentaje de la Superficie de Propietario")
    print(" 0. Salir")
    return str(input("Respuesta: "))

def ingresarNombreDeEdificio() -> str:
    return str(input("Nombre de Edificio: "))

def ingresarNombreDePropietario() -> str:
    return str(input("Nombre del Propietario: "))

def menu() -> None:
    opcion = str(ingresarOpcion())
    while opcion != '0':
        system("cls")
        match opcion:
            case '1': 
                nombre_edificio_ingresado = str(ingresarNombreDeEdificio())
                gestor_edificios.realizarOpcionUno(nombre_edificio_ingresado)
            case '2': 
                nombre_edificio_ingresado = str(ingresarNombreDeEdificio()) 
                gestor_edificios.realizarOpcionDos(nombre_edificio_ingresado)
            case '3':
                nombre_propietario = str(ingresarNombreDePropietario())
                gestor_edificios.realizarOpcionTres(nombre_propietario)
            case _: print("\t Error al ingresar la respuesta. Por favor, ingrese una opción especificada\n")
        opcion = (ingresarOpcion())
    system("cls")
    print(" Fin del programa.")

if __name__ == '__main__':
    system("cls")
    gestor_edificios = GestorEdificios()
    menu()