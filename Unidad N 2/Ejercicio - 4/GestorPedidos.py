from Pedido import Pedido
import csv

class GestorPedidos:
    __lista_pedidos: list = []

    def __init__(self):
        self.inicializarListaPedidos()

    def agregarPedido(self, unPedido):
        self.__lista_pedidos.append(unPedido)
    
    
    def inicializarListaPedidos(self):
        with open("datosPedidos.csv", 'r') as archivo_pedidos:
            pedidos = csv.reader(archivo_pedidos, delimiter=',')
            next(pedidos)
            print("\n")
            for datos in pedidos:
                patente_moto: str = datos[0]
                id_pedido: str = datos[1]
                comidas_pedidas: str = datos[2]
                tiempo_entrega: float = datos[3]
                tiempo_real_entrega: float = datos[4]
                precio_pedido: float = datos[5]
                unPedido = Pedido(patente_moto, id_pedido, comidas_pedidas, tiempo_entrega, tiempo_real_entrega, precio_pedido)
                self.agregarPedido(unPedido)
        archivo_pedidos.close()

    def mostrarListaPedidos(self):
        tamano_lista_pedidos = len(self.__lista_pedidos)
        for i in range(tamano_lista_pedidos):
            print(self.__lista_pedidos[i])