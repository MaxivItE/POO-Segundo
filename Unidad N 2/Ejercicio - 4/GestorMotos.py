from Moto import Moto
import csv

class GestorMotos:
    __lista_motos: list = []

    def __init__(self):
        self.inicializarListaMotos()
    
    def inicializarListaMotos(self):
        with open("datosMotos.csv", 'r') as archivo_motos:
            reader = csv.reader(archivo_motos, delimiter=',')
            next(reader)
            print("\n")
            for fila in reader:
                patente: str = fila[0]
                marca: str = fila[1]
                nombre_conductor: str = fila[2]
                apellido_conductor: str = fila[3]
                kilometraje: float = fila[4]
                unaMoto = Moto(patente, marca, nombre_conductor, apellido_conductor, kilometraje)
                self.__lista_motos.append(unaMoto)
        archivo_motos.close()

    def mostrarListaMotos(self):
        tamano_lista_motos = len(self.__lista_motos)
        for i in range(tamano_lista_motos):
            print(self.__lista_motos[i])
    
    def verificarPatente(self, patente_ingresada):
        tamano_lista_motos = len(self.__lista_motos)
        patente_encontrada = False
        i = 0
        while (i < tamano_lista_motos) and (patente_encontrada != True):
            patente_lista = self.__lista_motos[i].getPatente()
            if patente_ingresada == patente_lista:
                return True
            i+=1
        return patente_encontrada
