
class Mama:
    __DNI:str
    __edad: int
    __apellido: str
    __nombre: str

    def __init__(self, DNI, edad, apellido, nombre) -> None:
        self.__DNI = DNI
        self.__edad = edad
        self.__apellido = apellido
        self.__nombre = nombre

    def getDNIMama(self) -> str:
        return self.__DNI

    def getEdadMama(self) -> int:
        return self.__edad
    
    def getApellidoMama(self) -> str:
        return self.__apellido

    def getNombreMama(self) -> str:
        return self.__nombre

    def __str__(self) -> str:
        return '\n Documento: {}\n Edad: {}\n Apellido: {}\n Nombre: {}' .format(self.__DNI, self.__edad, self.__apellido, self.__nombre)
