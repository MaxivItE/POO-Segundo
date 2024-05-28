from MaterialRefractario import MaterialRefractario
import csv

class GestorMaterial:
    __lista_materiales: list

    def __init__(self) -> None:
        self.__lista_materiales = []
        self.cargarListaDeMateriales()

    def cargarListaDeMateriales(self) -> None:
        with open("materialesRefractarios.csv", 'r') as archivo_materiales:
            lector_materiales = csv.reader(archivo_materiales, delimiter = ',')
            next(lector_materiales)
            print("\n")
            for datos_material in lector_materiales:
                unMaterialRefractario:object = MaterialRefractario(material = str(datos_material[0]), caracteristicas = str(datos_material[1]), cantidad = int(datos_material[2]), costo_adicional = str(datos_material[3]))
                self.__lista_materiales.append(unMaterialRefractario)