
class Nacimiento:
    __DNI_mama: str
    __tipo_parto: str
    __fecha_parto: str
    __hora_parto: str
    __peso_bebe: str
    __altura_bebe: int

    def __init__(self, DNI_mama, tipo_parto, fecha_parto, hora_parto, peso_bebe, altura_bebe) -> None:
        self.__DNI_mama = DNI_mama
        self.__tipo_parto = tipo_parto
        self.__fecha_parto = fecha_parto
        self.__hora_parto = hora_parto
        self.__peso_bebe = peso_bebe
        self.__altura_bebe = altura_bebe

    def getDNIMadreNacimiento(self) -> str:
        return self.__DNI_mama

    def getTipoParto(self):
        return self.__tipo_parto

    def getPesoBebe(self):
        return self.__peso_bebe

    def getAlturaBebe(self):
        return self.__altura_bebe

    def __eq__(self, otroNacimiento) -> bool:
        if ((self.__DNI_mama == otroNacimiento.__DNI_mama) and (self.__fecha_parto == otroNacimiento.__fecha_parto)):
            return True
        else:
            return False

    def __str__(self) -> str:
        return '\n Documento de la madre: {}\n Tipo de Parto: {}\n Fecha: {}\n Hora: {}\n Peso: {}\n Altura: {}' .format(self.__DNI_mama, self.__tipo_parto, self.__fecha_parto, self.__hora_parto, self.__peso_bebe, self.__altura_bebe)