
class Transaccion:
    __CVU_transaccion: str
    __numero_transaccion: str
    __importe_transaccion: float
    __tipo_transaccion: str

    def __init__(self, CVU_transaccion, numero_transaccion, importe_transaccion, tipo_transaccion) -> None:
        self.__CVU_transaccion = CVU_transaccion
        self.__numero_transaccion = numero_transaccion
        self.__importe_transaccion = importe_transaccion
        self.__tipo_transaccion = tipo_transaccion
    
    def getCVUTransaccion(self) -> str:
        return self.__CVU_transaccion
    
    def getImporteTransaccion(self) -> float:
        return self.__importe_transaccion

    def __str__(self) -> str:
        return ' \n CVU: {}\n Número de Transacciones: {}\n Importe: {}\n Tipo de Transaccion (D: Débito - C: Crédito): {}' .format(self.__CVU_transaccion, self.__numero_transaccion, self.__importe_transaccion, self.__tipo_transaccion)
    