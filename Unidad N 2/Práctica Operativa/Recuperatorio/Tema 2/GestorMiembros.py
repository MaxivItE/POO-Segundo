from ClaseMiembro import Miembro
import numpy as np
import csv

class GestorMiembros:
    __arreglo_miembros: np.ndarray
    __cantidad: int
    __dimension: int
    __incremento: int

    def __init__(self) -> None:
        self.__arreglo_miembros = np.empty(0, dtype = Miembro)
        self.__cantidad = 0
        self.__dimension = 0
        self.__incremento = 1
        self.cargarArregloMiembros()

    def agregarMiembro(self, unMiembro) -> None:
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arreglo_miembros = np.resize(self.__arreglo_miembros, self.__dimension)
        self.__arreglo_miembros[self.__cantidad] = unMiembro
        self.__cantidad += 1

    def cargarArregloMiembros(self) -> None:
        archivo_miembros = open('Miembros.csv', mode = 'r')
        lector_miembros = csv.reader(archivo_miembros, delimiter = ';')
        miembro_encontrado:bool = True
        for datos_miembro in lector_miembros:
            if miembro_encontrado:
                miembro_encontrado = False
            else:
                unMiembro = Miembro(id_miembro = datos_miembro[0], nombre_miembro = datos_miembro[1], correo_electronico = datos_miembro[2])
                self.agregarMiembro(unMiembro)
        archivo_miembros.close()

    def verificarCorreoMiembro(self, correo_ingresado, gestor_visualizacion):
        pos_miembro:int = 0
        cantidad_miembros = int(len(self.__arreglo_miembros))
        miembro_encontrado:bool = False
        while pos_miembro < cantidad_miembros and miembro_encontrado != True:
            correo_miembro = str(self.__arreglo_miembros[pos_miembro].getCorreoElectronico())
            if correo_ingresado.lower() == correo_miembro.lower():
                id_miembro = int(self.__arreglo_miembros[pos_miembro].getIDMiembro())
                gestor_visualizacion.mostrarMinutosVisualizados(id_miembro)
                miembro_encontrado = True
            pos_miembro += 1
        if miembro_encontrado == False:
            print("\n No se encontró el Miembro.")

    def mostrarVisualizacionesSimultaneas(self, miembro) -> None:
        nombre_miembro = str(miembro.getNombreMiembro())
        correo_electronico = str(miembro.getCorreoElectronico())
        print(f"\n Miembro: {nombre_miembro}\n Correo Electrónico: {correo_electronico}")

    def obtenerIDMiembro(self, gestor_visualizacion):
        cantidad_miembros = int(len(self.__arreglo_miembros))
        visualizaciones_simultaneas:bool = False
        print("\n---MIEMBROS QUE HAN REALIZADO VISUALIZACIONES SIMULTÁNEAS---")
        for pos_miembro in range(cantidad_miembros):
            id_miembro = int(self.__arreglo_miembros[pos_miembro].getIDMiembro())
            visualizaciones_simultaneas = gestor_visualizacion.verificarVisualizacionesSimultaneas(id_miembro)
            if visualizaciones_simultaneas != False:
                self.mostrarVisualizacionesSimultaneas(self.__arreglo_miembros[pos_miembro])

    def mostrarMiembros(self) -> None:
        cantidad_miembros = int(len(self.__arreglo_miembros))
        print("\n---MOSTRAR MIEMBROS---")
        for pos_miembro in range(cantidad_miembros):
            print(self.__arreglo_miembros[pos_miembro])