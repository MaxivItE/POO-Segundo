from ClaseVisualizacion  import Visualizacion
import csv

class GestorVisualizaciones:
    __lista_visualizaciones: list

    def __init__(self) -> None:
        self.__lista_visualizaciones = []
        self.cargarListaVisualizaciones()

    def cargarListaVisualizaciones(self) -> None:
        with open('Visualizaciones.csv', mode = 'r') as archivo_visualizacion:
            lector_visualizacion = csv.reader(archivo_visualizacion, delimiter = ';')
            next(lector_visualizacion)
            print("\n")
            for datos_visualizacion in lector_visualizacion:
                unaVisualizacion = Visualizacion(id_miembro = int(datos_visualizacion[0]), id_pelicula = str(datos_visualizacion[1]), fecha = str(datos_visualizacion[2]), hora = str(datos_visualizacion[3]), minutos_visualizacion = int(datos_visualizacion[4]))
                self.__lista_visualizaciones.append(unaVisualizacion)

    def mostrarMinutosVisualizados(self, id_miembro) -> None:
        cantidad_minutos:int = 0
        cantidad_visualizaciones = len(self.__lista_visualizaciones)
        for pos_visualizacion in range(cantidad_visualizaciones):
            id_miembro_visualizacion = int(self.__lista_visualizaciones[pos_visualizacion].getIDMiembroVisualizacion())
            if id_miembro == id_miembro_visualizacion:
                minutos_visualizacion = int(self.__lista_visualizaciones[pos_visualizacion].getMinutosVisualizacion())
                cantidad_minutos += minutos_visualizacion
        print("\n---CANTIDAD TOTAL DE MINUTOS VISTOS DE PELICULAS EN NETVIEW---")
        print(f" Cantidad de Minutos vistos por el Miembro: {cantidad_minutos} minutos")

    def verificarVisualizacionesSimultaneas(self, id_miembro) -> bool:
        cantidad_visualizaciones = len(self.__lista_visualizaciones)
        for pos_visualizacion in range(cantidad_visualizaciones):
            id_miembro_visualizacion = int(self.__lista_visualizaciones[pos_visualizacion].getIDMiembroVisualizacion())
            if id_miembro == id_miembro_visualizacion:
                for pos_visualizacion2 in range(cantidad_visualizaciones):
                    if pos_visualizacion != pos_visualizacion2:
                        if self.__lista_visualizaciones[pos_visualizacion] == self.__lista_visualizaciones[pos_visualizacion2]:
                            return True
        return False

    def mostrarVisualizaciones(self) -> None:
        cantidad_visualizaciones = len(self.__lista_visualizaciones)
        print("\n---MOSTRAR VISUALIZACIONES---")
        for pos_visualizacion in range(cantidad_visualizaciones):
            print(self.__lista_visualizaciones[pos_visualizacion])