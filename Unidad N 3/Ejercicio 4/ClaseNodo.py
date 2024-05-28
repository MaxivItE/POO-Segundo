from ClasePublicacion import Publicacion

class Nodo:
    __publicacion: Publicacion
    __siguiente_publicacion: object

    def __init__(self, unaPublicacion) -> None:
        self.__publicacion = unaPublicacion
        self.__publicacion.cargarImporteDePublicacion(self.__publicacion)
        self.__siguiente_publicacion = None

    def setSiguientePublicacion(self, siguiente_publicacion) -> None:
        self.__siguiente_publicacion = siguiente_publicacion

    def getSiguientePublicacion(self) -> object:
        return self.__siguiente_publicacion

    def getDatoPublicacion(self):
        return self.__publicacion

    def __str__(self):
        return self.__publicacion.mostrarPublicacion()