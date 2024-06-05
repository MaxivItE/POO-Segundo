from os import system
from GestorInterfaces import Ingresar
from ClaseInterfaces import InterfaceIngresar
from GestorInterfaces import Mostrar
from ClaseInterfaces import InterfaceMostrar

def ingresarOpcion() -> str:
    print("\n ---MENU DE EXCEPCIONES---")
    print(" a. Insertar un elemento")
    print(" b. Agregar un elemento al final")
    print(" c. Mostrar un elemento")
    print(" d. Salir")
    return str(input("Respuesta: "))

def menu(lista_numeros) -> None:
    system("cls")
    opcion = ingresarOpcion()
    while opcion != 'd':
        system("cls")
        match opcion:
            case 'a':
                Ingresar(InterfaceIngresar(lista_numeros))
            case 'b':
                system("cls")
                valor = int(input("Valor a ingresar al final de la lista: "))
                system("cls")
                lista_numeros.agregarValorFinal(valor)
            case 'c':
                Mostrar(InterfaceMostrar(lista_numeros))
            case 'mostrar':
                lista_numeros.mostraLista()
            case _:
                print("\n Error al ingresar la opción. Por favor, ingrese una de las opciones especificadas")
        opcion = ingresarOpcion()
    system("cls")
    print("\n\t\t\t\t\t FIN DEL PROGRAMA")