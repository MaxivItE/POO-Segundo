from FechaDeFutbol import FechaDeFutbol
import csv
class GestorFechaDeFutbol:
    __lista_fecha_de_futbol: list = []

    def __init__(self) -> None:
        self.inicializarListaFechas()
    
    def inicializarListaFechas(self) -> None:
        with open("fechasFutbol.csv", 'r') as archivo_fechas:
            fecha = csv.reader(archivo_fechas, delimiter=',')
            next(fecha)
            print("\n")
            for datos_fecha in fecha:
                fecha_del_partido = str(datos_fecha[0])
                id_equipo_local = str(datos_fecha[1])
                id_equipo_visitante = str(datos_fecha[2])
                cantidad_goles_local = int(datos_fecha[3])
                cantidad_goles_visitante = int(datos_fecha[4])
                unaFecha = FechaDeFutbol(fecha_del_partido, id_equipo_local, id_equipo_visitante, cantidad_goles_local, cantidad_goles_visitante)
                self.__lista_fecha_de_futbol.append(unaFecha)

    def verificarPresentacionEquipo(self, id_equipo, id_equipo_local, id_equipo_visitante) -> str:
        if id_equipo == id_equipo_local:
            return 'Local'
        elif id_equipo == id_equipo_visitante: 
            return 'Visitante'

    def contarGolesDelPartido(self, gestor_equipo, goles_a_favor, goles_en_contra, posicion_equipo) -> None:
        gestor_equipo.acumularGolesAFavor(posicion_equipo, goles_a_favor)
        gestor_equipo.acumularGolesEnContra(posicion_equipo, goles_en_contra)

    def contarDiferenciaDeGoles(self, goles_a_favor, goles_en_contra) -> int:
        return goles_a_favor - goles_en_contra

    def contarPuntosDelPartido(self, goles_a_favor, goles_en_contra) -> int:
        if goles_a_favor > goles_en_contra:
            return 3
        elif goles_a_favor == goles_en_contra:
            return 1
        return 0

    def mostrarDatosDelPartido(self, fecha_del_partido, goles_a_favor, goles_en_contra, diferencia_de_goles, puntos) -> None:
        print(" {:<10} {:<10} {:<10} {:<15} {:<10}" .format(
        fecha_del_partido, goles_a_favor, goles_en_contra, diferencia_de_goles, puntos))

    def consultarPartidosDeEquipo(self, nombre_equipo_ingresado, id_equipo_lista) -> None:
        print(f"\n Equipo: {nombre_equipo_ingresado}")
        print(" {:<10} {:<10} {:<10} {:<15} {:<10}" .format("Fecha", "GF", "GC", "Dif. Goles", "Puntos"))
        for i in range(len(self.__lista_fecha_de_futbol)):
            goles_a_favor: int = 0
            goles_en_contra: int = 0
            fecha_de_partido = str(self.__lista_fecha_de_futbol[i].getFechaDePartido())
            id_equipo_local:str = self.__lista_fecha_de_futbol[i].getIdEquipoLocal()
            id_equipo_visitante:str = self.__lista_fecha_de_futbol[i].getIdEquipoVisitante()
            presentacion_equipo:str = self.verificarPresentacionEquipo(id_equipo_lista, id_equipo_local, id_equipo_visitante)
            match presentacion_equipo:
                case 'Local': 
                    goles_a_favor = int(self.__lista_fecha_de_futbol[i].getCantidadGolesLocal())
                    goles_en_contra = int(self.__lista_fecha_de_futbol[i].getCantidadGolesVisitante())
                    diferencia_de_goles = int(self.contarDiferenciaDeGoles(goles_a_favor, goles_en_contra))
                    puntos = int(self.contarPuntosDelPartido(goles_a_favor, goles_en_contra))
                    self.mostrarDatosDelPartido(fecha_de_partido, goles_a_favor, goles_en_contra, diferencia_de_goles, puntos)
                case 'Visitante':
                    goles_a_favor = int(self.__lista_fecha_de_futbol[i].getCantidadGolesVisitante())
                    goles_en_contra = int(self.__lista_fecha_de_futbol[i].getCantidadGolesLocal())
                    diferencia_de_goles = int(self.contarDiferenciaDeGoles(goles_a_favor, goles_en_contra))
                    puntos = int(self.contarPuntosDelPartido(goles_a_favor, goles_en_contra))
                    self.mostrarDatosDelPartido(fecha_de_partido, goles_a_favor, goles_en_contra, diferencia_de_goles, puntos)

    def actualizarPartidosDisputados(self, id_equipo, gestor_equipo, posicion_equipo) -> None:
        for i in range(len(self.__lista_fecha_de_futbol)):
            puntos:int = 0
            goles_a_favor: int = 0
            goles_en_contra: int = 0
            id_equipo_local = str(self.__lista_fecha_de_futbol[i].getIdEquipoLocal())
            id_equipo_visitante = str(self.__lista_fecha_de_futbol[i].getIdEquipoVisitante())
            presentacion_equipo = str(self.verificarPresentacionEquipo(id_equipo, id_equipo_local, id_equipo_visitante))
            match presentacion_equipo:
                case 'Local':
                    goles_a_favor = int(self.__lista_fecha_de_futbol[i].getCantidadGolesLocal())
                    goles_en_contra = int(self.__lista_fecha_de_futbol[i].getCantidadGolesVisitante())
                    self.contarGolesDelPartido(gestor_equipo, goles_a_favor, goles_en_contra, posicion_equipo)
                    puntos = int(self.contarPuntosDelPartido(goles_a_favor, goles_en_contra))
                case 'Visitante':
                    goles_a_favor = int(self.__lista_fecha_de_futbol[i].getCantidadGolesVisitante())
                    goles_en_contra = int(self.__lista_fecha_de_futbol[i].getCantidadGolesLocal())
                    self.contarGolesDelPartido(gestor_equipo, goles_a_favor, goles_en_contra, posicion_equipo)
                    puntos = int(self.contarPuntosDelPartido(goles_a_favor, goles_en_contra))
            diferencia_de_goles = self.contarDiferenciaDeGoles(goles_a_favor, goles_en_contra)
            gestor_equipo.acumularDiferenciaDeGoles(posicion_equipo, diferencia_de_goles)
            gestor_equipo.acumularPuntosDelEquipo(posicion_equipo, puntos)

    def consultarFechaDelTorneo(self) -> str:
        ultima_fecha = int(self.__lista_fecha_de_futbol[-1].getFechaDePartido())
        return ultima_fecha