
class Visualizacion:
    __id_miembro: int
    __id_pelicula: str
    __fecha: str
    __hora: str
    __minutos_visualizacion: int
    def __init__(self,id_miembro, id_pelicula, fecha, hora, minutos_visualizacion):
        self.__id_miembro = id_miembro
        self.__id_pelicula = id_pelicula
        self.__fecha = fecha
        self.__hora = hora
        self.__minutos_visualizacion = minutos_visualizacion

    def getIDMiembroVisualizacion(self):
        return self.__id_miembro

    def getMinutosVisualizacion(self):
        return self.__minutos_visualizacion

    def __eq__(self, otraVisualizacion):
        if ((self.__id_miembro == otraVisualizacion.__id_miembro) and (self.__fecha == otraVisualizacion.__fecha) and (self.__hora == otraVisualizacion.__hora)):
            return True
        else:
            return False

    def __str__(self):
        return '\n ID de Miembro: {}\n ID de Película: {}\n Fecha: {}\n Hora: {}\n Visualización: {} minutos' .format(self.__id_miembro, self.__id_pelicula, self.__fecha, self.__hora, self.__minutos_visualizacion)
