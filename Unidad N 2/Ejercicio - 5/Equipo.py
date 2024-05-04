
class Equipo: 
    __id_equipo: str
    __nombre_del_equipo: str
    __goles_a_favor: int
    __goles_en_contra: int
    __diferencia_de_goles: int
    __puntos: int

    def __init__(self, id_equipo, nombre_del_equipo, goles_a_favor:int = 0, goles_en_contra:int = 0, diferencia_de_goles:int = 0, puntos:int = 0) -> None:
        self.__id_equipo = id_equipo
        self.__nombre_del_equipo = nombre_del_equipo
        self.__goles_a_favor = goles_a_favor
        self.__goles_en_contra = goles_en_contra
        self.__diferencia_de_goles = diferencia_de_goles
        self.__puntos = puntos
    
    def getIdDeEquipo(self) -> str:
        return self.__id_equipo

    def getNombreEquipo(self) -> str:
        return self.__nombre_del_equipo

    def getGolesAFavor(self) -> int:
        return self.__goles_a_favor
    def setGolesAFavor(self, goles_a_favor) -> None:
        self.__goles_a_favor += goles_a_favor

    def getGolesEnContra(self) -> int:
        return self.__goles_en_contra
    def setGolesEnContra(self, goles_en_contra) -> None:
        self.__goles_en_contra += goles_en_contra

    def getDiferenciaDeGoles(self)  -> int:
        return self.__diferencia_de_goles
    def setDiferenciaDeGoles(self, diferencia_de_goles) -> None:
        self.__diferencia_de_goles += diferencia_de_goles

    def getPuntos(self) -> int:
        return self.__puntos
    def setPuntos(self, puntos) -> None:
        self.__puntos += puntos
    
    def __gt__(self, otroEquipo) -> bool:
        if self.__puntos != otroEquipo.__puntos:
            return self.__puntos > otroEquipo.__puntos
        elif self.__diferencia_de_goles != otroEquipo.__diferencia_de_goles:
            return self.__diferencia_de_goles > otroEquipo.__diferencia_de_goles
        else:
            return self.__goles_a_favor > otroEquipo.__goles_a_favor

    def __str__(self) -> str:
        return '\n Identificación del equipo: {}\n Nombre del Equipo: {}\n Goles a Favor: {}\n Goles en Contra: {}\n Diferencia de Goles: {}\n Puntos acumulados: {}' .format(
                                    self.__id_equipo,   self.__nombre_del_equipo, self.__goles_a_favor, self.__goles_en_contra, self.__diferencia_de_goles,  self.__puntos)