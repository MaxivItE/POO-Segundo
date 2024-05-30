
class Miembro:
    __id_miembro: int
    __nombre_miembro: str
    __correo_electronico: str

    def __init__(self, id_miembro, nombre_miembro, correo_electronico):
        self.__id_miembro = id_miembro
        self.__nombre_miembro = nombre_miembro
        self.__correo_electronico = correo_electronico

    def getIDMiembro(self):
        return self.__id_miembro

    def getNombreMiembro(self):
        return self.__nombre_miembro

    def getCorreoElectronico(self):
        return self.__correo_electronico

    def __str__(self):
        return '\n ID de Miembro: {}\n Apellido y Nombre: {}\n Correo Electrónico: {}' .format(self.__id_miembro, self.__nombre_miembro, self.__correo_electronico)