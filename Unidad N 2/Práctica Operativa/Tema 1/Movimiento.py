
class Movimiento:
    __numero_tarjeta: str
    __fecha: str
    __descripccion: str
    __tipo_movimiento: str
    __importe: float

    def __init__(self, numero_tarjeta, fecha, descripcion, tipo_movimiento, importe) -> None:
        self.__numero_tarjeta = numero_tarjeta
        self.__fecha = fecha
        self.__descripccion = descripcion
        self.__tipo_movimiento = tipo_movimiento
        self.__importe = importe
    
    def __str__(self) -> str:
        return '\n Número de Tarjeta:{}\n Fecha: {}\n Descripción: {}\n Tipo de Movimiento: {}\n Importe: {}' .format(self.__numero_tarjeta, self.__fecha, self.__descripccion, self.__tipo_movimiento, self.__importe)