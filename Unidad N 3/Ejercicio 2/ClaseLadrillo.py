
class Ladrillo:
    __alto:int = 7
    __largo:int = 25
    __ancho:int = 15
    __cantidad: int
    __identificador: int
    __kg_materia_prima: float
    __costo: float

    def __init__(self, cantidad, identificador, kg_materia_prima, costo) -> None:
        self.__cantidad = cantidad
        self.__identificador = identificador
        self.__kg_materia_prima = kg_materia_prima
        self.__costo = costo
    
    def getCantidadLadrillo(self) -> int:
        return self.__cantidad

    def getIDLadrillo(self) -> int:
        return self.__identificador
    
    def getCosto(self) -> float:
        return self.__costo

    def setCosto(self, costo_adicional) -> None:
        self.__costo += costo_adicional

    def __str__(self) -> str:
        return ' Alto: {} cm\n Largo: {} cm\n Ancho: {} cm\n Cantidad: {} unidades\n Identificador: {}\n Materia Prima: {} Kg\n Costo: ${}' .format(self.__alto, self.__largo, self.__ancho, self.__cantidad, self.__identificador, self.__kg_materia_prima, self.__costo)