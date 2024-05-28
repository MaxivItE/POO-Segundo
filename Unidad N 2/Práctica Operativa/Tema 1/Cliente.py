
class Cliente:
    __nombre: str
    __apellido: str
    __DNI: str
    __numero_tarjeta: str
    __saldo_anterior: float

    def __init__(self, nombre, apellido, DNI, numero_tarjeta, saldo_anterior) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__DNI = DNI
        self.__numero_tarjeta = numero_tarjeta
        self.__saldo_anterior = saldo_anterior

    def __str__(self) -> str:
        return '\n Nombre: {}\n Apellido: {}\n Documento: {}\n Número de Tarjeta: {}\n Saldo Anterior: {}' .format(self.__nombre, self.__apellido, self.__DNI, self.__numero_tarjeta, self.__saldo_anterior)
    