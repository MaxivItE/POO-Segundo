from Pedido import Pedido
import csv
from os import system
class GestorPedidos:
    __lista_pedidos: list = []

    def __init__(self):
        self.inicializarListaPedidos()

    def inicializarListaPedidos(self) -> None:
        with open("datosPedidos.csv", 'r') as archivo_pedidos:
            pedidos = csv.reader(archivo_pedidos, delimiter=',')
            next(pedidos)
            print("\n")
            for datos in pedidos:
                patente_moto: str = datos[0]
                id_pedido: str = datos[1]
                comidas_pedidas: str = datos[2]
                tiempo_entrega: int = datos[3]
                tiempo_real_entrega: int = datos[4]
                precio_pedido: float = datos[5]
                unPedido = Pedido(patente_moto, id_pedido, comidas_pedidas, tiempo_entrega, tiempo_real_entrega, precio_pedido)
                self.__lista_pedidos.append(unPedido)
        archivo_pedidos.close()

    def ordenarPedidos(self) -> None:
        min_index: int = 0
        min_value: int = 0
        aux: list = []
        tamano_lista_pedidos: int = len(self.__lista_pedidos)-1
        for i in range(0, tamano_lista_pedidos):
            min_index = i
            min_value = self.__lista_pedidos[min_index]
            for j in range(i, tamano_lista_pedidos):
                if min_value < self.__lista_pedidos[j+1]:
                    min_value = self.__lista_pedidos[j+1]
                    min_index = j+1
            if min_index != 1:
                aux = self.__lista_pedidos[i]
                self.__lista_pedidos[i] = self.__lista_pedidos[min_index]
                self.__lista_pedidos[min_index] = aux

    def agregarPedido(self, unPedido) -> None:
        archivo_pedido = open("datosPedidos.csv", 'a')
        patente_moto_archivo: str = unPedido.getPatenteMoto()
        id_pedido_archivo: str = unPedido.getIdPedido()
        comidas_pedidas_archivo: str = unPedido.getComidasPedidas()
        tiempo_entrega_archivo: int = unPedido.getTiempoEntrega()
        tiempo_real_entrega_archivo: int = unPedido.getTiempoRealEntrega()
        precio_pedido_archivo: float = unPedido.getPrecioPedido()
        archivo_pedido.write("\n" + patente_moto_archivo + ',' + id_pedido_archivo + ',' + comidas_pedidas_archivo + ',' + tiempo_entrega_archivo + ',' + tiempo_real_entrega_archivo + ',' + precio_pedido_archivo)
        self.__lista_pedidos.append(unPedido)
        archivo_pedido.close()

    def mostrarIdPedidos(self, lista_idPedidos) -> None:
        tamano_idPedidos_lista = len(lista_idPedidos)
        for i in range(tamano_idPedidos_lista):
            print(f" Identificador de Pedido de la patente ingresada: {lista_idPedidos[i]}")

    def buscarIdPedidos(self, patente_moto_ingresada, pedido, lista_idPedidos) -> None:
        patente_moto_lista = self.__lista_pedidos[pedido].getPatenteMoto()
        if patente_moto_ingresada == patente_moto_lista:
            id_pedido_lista: str = self.__lista_pedidos[pedido].getIdPedido()
            lista_idPedidos.append(id_pedido_lista)
    
    def verificarPedidoIngresado(self, lista_idPedidos, id_pedido_ingresado, patente_moto_ingresada) -> str:
        tamanolista_idPedidos = len(lista_idPedidos)
        i: int = 0
        id_pedidoLista_encontrado: bool = False
        while i < tamanolista_idPedidos and id_pedidoLista_encontrado != True:
            if id_pedido_ingresado == lista_idPedidos[i]:
                id_pedidoLista_encontrado = True
                id_pedido_ingresado = lista_idPedidos[i]
                return id_pedido_ingresado
            i+=1
        if i == tamanolista_idPedidos:
            system("cls")
            print(f" Error al ingresar el identificador del pedido de la patente {patente_moto_ingresada}. Ingrese una opción especificada de la patente .")
            self.mostrarIdPedidos(lista_idPedidos)
            id_pedido_ingresado: int = input("Ingrese Identificador de Pedido: ")
            return self.verificarPedidoIngresado(lista_idPedidos, id_pedido_ingresado, patente_moto_ingresada)

    def modificarTiempoRealEntrega(self, patente_moto_ingresada, id_pedido_ingresado, tiempo_real_ingresado, tamano_lista_pedidos) -> None:
        system("cls")
        i: int = 0
        tiempoReal_entrega_encontrado: bool = False
        while (i < tamano_lista_pedidos) and (tiempoReal_entrega_encontrado != True):
            patente_lista = self.__lista_pedidos[i].getPatenteMoto()
            idPedido_lista = self.__lista_pedidos[i].getIdPedido()
            if patente_moto_ingresada == patente_lista and id_pedido_ingresado == idPedido_lista:
                tiempoRealEntrega_anterior = self.__lista_pedidos[i].getTiempoRealEntrega()
                self.__lista_pedidos[i].setTiempoRealEntrega(tiempo_real_ingresado)
                tiempoRealEntrega_nuevo = self.__lista_pedidos[i].getTiempoRealEntrega()
                tiempoReal_entrega_encontrado = True
            i+=1
        print(f" Tiempo Real de Entrega del pedido anterior: {tiempoRealEntrega_anterior} minutos")
        print(f" Tiempo Real de Entrega del pedido nuevo: {tiempoRealEntrega_nuevo} minutos\n")

    def buscarPedidosPatente(self, patente_moto_ingresada, id_pedido_ingresado, tiempo_real_ingresado) -> None:
        tamano_lista_pedidos: int = len(self.__lista_pedidos)
        lista_idPedidos: list = []
        print(f" ***Pedidos de la moto {patente_moto_ingresada}***")
        for i in range(tamano_lista_pedidos):
            self.buscarIdPedidos(patente_moto_ingresada, i, lista_idPedidos)
        id_pedido_ingresado = self.verificarPedidoIngresado(lista_idPedidos, id_pedido_ingresado, patente_moto_ingresada)
        self.modificarTiempoRealEntrega(patente_moto_ingresada, id_pedido_ingresado, tiempo_real_ingresado, tamano_lista_pedidos)

    def mostrarTiempoRealEntregas(self, i) -> None:
        print(f" Tiempo Real de Entrega del Pedido {i+1}: {self.__lista_pedidos[i].getTiempoRealEntrega()} minutos")

    def buscarTiempoRealEntrega(self, patente_moto_ingresada) -> None:
        system("cls")
        tamano_lista_pedidos: int = len(self.__lista_pedidos)
        for i in range(tamano_lista_pedidos):
            patente_moto_lista: str = self.__lista_pedidos[i].getPatenteMoto()
            if patente_moto_ingresada == patente_moto_lista:
                self.mostrarTiempoRealEntregas(i)

    def listarPedidosMotos(self, patente_moto_lista, lista_id_pedidos, lista_id_tiempo_estimado, lista_tiempo_real, lista_precio):
        tamano_lista_pedidos: int = len(self.__lista_pedidos)
        i: int = 0
        while i < tamano_lista_pedidos:
            patente_lista_pedidos = self.__lista_pedidos[i].getPatenteMoto()
            if patente_moto_lista == patente_lista_pedidos:
                id_pedido_lista: str = self.__lista_pedidos[i].getIdPedido()
                lista_id_pedidos.append(id_pedido_lista)
                tiempo_estimado_lista: int = self.__lista_pedidos[i].getTiempoEntrega()
                lista_id_tiempo_estimado.append(tiempo_estimado_lista)
                tiempo_real_estimado_lista: int = self.__lista_pedidos[i].getTiempoRealEntrega()
                lista_tiempo_real.append(tiempo_real_estimado_lista)
                precio_pedido_lista: float = self.__lista_pedidos[i].getPrecioPedido()
                lista_precio.append(precio_pedido_lista)
            i+=1

    def mostrarListaPedidos(self) -> None:
        tamano_lista_pedidos: int = len(self.__lista_pedidos)
        for i in range(tamano_lista_pedidos):
            print(self.__lista_pedidos[i])