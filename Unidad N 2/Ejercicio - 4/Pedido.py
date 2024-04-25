
class Pedido:
    __patente_moto: str
    __id_pedido: str
    __comidas_pedidas: str
    __tiempo_entrega: float
    __tiempo_real_entrega: float = 0
    __precio_pedido: float

    def __init__(self, patente_moto, id_pedido, comidas_pedidas, tiempo_entrega, tiempo_real_entrega, precio_pedido):
        self.__patente_moto = patente_moto
        self.__id_pedido = id_pedido
        self.__comidas_pedidas = comidas_pedidas
        self.__tiempo_entrega = tiempo_entrega
        self.__tiempo_real_entrega = tiempo_real_entrega
        self.__precio_pedido = precio_pedido

    def __str__(self):
        return ' Patente de la moto del pedido: {}\n Identificador del Pedido: {}\n Comidas Pedidas: {}\n Tiempo estimado de entrega: {}\n Tiempo real de entrega: {}\n Precio: ${}\n' .format(self.__patente_moto, self.__id_pedido, self.__comidas_pedidas, self.__tiempo_entrega, self.__tiempo_real_entrega, self.__precio_pedido)