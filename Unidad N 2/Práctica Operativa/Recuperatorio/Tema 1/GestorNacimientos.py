from Nacimiento import Nacimiento
import csv

class GestorNacimientos:
    __lista_nacimiento:list

    def __init__(self) -> None:
        self.__lista_nacimiento = []
        self.cargarListaDeNacimientos()

    def cargarListaDeNacimientos(self) -> None:
        with open("Nacimientos.csv", 'r') as archivos_nacimientos:
            nacimiento = csv.reader(archivos_nacimientos, delimiter = ';')
            next(nacimiento)
            print("\n")
            for datos_nacimientos in nacimiento:
                unNacimiento = Nacimiento(DNI_mama = str(datos_nacimientos[0]), tipo_parto = str(datos_nacimientos[1]), fecha_parto = str(datos_nacimientos[2]), hora_parto = str(datos_nacimientos[3]), peso_bebe = str(datos_nacimientos[4]), altura_bebe = int(datos_nacimientos[5]))
                self.__lista_nacimiento.append(unNacimiento)

    def mostrarPartoMadre(self, DNI_ingresado) -> None:
        posicion_nacimiento:int = 0
        cantidad_nacimientos = len(self.__lista_nacimiento)
        while posicion_nacimiento < cantidad_nacimientos:
            DNI_lista = str(self.__lista_nacimiento[posicion_nacimiento].getDNIMadreNacimiento())
            if DNI_ingresado == DNI_lista:
                tipo_parto = str(self.__lista_nacimiento[posicion_nacimiento].getTipoParto())
                peso = str(self.__lista_nacimiento[posicion_nacimiento].getPesoBebe())
                altura = int(self.__lista_nacimiento[posicion_nacimiento].getAlturaBebe())
                print(f"\n Tipo De Parto: {tipo_parto}")
                print(" Bebe/s")
                print(f" Peso: {peso}      Altura: {altura}\n")
            posicion_nacimiento += 1

    def verificarPartosSimultaneos(self, DNI_madre) -> bool:
        cantidad_nacimientos = len(self.__lista_nacimiento)
        for pos_nacimiento in range(cantidad_nacimientos):
            DNI_madre_nacimiento = str(self.__lista_nacimiento[pos_nacimiento].getDNIMadreNacimiento())
            if DNI_madre == DNI_madre_nacimiento:
                for pos_nacimiento2 in range(cantidad_nacimientos):
                    if pos_nacimiento != pos_nacimiento2:
                        if self.__lista_nacimiento[pos_nacimiento] == self.__lista_nacimiento[pos_nacimiento2]:
                            return True
        return False

    def mostrarNacimientos(self) -> None:
        print("\n---MOSTRAR NACIMIENTOS---")
        for posicion_nacimiento in range(len(self.__lista_nacimiento)):
            print(self.__lista_nacimiento[posicion_nacimiento])