
class MaterialRefractario:
    __material: str
    __caracteristicas: str
    __cantidad: float
    __costo_adicional: float

    def __init__(self, material, caracteristicas, cantidad, costo_adicional) -> None:
        self.__material = material
        self.__caracteristicas = caracteristicas
        self.__cantidad = cantidad
        self.__costo_adicional = costo_adicional

    def getMaterial(self) -> str:
        return self.__material

    def getCaracteristicas(self) -> str:
        return self.__caracteristicas

    def getCostoAdicional(self) -> float:
        return self.__costo_adicional

    def __str__(self) -> str:
        return '\n Material: {}\n Características: {}\n Cantidad Material Utilizado: {} Kg\n Costo Adicional: ${}' .format(self.__material, self.__caracteristicas, self.__cantidad, self.__costo_adicional)