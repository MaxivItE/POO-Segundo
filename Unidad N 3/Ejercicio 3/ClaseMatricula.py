
class Matricula:
    __fecha_matricula: str
    __empleado: object
    __programa: object

    def __init__(self, fecha_matricula, empleado, programa) -> None:
        self.__fecha_matricula = fecha_matricula
        self.__empleado = empleado
        self.__programa = programa
    
    def getEmpleado(self) -> object:
        return self.__empleado

    def getPrograma(self) -> object:
        return self.__programa

    def __str__(self):
        return '\n Fecha de Matrícula: {}{}{}' .format(self.__fecha_matricula, self.__empleado, self.__programa)