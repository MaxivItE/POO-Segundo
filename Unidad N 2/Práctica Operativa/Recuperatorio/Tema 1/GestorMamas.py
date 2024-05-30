from Mama import Mama
import csv
import numpy as np

class GestorMadre:
    __arreglo_madres = np.ndarray
    __cantidad: int
    __dimension: int
    __incremento: int

    def agregarMadre(self, unaMadre) -> None:
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arreglo_madres = np.resize(self.__arreglo_madres, self.__dimension)
        self.__arreglo_madres[self.__cantidad] = unaMadre
        self.__cantidad += 1

    def __init__(self) -> None:
        self.__arreglo_madres = np.empty(0, dtype = Mama)
        self.__cantidad = 0
        self.__dimension = 0
        self.__incremento = 1
        self.cargarArregloMadres()

    def cargarArregloMadres(self) -> None:
        archivo_madres = open('Mamas.csv', mode = 'r')
        lector_madres = csv.reader(archivo_madres, delimiter = ';')
        madre_encontrada:bool = True
        for datos_madre in lector_madres:
            if madre_encontrada:
                madre_encontrada = False
            else:
                apellido_y_nombre = str(datos_madre[2])
                separador = int(apellido_y_nombre.find(','))
                apellido = str(apellido_y_nombre[0:separador])
                nombre = str(apellido_y_nombre[separador+2:-1])
                unaMadre = Mama(DNI = datos_madre[0], edad = datos_madre[1], apellido = apellido, nombre = nombre)
                self.agregarMadre(unaMadre)
        archivo_madres.close()

    def verificarDNIMadre(self, DNI_ingresado, gestor_nacimiento) -> None:
        posicion_madre:int = 0
        madre_encontrada:bool = False
        cantidad_madres = len(self.__arreglo_madres)
        print("\n---DATOS DEL PARTO---")
        while posicion_madre < cantidad_madres and madre_encontrada != True:
            DNI_arreglo = str(self.__arreglo_madres[posicion_madre].getDNIMama())
            if DNI_ingresado == DNI_arreglo:
                apellido = str(self.__arreglo_madres[posicion_madre].getApellidoMama())
                nombre = str(self.__arreglo_madres[posicion_madre].getNombreMama())
                edad = int(self.__arreglo_madres[posicion_madre].getEdadMama())
                print(f"\n Apellido y Nombre: {apellido}, {nombre}")
                print(f" Edad: {edad}")
                gestor_nacimiento.mostrarPartoMadre(DNI_ingresado)
                madre_encontrada = True
            posicion_madre += 1

    def verificarPartoMadre(self, gestor_nacimiento):
        posicion_madre:int = 0
        cantidad_madres = len(self.__arreglo_madres)
        partos_simultaneos_madre:bool
        print("\n ---MADRES CON PARTOS MÚLTIPLES---")
        for posicion_madre in range (cantidad_madres):
            DNI_madre = str(self.__arreglo_madres[posicion_madre].getDNIMama())
            partos_simultaneos_madre = gestor_nacimiento.verificarPartosSimultaneos(DNI_madre)
            if partos_simultaneos_madre != False:
                print(self.__arreglo_madres[posicion_madre])

    def mostrarMadres(self) -> None:
        print("\n---MOSTRAR MAMÁS---")
        for i in range(len(self.__arreglo_madres)):
            print(self.__arreglo_madres[i])