from ClaseInterfaces import InterfaceIngresar
from ClaseInterfaces import InterfaceMostrar
from os import system

def Ingresar(manejador_ingresar: InterfaceIngresar):
    try:
        valor = int(input("Valor a ingresar a la lista: "))
        posicion_valor = int(input("Posición del valor: "))
    except ValueError:
        system("cls")
        print(" Error al ingresar los datos. Los valores a ingresear deben ser números enteros")
    else:
        try:
            system("cls")
            manejador_ingresar.insertarElemento(valor, posicion_valor-1)
        except IndexError:
            print(" Error al ingresar el valor. La posición ingresada sobrepasa el tamaño de la lista")
        else:
            print((f" El valor ({valor}) se agregó en la posición ({posicion_valor}) de la lista correctamente."))
        finally:
            print("\n Volviendo al Menú Principal.")

def Mostrar(manejador_mostrar: InterfaceMostrar):
    try:
        posicion_valor = int(input("Posición del valor a mostrar: "))
    except ValueError:
        system("cls")
        print(" Error al ingresar los datos. Los valores a ingresear deben ser números enteros")
    else:
        try:
            system("cls")
            manejador_mostrar.mostrarElemento(posicion_valor-1)
        except IndexError:
            print(" Error al mostrar el valor. La posición ingresada sobrepasa el tamaño de la lsita")
        else:
            print((" El valor se mostró correctamente."))
        finally:
            print("\n Volviendo al Menú Principal.")