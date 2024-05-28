
class Ladrillo:
    __alto:int = 7
    __largo:int = 25
    __ancho:int = 15
    __cantidad: int
    __identificador: int
    __kg_materia_prima: float
    __costo: float
    __lista_materiales: list

    def __init__(self, cantidad, identificador, kg_materia_prima, costo) -> None:
        self.__cantidad = cantidad
        self.__identificador = identificador
        self.__kg_materia_prima = kg_materia_prima
        self.__costo = costo

    def setMaterialRefractario(self, unMaterialRefractario):
        self.__lista_materiales.append(unMaterialRefractario)

    def __str__(self) -> str:
        return '\n Alto: {}\n Largo: {}\n Ancho: {}\n Cantidad: {}\n Identificador: {}\n KG de materia Prima Utilizado: {}\n Costo: {}' .format(self.__alto, self.__largo, self.__ancho, self.__cantidad, self.__identificador, self.__kg_materia_prima, self.__costo)