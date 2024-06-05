from zope.interface import Interface

class InterfaceIngresar(Interface):
    def insertarElemento(valor, posicion_valor):
        pass

class InterfaceMostrar(Interface):
    def mostrarElemento(posicion_valor):
        pass