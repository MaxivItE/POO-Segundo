
class GestorMateriales:
    __lista_materiales: list

    def __init__(self) -> None:
        self.__lista_materiales = []

    def agregarMaterialRefractario(self, material_refractario) -> None:
        self.__lista_materiales.append(material_refractario)

    def mostrarMaterialesRefractarios(self) -> None:
        cantidad_materiales = len(self.__lista_materiales)
        print("---MOSTRAR MATERIALES REFRACTARIOS DE LA FABRICA 'NUESTRO HOGAR'---")
        for posicion_material in range(cantidad_materiales):
            print(self.__lista_materiales[posicion_material])