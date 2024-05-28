
class Edificio:
    __id_edificio: int
    __nombre_edificio: str
    __direccion: str
    __nombre_Empresa_constructora: str
    __cantidad_pisos: int
    __cantidad_departamentos: int
    __departamento:list

    def __init__(self, id_edificio, nombre_edificio, direccion, nombre_Empresa_constructora, cantidad_pisos, cantidad_departamentos) -> None:
        self.__id_edificio = id_edificio
        self.__nombre_edificio = nombre_edificio
        self.__direccion = direccion
        self.__nombre_Empresa_constructora = nombre_Empresa_constructora
        self.__cantidad_pisos = cantidad_pisos
        self.__cantidad_departamentos = cantidad_departamentos
        self.__departamento = []

    def getIdEdificio(self) -> int:
        return self.__id_edificio

    def getNombreEdificio(self) -> str:
        return self.__nombre_edificio

    def setDepartamento(self, unDepartamento) -> None:
        self.__departamento.append(unDepartamento)
    def getDepartamento(self):
        return self.__departamento

    def getSuperficieCubierta(self, posicion_departamento) -> None:
        return self.__departamento[posicion_departamento].getSuperficieCubierta()
    
    def getNombrePropietario(self, posicion_departamento) -> None:
        self.__departamento[posicion_departamento].getNombrePropietario()
    
    def getMostrarDatosDepartamentosEdificio(self):
        for i in range(len(self.__departamento)):
            print(self.__departamento[i].mostrarDatosDepartamento())        

    def mostrarDatosEdificios(self) -> str:
        print ('\n Identificador del Edificio: {}\n Nombre del Edificio: {}\n Dirección: {}\n Nombre de la Empresa Contructora: {}\n Cantidad de Pisos: {}\n Cantidad de Departamentos: {}' .format(self.__id_edificio, self.__nombre_edificio, self.__direccion, self.__nombre_Empresa_constructora, self.__cantidad_pisos, self.__cantidad_departamentos))
        for i in range(len(self.__departamento)):
            print(self.__departamento[i].mostrarDatosDepartamento())

    '''def __str__(self):
        cadena = 'Identificador del Edificio: ' +self.__id_edificio+'\n'
        cadena +='Nombre del Edificio: ' +self.__nombre_edificio+'\n'
        return cadena'''