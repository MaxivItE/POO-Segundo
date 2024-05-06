
class FechaDeFutbol:
    __fecha_del_partido: str
    __id_equipo_local: str
    __id_equipo_visitante: str
    __cantidad_goles_local: int
    __cantidad_goles_visitante: int

    def __init__(self, fecha_del_partido, id_equipo_local, id_equipo_visitante, cantidad_goles_local, cantidad_goles_visitante) -> None:
        self.__fecha_del_partido = fecha_del_partido
        self.__id_equipo_local = id_equipo_local
        self.__id_equipo_visitante = id_equipo_visitante
        self.__cantidad_goles_local = cantidad_goles_local
        self.__cantidad_goles_visitante = cantidad_goles_visitante

    def getFechaDePartido(self) -> str:
        return self.__fecha_del_partido
    def getIdEquipoLocal(self) -> str:
        return self.__id_equipo_local
    def getIdEquipoVisitante(self) -> str:
        return self.__id_equipo_visitante
    def getCantidadGolesLocal(self) -> int:
        return self.__cantidad_goles_local
    def getCantidadGolesVisitante(self) -> int:
        return self.__cantidad_goles_visitante
    
    def __str__(self) -> str:
        return ' Fecha_del_partido: {}\n Identificación del equipo Local: {}\n Identificación del equipo Visitante: {}\n Cantidad de Goles del equipo Local: {}\n Cantidad de Goles del equipo Visitante: {}' .format(self.__fecha_del_partido, self.__id_equipo_local, self.__id_equipo_visitante, self.__cantidad_goles_local, self.__cantidad_goles_visitante)