from Ladrillo import Ladrillo
import csv

class GestorLadrillo:
    __lista_ladrillos: list
    
    def __init__(self) -> None:
        self.__lista_ladrillos = []
        self.cargarListaDeLadrillos()

    def cargarListaDeLadrillos(self) -> None:
        with open("ladrillos.csv", 'r') as archivo_ladrillos:
            lector_ladrillos = csv.reader(archivo_ladrillos, delimiter = ',')
            for datos_ladrillo in lector_ladrillos:
                if datos_ladrillo[2] == 0:
                    unLadrillo = Ladrillo(cantidad = datos_ladrillo[0], identificador = datos_ladrillo[1], kg_materia_prima = datos_ladrillo[2])
                    self.__lista_ladrillos.append(unLadrillo)
                else:
                    ...
                
                