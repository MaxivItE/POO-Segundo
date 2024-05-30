
class Empleado:
    __nombre_apellido: str
    __id_empleado: int
    __puesto: str

    def __init__(self, nombre_apellido, id_empleado, puesto) -> None:
        self.__nombre_apellido = nombre_apellido
        self.__id_empleado = id_empleado
        self.__puesto = puesto

    def getNombreApellido(self) -> str:
        return self.__nombre_apellido

    def getIDEmpleado(self) -> int:
        return self.__id_empleado

    def __str__(self) -> str:
        return '\n Nombre y apellido: {}\n Identificación de Empleado: {}\n Puesto: {}' .format(self.__nombre_apellido, self.__id_empleado, self.__puesto)