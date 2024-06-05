from zope.interface import Interface
from zope.interface import implementer
from ClaseInterfaces import InterfaceIngresar
from ClaseInterfaces import InterfaceMostrar
@implementer(InterfaceIngresar)
@implementer(InterfaceMostrar)

class ListaNumeros:
    __lista_valores:list

    def __init__(self) -> None:
        self.__lista_valores = []
        self.cargarLista()

    def cargarLista(self) -> None:
        cantidad_valores:int = 6
        for i in range(cantidad_valores):
            self.__lista_valores.append(0)

    @implementer(Interface)
    def insertarElemento(self, valor, posicion_valor) -> None:
        cantidad_valores = int(len(self.__lista_valores))
        if posicion_valor > cantidad_valores:
            raise IndexError
        else:
            self.__lista_valores[posicion_valor] = valor

    def agregarValorFinal(self, valor) -> None:
        self.__lista_valores[-1] = valor
        print(f"\n Valor ({valor}) agregado al final de la lista.")

    @implementer(Interface)
    def mostrarElemento(self, posicion_valor) -> None:
        canttidad_valores = int(len(self.__lista_valores))
        if posicion_valor > canttidad_valores:
            raise IndexError
        else:
            print(f"\n El valor en la posicion ({posicion_valor + 1}) es: ({self.__lista_valores[posicion_valor]})")

    def mostraLista(self) -> None:
        print("\n---MOSTRAR VALORES DE LA LISTA---\n")
        for i in range(len(self.__lista_valores)):
            print(f" {i+1}: ({self.__lista_valores[i]})")