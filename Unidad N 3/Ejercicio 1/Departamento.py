
class Departamento:
    __id_departamento: int
    __nombre_apellido_propietario: str
    __numero_piso: int
    __numero_departamento: int
    __cantidad_habitaciones: int
    __cantidad_banos: int
    __superficie_cubierta: float

    def __init__(self, id_departamento, nombre_apellido_propietario, numero_piso, numero_departamento, cantidad_habitaciones, cantidad_banos, superficie_cubierta) -> None:
        self.__id_departamento = id_departamento
        self.__nombre_apellido_propietario = nombre_apellido_propietario
        self.__numero_piso = numero_piso
        self.__numero_departamento = numero_departamento
        self.__cantidad_habitaciones = cantidad_habitaciones
        self.__cantidad_banos = cantidad_banos
        self.__superficie_cubierta = superficie_cubierta

    def getIDDepartamento(self) -> int:
        return self.__id_departamento

    def getNombrePropietario(self) -> str:
        return self.__nombre_apellido_propietario

    def getSuperficieCubierta(self) -> float:
        return self.__superficie_cubierta

    def mostrarDatosDepartamento(self) -> str:
        return '\n Identificador de Departamento: {}\n Nombre y Apellido del Propietario: {}\n Número de Piso: {}\n Número de Departamento: {}\n Cantidad de Habitaciones: {}\n Cantidad de Baños: {}\n Superficie Cubiertas: {}' .format(self.__id_departamento, self.__nombre_apellido_propietario, self.__numero_piso, self.__numero_departamento, self.__cantidad_habitaciones, self.__cantidad_banos, self.__superficie_cubierta)