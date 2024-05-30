
class ProgramaCapacitacion:
    __nombre_programa: str
    __codigo_programa: str
    __duracion_programa: int

    def __init__(self, nombre_programa, codigo_programa, duracion_programa) -> None:
        self.__nombre_programa = nombre_programa
        self.__codigo_programa = codigo_programa
        self.__duracion_programa = duracion_programa

    def getNombrePrograma(self) -> str:
        return self.__nombre_programa
    
    def getDuracionPrograma(self) -> int:
        return self.__duracion_programa

    def __str__(self) -> str:
        return '\n Nombre del Programa: {}\n Código: {}\n Duración del programa: {}' .format(self.__nombre_programa, self.__codigo_programa, self.__duracion_programa)