
class Pedido:
    __patente_moto: str
    __id_pedido: str
    __comidas_pedidas: str
    __tiempo_entrega: int
    __tiempo_real_entrega: int = 0
    __precio_pedido: float

    def __init__(self, patente_moto, id_pedido, comidas_pedidas, tiempo_entrega, tiempo_real_entrega = 0, precio_pedido = float):
        self.__patente_moto = patente_moto
        self.__id_pedido = id_pedido
        self.__comidas_pedidas = comidas_pedidas
        self.__tiempo_entrega = tiempo_entrega
        self.__tiempo_real_entrega = tiempo_real_entrega
        self.__precio_pedido = precio_pedido
    
    def getPatenteMoto(self) -> str:
        return self.__patente_moto
    def getIdPedido(self) -> str:
        return self.__id_pedido
    def getComidasPedidas(self) -> str:
        return self.__comidas_pedidas
    def getTiempoEntrega(self) -> int:
        return self.__tiempo_entrega
    def getTiempoRealEntrega(self) -> int:
        return self.__tiempo_real_entrega
    def setTiempoRealEntrega(self, nuevo_tiempoReal_entrega):
        self.__tiempo_real_entrega = nuevo_tiempoReal_entrega
    def getPrecioPedido(self) -> float:
        return self.__precio_pedido
    
    def __lt__(self, otroPedido):
        if self.__patente_moto < otroPedido.__patente_moto:
            return False
        else:
            return True

    def __str__(self):
        return ' Patente de la moto del pedido: {}\n Identificador del Pedido: {}\n Comidas Pedidas: {}\n Tiempo estimado de entrega: {}\n Tiempo real de entrega: {}\n Precio: ${}\n' .format(
                self.__patente_moto, self.__id_pedido, self.__comidas_pedidas, self.__tiempo_entrega, self.__tiempo_real_entrega, self.__precio_pedido)