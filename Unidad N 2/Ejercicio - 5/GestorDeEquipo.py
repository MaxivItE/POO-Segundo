from Equipo import Equipo
import csv
class GestorDeEquipo:
    __lista_de_equipos: list = []

    def __init__(self) -> None:
        self.inicializarListaDeEquipos()

    def inicializarListaDeEquipos(self) -> None:
        with open("equipos2024.csv", 'r') as archivo_equipos_2024:
            equipo = csv.reader(archivo_equipos_2024, delimiter=',')
            next(equipo)
            print("\n")
            for datos_equipo in equipo:
                id_equipo = str(datos_equipo[0])
                nombre_del_equipo = str(datos_equipo[1])
                unEquipo = Equipo (id_equipo, nombre_del_equipo)
                self.__lista_de_equipos.append(unEquipo)

    def acumularGolesAFavor(self, posicion_equipo, goles_de_equipo) -> None:
        self.__lista_de_equipos[posicion_equipo].setGolesAFavor(goles_de_equipo)

    def acumularGolesEnContra(self, posicion_equipo, goles_de_equipo) -> None:
        self.__lista_de_equipos[posicion_equipo].setGolesEnContra(goles_de_equipo)

    def acumularDiferenciaDeGoles(self,posicion_equipo, diferencia_de_goles) -> None:
        self.__lista_de_equipos[posicion_equipo].setDiferenciaDeGoles(diferencia_de_goles)

    def acumularPuntosDelEquipo(self, posicion_equipo, puntos) -> None:
        self.__lista_de_equipos[posicion_equipo].setPuntos(puntos)

    def actualizarDatosDeLosEquipos(self, gestor_fechas) -> None:
        for posicion_equipo in range(len(self.__lista_de_equipos)):
            id_equipo_lista: int = self.__lista_de_equipos[posicion_equipo].getIdDeEquipo()
            gestor_fechas.actualizarPartidosDisputados(id_equipo_lista, self, posicion_equipo)
    
    def ordenarTablaDePosiciones(self):
        min_index: int = 0
        min_value: int = 0
        aux: list = []
        tamano_lista_equipos: int = len(self.__lista_de_equipos)-1
        for i in range(0, tamano_lista_equipos):
            min_index = i
            min_value = self.__lista_de_equipos[min_index]
            for j in range(i, tamano_lista_equipos):
                if min_value < self.__lista_de_equipos[j+1]:
                    min_value = self.__lista_de_equipos[j+1]
                    min_index = j+1
            if min_index != 1:
                aux = self.__lista_de_equipos[i]
                self.__lista_de_equipos[i] = self.__lista_de_equipos[min_index]
                self.__lista_de_equipos[min_index] = aux

    def mostrarTablaDePosiciones(self, gestor_fecha) -> None:
        fecha_del_torneo: str = gestor_fecha.consultarFechaDelTorneo()
        print("\t\t\t\t***LIGUILLA DE RAWSON***")
        print(" {:<10} {:<20} {:<10} {:<10} {:<10} {:<15} {:<10}" .format("Posición", "Equipo", "Fecha", "GF", "GC", "Dif. Goles", "Puntos"))
        for i in range(len(self.__lista_de_equipos)):
            print(" {:<10} {:<20} {:<10} {:<10} {:<10} {:<15} {:<10}" .format (i+1, self.__lista_de_equipos[i].getNombreEquipo(), fecha_del_torneo, self.__lista_de_equipos[i].getGolesAFavor(), self.__lista_de_equipos[i].getGolesEnContra(), self.__lista_de_equipos[i].getDiferenciaDeGoles(), self.__lista_de_equipos[i].getPuntos()))

    def buscarDatosDeEquipo(self, nombre_equipo_ingresado, gestor_fechas) -> None:
        posicion_equipo_lista:int = 0
        equipo_encontrado:bool = False
        tamano_lista_equipo = len(self.__lista_de_equipos)
        while posicion_equipo_lista < tamano_lista_equipo and equipo_encontrado != True:
            nombre_equipo_lista = str(self.__lista_de_equipos[posicion_equipo_lista].getNombreEquipo())
            id_equipo_lista = str(self.__lista_de_equipos[posicion_equipo_lista].getIdDeEquipo())
            if nombre_equipo_ingresado == nombre_equipo_lista:
                gestor_fechas.consultarPartidosDeEquipo(nombre_equipo_ingresado, id_equipo_lista)
                equipo_encontrado = True
            posicion_equipo_lista+=1