class Moto:
    __patente: str
    __marca: str
    __nombre_conductor: str
    __apellido_conductor: str
    __kilometraje: float

    def __init__(self, patente, marca, nombre_conductor, apellido_conductor, kilometraje):
        self.__patente = patente
        self.__marca = marca
        self.__nombre_conductor = nombre_conductor
        self.__apellido_conductor = apellido_conductor
        self.__kilometraje = kilometraje
    
    def getPatente(self):
        return self.__patente
    
    
    def __str__(self):
        return ' Patente: {}\n Marca: {}\n Nombre del conductor: {}\n Apellido: {}\n Kilometraje de la moto: {}\n' .format(self.__patente, self.__marca, self.__nombre_conductor, self.__apellido_conductor, self.__kilometraje)
    